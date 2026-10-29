#!/usr/bin/env python3
"""Helpers for a name-only rerun: which names are ruled out, the copy of a
package kept before a rerun or a swap changes it, the swap of an accepted name
through the package, and the check of the ranked shortlist a rerun ends with.

Nothing here records a gate or touches the run journal; `journal.py` and the
launcher (`gp_run.py prepare --rename` and `--accept-name`) do, and call these.

The swap replaces the earlier name in the package's deliverables, never in its
records, and never inside a URL:
  - the name exactly as given (`Rewound`) and in capitals (`REWOUND`), as
    whole words;
  - its lowercase letters and digits (`rewound`) only where they are glued to
    another letter, digit, `@`, or `_`, as in a proposed handle or domain
    (`@rewound`, `getrewound.app`, `rewoundcamera.app`).
A lowercase whole word is left alone, because it may be ordinary English ("the
film is rewound"), and so is a bare domain such as `rewound.app`, which may be
a fact about someone else's domain. Records (HISTORY below) say what was found,
judged, or decided under the earlier name, and stay as written.
Every line the swap changed, and every occurrence it left outside a record, is
listed in a review sheet the run works through by hand.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

SHORTLIST = "02-brand/name-shortlist.md"
TOURNAMENT = "02-brand/tournament"

# Package paths that record what a run found, judged, or decided; the swap
# never changes them. A path ending in "/" or "-", or naming the tournament,
# covers everything it begins (so `02-brand/tournament-rewound/` too).
HISTORY = (
    gc.JOURNAL_NAME, "decisions-log.md", "sources.md", "sources-exempt.md", "sources.d/", gc.AUDIT_NAME,
    "run-evidence/", "01-research/name-collisions.md", "02-brand/naming-decision.md", SHORTLIST, TOURNAMENT,
    "02-brand/gate-test-", "03-site/screenshot-gate.md", "04-video/gate-report.md", "08-redteam/",
)
# Deliverables inside a record folder, which the swap does change.
NOT_HISTORY = ("08-redteam/pre-publication-checklist.md",)

# Files the swap reads as text: what the checks read, plus the code and styles
# that build renders (a video's title cards, a page's form messages).
SWAP_SUFFIXES = gc.TEXT_SUFFIXES | {".py", ".js", ".mjs", ".css", ".xml", ".srt", ".vtt"}
MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov", ".m4v", ".pdf"}

NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9 .'&-]{0,39}")
# A swapped line that may state a fact about the earlier name rather than use
# it as the brand: it cites a source, or talks about names, domains, or marks.
FACT_HINT_RE = re.compile(
    r"https?://|\[[A-Z][A-Z0-9-]*\]|\b(?:collid\w*|collision\w*|pulled|registered|held|belongs?|owned|taken|"
    r"trademark\w*|USPTO|called|named|means?|meaning|why|reserv\w*)\b", re.I)


def slug(name):
    """A name's lowercase letters and digits, as a handle or domain spells it."""
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def valid_name(name):
    """Why a name cannot be handed over or ruled out, or None."""
    if not NAME_RE.fullmatch(name or "") or not slug(name):
        return ("%r is not a name: use 1 to 40 letters, digits, spaces, and . ' & -, starting with a letter "
                "or digit" % name)
    return None


def ruled_out(name, names, roots):
    """Why a name is ruled out, or None: it is one of `names` in any case or
    spacing, or contains one of `roots` in any case or spacing."""
    key = slug(name)
    for other in names or []:
        if key == slug(other):
            return "%s is ruled out (as %s)" % (name, other)
    for root in roots or []:
        if slug(root) and slug(root) in key:
            return "%s shares the ruled-out root %s" % (name, root)
    return None


def is_history(rel):
    rel = rel.replace(os.sep, "/")
    if rel in NOT_HISTORY:
        return False
    return any(rel == h or rel.startswith(h) for h in HISTORY)


def backup(pkg, work, label, now):
    """Copy the whole package to `<work>/backups/<UTC time>-<label>/` and
    return that folder. The cache folder is the one place besides the package
    a run may write, so the copy survives the run and needs no git."""
    pkg = Path(pkg)
    root = Path(work) / "backups"
    root.mkdir(parents=True, exist_ok=True)
    base = "%s-%s" % (now.strftime("%Y%m%dT%H%M%SZ"), re.sub(r"[^A-Za-z0-9_-]+", "-", label).strip("-"))
    dest, n = root / base, 2
    while dest.exists():
        dest = root / ("%s-%d" % (base, n))
        n += 1
    shutil.copytree(str(pkg), str(dest), symlinks=True)
    copied = sum(len(files) for _, _, files in os.walk(str(dest)))
    original = sum(len(files) for _, _, files in os.walk(str(pkg)))
    if copied != original:
        raise OSError("the copy of %s in %s holds %d files, not %d" % (pkg, dest, copied, original))
    return dest


