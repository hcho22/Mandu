#!/usr/bin/env python3
"""Layout check: does a Candidate Package hold what gr0wthlab reads, in a form
gr0wthlab can parse?

gr0wthlab (the Marketing Engineer) reads a Product's package through its
registry, config/products.json. This check takes RepToday's entry there as the
template (the live registry when one is readable, else the snapshot in
references/registry-template.json), points it at the package's own folder
(`projects/<Product>/gtm/` or a dated `gtm-candidate-<date>/`), maps every
path it names into the package, and verifies:

1. every file and folder the entry names exists (a folder holds at least one
   visible file; a `files_starting_with` source has at least one match);
2. each file gr0wthlab parses with code follows the rules its readers
   enforce (src/gr0wthlab/kit.py, results.py, shots.py, weekly_changes.py,
   drafts.py, posts.py, lint.py; each check names the function it mirrors):
   zero-padded Angle IDs; the exact platform names TikTok and YouTube Shorts;
   Formats naming a recording the filming plan knows; signal and kill cells
   naming numbers gr0wthlab asks the Studio of each calendar day's primary
   platform that runs the Angle for, and its own Platform's when no fixed
   day runs it or the flex slot can put it there; the pre-publication checklist's items, titles, and blocking scopes
   as gr0wthlab reads them; and a creative-log.json its kill and change
   edits can make, against the Angle bank's own header; and the Test Kit
   meets the run's own floor: at least 15
   distinct Angles, hook-only A/B pairs, and a 14-day calendar;
3. with --write-entry, writes `handoff/registry-entry.json`: RepToday's entry
   with the Product's name and the package's folder, ready for the reviewed
   gr0wthlab change at Handoff.

Usage: check_layout.py PACKAGE --product NAME [--registry products.json] [--write-entry] [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402
import brand_lint  # noqa: E402

TEMPLATE = gc.REFERENCES / "registry-template.json"
# The platforms gr0wthlab runs, spelled as config/platforms.json and the post
# Draft name them: posts.py compares a calendar day's primary platform to the
# platform assignment's names exactly, and the flex edit (weekly_changes.py
# compose_flex) copies an Angle's Platform cell into the calendar, so both
# cells use these exact names.
PLATFORMS = ("TikTok", "YouTube Shorts")
MIN_ANGLES = 15
CALENDAR_DAYS = 14
FLOOR_RE = re.compile(r"Any post under (\d[\d,]*) impressions is unread")
PAIR_HEAD_RE = re.compile(r"^## (AB-\d+)\b.*$")
LEG_RE = re.compile(r"^- Leg ([AB]) hook: (.*)$")
QUOTED_RE = re.compile(r"\"([^\"]+)\"")
PAIR_LEG_RE = re.compile(r"\b(AB-\d+) leg ([AB])\b")
# The recording types gr0wthlab's filming plan reads from a Format (shots.py
# CAPTURES).
FORMAT_KINDS = re.compile(r"\bfounder[- ]on[- ]camera\b|\bscreen[- ]record(?:ing)?s?\b|\btime-?lapse\b|"
                          r"\bslow[- ]motion\b|\bhigh-frame-rate\b|\bdemo\b|\bpan\b|\bvideo\b", re.I)
# The calendar days the day-7 Weekly Read covers (exchange.py READ_DAYS): only
# an Angle one of them runs can earn the flex slot (weekly_read.py).
EARNING_DAYS = 5
# The numbers gr0wthlab asks each platform's Studio for, and the words a
# signal or kill criterion uses for each (results.py LABELS and TERMS).
STUDIO_NUMBERS = {
    "TikTok": ("watched_full_percent", "average_watch_time_seconds", "likes", "comments", "shares", "saves",
               "profile_visits"),
    "YouTube Shorts": ("viewed_percent", "average_percentage_viewed", "likes", "comments", "shares"),
}
METRIC_TERMS = (
    ("watched_full_percent", ("watched-full", "watched full", "watch-through", "watch through")),
    ("viewed_percent", ("viewed-vs-swiped", "viewed vs swiped", "viewed vs. swiped", "viewed rate")),
    ("average_percentage_viewed", ("% viewed", "percent viewed", "percentage viewed")),
    ("average_watch_time_seconds", ("watch time",)),
    ("saves", ("saves",)),
    ("shares", ("shares",)),
    ("likes", ("likes",)),
    ("profile_visits", ("profile visit",)),
    ("comments", ("comment",)),
)
# The pre-publication checklist as gr0wthlab reads it (kit.py CHECKBOX, BLOCKING, NAMED_CLAIM, SOCIAL_SCOPES).
CHECK_ITEM_RE = re.compile(r"^- \[([ xX])\] (.*)$")
BLOCKING_RE = re.compile(r"\(blocking: ([^)]*)\)")
BLOCKING_LIKE_RE = re.compile(r"\(\s*blocking\b", re.I)
UNREAD_ITEM_RE = re.compile(r"\s*[-*+]\s*\[[ xX]?\]")
NAMED_CLAIM_RE = re.compile(r"the \"([^\"]+)\" claim")
SOCIAL_SCOPES = ("everything public", "social")
CREATIVE_KEYS = {"angle_id", "hook", "platform", "hypothesis", "format", "preregistered_success_signal",
                 "kill_criterion", "pain_rank", "pain_state", "verbatim_quote", "pain_source_url",
                 "ab_pair", "results", "status"}
# The creative-log fields a new Angle's record takes from its row of angles.md,
# by the column each is read from (weekly_changes.py RECORD_CELLS).
RECORD_CELLS = {"hypothesis": "Hypothesis", "format": "Format", "preregistered_success_signal": "signal",
                "kill_criterion": "Kill"}


def default_registries():
    paths = []
    env = os.environ.get("GR0WTHLAB_DIR")
    if env:
        paths.append(Path(env) / "config" / "products.json")
    paths.append(Path.home() / "gr0wthlab" / "config" / "products.json")
    paths.append(Path.home() / "Developer" / "FM_Private" / "firstmate-private" / "projects" /
                 "gr0wthlab" / "config" / "products.json")
    return paths


def load_template(registry=None):
    """Return (entry with {product} placeholders, where it came from)."""
    for path in ([Path(registry)] if registry else default_registries()):
        try:
            data = gc.read_json(path)
        except (OSError, ValueError):
            continue
        for product in data.get("products", []):
            if product.get("name") == "RepToday" and product.get("go_to_market_package"):
                entry = product["go_to_market_package"]
                text = json.dumps(entry)
                text = re.sub(r"projects/RepToday/(?!gtm/)[^\"]*launch-checklist[^\"]*\.md",
                              "projects/{product}/gtm/launch-checklist.md", text)
                text = text.replace("projects/RepToday/", "projects/{product}/")
                return json.loads(text), str(path)
    return gc.read_json(TEMPLATE)["go_to_market_package"], str(TEMPLATE)


def package_prefix(pkg, product):
    """The registry path of the package: `projects/<Product>/<its folder>/`."""
    return "projects/%s/%s/" % (product, Path(pkg).resolve().name)


def fill(entry, product, prefix):
    text = json.dumps(entry).replace("projects/{product}/gtm/", prefix)
    return json.loads(text.replace("{product}", product))


def to_package(pkg, prefix, path):
    if not path.startswith(prefix):
        return None
    return pkg / path[len(prefix):]


def check_paths(pkg, prefix, entry, problems):
    needed = []
    for source in entry.get("sources", []):
        needed.append((source["path"], source.get("files_starting_with")))
    needed.append((entry.get("launch_checklist"), None))
    for block in ("post_drafts", "weekly_read", "listening", "outreach"):
        for key, value in (entry.get(block) or {}).items():
            if key != "note" and isinstance(value, str) and value.startswith("projects/"):
                needed.append((value, None))
    seen = set()
    for path, starts in needed:
        if not path or (path, starts) in seen:
            continue
        seen.add((path, starts))
        target = to_package(pkg, prefix, path)
        if target is None:
            problems.append("registry path %s lies outside %s" % (path, prefix))
            continue
        relative = gc.rel(pkg, target)
        if path.endswith("/"):
            files = [p for p in target.iterdir() if p.is_file() and not p.name.startswith(".")] \
                if target.is_dir() else []
            if starts:
                files = [p for p in files if p.name.startswith(starts)]
            if not files:
                problems.append("%s/ holds no %sfiles gr0wthlab can read" % (
                    relative, "'%s*' " % starts if starts else ""))
        elif not target.is_file():
            problems.append("%s is missing (gr0wthlab reads it)" % relative)
    return len(seen)


def read(pkg, relative):
    path = pkg / relative
    return path.read_text(encoding="utf-8") if path.is_file() else None


def check_calendar(text, problems):
    table = gc.find_table(text, ("Day", "Asset", "Angle", "platform"))
    if not table:
        problems.append("cadence-14-day.md: no table with columns Day, Asset, Angle, platform")
        return {}
    header, rows, idx = table
    days, flex = {}, []
    for row in rows:
        if len(row) != len(header):
            problems.append("cadence-14-day.md: a row has %d cells, the header %d" % (len(row), len(header)))
            continue
        day = row[idx["Day"]]
        if not re.fullmatch(r"[0-9]+", day):
            problems.append("cadence-14-day.md: Day %r is not a number" % day)
            continue
        if day in days:
            problems.append("cadence-14-day.md: day %s repeats" % day)
        angle_cell = row[idx["Angle"]]
        if row[idx["platform"]] not in PLATFORMS:
            problems.append("cadence-14-day.md: day %s primary platform %r is not exactly TikTok or YouTube Shorts "
                            "(gr0wthlab's post Draft compares it to the platform names as written)"
                            % (day, row[idx["platform"]]))
        m = re.match(r"(P\d+)\b", angle_cell)
        leg = PAIR_LEG_RE.search(angle_cell)
        named = sorted(set(re.findall(r"\bP\d+\b", angle_cell)))
        if not m:
            flex.append(day)
            if len(named) != 1:
                problems.append("cadence-14-day.md: flex day %s must name exactly one fallback Angle (P..)" % day)
        days[day] = {"angle": m.group(1) if m else None, "leg": leg.groups() if leg else None,
                     "platform": row[idx["platform"]], "fallback": named[0] if not m and len(named) == 1 else None}
    for d in range(1, CALENDAR_DAYS):
        if str(d) not in days:
            problems.append("cadence-14-day.md: day %d is missing (days 1-13 must exist)" % d)
    if len(flex) > 1:
        problems.append("cadence-14-day.md: %d flex days (%s); exactly one row may lack a fixed Angle"
                        % (len(flex), ", ".join(flex)))
    return days


def metrics_named(text):
    """The numbers a signal or kill criterion names (results.py numbers_named)."""
    lowered = text.lower()
    return [number for number, words in METRIC_TERMS if any(word in lowered for word in words)]


def check_angles(text, rules, problems, warnings):
    """The Angle bank as gr0wthlab's kit.parse_angles reads it, and what its
    filming plan (shots.py shot_list) needs of each row."""
    table = gc.find_table(text, gc.ANGLE_COLUMNS)
    if not table:
        problems.append("angles.md: no table with columns %s" % ", ".join(gc.ANGLE_COLUMNS))
        return {}
    header, rows, idx = table
    if len(set(idx.values())) != len(idx):
        problems.append("angles.md: two wanted columns match the same header; make headers unambiguous")
    prefix = (rules or {}).get("pain_source_url_must_start_with") or "https://"
    angles = {}
    for row in rows:
        cell = row[idx["ID"]].strip() if len(row) > idx["ID"] else ""
        if not re.fullmatch(r"P\d+", cell):
            if re.match(r"\W*[Pp]\W*\d", cell):
                problems.append("angles.md: ID %r is not P and digits, so gr0wthlab skips its row" % cell)
            continue
        if len(row) != len(header):
            problems.append("angles.md: %s has %d cells, the header %d" % (cell, len(row), len(header)))
            continue
        aid = cell
        if aid in angles:
            problems.append("angles.md: %s repeats" % aid)
        hook = row[idx["Hook"]].strip()
        if not re.fullmatch(r"\"([^\"]+)\"", hook):
            problems.append("angles.md: %s Hook must be one straight-quoted string, got %r" % (aid, hook[:60]))
        urls = re.findall(r"https?://[^\s)\]]+", row[idx["pain"]])
        if not any(u.startswith(prefix) for u in urls):
            problems.append("angles.md: %s pain cell has no source URL starting %s" % (aid, prefix))
        platform = row[idx["Platform"]].strip()
        if platform not in PLATFORMS:
            problems.append("angles.md: %s Platform %r is not exactly TikTok or YouTube Shorts (gr0wthlab's flex "
                            "edit copies it into the calendar as written)" % (aid, platform))
        if not FORMAT_KINDS.search(row[idx["Format"]]):
            problems.append("angles.md: %s Format names no recording type gr0wthlab's filming plan knows "
                            "(founder on camera, screen record, time-lapse, slow motion, high-frame-rate, demo, "
                            "pan, video), so it cannot plan the Angle's shots" % aid)
        angles[aid] = {"hook": hook.strip('"'), "platform": platform, "signal": row[idx["signal"]],
                       "kill": row[idx["Kill"]]}
    width = max(2, min((len(aid) - 1 for aid in angles), default=2))
    unpadded = [aid for aid in angles if aid != "P%0*d" % (width, int(aid[1:]))]
    if unpadded:
        problems.append("angles.md: Angle IDs must be zero-padded to one width of at least two digits (P01, "
                        "P02, ...), as gr0wthlab numbers a new Angle (weekly_changes.py next_number): %s"
                        % ", ".join(unpadded))
    if not angles:
        problems.append("angles.md: no Angle rows (IDs like P01)")
    elif len(angles) < MIN_ANGLES:
        problems.append("angles.md: %d Angles; a Test Kit needs at least %d distinct Angles" % (len(angles), MIN_ANGLES))
    return angles


def metric_words(numbers):
    return ", ".join(words[0] for number, words in METRIC_TERMS if number in numbers)


def check_pairs(text, angles, problems):
    pairs, current = {}, None
    for line in text.splitlines():
        head = PAIR_HEAD_RE.match(line)
        if head:
            pid = head.group(1)
            m_angle = re.search(r"\bangle (P\d+)", line)
            m_paren = re.search(r"\(([^)]*)\)\s*$", line)
            parts = [p.strip() for p in m_paren.group(1).split(",")] if m_paren else []
            if not m_angle or len(parts) < 2:
                problems.append("ab-pairs.md: heading %r must name 'angle P..' and end with "
                                "'(angle P.., Platform, ...)'" % line.strip())
            elif parts[1] not in PLATFORMS:
                problems.append("ab-pairs.md: %s platform %r is not TikTok or YouTube Shorts" % (pid, parts[1]))
            current = pairs.setdefault(pid, {"angle": m_angle.group(1) if m_angle else None, "legs": {}})
            continue
        if line.startswith("## "):
            current = None
            continue
        leg = LEG_RE.match(line)
        if leg and current is not None:
            q = QUOTED_RE.search(leg.group(2))
            if not q:
                problems.append("ab-pairs.md: leg %s has no quoted Hook" % leg.group(1))
            current["legs"][leg.group(1)] = q.group(1) if q else None
    if not pairs:
        problems.append("ab-pairs.md: no pair sections (## AB-1: ... (angle P.., TikTok, ...))")
    for pid, pair in pairs.items():
        if set(pair["legs"]) != {"A", "B"}:
            problems.append("ab-pairs.md: %s needs both '- Leg A hook:' and '- Leg B hook:' lines" % pid)
        if pair["angle"] and angles and pair["angle"] not in angles:
            problems.append("ab-pairs.md: %s names %s, which angles.md does not hold" % (pid, pair["angle"]))
        if pair["legs"].get("A") and pair["legs"].get("A") == pair["legs"].get("B"):
            problems.append("ab-pairs.md: %s legs have the same Hook; only the Hook may differ, and it must" % pid)
    return pairs


def check_calendar_links(days, angles, pairs, problems):
    for day, info in days.items():
        if info["angle"] and angles and info["angle"] not in angles:
            problems.append("cadence-14-day.md: day %s names %s, which angles.md does not hold" % (day, info["angle"]))
        if info["leg"]:
            pid, _ = info["leg"]
            pair = pairs.get(pid)
            if not pair:
                problems.append("cadence-14-day.md: day %s names %s, which ab-pairs.md does not hold" % (day, pid))
            elif info["angle"] and pair["angle"] != info["angle"]:
                problems.append("cadence-14-day.md: day %s runs %s on %s, but the pair is for %s"
                                % (day, pid, info["angle"], pair["angle"]))


def check_metrics(days, angles, problems):
    """Each Angle's signal and kill criterion against the numbers gr0wthlab
    asks for its posts (results.py asks_for): the numbers of the primary
    platform of each fixed calendar day that runs it, and of its own Platform
    when no fixed day runs it or when the flex edit (weekly_changes.py
    compose_flex) can put it there: as the flex row's named fallback, or as
    the Angle that earned the slot, which only an Angle a day of the day-7
    Weekly Read runs can be (weekly_read.py)."""
    flex = [info["fallback"] for info in days.values() if info["angle"] is None]
    runs, own = {}, set(flex)
    for day, info in days.items():
        if info["angle"] in angles:
            runs.setdefault(info["angle"], {}).setdefault(info["platform"], []).append(day)
            if flex and int(day) <= EARNING_DAYS:
                own.add(info["angle"])
    for aid, angle in angles.items():
        platforms = dict(runs.get(aid, {}))
        if aid in own or not platforms:
            platforms.setdefault(angle["platform"], [])
        for platform, on_days in platforms.items():
            asked = STUDIO_NUMBERS.get(platform)
            if asked is None:
                continue
            where = " (cadence-14-day.md day %s)" % ", ".join(on_days) if on_days else ""
            for column, label in (("signal", "signal"), ("kill", "kill criterion")):
                named = metrics_named(angle[column])
                missing = metric_words([n for n in named if n not in asked])
                if not [n for n in named if n in asked]:
                    problems.append("angles.md: %s %s names no number gr0wthlab asks %s for (%s)%s%s"
                                    % (aid, label, platform, metric_words(asked),
                                       "; it names only %s" % missing if missing else "", where))
                elif missing:
                    problems.append("angles.md: %s %s names %s, which gr0wthlab does not ask %s for%s"
                                    % (aid, label, missing, platform, where))


def check_platforms(text, problems):
    found, inside = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = "test platforms" in line.lower()
            continue
        if inside:
            m = re.match(r"### \d+\. (.+?)(?: \([^)]*\))?\s*$", line)
            if m:
                found.append(m.group(1))
    if not found:
        problems.append("platform-assignment.md: no '## ... test platforms' section with '### 1. TikTok (primary)' items")
    for name in found:
        if name not in PLATFORMS:
            problems.append("platform-assignment.md: %r is not a platform gr0wthlab runs (%s)" % (name, ", ".join(PLATFORMS)))
    return found


def checklist_items(text):
    """The checklist's items as gr0wthlab's kit.parse_checklist reads them:
    (line, done, title, scope, full text), and every line any item covers."""
    items, covered = [], set()
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        m = CHECK_ITEM_RE.match(lines[index])
        if not m:
            index += 1
            continue
        body, number = [m.group(2)], index + 1
        covered.add(index)
        index += 1
        while index < len(lines) and lines[index].startswith("  ") and lines[index].strip():
            body.append(lines[index].strip())
            covered.add(index)
            index += 1
        full = " ".join(body)
        bold = re.search(r"\*\*(.+?)\*\*", full)
        title = (bold.group(1) if bold else re.split(r"(?<=[.:;])\s", full, maxsplit=1)[0]).strip()
        scopes = BLOCKING_RE.findall(full)
        scope = tuple(t.strip().casefold() for t in re.split(r"[,;]", scopes[-1]) if t.strip()) if scopes else None
        items.append((number, m.group(1) != " ", title, scope, full))
    return items, covered


def check_checklist(text, problems, warnings):
    """Each item's title and blocking scope as gr0wthlab reads them (kit.py
    parse_checklist, drafts.py checklist_status): an open item blocks a post
    when its last `(blocking: ...)` scope starts with "everything public" or
    "social", unless its title names `the "<claim>" claim`, which narrows it
    to posts carrying that claim."""
    items, covered = checklist_items(text)
    if not items:
        problems.append("pre-publication-checklist.md: no '- [ ] **Title** ...' items")
    starts = {number - 1 for number, _, _, _, _ in items}
    after_item = False
    for index, line in enumerate(text.splitlines()):
        if index in starts:
            after_item = True
            continue
        if line.startswith("#"):
            after_item = False
        elif UNREAD_ITEM_RE.match(line):
            problems.append("pre-publication-checklist.md:%d: a checkbox gr0wthlab does not read as an item (an "
                            "indented one is read as part of the item above, its blocking scope included); an item "
                            "starts '- [ ] ' at column 0" % (index + 1))
        elif after_item and index not in covered and BLOCKING_LIKE_RE.search(line):
            problems.append("pre-publication-checklist.md:%d: this line is not part of the item above it in "
                            "gr0wthlab's reading, which ends an item at its first blank or unindented line, so its "
                            "blocking scope is never read; put it on a line indented two spaces right under the "
                            "item" % (index + 1))
    for number, done, title, scope, full in items:
        where = "pre-publication-checklist.md:%d" % number
        if not re.search(r"\w", title):
            problems.append("%s: the item has no title gr0wthlab can read (its **bold** text, else its first "
                            "sentence)" % where)
        if len(BLOCKING_LIKE_RE.findall(full)) != len(BLOCKING_RE.findall(full)):
            problems.append("%s: a blocking scope gr0wthlab cannot read; write it '(blocking: scope)', lower case, "
                            "with one closing parenthesis" % where)
        if scope == ():
            problems.append("%s: '(blocking: )' names no scope" % where)
        if len(set(BLOCKING_RE.findall(full))) > 1:
            problems.append("%s: more than one blocking scope; gr0wthlab reads only the last" % where)
        social = any(t.startswith(SOCIAL_SCOPES) for t in scope or ())
        if not done and social and not NAMED_CLAIM_RE.search(title):
            if NAMED_CLAIM_RE.search(full):
                problems.append("%s: the item names its claim outside its title, where gr0wthlab does not read "
                                "it, so it blocks every post Draft; put the claim in the **bold** title" % where)
            else:
                warnings.append("%s: open item blocks every gr0wthlab post Draft until the Founder closes it: %s"
                                % (where, full[:80]))
    return items


def check_competitors(pkg, problems):
    names = []
    folder = pkg / "01-research"
    for path in sorted(folder.glob("competitor*")) if folder.is_dir() else []:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            m = re.match(r"# Competitor Teardown: (.+)$", line)
            if m:
                names.append(m.group(1))
            m = re.match(r"## \d+\. (.+)$", line)
            if m:
                nxt = next((rest for rest in lines[i + 1:] if rest.strip()), "")
                if nxt.startswith("Source:"):
                    names.append(m.group(1))
            if line.startswith("Scope:"):
                m = re.findall(r"\(([^)]*)\)", line)
                if m:
                    names.extend(p.strip() for p in m[-1].split(","))
    names = [re.split(r" \(|: | - | \| |! ", n)[0].strip() for n in names]
    names = [n for n in names if len(n) >= 3]
    if not names:
        problems.append("01-research/competitor*: no competitor names gr0wthlab can read "
                        "('# Competitor Teardown: <name>')")
    return names


def check_read_results(text, problems):
    m = FLOOR_RE.search(text or "")
    if not m:
        problems.append("read-the-results.md: no line 'Any post under N impressions is unread' (gr0wthlab's floor)")
    elif "views" not in text[m.start(): m.start() + 300]:
        problems.append("read-the-results.md: the floor line must say it counts each platform's views")


def check_creative_log(text, angles, problems, header=()):
    """creative-log.json as gr0wthlab's Weekly Read edits it: a list of Angle
    records, alone or under an object's "angles" (weekly_changes.py
    log_records), one record per Angle that its kill can mark (compose_kill),
    and a shape that a changed Angle's new record can be added to
    (compose_record)."""
    try:
        data = json.loads(text)
    except ValueError as exc:
        problems.append("creative-log.json is not valid JSON: %s" % exc)
        return
    records = data.get("angles") if isinstance(data, dict) else data
    if not isinstance(records, list):
        problems.append("creative-log.json must be a list or an object with an 'angles' list")
        return
    seen = {}
    platform_names = {}
    for position, record in enumerate(records):
        if not isinstance(record, dict) or "angle_id" not in record:
            problems.append("creative-log.json: every record needs an angle_id")
            continue
        angle_id = record["angle_id"]
        extra = set(record) - CREATIVE_KEYS
        if extra:
            problems.append("creative-log.json: %s has keys gr0wthlab does not accept: %s"
                            % (angle_id, ", ".join(sorted(extra))))
        if not isinstance(angle_id, str) or not re.fullmatch(r"P\d+(?:-.*)?", angle_id):
            problems.append("creative-log.json: angle_id %r must be its Angle's ID, alone or followed by a hyphen "
                            "(P01 or P01-waiting), as gr0wthlab finds a record to kill" % (angle_id,))
            continue
        number = angle_id.split("-", 1)[0]
        seen[number] = seen.get(number, 0) + 1
        for key, column in RECORD_CELLS.items():
            if key in record and header and gc._match_column(header, column) is None:
                problems.append("creative-log.json: %s holds %s, but angles.md has no %s column for a new Angle's "
                                "record to take it from" % (angle_id, key, column))
        if number in angles:
            platform_names.setdefault(angles[number]["platform"], set()).add(
                record.get("platform") if isinstance(record.get("platform"), str) else None)
        if record.get("status") != "draft" or "results" not in record or record["results"] is not None:
            problems.append("creative-log.json: %s must start with status \"draft\" and results null" % angle_id)
        if not kill_edit_works(text, data, position, record):
            problems.append("creative-log.json: %s needs its angle_id on a line of its own, followed in the same "
                            "record by its status line, which gr0wthlab's kill edits" % angle_id)
    for aid in angles:
        if seen.get(aid, 0) != 1:
            problems.append("creative-log.json: %s needs exactly one record, has %d" % (aid, seen.get(aid, 0)))
    for platform, names in platform_names.items():
        if len(names) > 1 or None in names:
            problems.append("creative-log.json: Angles on %s must all use one platform string: %s"
                            % (platform, ", ".join(sorted(str(n) for n in names))))
    if records and isinstance(records[-1], dict) and not record_edit_works(text, data, records[-1]):
        problems.append("creative-log.json must be pretty-printed, one key per line, with the last record's '}' "
                        "line followed by the list's ']' line, so gr0wthlab can add a new Angle's record")


def exact_edit(text, old, new):
    """The text after one exact edit, or None when gr0wthlab would refuse it
    (weekly_changes.py edit_problems)."""
    if text.count(old) != 1 or "```" in old + new:
        return None
    if any(line.startswith("#") for line in old.split("\n") + new.split("\n")):
        return None
    return text.replace(old, new, 1)


def kill_edit_works(text, data, position, record):
    """Whether gr0wthlab's kill edit of this record (compose_kill) changes
    exactly its status and adds the reads it was killed on."""
    lines = text.split("\n")
    named = re.compile(r'\s*"angle_id"\s*:\s*' + re.escape(json.dumps(record["angle_id"])) + r"\s*,?\s*")
    starts = [i for i, line in enumerate(lines) if named.fullmatch(line)]
    status = re.compile(r'(\s*)"status"(\s*:\s*)"[^"\\]*"(,?)\s*')
    if len(starts) != 1:
        return False
    found = next((i for i in range(starts[0], len(lines)) if status.fullmatch(lines[i])), None)
    if found is None:
        return False
    indent, colon, comma = status.fullmatch(lines[found]).groups()
    reads = ["2026-01-07", "2026-01-14"]
    new = lines[starts[0]:found] + ['%s"status"%s"killed",' % (indent, colon),
                                     '%s"killed_on_reads"%s%s%s' % (indent, colon, json.dumps(reads), comma)]
    changed = exact_edit(text, "\n".join(lines[starts[0]:found + 1]), "\n".join(new))
    expected = json.loads(json.dumps(data))
    target = expected["angles"] if isinstance(expected, dict) else expected
    target[position] = dict(record, status="killed", killed_on_reads=reads)
    try:
        return changed is not None and json.loads(changed) == expected
    except ValueError:
        return False


def record_edit_works(text, data, last):
    """Whether gr0wthlab can add a record after the last one with an exact
    edit (compose_record): a '}' line then a ']' line, and the record
    indented as the file indents its records."""
    record = dict(last, angle_id="P999", status="draft", results=None)
    expected = json.loads(json.dumps(data))
    (expected["angles"] if isinstance(expected, dict) else expected).append(record)
    lines = text.split("\n")
    for end in range(len(lines) - 1, 1, -1):
        if lines[end].strip() not in ("]", "],") or lines[end - 1].strip() != "}":
            continue
        brace, inner = lines[end - 1], lines[end - 2]
        indent = brace[:len(brace) - len(brace.lstrip())]
        step = max(len(inner) - len(inner.lstrip()) - len(indent), 1)
        added = [indent + line for line in json.dumps(record, indent=step, ensure_ascii=False).split("\n")]
        changed = exact_edit(text, "\n".join(lines[end - 1:end + 1]), "\n".join([brace + ","] + added + [lines[end]]))
        try:
            if changed is not None and json.loads(changed) == expected:
                return True
        except ValueError:
            continue
    return False


def check(pkg, product, registry=None, write_entry=False):
    pkg = Path(pkg)
    problems, warnings = [], []
    template, origin = load_template(registry)
    prefix = package_prefix(pkg, product)
    entry = fill(template, product, prefix)
    count = check_paths(pkg, prefix, entry, problems)
    rules = None
    rules_text = read(pkg, brand_lint.RULES_PATH)
    if rules_text is not None:
        try:
            rules = json.loads(rules_text)
            problems += ["brand-rules.json: %s" % p for p in brand_lint.validate_rules(rules)]
        except ValueError as exc:
            problems.append("brand-rules.json is not valid JSON: %s" % exc)
    kit = "05-social-pmf/"
    days = check_calendar(read(pkg, kit + "cadence-14-day.md") or "", problems) \
        if read(pkg, kit + "cadence-14-day.md") is not None else {}
    angles = check_angles(read(pkg, kit + "angles.md") or "", rules, problems, warnings) \
        if read(pkg, kit + "angles.md") is not None else {}
    pairs = check_pairs(read(pkg, kit + "ab-pairs.md") or "", angles, problems) \
        if read(pkg, kit + "ab-pairs.md") is not None else {}
    check_calendar_links(days, angles, pairs, problems)
    check_metrics(days, angles, problems)
    if read(pkg, kit + "platform-assignment.md") is not None:
        found = check_platforms(read(pkg, kit + "platform-assignment.md"), problems)
        if rules and isinstance(rules.get("caption_call_to_action"), dict):
            links = rules["caption_call_to_action"].get("links") or {}
            if set(links) != set(found):
                problems.append("brand-rules caption_call_to_action.links keys %s differ from the test platforms %s"
                                % (sorted(links), found))
    if read(pkg, kit + "read-the-results.md") is not None:
        check_read_results(read(pkg, kit + "read-the-results.md"), problems)
    if read(pkg, kit + "creative-log.json") is not None:
        bank = gc.find_table(read(pkg, kit + "angles.md") or "", gc.ANGLE_COLUMNS)
        check_creative_log(read(pkg, kit + "creative-log.json"), angles, problems, bank[0] if bank else ())
    else:
        problems.append("05-social-pmf/creative-log.json is missing (gr0wthlab writes kills into it)")
    checklist = read(pkg, "08-redteam/pre-publication-checklist.md")
    if checklist is not None:
        check_checklist(checklist, problems, warnings)
    competitors = check_competitors(pkg, problems)
    result = {"template": origin, "paths": count, "angles": len(angles), "pairs": len(pairs),
              "days": len(days), "competitors": competitors, "problems": problems, "warnings": warnings}
    if write_entry and not problems:
        out = pkg / "handoff" / "registry-entry.json"
        gc.write_json(out, {
            "comment": "The go_to_market_package entry for %s in gr0wthlab's config/products.json, ready "
                       "for the reviewed gr0wthlab change firstmate makes at Handoff. It is RepToday's entry "
                       "with the name changed and every path pointing into %s; only launch_checklist differs, "
                       "pointing inside the package. "
                       "The rest of the Product's registry entry (repository, filming, waitlist, "
                       "beta_recruiting) is product-specific and is set by that change; see handoff/README.md."
                       % (product, prefix),
            "template": origin,
            "go_to_market_package": entry,
        })
        result["entry"] = str(out)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Layout check against gr0wthlab's needed files")
    parser.add_argument("package")
    parser.add_argument("--product", required=True)
    parser.add_argument("--registry")
    parser.add_argument("--write-entry", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package, args.product, args.registry, args.write_entry)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        for warning in result["warnings"]:
            print("WARN " + warning)
        print("%s: %d registry paths, %d Angles, %d pairs, %d calendar days, %d competitors (template %s)" % (
            "PASS" if not result["problems"] else "FAIL", result["paths"], result["angles"],
            result["pairs"], result["days"], len(result["competitors"]), result["template"]))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
