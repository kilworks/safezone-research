"""Build the generated part of codex/ from kb/ and theory/ (Phase 8, Editor role, no new facts).

Writes:
  codex/rules/<family>.md   every mechanic of a family, in the template of master prompt section 10
  codex/sigils/<sigil>.md   every mechanic that names the sigil
  codex/theorems/T-xxxx.md  each theorem, extracted verbatim from theory/*.md
  codex/unknowns.md         every open question and contradiction, by priority
Every line that carries a number also carries the ID it comes from, so
tools/check_codex.py can trace it. Hand-written pages (codex/index.md,
codex/strategy/) are not touched.

Usage: py -3 tools/build_codex.py
"""
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CODEX = ROOT / "codex"
STRENGTH = ["UNKNOWN", "CONTRADICTED", "HYPOTHESIS", "CONDITIONAL", "DERIVED", "DOCUMENTED", "CORROBORATED"]
PRIORITY = ["critical", "high", "medium", "low"]
SIGILS = ["piety", "greed", "ingenuity", "trolling", "death", "endurance", "necromancy", "protection", "healing"]


def load(kind):
    return {r["id"]: r for r in (yaml.safe_load(f.read_text("utf-8")) for f in sorted((ROOT / "kb" / kind).glob("*.yaml")))}


def lowest(labels):
    return min(labels, key=STRENGTH.index) if labels else "UNKNOWN"


def unknown_link(u, depth="../"):
    return f"[{u}]({depth}unknowns.md#{u.lower()})"


def mechanic_block(m, unknowns, contra_by_mech, theorems_by_mech):
    mid = m["id"]
    out = [f'<a id="{mid.lower()}"></a>', "", f"### {mid}: {m['name']}", "", f"Label: `{m['label']}`. Sigils: {', '.join(m['sigils'])}.", "",
           "**Official text** (snapshot 2026-11-11):", ""]
    for s in m["sources"]:
        out.append(f"- {mid} `{s['clause']}`: \"{s['quote']}\" ([source]({s['url']}))")
    out += ["", "**Formal model:**", ""]
    for k, v in m["formal"]["readings"].items():
        out.append(f"- {mid} reading {k}: `{v}`")
    if m["formal"].get("domain"):
        out.append(f"- {mid} domain: {m['formal']['domain']}")
    for k, v in (m["formal"].get("parameters") or {}).items():
        out.append(f"- {mid} parameter `{k}`: {v}")
    if theorems_by_mech.get(mid):
        out += ["", "**Consequences:** " + ", ".join(f"[{t}](../theorems/{t}.md)" for t in sorted(theorems_by_mech[mid]))]
    links = sorted(set(m.get("depends_on", []) + m.get("interacts_with", [])))
    if links:
        out += ["", "**Interactions:** " + ", ".join(links)]
    opens = m.get("open_unknowns", [])
    if opens:
        out += ["", "**Open questions:**", ""]
        out += [f"- {unknown_link(u)} ({unknowns[u]['priority']}): {unknowns[u]['question']}" for u in opens if u in unknowns]
    if contra_by_mech.get(mid):
        out += ["", "**Contradictions:** " + ", ".join(f"{unknown_link(c)}" for c in sorted(contra_by_mech[mid]))]
    if m.get("notes"):
        out += ["", f"Notes ({mid}): " + " ".join(m["notes"].split())]
    return out + [""]


def page(title, mechs, unknowns, contra_by_mech, theorems_by_mech, intro):
    labels = [m["label"] for m in mechs]
    counts = ", ".join(f"{labels.count(l)} `{l}`" for l in reversed(STRENGTH) if labels.count(l))
    opens = sorted({u for m in mechs for u in m.get("open_unknowns", [])})
    tested = sorted({t for m in mechs for t in theorems_by_mech.get(m["id"], [])})
    out = [f"# {title}", "", "## Summary", "", intro, "",
           f"This page gathers {len(mechs)} rules ({counts}). Every rule below quotes the official wiki word for word "
           "and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.", "",
           "## Rules", ""]
    for m in mechs:
        out += mechanic_block(m, unknowns, contra_by_mech, theorems_by_mech)
    out += ["## Simulation check", "",
            ("Theorems with tests in `sim/tests/`: " + ", ".join(f"[{t}](../theorems/{t}.md)" for t in tested)) if tested
            else "No theorem or simulation covers this page yet.", "",
            "## Open questions", "", ", ".join(unknown_link(u) for u in opens) if opens else "None.", "",
            "## Confidence", "", f"`{lowest(labels)}`: the lowest label among the rules on this page.", ""]
    return "\n".join(out)