def set_aside_tournament(pkg, old):
    """Move the package's tournament to `02-brand/tournament-<old>/` (or
    `-2`, `-3`, ...) so a rerun's tournament starts in an empty folder and the
    earlier one stays readable. Returns the new folder's package path, or None
    when there was no tournament."""
    pkg = Path(pkg)
    current = pkg / TOURNAMENT
    if not current.is_dir():
        return None
    base = "%s-%s" % (TOURNAMENT, slug(old))
    dest, n = pkg / base, 2
    while dest.exists():
        dest = pkg / ("%s-%d" % (base, n))
        n += 1
    current.rename(dest)
    return gc.rel(pkg, dest)


def _spans(line):
    """(text, is_url) pieces of a line, so a URL is never changed."""
    out, last = [], 0
    for m in gc.URL_RE.finditer(line):
        out.append((line[last:m.start()], False))
        out.append((m.group(0), True))
        last = m.end()
    out.append((line[last:], False))
    return out


def _patterns(old, new):
    edge = r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])"
    pairs = [(re.compile(edge % re.escape(old)), new)]
    if old.upper() != old:
        pairs.append((re.compile(edge % re.escape(old.upper())), new.upper()))
    low = re.escape(slug(old))
    pairs.append((re.compile(r"(?<=[A-Za-z0-9@_])%s|%s(?=[A-Za-z0-9_])" % (low, low)), slug(new)))
    return pairs


def _leftover_re(old):
    words = [re.escape(w) for w in re.split(r"\s+", old.strip())]
    return re.compile(r"%s|%s" % (r"\s*".join(words), re.escape(slug(old))), re.I)


def swap_text(text, old, new):
    """(new text, [(line number, line after)] changed, [(line number, line)]
    still naming the earlier name outside a URL)."""
    pairs, leftover = _patterns(old, new), _leftover_re(old)
    changed, left, out = [], [], []
    for number, line in enumerate(text.split("\n"), 1):
        pieces = []
        for piece, is_url in _spans(line):
            if not is_url:
                for pattern, repl in pairs:
                    piece = pattern.sub(repl, piece)
            pieces.append(piece)
        after = "".join(pieces)
        if after != line:
            changed.append((number, after))
        if any(not is_url and leftover.search(piece) for piece, is_url in _spans(after)):
            left.append((number, after))
        out.append(after)
    return "\n".join(out), changed, left


def _files(pkg):
    for root, dirs, files in os.walk(str(pkg)):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "__pycache__")
        for name in sorted(files):
            if not name.startswith("."):
                yield Path(root) / name


def swap(pkg, old, new):
    """Swap `old` for `new` through the package's deliverables, in place.

    Returns {"files": {path: lines changed}, "changed": {path: [(n, line)]},
    "left": {path: [(n, line)]}, "media": [paths], "svgs": [paths]}: what
    changed, where the earlier name still stands outside a record, every
    rendered image or video (all but the real screens `screens-manifest.md`
    names) that may show the earlier name, and every changed SVG, which may
    draw it in shapes."""
    pkg = Path(pkg)
    manifest = pkg / "screens-manifest.md"
    screens = manifest.read_text(encoding="utf-8") if manifest.is_file() else ""
    report = {"files": {}, "changed": {}, "left": {}, "media": [], "svgs": []}
    for path in _files(pkg):
        rel = gc.rel(pkg, path)
        if is_history(rel):
            continue
        suffix = path.suffix.lower()
        if suffix in MEDIA_SUFFIXES:
            if path.name not in screens:
                report["media"].append(rel)
            continue
        if suffix not in SWAP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        after, changed, left = swap_text(text, old, new)
        if changed:
            path.write_text(after, encoding="utf-8")
            report["files"][rel] = len(changed)
            report["changed"][rel] = changed
            if suffix == ".svg":
                report["svgs"].append(rel)
        if left:
            report["left"][rel] = left
    return report


