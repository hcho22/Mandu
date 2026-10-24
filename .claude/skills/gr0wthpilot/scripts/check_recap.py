#!/usr/bin/env python3
"""Recap check: `recap.html` is the Candidate Package's single front door.

It passes only when:
- every relative link and image in it resolves to a file or folder in the
  package, and
  every #anchor it names exists in the page it points at;
- it has the sections a reader needs, by id: `naming` (the naming verdict),
  `thesis`, `objection` (the strongest surviving objection, beside the thesis),
  `deliverables` (the deliverables map), and `handoff`;
- the naming section says clearance is UNVERIFIED;
- the handoff section holds the package's ready one-line Handoff word for
  word, and no other: `<Product> - hand to gr0wthlab` for `gtm/`, or
  `<Product> - hand to gr0wthlab (<folder>)` for a dated candidate folder. A
  package the run journal marks `beside-live` sits beside the Product's live
  package and cannot be handed off yet, so its handoff section holds no
  Handoff line at all;
- the deliverables map links every numbered folder the package has, every
  extra in `09-extras/`, and the package's records.

Usage: check_recap.py PACKAGE --product NAME [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

SECTIONS = ("naming", "thesis", "objection", "deliverables", "handoff")
RECORDS = ("README.md", "decisions-log.md", "sources.md", "self-grade.md", "launch-checklist.md",
           gc.AUDIT_NAME, "handoff/registry-entry.json", gc.JOURNAL_NAME)


class _Sections(gc._TextAndLinks):
    """Collect the text and links inside each element whose id is a section."""

    def __init__(self):
        super().__init__()
        self.stack = []
        self.section_text = {}
        self.section_links = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        super().handle_starttag(tag, attrs)
        if tag in ("br", "img", "meta", "link", "input", "hr", "source"):
            if self.stack and a.get("href" if tag == "link" else "src"):
                for name in self.open_sections():
                    self.section_links[name].append(a.get("src") or a.get("href"))
            return
        self.stack.append((tag, a.get("id") if a.get("id") in SECTIONS else None))
        if a.get("id") in SECTIONS:
            self.section_text.setdefault(a["id"], [])
            self.section_links.setdefault(a["id"], [])
        if a.get("href"):
            for name in self.open_sections():
                self.section_links[name].append(a["href"])

    def handle_endtag(self, tag):
        super().handle_endtag(tag)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        super().handle_data(data)
        for name in self.open_sections():
            self.section_text[name].append(data)

    def open_sections(self):
        return [name for _, name in self.stack if name]


def link_target(pkg, base, href):
    parsed = urllib.parse.urlsplit(href)
    if parsed.scheme or href.startswith(("//", "mailto:", "tel:", "data:", "javascript:")):
        return None, None
    path = urllib.parse.unquote(parsed.path)
    target = (base.parent / path).resolve() if path else base.resolve()
    return target, parsed.fragment or None


def ids_of(path):
    if path.suffix.lower() not in (".html", ".htm"):
        return None
    return gc.read_html(path.read_text(encoding="utf-8", errors="replace")).ids


def check(pkg, product):
    pkg = Path(pkg)
    recap = pkg / "recap.html"
    if not recap.is_file():
        return {"links": 0, "problems": ["recap.html is missing"]}
    text = recap.read_text(encoding="utf-8")
    parser = _Sections()
    parser.feed(text)
    parser.close()
    problems = []
    checked = 0
    for tag, key, href in parser.links:
        target, fragment = link_target(pkg, recap, href)
        if target is None:
            continue
        checked += 1
        try:
            target.relative_to(pkg.resolve())
        except ValueError:
            problems.append("recap.html links outside the package: %s" % href)
            continue
        if not target.exists():
            problems.append("recap.html: %s %s does not resolve" % (key, href))
            continue
        if fragment and target.is_file():
            ids = ids_of(target)
            if ids is not None and fragment not in ids:
                problems.append("recap.html: %s points at #%s, which %s does not have" % (href, fragment, target.name))
    for name in SECTIONS:
        if name not in parser.section_text:
            problems.append("recap.html has no element with id=\"%s\"" % name)
    naming = " ".join(" ".join(parser.section_text.get("naming", [])).split())
    if "naming" in parser.section_text and "UNVERIFIED" not in naming:
        problems.append("recap.html naming section must say trademark and store-name clearance are UNVERIFIED")
    handoff = " ".join(" ".join(parser.section_text.get("handoff", [])).split())
    line = gc.handoff_line(product, pkg.resolve().name)
    beside_live = (gc.load_journal(pkg) or {}).get("kind") == "beside-live"
    given = re.findall(r"(?<![\w-])%s - hand to gr0wthlab(?: \([^)]*\))?" % re.escape(product), handoff)
    if "handoff" in parser.section_text and beside_live and given:
        problems.append("recap.html handoff section holds %r, but a package beside a live one has no ready "
                        "Handoff line" % given[0])
    elif "handoff" in parser.section_text and not beside_live and (not given or set(given) != {line}):
        problems.append("recap.html handoff section must hold the line %r word for word, and no other Handoff "
                        "line" % line)
    mapped = set()
    for href in parser.section_links.get("deliverables", []):
        target, _ = link_target(pkg, recap, href)
        if target is not None and target.exists():
            mapped.add(target)
    def linked(path):
        resolved = path.resolve()
        return any(t == resolved or gc.rel(pkg, t).startswith(gc.rel(pkg, resolved) + "/") for t in mapped)
    for folder in sorted(p for p in pkg.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
        if not linked(folder):
            problems.append("the deliverables map does not link %s/" % folder.name)
    extras = pkg / "09-extras"
    if extras.is_dir():
        for item in sorted(p for p in extras.iterdir() if not p.name.startswith(".")):
            if not linked(item):
                problems.append("the deliverables map does not link the extra 09-extras/%s" % item.name)
    for name in RECORDS:
        if (pkg / name).exists() and not linked(pkg / name):
            problems.append("the deliverables map does not link %s" % name)
    return {"links": checked, "problems": problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Recap check")
    parser.add_argument("package")
    parser.add_argument("--product", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package, args.product)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: %d links checked, %d problem(s)" % ("PASS" if not result["problems"] else "FAIL",
                                                      result["links"], len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
