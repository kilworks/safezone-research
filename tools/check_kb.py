"""Validate kb/ against kb/schema.json and the clause corpus.

Fails (exit 1) when: a record breaks the schema; a file name does not match its id;
an ID referenced anywhere does not exist; a source quote is not a verbatim
substring of the clause it cites; a clause is cited by no mechanic and not listed
in kb/flavor.yaml (only with --coverage).

Usage: py -3 tools/check_kb.py [--coverage]
"""
import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "kb"
KINDS = {"mechanics": "mechanic", "unknowns": "unknown", "evidence": "evidence", "contradictions": "contradiction"}
SNAPSHOT = "2026-11-11"  # the only rule source; Wayback captures are history (corpus/diffs/), decided by kil 2026-11-11
REF = re.compile(r"\b([MUECTH])-([0-9]{4})\b")


def load_clauses():
    out = {}
    for f in sorted((ROOT / "corpus" / "clauses").glob("*.yaml")):
        doc = yaml.safe_load(f.read_text("utf-8"))
        for c in doc["clauses"]:
            out[c["id"]] = (doc["page"], c["quote"])
    return out


def norm(s):
    return " ".join(s.split())


def theorem_ids():
    ids = set()
    for f in (ROOT / "theory").glob("*.md") if (ROOT / "theory").exists() else []:
        ids |= {f"T-{n}" for n in re.findall(r"\*\*Theorem T-([0-9]{4})", f.read_text("utf-8"))}
    return ids


def main(argv):
    schema = json.loads((KB / "schema.json").read_text("utf-8"))
    clauses = load_clauses()
    errors, records = [], {}
    for d, kind in KINDS.items():
        sub = {"$ref": f"#/$defs/{kind}", "$defs": schema["$defs"]}
        for f in sorted((KB / d).glob("*.yaml")) if (KB / d).exists() else []:
            try:
                rec = yaml.safe_load(f.read_text("utf-8"))
                jsonschema.validate(rec, sub)
            except Exception as e:  # report every bad file, keep going
                errors.append(f"{f.relative_to(ROOT)}: {str(e).splitlines()[0]}")
                continue
            if f.stem != rec["id"]:
                errors.append(f"{f.relative_to(ROOT)}: id {rec['id']} does not match file name")
            if rec["id"] in records:
                errors.append(f"{f.relative_to(ROOT)}: duplicate id {rec['id']}")
            records[rec["id"]] = (f, rec)
    known = set(records) | theorem_ids()
    hyp = set()
    for f in (ROOT / "theory").glob("*.md") if (ROOT / "theory").exists() else []:
        hyp |= {f"H-{n}" for n in re.findall(r"\bH-([0-9]{4})\b", f.read_text("utf-8"))}
    cited = set()
    for rid, (f, rec) in records.items():
        for s in rec.get("sources", []) + rec.get("sides", []):
            cited.add(s["clause"])
            if s["clause"] not in clauses:
                errors.append(f"{rid}: clause {s['clause']} does not exist")
                continue
            page, text = clauses[s["clause"]]
            if norm(s["quote"]) not in norm(text):
                errors.append(f"{rid}: quote is not verbatim in {s['clause']}: {s['quote'][:60]!r}")
            if s["snapshot"] != SNAPSHOT:
                errors.append(f"{rid}: source snapshot {s['snapshot']} is not {SNAPSHOT} (older captures are history only)")
            if s["url"].split("#")[0].rstrip("/") != page.rstrip("/"):
                errors.append(f"{rid}: url {s['url']} is not the page of {s['clause']}")
        if rec.get("label") == "DOCUMENTED" and not rec.get("sources"):
            errors.append(f"{rid}: DOCUMENTED without a verbatim source")
        body = yaml.safe_dump({k: v for k, v in rec.items() if k != "id"}, allow_unicode=True)
        for letter, num in REF.findall(body):
            ref = f"{letter}-{num}"
            if letter == "H":
                continue  # hypotheses live in theory/, checked there
            if ref not in known:
                errors.append(f"{rid}: dangling reference {ref}")
    flavor_file = KB / "flavor.yaml"
    flavor = yaml.safe_load(flavor_file.read_text("utf-8"))["clauses"] if flavor_file.exists() else {}
    for c in flavor:
        if c not in clauses:
            errors.append(f"kb/flavor.yaml: clause {c} does not exist")
    uncovered = sorted(set(clauses) - cited - set(flavor))
    if "--coverage" in argv and uncovered:
        errors.append(f"{len(uncovered)} clauses neither formalized nor flavor: {', '.join(uncovered[:15])}...")
    counts = {d: sum(1 for r in records if r.startswith(k)) for d, k in
              [("mechanics", "M-"), ("unknowns", "U-"), ("evidence", "E-"), ("contradictions", "C-")]}
    print(f"records {counts}; clauses {len(clauses)}, cited {len(cited & set(clauses))}, flavor {len(flavor)}, uncovered {len(uncovered)}")
    for e in errors:
        print("ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
