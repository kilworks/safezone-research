"""Render a saved wiki page as plain text, one block per line, with [#anchor] markers.

Usage: py -3 tools/page_text.py <path/to/index.html>
Only <body> is rendered; <nav> and <footer> are skipped.
"""
import gzip
import sys
from pathlib import Path
from html.parser import HTMLParser

BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "dt", "dd", "div", "section", "br", "table", "figcaption", "summary"}
SKIP = {"script", "style", "svg", "noscript", "nav", "footer"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.cur, self.depth_main, self.skip = [], [], 0, 0

    def flush(self):
        line = " ".join("".join(self.cur).split())
        if line:
            self.out.append(line)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "body":
            self.depth_main += 1
        if tag in SKIP:
            self.skip += 1
        if not self.depth_main or self.skip:
            return
        if tag in BLOCK:
            self.flush()
        if a.get("id"):
            self.cur.append(f"[#{a['id']}] ")
        if tag in ("td", "th"):
            self.cur.append(" | ")
        if tag == "img" and a.get("alt"):
            self.cur.append(f"[img:{a['alt']}]")

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip -= 1
        if self.depth_main and not self.skip and tag in BLOCK:
            self.flush()
        if tag == "body":
            self.flush()
            self.depth_main -= 1

    def handle_data(self, data):
        if self.depth_main and not self.skip:
            self.cur.append(data)


def render(path):
    p = Text()
    raw = Path(path).read_bytes()
    if raw[:2] == bytes([0x1F, 0x8B]):
        raw = gzip.decompress(raw)  # Wayback id_ captures keep the original Content-Encoding
    p.feed(raw.decode("utf-8", "replace"))
    p.flush()
    return p.out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(render(sys.argv[1])))
