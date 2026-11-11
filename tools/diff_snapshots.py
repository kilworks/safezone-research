"""Record every text change of a wiki page across dated snapshots (corpus/diffs/).

Orders the Wayback captures and the live snapshot of each page, renders their
text, and writes one Markdown file per page with a line diff for each pair of
consecutive captures whose text differs. Captures with identical text are listed,
not diffed (Wayback digests also change on markup-only edits).

History only: the KB, theory and simulator use the live snapshot alone (kil, 2026-11-11).
Result blocks (placements, statistics, clips) are cut because they name contestants.

Usage: py -3 tools/diff_snapshots.py <live-date>
"""
import difflib
import json
import sys
from pathlib import Path

from page_text import render

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ("[#placements]", "Winner:")
OMITTED = "[event results, statistics and clips omitted: they name contestants]"


def redact(text):
    for n, line in enumerate(text):
        if line.startswith(RESULTS):
            return text[:n] + [OMITTED]
    return text


def main(live):
    man = json.loads((ROOT / "corpus" / "manifest.json").read_text("utf-8"))
    pages = {}
    for e in man:
        if e.get("status") != 200:
            continue
        url = e.get("original_url") or e["url"]
        if "/safezone" not in url or not e["path"].endswith("index.html"):
            continue
        if e["date"] == live or e["date"].startswith("wayback-"):
            stamp = e["date"].removeprefix("wayback-")
            stamp = stamp if e["date"] != live else live.replace("-", "") + "999999"
            pages.setdefault(url, []).append((stamp, e))
    outdir = ROOT / "corpus" / "diffs"
    outdir.mkdir(parents=True, exist_ok=True)
    for url, caps in sorted(pages.items()):
        if len(caps) < 2:
            continue
        caps.sort(key=lambda c: c[0])
        slug = url.split("/safezone", 1)[1].strip("/").replace("/", "-") or "overview"
        lines = [f"# Text changes: {url}", "",
                 f"{len(caps)} captures (Wayback `id_` originals, plus the live snapshot of {live}). "
                 "Navigation and site chrome are excluded; diff of rendered text only.", "",
                 "History only. These captures are not sources for the knowledge base, the theory or the simulator: "
                 f"only the {live} snapshot is (decision of the project owner, 2026-11-11).", ""]
        prev, prev_stamp, changes = None, None, 0
        for stamp, e in caps:
            text = redact(render(ROOT / e["path"])[3:])
            label = e["date"] if e["date"] == live else f"Wayback {stamp}"
            if prev is None:
                lines += [f"## {label}: first capture", "", "```", *text, "```", ""]
            elif text == prev:
                lines += [f"- {label}: text identical to {prev_stamp}", ""]
            else:
                changes += 1
                d = [l for l in difflib.unified_diff(prev, text, prev_stamp, label, lineterm="", n=0)
                     if not l.startswith("@@")]
                lines += [f"## {label}: changed since {prev_stamp}", "", "```diff", *d, "```", ""]
            prev, prev_stamp = text, label
        (outdir / f"{slug}.md").write_text("\n".join(lines), "utf-8", newline="\n")
        print(f"{changes:3d} text changes over {len(caps)} captures: {url}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1])
