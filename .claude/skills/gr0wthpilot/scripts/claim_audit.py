#!/usr/bin/env python3
"""Claim audit for a Candidate Package.

Three checks, all from the truth policy (facts, numbers, quotes, and competitor
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
   The run's machine records (`run-audit.md`, `run-evidence/`, the journal)
   and the red team's records in `08-redteam/` are not claims and are
   skipped. An HTML block is cited by a URL or link inside that block, or,
   inside a blockquote, by that quote's citation (below);
   each attribute a reader sees (alt, title, aria-label, placeholder, label, a
   button's or text field's value, the meta title, description, image alt,
   and site name) and each JSON-LD string is checked on its own, cited only
   by a URL or label inside it. An HTML blockquote, like a Markdown one,
   needs a URL, label, or citation link inside it, in its cite attribute, or
   in the caption of the figure that holds it (the HTML place for a quote's
   attribution, as the next line is in Markdown); a link elsewhere on the
   page does not count.
3. A page's structured data (JSON-LD, microdata, or RDFa) carries no rating
   or review, cited or not: a Product has none before launch. The audit
   refuses a rating or review property (aggregateRating, review, reviews,
   reviewRating, ratingValue, ratingCount, reviewCount) and a node typed as
   one of schema.org's Review or Rating types or their subtypes, named in
   RATING_TYPES, or any type whose name ends in Review or Rating.

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
# A column whose header names one of these, as a whole word, holds the run's
# own numbers; a market-size column holds the market's, which need a source.
OWN_NUMBER_COLUMN = re.compile(
    r"\b(?:scores?|weights?|signals?|kill|targets?|thresholds?|floors?|budgets?|goals?|margins?|ranks?|days?|"
    r"slots?|durations?|lengths?|sizes?)\b", re.I)
MARKET_COLUMN = re.compile(r"\bmarket\b", re.I)
SKIP_DIRS = ("run-evidence", "01-research/last30days")
# The red team's records, which quote the claims they cut word for word; the
# claims ledger there is checked on its own.
REVIEW_DIRS = ("08-redteam",)
SKIP_NAMES = {"sources.md", "sources-exempt.md", gc.JOURNAL_NAME, gc.AUDIT_NAME, "claims-ledger.md"}
SCAN_SUFFIXES = {".md", ".html", ".htm", ".txt"}
RATING_PROPERTIES = {"aggregaterating", "review", "reviews", "reviewrating", "ratingvalue", "ratingcount",
                     "reviewcount"}
# schema.org's Review and Rating types and their subtypes, some of whose names
# end in neither word, and any other type whose name does.
RATING_TYPES = {"review", "claimreview", "criticreview", "employerreview", "mediareview", "recommendation",
                "userreview", "rating", "aggregaterating", "employeraggregaterating", "endorsementrating"}
RATING_TYPE_ENDINGS = ("review", "rating")


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
                if column and OWN_NUMBER_COLUMN.search(column) and not MARKET_COLUMN.search(column):
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
    page = gc.read_html(text)
    for block, hrefs, quote in page.page_copy():
        found = triggers_in(block)
        if found and not cites(" ".join([block] + ['href="%s"' % h for h in hrefs]), pkg, path) \
                and not (quote and quote_cited(pkg, path, quote)):
            problems.append(finding(pkg, path, 0, found, block))
    for quote in page.page_quotes():
        if quote[0] and not quote_cited(pkg, path, quote):
            problems.append(finding(pkg, path, 0, ["quote"], quote[0]))
    ratings = sorted({name for kind, name in page.schema_terms
                      if (name.lower() in RATING_PROPERTIES if kind == "property"
                          else name.lower() in RATING_TYPES or name.lower().endswith(RATING_TYPE_ENDINGS))})
    if ratings:
        problems.append("%s: structured data carries ratings or reviews (%s); a Product has none before launch, "
                        "so take them out" % (gc.rel(pkg, path), ", ".join(ratings)))


def quote_cited(pkg, path, quote):
    """Whether an HTML blockquote, as `page_quotes()` gives it, is cited: by a
    URL, label, or citation link inside it, in its cite attribute, or in the
    caption of the figure that holds it."""
    text, caption, hrefs = quote
    return cites(" ".join([text, caption] + ['href="%s"' % h for h in hrefs]), pkg, path)


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
                needle = comparable(claim)
                for name, texts in deliverables:
                    if any(needle in text for text in texts):
                        problems.append("%s: REFUTED claim %s still appears in %s" % (LEDGER, cid, name))
    if not count:
        problems.append("%s holds no claims" % LEDGER)
    return count


def comparable(text):
    """Text as a reader sees it, for finding a claim in it: a Markdown link's
    words without its address, no emphasis marks, lower case, single spaces."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return " ".join(re.sub(r"[*_~`]", "", text).lower().split())


def deliverable_text(pkg):
    """Each deliverable's texts to look for a claim in: Markdown without its
    emphasis and link addresses, and an HTML page both as written (so a claim
    in an attribute or a script is found) and as a reader sees it (its words
    without markup between them, and the attribute and JSON-LD copy it shows)."""
    out = []
    for path in gc.package_text_files(pkg, skip_dirs=SKIP_DIRS + REVIEW_DIRS):
        if path.suffix.lower() in SCAN_SUFFIXES and path.name not in SKIP_NAMES:
            text = path.read_text(encoding="utf-8", errors="replace")
            texts = [text]
            if path.suffix.lower() in (".html", ".htm"):
                texts.append(" ".join(unit for unit, _, _ in gc.read_html(text).page_copy()))
            out.append((gc.rel(pkg, path), [comparable(t) for t in texts]))
    return out


def check(pkg):
    pkg = Path(pkg)
    problems = []
    claims = audit_ledger(pkg, problems)
    scanned = 0
    for path in gc.package_text_files(pkg, skip_dirs=SKIP_DIRS + REVIEW_DIRS):
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
