"""Polite fetcher for the Safe Zone wiki corpus (SCOPE.md, Allowed 1 and 2).

Reads each URL like a browser would, at most 1 request per second, honoring
robots.txt. Saves bytes under corpus/raw/<date>/ (gitignored) and appends one
entry per URL to corpus/manifest.json: url, date, HTTP status, SHA-256, size.

Usage:
  py -3 tools/fetch_corpus.py <date> <url> [<url> ...]
  py -3 tools/fetch_corpus.py <date> --pages     # the 19 wiki pages + referenced assets
"""
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "corpus" / "manifest.json"
HOST = "https://iceposeidon.com"
UA = "safezone-research/0.1 (offline rule study; 1 req/s; contact via GitHub)"
PAGES = ["/safezone", "/safezone/wiki", "/safezone/wiki/strategy", "/safezone/wiki/sigils"] + [
    f"/safezone/wiki/sigils/{s}" for s in
    "piety greed ingenuity trolling death endurance necromancy protection healing".split()
] + [f"/safezone/wiki/{p}" for p in "items weapons damage poison zombies merchant attacks".split()]

_last = [0.0]
_robots = {}


def allowed(url):
    parts = urllib.parse.urlsplit(url)
    base = f"{parts.scheme}://{parts.netloc}"
    if base not in _robots:
        # read with our own UA: RobotFileParser.read() sends Python's default UA, which Cloudflare 403s
        rp = urllib.robotparser.RobotFileParser(base + "/robots.txt")
        try:
            with urllib.request.urlopen(urllib.request.Request(base + "/robots.txt", headers={"User-Agent": UA}), timeout=30) as r:
                rp.parse(r.read().decode("utf-8", "replace").splitlines())
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                rp.disallow_all = True
            else:
                rp = None  # 404 or other: no robots policy, allow all (RFC 9309)
        _robots[base] = rp
    rp = _robots[base]
    return rp is None or rp.can_fetch(UA, url)


def local_path(date, url):
    parts = urllib.parse.urlsplit(url)
    path = parts.path.lstrip("/") or "index"
    if path.endswith("/") or "." not in path.rsplit("/", 1)[-1]:
        path = path.rstrip("/") + "/index.html"
    return ROOT / "corpus" / "raw" / date / parts.netloc / path


def fetch(date, url):
    if not allowed(url):
        return {"url": url, "date": date, "status": "robots-disallowed"}
    wait = 1.0 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status, body, ctype = r.status, r.read(), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        status, body, ctype = e.code, e.read(), e.headers.get("Content-Type", "")
    finally:
        _last[0] = time.time()
    out = local_path(date, url)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(body)
    return {"url": url, "date": date, "status": status, "content_type": ctype,
            "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
            "path": out.relative_to(ROOT).as_posix()}


def referenced_assets(html, page_url):
    """Assets the page itself references: scripts, stylesheets, images, modulepreloads."""
    refs = set(re.findall(r'<script[^>]+src="([^"]+)"', html))
    refs |= set(re.findall(r'<link[^>]+href="([^"]+\.(?:css|js))"', html))
    refs |= set(re.findall(r'<img[^>]+src="([^"]+)"', html))
    urls = {urllib.parse.urljoin(page_url, r.replace("&amp;", "&")) for r in refs}
    return sorted(u for u in urls if u.startswith(HOST))


def save_manifest(entries):
    old = json.loads(MANIFEST.read_text("utf-8")) if MANIFEST.exists() else []
    keep = {(e["url"], e["date"]): e for e in old}
    for e in entries:
        keep[(e["url"], e["date"])] = e
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(sorted(keep.values(), key=lambda e: (e["date"], e["url"])),
                                   indent=1) + "\n", "utf-8", newline="\n")


def main(argv):
    date, rest = argv[0], argv[1:]
    entries = []
    if rest == ["--pages"]:
        assets = set()
        for p in PAGES:
            e = fetch(date, HOST + p)
            entries.append(e)
            print(e["status"], e.get("bytes"), e["url"])
            if e["status"] == 200:
                assets |= set(referenced_assets((ROOT / e["path"]).read_text("utf-8", "replace"), e["url"]))
        rest = sorted(assets)
    for u in rest:
        e = fetch(date, u)
        entries.append(e)
        print(e["status"], e.get("bytes"), e["url"])
    save_manifest(entries)


if __name__ == "__main__":
    main(sys.argv[1:])
