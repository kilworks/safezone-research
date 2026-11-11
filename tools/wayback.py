"""Wayback Machine snapshots of the 19 wiki pages (SCOPE.md, Allowed 3).

For each page, lists captures with the CDX API, keeps one capture per distinct
content digest, fetches its original bytes (id_ form) at 1 request per second,
and records it in corpus/manifest.json with date = the capture timestamp.

Usage: py -3 tools/wayback.py
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import fetch_corpus as fc

PACE = 5.0
CDX = "https://web.archive.org/cdx/search/cdx?"


def captures(page_url):
    q = urllib.parse.urlencode({"url": page_url, "output": "json", "fl": "timestamp,digest,statuscode",
                                "filter": "statuscode:200", "collapse": "digest"})
    fc.fetch_wait()
    with urllib.request.urlopen(urllib.request.Request(CDX + q, headers={"User-Agent": fc.UA}), timeout=60) as r:
        rows = json.loads(r.read() or b"[]")
    return rows[1:]  # first row is the header


def polite(call, *args, **kw):
    """archive.org refuses connections above ~15 requests/min: pace at 5 s, back off on refusal."""
    for attempt in range(4):
        time.sleep(PACE)
        try:
            return call(*args, **kw)
        except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
            print("  retry after", 60 * (attempt + 1), "s:", e)
            time.sleep(60 * (attempt + 1))
    raise RuntimeError("archive.org unreachable")


def main():
    have = {e["url"] for e in json.loads(fc.MANIFEST.read_text("utf-8"))}
    for p in fc.PAGES:
        url = fc.HOST + p
        rows = polite(captures, url)
        print(len(rows), "distinct captures", url)
        entries = []
        for ts, digest, _ in rows:
            wb = f"https://web.archive.org/web/{ts}id_/{url}"
            if wb in have:
                continue
            e = polite(fc.fetch, f"wayback-{ts}", wb, save_as=url)
            e.update(original_url=url, wayback_digest=digest)
            entries.append(e)
            print(" ", e["status"], ts, e.get("bytes"))
        fc.save_manifest(entries)


if __name__ == "__main__":
    sys.exit(main())