def theorems():
    """Extract each '**Theorem T-xxxx' section verbatim from theory/*.md, with its file and cited mechanics."""
    found = {}
    for f in sorted((ROOT / "theory").glob("*.md")):
        text = f.read_text("utf-8")
        starts = [m.start() for m in re.finditer(r"^\*\*Theorem T-\d{4}", text, re.M)]
        for i, s in enumerate(starts):
            nxt = [p for p in (text.find("\n## ", s), text.find("\n### ", s),
                               starts[i + 1] if i + 1 < len(starts) else -1) if p > 0]
            body = text[s:min(nxt) if nxt else len(text)].strip()
            tid = re.match(r"\*\*Theorem (T-\d{4})", body).group(1)
            found[tid] = (f.name, body, set(re.findall(r"\bM-\d{4}\b", body)))
    return found


ID = re.compile(r"(?<![\[#/\w-])([MUCT])-(\d{4})\b(?!\])")


def linkify(text, prefix, family_of):
    """Make every M-, U-, C-, T- id a link; prefix is the path from the page to codex/. Headings stay plain."""
    def sub(m):
        i = f"{m.group(1)}-{m.group(2)}"
        if m.group(1) == "M":
            fam = family_of.get(i)
            return f"[{i}]({prefix}rules/{fam}.md#{i.lower()})" if fam else i
        if m.group(1) == "T":
            return f"[{i}]({prefix}theorems/{i}.md)"
        return f"[{i}]({prefix}unknowns.md#{i.lower()})"
    return "\n".join(l if l.startswith(("#", "<a ")) else ID.sub(sub, l) for l in text.split("\n"))


def plain(intros, key):
    text = (intros or {}).get(key)
    return f"\n\n### In plain words\n\n{text.strip()}" if text else ""


def write(path, text, prefix, family_of):
    path.write_text(linkify(text, prefix, family_of), "utf-8", newline="\n")


