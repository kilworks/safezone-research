"""Check the Korean section (ko/) against its English sources, mechanically.

For every translated field of ko/i18n/*.yaml and every hand-translated file (ko/README.md, ko/theory/*.md):
  - the same M-, U-, C-, T-, E- ids as the source, no more, no fewer;
  - every number of the source appears in the translation (numbers are never spelled out);
  - text that is prose in English contains Hangul (nothing left untranslated);
  - files keep the same count of $ (math), ``` fences and headings.
It cannot judge meaning: that is the adversarial reviewer's job. Exit 1 on any problem.

Usage: py -3 tools/check_ko.py [--quiet] [--file ko/i18n/<name>.yaml | ko/theory/<name>.md]
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
IDS = re.compile(r"\b[MUCTE]-\d{4}(?!\d)")
NUM = re.compile(r"\d+(?:[.,]\d+)*")
HANGUL = re.compile(r"[가-힣]")
WORDS = re.compile(r"\b[A-Za-z]{3,}\b")
FIELDS = {"mechanics": ("name", "notes", "domain"), "unknowns": ("question", "why_it_matters", "sweep_range", "resolution"),
          "contradictions": ("summary",)}
VERBATIM_OK = {"M-0117.readings.A", "M-0119.parameters.list"}  # a pure formula and a list of in-game names: kept in English on purpose


def compare(where, en, ko, problems):
    if set(IDS.findall(en)) != set(IDS.findall(ko)):
        problems.append(f"{where}: ids differ, en {sorted(set(IDS.findall(en)) - set(IDS.findall(ko)))} "
                        f"ko {sorted(set(IDS.findall(ko)) - set(IDS.findall(en)))}")
    lost = set(NUM.findall(en)) - set(NUM.findall(ko))
    if lost:
        problems.append(f"{where}: numbers missing {sorted(lost)[:8]}")
    if len(WORDS.findall(en)) >= 4 and not HANGUL.search(ko) and where not in VERBATIM_OK:
        problems.append(f"{where}: no Hangul, looks untranslated")


def pairs(rec, kind):
    """(field, english value, list of (subkey, english string)) for every translatable field of a record."""
    out = [(f, rec.get(f)) for f in FIELDS[kind] if rec.get(f)]
    if kind == "mechanics":
        out += [("quotes", [s["quote"] for s in rec["sources"]]), ("readings", rec["formal"]["readings"])]
        if rec["formal"].get("parameters"):
            out.append(("parameters", rec["formal"]["parameters"]))
    if kind == "unknowns":
        out.append(("resolution_paths", rec["resolution_paths"]))
        if rec.get("readings"):
            out.append(("readings", rec["readings"]))
    if kind == "contradictions":
        out.append(("quotes", [s["quote"] for s in rec["sides"]]))
    return out


def main():
    problems = []
    tr = {}
    for f in sorted((ROOT / "ko" / "i18n").glob("*.yaml")):
        data = yaml.safe_load(f.read_text("utf-8")) or {}
        for k in data:
            if k in tr:
                problems.append(f"{f.name}: {k} also in another file")
        tr.update(data)
    known = set()
    for kind in FIELDS:
        for f in sorted((ROOT / "kb" / kind).glob("*.yaml")):
            rec = yaml.safe_load(f.read_text("utf-8"))
            known.add(rec["id"])
            t = tr.get(rec["id"]) or {}
            for field, en in pairs(rec, kind):
                ko = t.get(field)
                where = f"{rec['id']}.{field}"
                if isinstance(en, str):
                    if not isinstance(ko, str):
                        problems.append(f"{where}: missing")
                    else:
                        compare(where, en, ko, problems)
                elif isinstance(en, list):
                    if not (isinstance(ko, list) and len(ko) == len(en)):
                        problems.append(f"{where}: missing or wrong length")
                    else:
                        for n, (a, b) in enumerate(zip(en, ko)):
                            compare(f"{where}[{n}]", a, str(b), problems)
                else:
                    if not (isinstance(ko, dict) and set(ko) == set(en)):
                        problems.append(f"{where}: missing or other keys")
                    else:
                        for k in en:
                            compare(f"{where}.{k}", en[k], str(ko[k]), problems)
    intros = yaml.safe_load((ROOT / "codex" / "intros.yaml").read_text("utf-8"))
    for k, en in intros.items():
        known.add(k)
        if not isinstance(tr.get(k), str):
            problems.append(f"{k}: missing")
        else:
            compare(k, en, tr[k], problems)
    problems += [f"{k}: not a kb record or intro key" for k in tr if k not in known]
    for en_path in [ROOT / "README.md"] + sorted((ROOT / "theory").glob("*.md")):
        rel = en_path.relative_to(ROOT)
        ko_path = ROOT / "ko" / rel
        if not ko_path.exists():
            problems.append(f"ko/{rel.as_posix()}: missing")
            continue
        en, ko = en_path.read_text("utf-8"), ko_path.read_text("utf-8")
        compare(f"ko/{rel.as_posix()}", en, ko, problems)
        for mark, pat in (("$", r"\$"), ("```", r"```"), ("headings", r"(?m)^#+ ")):
            if len(re.findall(pat, en)) != len(re.findall(pat, ko)):
                problems.append(f"ko/{rel.as_posix()}: {mark} count {len(re.findall(pat, en))} in English, {len(re.findall(pat, ko))} in Korean")
    if "--file" in sys.argv:  # only the problems of one translator's file: its keys, or its own path
        target = sys.argv[sys.argv.index("--file") + 1].replace("\\", "/")
        tp = ROOT / target
        keys = set(yaml.safe_load(tp.read_text("utf-8")) or {}) if tp.suffix == ".yaml" and tp.exists() else set()
        problems = [p for p in problems if p.split(": ")[0].split(".")[0].split("[")[0] in keys or p.startswith(target)]
    if "--quiet" not in sys.argv or not problems:
        for p in problems:
            print(p)
    print(f"check_ko: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
