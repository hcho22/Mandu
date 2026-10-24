#!/usr/bin/env python3
"""Source and link check for a Candidate Package.

Truth policy: every fact carries a URL fetched during the run, and a claim
whose URL was not fetched is deleted. This check makes that mechanical:

1. Every entry in `sources.md` is well formed:
   `- <URL> - fetched <YYYY-MM-DDTHH:MM[:SS]Z> - <what it supports>`.
2. Every entry was fetched in this run, by tool record rather than by anyone's
   say-so: the guard's WebFetch log (its live one during a run, which the run
   cannot write; otherwise the copy in `run-evidence/fetch-log.jsonl`) shows a
   2xx fetch, or the URL appears in last30days output whose SHA-256 the
   gp-last30days wrapper recorded.
   A URL whose only fetches failed is a dead link.
3. Every entry in a `sources.d/` fragment, where parallel agents record their
   URLs, has been merged into `sources.md` (scripts/merge_sources.py).
4. Every URL cited anywhere in the package is listed in `sources.md`, except
   namespace and font URLs and the prefixes `sources-exempt.md` lists with a
   reason. The run's machine records (`run-audit.md`, `run-evidence/`, the
   journal) are not claims and are not read for citations.

Usage: check_sources.py PACKAGE [--fetch-log FILE ...] [--last30days-log FILE ...] [--json]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

ENTRY_RE = re.compile(r"^\s*[-*]\s+(https?://\S+)\s+-\s+fetched\s+(\S+)\s+-\s+(\S.*)$")
LOOSE_ENTRY_RE = re.compile(r"^\s*[-*]\s+<?https?://")
EXEMPT_RE = re.compile(r"^\s*[-*]\s+(https?://\S+)\s+-\s+(\S.*)$")
BUILTIN_EXEMPT = (
    "http://www.w3.org/", "https://www.w3.org/", "http://schema.org", "https://schema.org",
    "https://fonts.googleapis.com", "https://fonts.gstatic.com", "http://localhost",
    "http://127.0.0.1", "https://localhost", "http://ns.adobe.com/", "http://purl.org/",
)
# Files that are evidence or machine records rather than claims.
SKIP_FILES = {"sources.md", "sources-exempt.md", gc.JOURNAL_NAME, gc.AUDIT_NAME}
SKIP_DIRS = ("run-evidence", "01-research/last30days", "sources.d")


def under_prefix(key, prefix):
    """Whether a normalized URL lies under an exempt prefix, matched at a path
    boundary: `.../r/testprod/` covers `.../r/testprod/comments/x`, not
    `.../r/testprodfans/`."""
    base = https(prefix)
    return key == base or (key.startswith(base) and key[len(base)] in "/?#:")


def https(url):
    url = gc.normalize_url(url)
    return "https://" + url[len("http://"):] if url.startswith("http://") else url


def parse_sources(pkg):
    path = pkg / "sources.md"
    entries, problems = {}, []
    if not path.is_file():
        return entries, ["sources.md is missing"]
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = ENTRY_RE.match(line)
        if m:
            url, stamp, what = gc.clean_url(m.group(1)), m.group(2), m.group(3)
            if gc.parse_iso_z(stamp) is None:
                problems.append("sources.md:%d: fetch time %r is not YYYY-MM-DDTHH:MMZ" % (number, stamp))
            entries.setdefault(https(url), []).append({"url": url, "line": number, "stamp": stamp, "what": what})
        elif LOOSE_ENTRY_RE.match(line):
            problems.append("sources.md:%d: malformed entry (want `- URL - fetched TIME - what it supports`)" % number)
    if not entries:
        problems.append("sources.md lists no sources")
    return entries, problems


def parse_exempt(pkg):
    path = pkg / "sources-exempt.md"
    prefixes, problems = list(BUILTIN_EXEMPT), []
    if path.is_file():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not LOOSE_ENTRY_RE.match(line):
                continue
            m = EXEMPT_RE.match(line)
            if not m or len(m.group(2).strip()) < 10:
                problems.append("sources-exempt.md:%d: each exempt prefix needs a reason" % number)
                continue
            prefixes.append(gc.clean_url(m.group(1)))
    return prefixes, problems


def run_config():
    config = os.environ.get("GR0WTHPILOT_CONFIG")
    return gc.read_json(Path(config)) if config and Path(config).is_file() else None


def default_logs(pkg, name, cfg):
    """During a run, only the live log its config names, which for WebFetch is
    the guard's own record; with no run config, the copy audit_run.py made in
    `run-evidence/`, which holds only that run's records."""
    return [Path(cfg[gc.RUN_LOGS[name]])] if cfg else [pkg / "run-evidence" / name]