def main():
    mechs, unknowns, contras = load("mechanics"), load("unknowns"), load("contradictions")
    family_of = {m["id"]: m["family"] for m in mechs.values()}
    ipath = CODEX / "intros.yaml"  # hand-written plain-language explanations, every fact tagged with its id
    intros = yaml.safe_load(ipath.read_text("utf-8")) if ipath.exists() else {}
    contra_by_mech = defaultdict(set)
    for c in contras.values():
        for m in c.get("mechanics", []):
            contra_by_mech[m].add(c["id"])
    thms = theorems()
    theorems_by_mech = defaultdict(set)
    for tid, (_, _, ms) in thms.items():
        for m in ms:
            theorems_by_mech[m].add(tid)
    for sub in ("rules", "sigils", "theorems"):
        (CODEX / sub).mkdir(parents=True, exist_ok=True)

    families = defaultdict(list)
    for m in mechs.values():
        families[m["family"]].append(m)
    for fam, ms in sorted(families.items()):
        intro = f"Rules of the `{fam}` family, as the wiki states them on 2026-11-11." + plain(intros, f"family:{fam}")
        write(CODEX / "rules" / f"{fam}.md", page(f"Rules: {fam}", ms, unknowns, contra_by_mech, theorems_by_mech, intro), "../", family_of)
    for s in SIGILS:
        ms = [m for m in mechs.values() if s in m["sigils"]]
        intro = f"Rules that name the Sigil of {s.capitalize()}, as the wiki states them on 2026-11-11." + plain(intros, f"sigil:{s}")
        write(CODEX / "sigils" / f"{s}.md", page(f"Sigil of {s.capitalize()}", ms, unknowns, contra_by_mech, theorems_by_mech, intro), "../", family_of)
    for tid, (fname, body, _) in sorted(thms.items()):
        write(CODEX / "theorems" / f"{tid}.md", 
            f"# {tid}\n\nExtracted from [theory/{fname}](../../theory/{fname}), where the full context, the proof and the test are.\n\n"
            + body.replace("](", "](../../theory/").replace("](../../theory/http", "](http") + "\n", "../", family_of)

    out = ["# Open questions and contradictions", "",
           "Everything the official wiki leaves undecided, as of the 2026-11-11 snapshot. Each question lists the competing readings and "
           "what would settle it. No model in this project picks a reading silently: every simulation is run under each reading that matters.", ""]
    counts = {p: sum(1 for u in unknowns.values() if u["priority"] == p and u["status"] == "open") for p in PRIORITY}
    out += ["Open questions by priority: " + ", ".join(f"{counts[p]} {p}" for p in PRIORITY) + f" (source: kb/unknowns/, {len(unknowns)} records).", ""]
    for p in PRIORITY:
        out += [f"## Priority: {p}", ""]
        for u in sorted((u for u in unknowns.values() if u["priority"] == p), key=lambda u: u["id"]):
            out += [f"### {u['id']}", "", f"{u['id']}: {u['question']} Status: `{u['status']}`.", "",
                    f"Why it matters ({u['id']}): {u['why_it_matters']}", ""]
            for k, v in (u.get("readings") or {}).items():
                out.append(f"- {u['id']} reading {k}: {v}")
            if u.get("parameter"):
                out.append(f"- {u['id']} free parameter `{u['parameter']}`, swept over {u.get('sweep_range', 'a range to be set')}")
            out += [f"- {u['id']} resolution: {r}" for r in u["resolution_paths"]]
            if u.get("resolution"):
                out.append(f"- {u['id']} resolved: {u['resolution']}")
            out.append("")
    out += ["## Contradictions between pages", ""]
    for c in sorted(contras.values(), key=lambda c: c["id"]):
        out += [f"### {c['id']}", "", f"{c['id']}: {c['summary']} Status: `{c['status']}`.", ""]
        out += [f"- {c['id']} `{s['clause']}`: \"{s['quote']}\" ([source]({s['url']}))" for s in c["sides"]]
        out.append("")
    write(CODEX / "unknowns.md", "\n".join(out), "", family_of)
    idx = ["# Safe Zone Codex: index", "",
           "Everything in this encyclopedia, one click away. Rules are quoted word for word from the official wiki "
           "(snapshot 2026-11-11), translated into formulas, and every ambiguity is listed as an open question. "
           "Labels: `DOCUMENTED` (the wiki says it), `DERIVED` (proven), `CONDITIONAL` (proven under one reading of an open question), "
           "`CONTRADICTED` (two pages disagree), `UNKNOWN`. Back to the [project README](../README.md).", "",
           "## Sigils", ""] + [f"- [Sigil of {s.capitalize()}](sigils/{s}.md)" for s in SIGILS]
    idx += ["", "## Rules by family", ""] + [f"- [{f}](rules/{f}.md): {len(ms)} rules" for f, ms in sorted(families.items())]
    idx += ["", "## Theorems", ""] + [f"- {t}: from theory/{thms[t][0]}" for t in sorted(thms)]
    idx += ["", "## Open questions", "", "- [All open questions and contradictions](unknowns.md)", "",
            "## Every rule", ""] + [f"- {m['id']}: {m['name']} (`{m['label']}`)" for m in sorted(mechs.values(), key=lambda m: m["id"])]
    write(CODEX / "index.md", "\n".join(idx) + "\n", "", family_of)
    print(f"rules {len(families)} pages, sigils {len(SIGILS)}, theorems {len(thms)}, unknowns {len(unknowns)}, contradictions {len(contras)}")


if __name__ == "__main__":
    main()
