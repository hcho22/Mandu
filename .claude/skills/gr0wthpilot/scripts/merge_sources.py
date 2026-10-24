#!/usr/bin/env python3
"""Rebuild a Candidate Package's `sources.md` from its `sources.d/` fragments.

Parallel agents never write `sources.md` itself, since two of them would race:
each records the URLs it cites in its own fragment, `sources.d/<name>.md`, one
line per URL (`- URL - fetched YYYY-MM-DDTHH:MMZ - what it supports`). This
script merges every fragment into `sources.md`, one section per fragment, in
name order, dropping exact repeats within a fragment; a line two fragments
both carry stays in each one's section. Run it after every fan-out; the source
check refuses a fragment entry that `sources.md` does not carry.

Usage: merge_sources.py PACKAGE
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sources  # noqa: E402

HEADER = [
    "# Sources",
    "",
    "Every URL this Candidate Package cites, with the UTC time it was fetched in this run.",
    "A URL is listed only if it was fetched during the run; `scripts/check_sources.py` verifies that against the guard's own fetch log.",
    "This file is rebuilt from `sources.d/` by `scripts/merge_sources.py`; edit the fragments, not this file.",
]


def merge(pkg):
    pkg = Path(pkg)
    fragments = sorted((pkg / "sources.d").glob("*.md")) if (pkg / "sources.d").is_dir() else []
    lines, entries = list(HEADER), 0
    for fragment in fragments:
        seen, body = set(), []
        for line in fragment.read_text(encoding="utf-8").splitlines():
            if check_sources.ENTRY_RE.match(line) and line.strip() not in seen:
                seen.add(line.strip())
                body.append(line.strip())
        if body:
            lines += ["", "## %s" % fragment.stem, ""] + body
            entries += len(body)
    (pkg / "sources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"fragments": len(fragments), "entries": entries}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("package")
    args = parser.parse_args(argv)
    result = merge(args.package)
    print("merged %d entries from %d fragment(s) into sources.md" % (result["entries"], result["fragments"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