def write_review(path, old, new, report, backup_dir, product):
    """The review sheet a run works through after a swap, kept in the cache
    folder: it quotes package text no check should read as the package's own."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines_changed = sum(report["files"].values())
    out = [
        "# Name swap review: %s to %s (%s)" % (old, new, product),
        "",
        "The launcher swapped the name before this session started; the package as it was is kept in %s." % backup_dir,
        "The swap changed the name as given and in capitals as whole words, and its lowercase spelling inside handles "
        "and domains, in every deliverable; it changed no URL and no record (%s)." % ", ".join(HISTORY),
        "Work through every line below: keep it, or rewrite it.",
        "A line that states a fact about %s (a collision, a domain or app someone else holds, a clearance step), or "
        "reasons from what the word %s means, is not true of %s: restore %s there as the earlier name, or rewrite or "
        "cut the reasoning." % (old, old, new, old),
        "Lines marked CHECK cite a source or talk about names, domains, or marks; that is a hint, not the whole list.",
        "",
        "## Swapped lines (%d in %d files)" % (lines_changed, len(report["files"])),
        "",
    ]
    for rel in sorted(report["changed"]):
        out.append("### %s" % rel)
        out.append("")
        for number, line in report["changed"][rel]:
            out.append("- %sL%d: %s" % ("CHECK " if FACT_HINT_RE.search(line) else "", number, line.strip()))
        out.append("")
    out += ["## Not swapped (%d lines in %d files)" % (sum(len(v) for v in report["left"].values()),
                                                       len(report["left"])), "",
            "Each still names %s outside a URL: a lowercase word (perhaps ordinary English), a bare domain, or a form "
            "the swap does not touch. Decide each one." % old, ""]
    for rel in sorted(report["left"]):
        out.append("### %s" % rel)
        out.append("")
        for number, line in report["left"][rel]:
            out.append("- L%d: %s" % (number, line.strip()))
        out.append("")
    out += ["## Drawn: SVGs the swap changed (%d)" % len(report["svgs"]), "",
            "Their text changed; any that spells %s in shapes (a wordmark) must be drawn again for %s." % (old, new), ""]
    out += ["- %s" % rel for rel in report["svgs"]] + [""]
    out += ["## Rendered: images and video that may show %s (%d)" % (old, len(report["media"])), "",
            "Every image or video outside the records that `screens-manifest.md` does not name as a real screen.",
            "Render again each one that shows the name, from its swapped source.", ""]
    out += ["- %s" % rel for rel in report["media"]] + [""]
    path.write_text("\n".join(out), encoding="utf-8")
    return path


SECTION_RE = re.compile(r"^## (.+?)\s*$", re.M)
RANKED_RE = re.compile(r"^(\d+)\.\s+(.+?)\s+`?\[PROPOSAL\]`?$")
EVIDENCE = (("App Store", True), ("Web", True), ("Domains", False))


def _sections(text):
    marks = list(SECTION_RE.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        yield m.group(1), text[m.end():end]


def check_shortlist(path, product, names, roots):
    """(problems, ranked names) of a rerun's shortlist; see "Shortlist" in
    references/research.md for the format."""
    path = Path(path)
    if not path.is_file():
        return ["%s is missing" % SHORTLIST], []
    text = path.read_text(encoding="utf-8")
    problems, ranked, next_step = [], [], None
    for heading, body in _sections(text):
        m = RANKED_RE.match(heading)
        if heading.lower().startswith("next step"):
            next_step = body
            continue
        if not m:
            continue
        rank, name = int(m.group(1)), m.group(2).strip()
        ranked.append(name)
        if rank != len(ranked):
            problems.append("%s is ranked %d where rank %d belongs; rank the names 1, 2, 3, ... in order"
                            % (name, rank, len(ranked)))
        why = ruled_out(name, names, roots) or valid_name(name)
        if why:
            problems.append(why)
        for label, absence_ok in EVIDENCE:
            line = re.search(r"^\s*[-*]\s*%s:(.*)$" % re.escape(label), body, re.M)
            if not line:
                problems.append("%s has no '- %s:' line with its evidence" % (name, label))
            elif not gc.find_urls(line.group(1)) and not (absence_ok and re.search(r"\bnone seen\b", line.group(1),
                                                                                    re.I)):
                problems.append("%s's %s line cites no URL%s" % (name, label, " and does not say 'none seen'"
                                                                 if absence_ok else ""))
        if "UNVERIFIED" not in body:
            problems.append("%s's section must say its trademark and App Store name clearance are UNVERIFIED" % name)
    if len({slug(n) for n in ranked}) != len(ranked):
        problems.append("a name appears twice in the shortlist")
    if not 3 <= len(ranked) <= 7:
        problems.append("the shortlist ranks %d names; rank about five (3 to 7), each under a '## <rank>. <Name> "
                        "[PROPOSAL]' heading" % len(ranked))
    command = "bin/gr0wthpilot %s --accept-name" % product
    if next_step is None:
        problems.append("the shortlist has no '## Next step' section")
    elif "App Store Connect" not in next_step or command not in next_step:
        problems.append("the '## Next step' section must tell the Founder to try the names in App Store Connect in "
                        "order and to run `%s \"<name>\"` with the first one it accepts" % command)
    return problems, ranked