def read_jsonl(paths, run_id=None):
    """The records in these logs; with a run id, only that run's (the logs
    are kept per Product, so they also hold earlier runs' records)."""
    for path in paths:
        if not Path(path).is_file():
            continue
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if isinstance(record, dict) and (not run_id or record.get("run_id") == run_id):
                yield record


def fetched_urls(fetch_logs, l30_logs, run_id=None):
    """Return {normalized url: [codes]} from the guard's WebFetch log, plus
    URLs inside verified last30days output (code 200), for this run only."""
    seen = {}
    for record in read_jsonl(fetch_logs, run_id):
        if record.get("url"):
            seen.setdefault(https(record["url"]), []).append(record.get("code"))
    for record in read_jsonl(l30_logs, run_id):
        for f in record.get("files") or []:
            p = Path(f.get("path", ""))
            if not p.is_file():
                continue
            data = p.read_bytes()
            if hashlib.sha256(data).hexdigest() != f.get("sha256"):
                continue
            for url in gc.find_urls(data.decode("utf-8", "replace")):
                seen.setdefault(https(url), []).append(200)
    return seen


def cited_urls(pkg):
    cited = {}
    for path in gc.package_text_files(pkg, skip_dirs=SKIP_DIRS):
        if path.name in SKIP_FILES or path.name.endswith(".jsonl"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            for url in gc.find_urls(line):
                cited.setdefault(https(url), []).append("%s:%d" % (gc.rel(pkg, path), number))
    return cited


def check(pkg, fetch_logs=None, l30_logs=None):
    pkg = Path(pkg)
    entries, problems = parse_sources(pkg)
    exempt, more = parse_exempt(pkg)
    problems += more
    cfg = run_config()
    fetched = fetched_urls(fetch_logs or default_logs(pkg, "fetch-log.jsonl", cfg),
                           l30_logs or default_logs(pkg, "last30days-log.jsonl", cfg),
                           cfg.get("run_id") if cfg else None)
    for key, rows in sorted(entries.items()):
        codes = fetched.get(key)
        where = "sources.md:%d" % rows[0]["line"]
        if not codes:
            problems.append("%s: %s was not fetched in this run (no WebFetch or last30days record); "
                            "fetch it or delete the claim" % (where, rows[0]["url"]))
        elif not any(isinstance(c, int) and 200 <= c < 300 for c in codes):
            problems.append("%s: %s is a dead or refused link (HTTP %s); delete the claim"
                            % (where, rows[0]["url"], ",".join(str(c) for c in codes)))
    fragments = sorted((pkg / "sources.d").glob("*.md")) if (pkg / "sources.d").is_dir() else []
    for fragment in fragments:
        for number, line in enumerate(fragment.read_text(encoding="utf-8").splitlines(), 1):
            m = ENTRY_RE.match(line)
            if m and https(m.group(1)) not in entries:
                problems.append("sources.d/%s:%d: %s is not in sources.md; run scripts/merge_sources.py"
                                % (fragment.name, number, m.group(1)))
    cited = cited_urls(pkg)
    for key, places in sorted(cited.items()):
        if key in entries or any(under_prefix(key, p) for p in exempt):
            continue
        problems.append("%s: %s is cited but not listed in sources.md" % (places[0], key))
    return {"sources": len(entries), "cited": len(cited), "problems": problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Source and link check for a Candidate Package")
    parser.add_argument("package")
    parser.add_argument("--fetch-log", action="append")
    parser.add_argument("--last30days-log", action="append")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package, args.fetch_log, args.last30days_log)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: %d sources, %d cited URLs, %d problem(s)" % (
            "PASS" if not result["problems"] else "FAIL", result["sources"], result["cited"],
            len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
