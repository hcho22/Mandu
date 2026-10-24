#!/usr/bin/env python3
"""Run every Candidate Package check at once: sources and links, the claim
audit, the layout check (writing the Handoff registry entry when it passes),
the brand lint, the site screenshot gate, the Launch Set gate, the video gate,
and the recap check. Phase 5's package gate runs exactly this.

Usage: check_all.py PACKAGE --product NAME
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import journal  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("package")
    parser.add_argument("--product", required=True)
    args = parser.parse_args(argv)
    problems = journal.all_checks(Path(args.package).resolve(), {"product": args.product})
    for problem in problems:
        print("FAIL " + problem)
    print("%s: %d problem(s)" % ("PASS" if not problems else "FAIL", len(problems)))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
