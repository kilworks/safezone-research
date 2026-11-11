"""Split each saved wiki page into atomic clauses (Phase 1, Clause Extractor role).

Mechanical, no interpretation: one clause per sentence or table row, with the
anchor and section heading it sits under and its verbatim text. Writes
corpus/clauses/<page>.yaml and prints the clause count per page.

Usage: py -3 tools/extract_clauses.py <snapshot-date>
"""
import json
import re
import sys
from pathlib import Path

import yaml

from page_text import render

ROOT = Path(__file__).resolve().parent.parent
HEADER_LINES = 3  # "Ice Poseidon", logo, menu id: site chrome before the page title
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"(])")


def slug(url):
    return url.split("/safezone", 1)[1].strip("/").replace("/", "-") or "overview"


def clauses_of(lines):
    out, anchor, section, after_anchor = [], None, None, False
    for line in lines[HEADER_LINES:]:
        m = re.match(r"^\[#([^\]]+)\]\s*(.*)$", line)
        if m:
            anchor, rest, after_anchor = m.group(1), m.group(2), True
            if not rest:
                continue
            line = rest
        if section is None or after_anchor:
            section, after_anchor = line, False  # first line of the page or of an anchored block is a heading
            continue
        if line.strip("| ") == "":
            continue  # empty table cell separator
        if line.startswith("|"):
            parts = [line]
        else:
            parts = [s for s in SENTENCE_END.split(line) if s.strip()]
        for p in parts:
            kind = "row" if p.startswith("|") else "sentence" if re.search(r"[.!?:]$", p) else "label"
            out.append({"anchor": anchor, "section": section, "kind": kind, "quote": p.strip()})
    return out


def main(date):
    manifest = json.loads((ROOT / "corpus" / "manifest.json").read_text("utf-8"))
    pages = [e for e in manifest if e["date"] == date and e.get("status") == 200
             and "/safezone" in e["url"] and e["path"].endswith("index.html")]
    outdir = ROOT / "corpus" / "clauses"
    outdir.mkdir(parents=True, exist_ok=True)
    total = 0
    for e in sorted(pages, key=lambda e: e["url"]):
        lines = render(ROOT / e["path"])
        if len(lines) <= HEADER_LINES:
            print(f"{0:4d} {e['url']} (no content: redirect or empty)")
            continue
        s = slug(e["url"])
        cl = clauses_of(lines)
        for i, c in enumerate(cl, 1):
            c["id"] = f"{s}-{i:03d}"
        doc = {"page": e["url"], "snapshot": date, "sha256": e["sha256"], "title": lines[HEADER_LINES],
               "clauses": [{k: c[k] for k in ("id", "anchor", "section", "kind", "quote")} for c in cl]}
        (outdir / f"{s}.yaml").write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=1000),
                                          "utf-8", newline="\n")
        total += len(cl)
        print(f"{len(cl):4d} {e['url']}")
    print(f"{total:4d} total")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1])
