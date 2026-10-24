"""Shared helpers for Gr0wthPilot's launcher, guard, and check scripts.

Standard library only, and Python 3.7 compatible, because the Founder's Mac
runs `python3` 3.7.9 by default.
"""

from __future__ import annotations

import datetime as dt
import html.parser
import json
import os
import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFERENCES = SKILL_DIR / "references"

JOURNAL_NAME = "run-journal.json"
JOURNAL_FORMAT = 1
AUDIT_NAME = "run-audit.md"

# A run's logs: the file name each has in `run-evidence/`, and the run-config
# key naming where its live copy is written.
RUN_LOGS = {"tool-log.jsonl": "tool_log", "fetch-log.jsonl": "fetch_log",
            "last30days-log.jsonl": "last30days_log"}

# Text files the checks read. Media and binary files are skipped.
TEXT_SUFFIXES = {".md", ".html", ".htm", ".json", ".txt", ".csv", ".svg", ".yaml", ".yml"}

URL_RE = re.compile(r"https?://[^\s<>\"'`\[\]|]+")
TRAILING_PUNCT = ".,;:!?*_"


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso_z(moment: dt.datetime) -> str:
    return moment.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso_z(text: str):
    """Parse YYYY-MM-DDTHH:MM[:SS]Z; return None when the text is not that."""
    m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})(?::(\d{2}))?Z", text.strip())
    if not m:
        return None
    seconds = m.group(3) or "00"
    try:
        return dt.datetime.strptime(
            "%sT%s:%s" % (m.group(1), m.group(2), seconds), "%Y-%m-%dT%H:%M:%S"
        ).replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def read_json(path: Path):
    with open(str(path), encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(str(tmp), "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(str(tmp), str(path))


def clean_url(url: str) -> str:
    """Drop trailing punctuation, and a closing parenthesis that has no
    opening one in the URL (a Markdown link's, or prose's around the URL)."""
    while True:
        stripped = url.rstrip(TRAILING_PUNCT)
        if stripped.endswith(")") and stripped.count(")") > stripped.count("("):
            stripped = stripped[:-1]
        if stripped == url:
            return url
        url = stripped


def normalize_url(url: str) -> str:
    """Compare URLs without their fragment and trailing slash."""
    url = clean_url(url)
    url = url.split("#", 1)[0]
    if url.endswith("/") and url.count("/") > 3:
        url = url.rstrip("/")
    elif url.endswith("/"):
        url = url[:-1]
    scheme, _, rest = url.partition("://")
    host, slash, path = rest.partition("/")
    return "%s://%s%s%s" % (scheme.lower(), host.lower(), slash, path)


def find_urls(text: str):
    return [clean_url(u) for u in URL_RE.findall(text)]


def package_text_files(pkg: Path, skip_dirs=()):
    """Yield every text file under the package, skipping hidden folders."""
    skip = {str((pkg / d).resolve()) for d in skip_dirs}
    for root, dirs, files in os.walk(str(pkg)):
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and str((Path(root) / d).resolve()) not in skip
        )
        for name in sorted(files):
            path = Path(root) / name
            if path.suffix.lower() in TEXT_SUFFIXES and not name.startswith("."):
                yield path


def rel(pkg: Path, path: Path) -> str:
    try:
        return str(path.resolve().relative_to(pkg.resolve()))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# Markdown tables, parsed the way gr0wthlab's kit.py parses them.

SEPARATOR_RE = re.compile(r"\|?(\s*:?-+:?\s*\|)+\s*:?-*:?\s*\|?")


def split_cells(line: str):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, current, escaped = [], [], False
    for ch in line:
        if escaped:
            current.append(ch)
            escaped = False
        elif ch == "\\":
            current.append(ch)
            escaped = True
        elif ch == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    cells.append("".join(current).strip())
    return cells


def _match_column(header, wanted):
    lowered = [h.lower() for h in header]
    want = wanted.lower()
    for i, h in enumerate(lowered):
        if h == want:
            return i
    for i, h in enumerate(lowered):
        if h.startswith(want):
            return i
    for i, h in enumerate(lowered):
        if want in h:
            return i
    return None


def find_table(text: str, wanted):
    """Return (header, rows, column_index) for the first table holding every
    wanted column, or None. Mirrors gr0wthlab kit.py's table rule."""
    lines = text.splitlines()
    for i, line in enumerate(lines[:-1]):
        if not line.lstrip().startswith("|"):
            continue
        if not SEPARATOR_RE.fullmatch(lines[i + 1].strip()):
            continue
        header = split_cells(line)
        index = {}
        for column in wanted:
            found = _match_column(header, column)
            if found is None:
                break
            index[column] = found
        else:
            rows = []
            for row_line in lines[i + 2:]:
                if not row_line.lstrip().startswith("|"):
                    break
                rows.append(split_cells(row_line))
            return header, rows, index
    return None


# ---------------------------------------------------------------------------
# HTML text, for checks that read page copy.

class _TextAndLinks(html.parser.HTMLParser):
    SKIP = {"script", "style", "noscript", "template"}
    BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article",
             "header", "footer", "tr", "td", "th", "br", "blockquote", "figcaption",
             "dt", "dd", "summary", "details", "main", "aside", "nav", "button", "label"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = [[]]
        self.links = []
        self.ids = set()
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if attrs.get("name") and tag == "a":
            self.ids.add(attrs["name"])
        if tag in self.SKIP:
            self.skip_depth += 1
        if tag in self.BLOCK:
            self.blocks.append([])
        for key in ("href", "src", "poster", "data"):
            if attrs.get(key):
                self.links.append((tag, key, attrs[key]))
        if tag == "source" and attrs.get("srcset"):
            self.links.append((tag, "srcset", attrs["srcset"].split()[0]))

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
        if tag in self.BLOCK:
            self.blocks.append([])

    def handle_data(self, data):
        if not self.skip_depth:
            self.blocks[-1].append(data)


def parse_html(text: str):
    parser = _TextAndLinks()
    parser.feed(text)
    parser.close()
    blocks = [" ".join(" ".join(b).split()) for b in parser.blocks]
    return [b for b in blocks if b], parser.links, parser.ids


def markdown_units(text: str):
    """Yield (line_number, text) for prose units of a Markdown file, skipping
    fenced code. Table rows are yielded whole."""
    in_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue
        yield number, line


def handoff_line(product: str, folder: str) -> str:
    """The Founder's ready Handoff line for a Candidate Package in
    `projects/<product>/<folder>/`; a package outside `gtm/` is named."""
    if folder == "gtm":
        return "%s - hand to gr0wthlab" % product
    return "%s - hand to gr0wthlab (%s)" % (product, folder)


def load_journal(pkg: Path):
    path = pkg / JOURNAL_NAME
    if not path.is_file():
        return None
    return read_json(path)
