"""Check a finished run before it is handed to hcho. It fails when:
  - a URL the report cites was neither read by this run (sources.csv), named in a
    response the run read (a value in data/*.csv), nor captured by hcho
    (capture/captures.csv);
  - a line marked SEEN carries no link and no data or capture file;
  - a play misses a required field or its prompt;
  - a required section is missing for the run's mode;
  - an image the report shows is not in the run folder;
  - the text has an em dash (hcho's standing rule);
  - an API key reached the run's log.
"""

from __future__ import annotations

import re
from pathlib import Path

import gt_common as gc

URL_RE = re.compile(r"https?://[^\s<>\"'`)\]|]+")
TRAILING = ".,;:!?*_"
REQUIRED = {
    "full": ["The path", "Plays", "Things to skip", "Timeline", "By channel", "14-day plan", "Method notes"],
    "content": ["Across channels", "Method notes"],
}
PLAY_FIELDS = ["Stage", "Evidence", "Effort", "First result", "Cost"]


def _norm(url: str) -> str:
    url = url.rstrip(TRAILING)
    # A Wayback snapshot is read as .../web/<ts>id_/<page> and cited as .../web/<ts>/<page>.
    url = re.sub(r"(web\.archive\.org/web/\d+)id_/", r"\1/", url)
    return gc.normalize_url(url)


def citable(run: Path) -> set:
    urls = {_norm(u) for u in gc.logged_urls(run)}
    for csv_path in (run / "data").glob("*.csv"):
        for row in gc.read_csv(csv_path):
            for value in row.values():
                for found in URL_RE.findall(value or ""):
                    urls.add(_norm(found))
    for row in gc.read_csv(run / "sources.csv"):
        if row.get("status", "").isdigit() and int(row["status"]) < 400 and row.get("route") == "rea":
            urls.add(_norm(row["url"].split("?")[0]))
    return urls


def _sections(text):
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]


def _plays(text):
    m = re.search(r"^##\s+Plays\s*$(.*?)(?=^##\s)", text + "\n## end\n", re.M | re.S)
    if not m:
        return []
    blocks = re.split(r"^###\s+", m.group(1), flags=re.M)[1:]
    return blocks


def check(run) -> list:
    run = Path(run)
    meta = gc.load_run(run)
    mode = meta.get("mode", "full")
    report_name = "playbook.md" if mode == "full" else "content.md"
    report = run / report_name
    problems = []
    if not report.exists():
        return ["%s is missing" % report_name]
    text = report.read_text(encoding="utf-8")

    if "\u2014" in text:
        lines = [str(n) for n, line in enumerate(text.splitlines(), 1) if "\u2014" in line]
        problems.append("em dash on line(s) %s; use a plain dash" % ", ".join(lines[:10]))

    have = [s.lower() for s in _sections(text)]
    for wanted in REQUIRED.get(mode, []):
        if not any(s.startswith(wanted.lower()) for s in have):
            problems.append("missing section: ## %s" % wanted)

    allowed = citable(run)
    for number, line in enumerate(text.splitlines(), 1):
        for url in URL_RE.findall(line):
            if _norm(url) not in allowed:
                problems.append("line %d cites a URL this run did not read: %s" % (number, url.rstrip(TRAILING)))
        if re.search(r"\bSEEN\b", line) and not (URL_RE.search(line) or re.search(r"\b(data|capture|img)/[\w./-]+", line)
                                                 or re.search(r"\]\((?!http)[^)]+\)", line)):
            problems.append("line %d is marked SEEN but names no source (a link, or a data/ or capture/ file)" % number)
        for src in re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", line):
            if not src.startswith("http") and not (run / src).exists():
                problems.append("line %d shows an image that is not in the run: %s" % (number, src))

    if mode == "full":
        plays = _plays(text)
        if not plays:
            problems.append("## Plays has no plays (### headings)")
        for block in plays:
            name = block.splitlines()[0].strip()
            for field in PLAY_FIELDS:
                if not re.search(r"\*\*%s:?\*\*" % re.escape(field), block):
                    problems.append("play '%s' has no **%s:** line" % (name, field))
            if "```prompt" not in block:
                problems.append("play '%s' has no ```prompt block" % name)

    sources = run / "sources.csv"
    if sources.exists() and re.search(r"[?&](key|api_key|token|access_token)=(?!REDACTED)[^&\s,]+",
                                      sources.read_text(encoding="utf-8")):
        problems.append("sources.csv holds an unredacted key or token")

    html_out = report.with_suffix(".html")
    if not html_out.exists():
        problems.append("%s is missing; run `gt.py render`" % html_out.name)
    elif html_out.stat().st_mtime < report.stat().st_mtime:
        problems.append("%s is older than %s; run `gt.py render` again" % (html_out.name, report_name))
    return problems
