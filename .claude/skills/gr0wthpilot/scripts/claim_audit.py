#!/usr/bin/env python3
"""Claim audit for a Candidate Package.

Two checks, both from the truth policy (facts, numbers, quotes, and competitor
details are never invented; guesses are labeled):

1. The claims ledger, `08-redteam/claims-ledger.md`, holds every load-bearing
   claim with its source and the skeptics' verdict. Each row needs a source (a
   URL or a `repo:` path), a verdict of STANDS, WEAKENED, or REFUTED, and a
   "Shipped as" cell; a REFUTED claim ships nowhere.
2. Every stat-like sentence anywhere in the package (a percentage, a price, a
   multiplier, a count of users or reviews, a rating, a ranking, "studies
   show", "the only app") carries, in the same line or text block, a citation
   or a label:
     - a URL, a `repo:path` reference into the Product's repository, a link
       to a file in `01-research/`, `sources.md`, or the claims ledger, or a
       source key the same file defines as a Markdown reference line,
       `[L]: https://...`, cited as `[L]` (or as a bare `L` in a Source column);
     - [ASSUMPTION ...], [PROJECTION ...], [TARGET ...], [PROPOSAL ...], or
       [DECIDED BY AGENT ...].
   Table cells under a column for scores, weights, signals, kill criteria,
   targets, thresholds, or budgets are the run's own numbers and are skipped.

Usage: claim_audit.py PACKAGE [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

LEDGER = "08-redteam/claims-ledger.md"
LEDGER_COLUMNS = ("ID", "Claim", "Source", "Verdict", "Shipped")
VERDICTS = ("STANDS", "WEAKENED", "REFUTED")

TRIGGERS = [
    ("percentage", re.compile(r"(?<![\w.])\d+(?:\.\d+)?\s?%")),
    ("price", re.compile(r"[$€£¥]\s?\d")),
    ("multiplier", re.compile(r"(?<![\w.])\d+(?:\.\d+)?x\b(?!\s?\d)", re.I)),
    ("count", re.compile(
        r"(?<![\w.])\d[\d,.]*\s?(?:k|m|b|thousand|million|billion)?\+?\s+(?:monthly\s+|daily\s+|active\s+)?"
        r"(?:users|people|downloads|installs|reviews|ratings|subscribers|followers|customers|members|"
        r"creators|searches|visits|visitors|views|apps|photographers|teams|companies|developers|"
        r"respondents|adults|americans|students|parents)\b", re.I)),
    ("rating", re.compile(r"(?<![\w.])\d(?:\.\d)?\s?(?:stars?\b|★|/\s?5\b)", re.I)),
    ("ranking", re.compile(r"\b(?:ranked|ranks|ranking)\s+(?:#|no\.?\s?)?\d+|#\d+\s+in\s+[A-Z]", re.I)),
    ("research", re.compile(r"\b(?:studies show|research shows|according to|study found|"
                            r"survey(?:s|ed)? (?:show|found)|data shows|experts say)\b", re.I)),
    ("superlative", re.compile(r"\b(?:the only (?:app|tool|product|camera)|the first (?:app|tool)|"
                               r"no other app|market leader|fastest[- ]growing|most popular|"
                               r"number one|#1 app)\b", re.I)),
]
LABEL_RE = re.compile(r"\[(?:ASSUMPTION|PROJECTION|TARGET|PROPOSAL|DECIDED BY AGENT)\b", re.I)
REPO_RE = re.compile(r"\brepo:\s?[\w./-]+")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)|href=\"([^\"]+)\"")
OWN_NUMBER_COLUMN = re.compile(
    r"score|weight|signal|kill|target|threshold|floor|budget|goal|margin|points|rubric|rank|"
    r"total|day|slot|duration|length|size|budget", re.I)
SKIP_DIRS = ("run-evidence", "01-research/last30days")
SKIP_NAMES = {"sources.md", "sources-exempt.md", gc.JOURNAL_NAME, "claims-ledger.md"}
SCAN_SUFFIXES = {".md", ".html", ".htm", ".txt"}


REF_DEF_RE = re.compile(r"^\s*\[([^\]\s]{1,40})\]:\s*(?:<)?https?://\S+", re.M)


def source_keys(text):
    """Source keys a file defines as Markdown reference lines: `[L]: https://...`."""
    return set(REF_DEF_RE.findall(text))


def cites(text, pkg, path, keys=()):
    if gc.URL_RE.search(text) or LABEL_RE.search(text) or REPO_RE.search(text):
        return True
    if keys and any(k in keys for k in re.findall(r"\[([^\]\s]{1,40})\]", text)):
        return True
    for m in LINK_RE.finditer(text):
        target = (m.group(1) or m.group(2) or "").split("#", 1)[0]
        if not target or target.startswith(("http", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            relative = str(resolved.relative_to(pkg.resolve()))
        except ValueError:
            continue
        if resolved.exists() and (relative.startswith("01-research/") or relative in ("sources.md", LEDGER)):
            return True
    return False


def triggers_in(text):
    return [name for name, regex in TRIGGERS if regex.search(text)]


def table_cells(line, header):
    cells = gc.split_cells(line)
    if not header or len(cells) != len(header):
        return [(None, line)]
    return list(zip(header, cells))


def audit_markdown(pkg, path, text, problems):
    keys = source_keys(text)
    header = None
    lines = text.splitlines()
    in_fence = in_comment = False
    block_quote = []
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if "<!--" in stripped and "-->" not in stripped:
            in_comment = True
        if in_comment:
            if "-->" in stripped:
                in_comment = False
            continue
        if stripped.startswith("|"):
            nxt = lines[number] if number < len(lines) else ""
            if gc.SEPARATOR_RE.fullmatch(nxt.strip()):
                header = gc.split_cells(line)
                continue
            if gc.SEPARATOR_RE.fullmatch(stripped):
                continue
            row_cites = cites(line, pkg, path, keys)
            if not row_cites and header and keys:
                for column, cell in table_cells(line, header):
                    if column and re.match(r"sources?$", column.strip(), re.I) and \
                            all(part.strip() in keys for part in re.split(r"[,;/ ]+", cell) if part.strip()):
                        row_cites = bool(cell.strip())
            for column, cell in table_cells(line, header):
                if column and OWN_NUMBER_COLUMN.search(column):
                    continue
                found = triggers_in(cell)
                if found and not row_cites:
                    problems.append(finding(pkg, path, number, found, cell))
            continue
        header = None
        if stripped.startswith(">"):
            block_quote.append((number, stripped))
            nxt = lines[number].strip() if number < len(lines) else ""
            if not nxt.startswith(">"):
                joined = " ".join(t for _, t in block_quote) + " " + nxt
                if not cites(joined, pkg, path, keys):
                    problems.append(finding(pkg, path, block_quote[0][0], ["quote"], joined))
                block_quote = []
            continue
        found = triggers_in(stripped)
        if found and not REF_DEF_RE.match(stripped) and not cites(stripped, pkg, path, keys):
            problems.append(finding(pkg, path, number, found, stripped))


def audit_html(pkg, path, text, problems):
    blocks, _, _ = gc.parse_html(text)
    for block in blocks:
        found = triggers_in(block)
        if found and not cites(block, pkg, path):
            # HTML text drops hrefs, so check the raw markup around the text too.
            index = text.find(block[:40])
            window = text[max(0, index - 600): index + len(block) + 600] if index >= 0 else ""
            if not cites(window, pkg, path):
                problems.append(finding(pkg, path, 0, found, block))


def finding(pkg, path, number, found, text):
    where = gc.rel(pkg, path) + (":%d" % number if number else "")
    snippet = " ".join(text.split())[:160]
    return "%s: %s with no citation or label: %s" % (where, "/".join(found), snippet)


def audit_ledger(pkg, problems):
    path = pkg / LEDGER
    if not path.is_file():
        problems.append("%s is missing" % LEDGER)
        return 0
    table = gc.find_table(path.read_text(encoding="utf-8"), LEDGER_COLUMNS)
    if not table:
        problems.append("%s has no table with columns %s" % (LEDGER, ", ".join(LEDGER_COLUMNS)))
        return 0
    header, rows, idx = table
    deliverables = None
    count = 0
    for row in rows:
        if len(row) != len(header):
            problems.append("%s: a row has %d cells, the header %d" % (LEDGER, len(row), len(header)))
            continue
        count += 1
        cid, claim = row[idx["ID"]], row[idx["Claim"]]
        source, verdict, shipped = row[idx["Source"]], row[idx["Verdict"]], row[idx["Shipped"]]
        if not (gc.URL_RE.search(source) or REPO_RE.search(source)):
            problems.append("%s: %s has no source URL or repo: path" % (LEDGER, cid))
        word = next((v for v in VERDICTS if verdict.strip().upper().startswith(v)), None)
        if not word:
            problems.append("%s: %s verdict %r is not STANDS, WEAKENED, or REFUTED" % (LEDGER, cid, verdict))
        if not shipped.strip():
            problems.append("%s: %s has no 'Shipped as' entry" % (LEDGER, cid))
        if word == "REFUTED":
            if not re.match(r"^\s*(cut|not shipped|-|none|deleted)\b", shipped, re.I):
                problems.append("%s: %s was REFUTED but is shipped as %r" % (LEDGER, cid, shipped))
            if len(claim.split()) >= 6:
                if deliverables is None:
                    deliverables = deliverable_text(pkg)
                needle = " ".join(claim.lower().split())
                for name, text in deliverables:
                    if needle in text:
                        problems.append("%s: REFUTED claim %s still appears in %s" % (LEDGER, cid, name))
    if not count:
        problems.append("%s holds no claims" % LEDGER)
    return count


def deliverable_text(pkg):
    out = []
    for path in gc.package_text_files(pkg, skip_dirs=SKIP_DIRS + ("08-redteam",)):
        if path.suffix.lower() in SCAN_SUFFIXES and path.name not in SKIP_NAMES:
            out.append((gc.rel(pkg, path), " ".join(path.read_text(encoding="utf-8", errors="replace").lower().split())))
    return out


def check(pkg):
    pkg = Path(pkg)
    problems = []
    claims = audit_ledger(pkg, problems)
    scanned = 0
    for path in gc.package_text_files(pkg, skip_dirs=SKIP_DIRS):
        if path.suffix.lower() not in SCAN_SUFFIXES or path.name in SKIP_NAMES or path.name.startswith("."):
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix.lower() in (".html", ".htm"):
            audit_html(pkg, path, text, problems)
        else:
            audit_markdown(pkg, path, text, problems)
    return {"claims": claims, "files": scanned, "problems": problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Claim audit for a Candidate Package")
    parser.add_argument("package")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: %d ledger claims, %d files scanned, %d problem(s)" % (
            "PASS" if not result["problems"] else "FAIL", result["claims"], result["files"],
            len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
