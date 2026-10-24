#!/usr/bin/env python3
"""List the key names in the `.env` files a run may use, never their values.

No new spending: a run may use a paid tool only when its key is already in the
Product's `.env`. This prints which keys exist, by name, so a run can decide
without a secret value ever entering its context, a file, or a log.

Usage: env_keys.py [--config FILE]     (defaults to the run's GR0WTHPILOT_CONFIG)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

KEY_RE = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")


def keys_in(path):
    names = []
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        m = KEY_RE.match(line)
        if m and m.group(2).strip().strip("'\""):
            names.append(m.group(1))
    return names


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config")
    args = parser.parse_args(argv)
    config = args.config or os.environ.get("GR0WTHPILOT_CONFIG")
    files = []
    if config and Path(config).is_file():
        files = json.loads(Path(config).read_text(encoding="utf-8")).get("env_files") or []
    found = {}
    for name in files:
        if Path(name).is_file():
            found[name] = keys_in(name)
    print(json.dumps({"env_files_checked": files, "keys_by_file": found,
                      "note": "names only; values are never printed"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
