#!/usr/bin/env python3
"""Brand-rules lint for a Candidate Package.

`09-extras/marketing-agent/brand-rules.json` is the brand lint's one rule
source, and gr0wthlab's post-Draft lint reads the same file after Handoff, so
this script first validates it against the schema gr0wthlab's lint accepts
(an unknown key there blocks every Draft), then applies it:

- every rule gr0wthlab applies to a post, with its matching, to every Hook in
  `05-social-pmf/angles.md` and `ab-pairs.md` and to the social copy (the
  Launch Set and the week-1 drafts);
- the rules that hold for any page a stranger reads (banned characters, stock
  phrases, fake scarcity, loss framing, [NEED:] markers) to the site, the video
  script, and the extras, whose sourced numbers the claim audit covers; a
  page's copy is its words and the attributes and JSON-LD a reader, search
  result, or share card shows.

Usage: brand_lint.py PACKAGE [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

RULES_PATH = "09-extras/marketing-agent/brand-rules.json"

STRING_LISTS = ("banned_words_in_hook", "banned_social_proof_in_hook", "all_caps_allowlist",
                "stock_phrases", "capped_words", "invented_proof_terms", "invented_proof_quantities",
                "fake_scarcity", "lint_allow_phrases", "loss_framing", "sponsorship_asks")
INTS = ("hook_max_words", "capped_words_per_paragraph", "long_sentence_words", "long_sentence_commas")
BOOLS = ("hook_must_not_be_question", "no_emoji_in_hook", "no_all_caps_words_in_hook")
OTHER = ("banned_characters_anywhere", "pain_source_url_must_start_with", "required_sections",
         "required_disclosure", "frozen_hooks_exempt_from", "caption_call_to_action", "comment", "notes")
KNOWN = set(STRING_LISTS) | set(INTS) | set(BOOLS) | set(OTHER)
REQUIRED = ("hook_max_words", "hook_must_not_be_question", "banned_words_in_hook",
            "banned_characters_anywhere", "pain_source_url_must_start_with", "caption_call_to_action")
TEST_PLATFORMS = ("TikTok", "YouTube Shorts")
COPY_SKIP = {"BUILD-SPEC.md", "README.md"}


def has_alnum(text):
    return any(ch.isalnum() for ch in text)


def validate_rules(rules, source_tags=None):
    problems = []
    if not isinstance(rules, dict):
        return ["brand-rules.json must be a JSON object"]
    for key in rules:
        if key not in KNOWN:
            problems.append("unknown key %r (gr0wthlab's lint would block every Draft)" % key)
    for key in REQUIRED:
        if key not in rules:
            problems.append("missing %r" % key)
    for key in STRING_LISTS:
        if key in rules:
            value = rules[key]
            if not isinstance(value, list) or not all(isinstance(v, str) and has_alnum(v) for v in value):
                problems.append("%s must be a list of strings, each with a letter or digit" % key)
    if "banned_characters_anywhere" in rules:
        value = rules["banned_characters_anywhere"]
        if not isinstance(value, list) or not all(isinstance(v, str) and v.strip() for v in value):
            problems.append("banned_characters_anywhere must be a list of non-blank strings")
    for key in INTS:
        if key in rules and (isinstance(rules[key], bool) or not isinstance(rules[key], int) or rules[key] < 0):
            problems.append("%s must be a whole number" % key)
    for key in BOOLS:
        if key in rules and not isinstance(rules[key], bool):
            problems.append("%s must be true or false" % key)
    prefix = rules.get("pain_source_url_must_start_with")
    if prefix is not None and (not isinstance(prefix, str) or not prefix):
        problems.append("pain_source_url_must_start_with must be a non-empty string")
    frozen = rules.get("frozen_hooks_exempt_from")
    if frozen is not None and (not isinstance(frozen, list) or
                               not set(frozen) <= {"hook_max_words", "banned_words_in_hook"}):
        problems.append("frozen_hooks_exempt_from may name only hook_max_words and banned_words_in_hook")
    cta = rules.get("caption_call_to_action")
    if cta is not None:
        if not isinstance(cta, dict) or set(cta) != {"line", "links"}:
            problems.append("caption_call_to_action must have exactly the keys line and links")
        else:
            line = cta["line"]
            if not isinstance(line, str) or "\n" in line or line.count("{link}") != 1 or \
                    not has_alnum(line.replace("{link}", "")):
                problems.append("caption_call_to_action.line must be one line with {link} once and words of its own")
            links = cta["links"]
            if not isinstance(links, dict) or not links:
                problems.append("caption_call_to_action.links must be a non-empty map")
            else:
                if set(links) != set(TEST_PLATFORMS):
                    problems.append("caption_call_to_action.links keys must be exactly %s" % ", ".join(TEST_PLATFORMS))
                tags = []
                for name, value in links.items():
                    if not isinstance(value, str) or found_links(value) != [value] or "://" in value \
                            or "/" not in value:
                        problems.append("link for %s must be a bare address with a domain, like site.app/tag" % name)
                        continue
                    tags.append(value.rsplit("/", 1)[1])
                if len(set(tags)) != len(tags):
                    problems.append("each platform's link needs a different Source tag")
                if source_tags is not None:
                    for tag in tags:
                        if tag not in source_tags:
                            problems.append("link tag %r is not a Waitlist Source tag" % tag)
    return problems


# Matching ported from gr0wthlab's src/gr0wthlab/lint.py (commit 6776dd0), so a
# Hook or post that passes here passes gr0wthlab's post-Draft lint after Handoff.
EMOJI_ABOVE = 0x2100
NUMBER = r"\d(?:[\d,.]*\d)?\s*(?:k|m|million|thousand)?\+?"
SEPARATOR = r"[\s_\-‐-―]+"
LETTER = r"[^\W_]"
BEFORE, AFTER = "(?<!%s)" % LETTER, "(?!%s)" % LETTER
QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"'})
NEED_MARKER = re.compile(r"\[NEED:[^\]]*\]", re.IGNORECASE)
# Anything a reader could follow: an address with its scheme, a www. name, a bare domain, or a Markdown link.
LINK = re.compile(
    r"(?:https?://|www\.)[^\s<>\"]+"
    r"|(?<![\w@./-])(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}(?![a-z0-9-])(?:/[^\s<>\"]*)?",
    re.IGNORECASE,
)
MARKDOWN_LINK = re.compile(r"\]\(")


def found_links(text):
    """Everything in a text a reader could follow as a link, as gr0wthlab's lint
    reads it: as written, without the punctuation that ends a sentence."""
    found = [m.group(0).rstrip(".,;:!?)'") for m in LINK.finditer(text)]
    return found + ["a Markdown link"] * len(MARKDOWN_LINK.findall(text))


def plain(text):
    return text.translate(QUOTES)


def phrase(term, tag=False):
    words = [w for w in re.split(SEPARATOR, plain(term)) if w]
    if tag:
        words = [w if w == "{n}" else re.sub(r"\W", "", w) for w in words]
    return ("_*" if tag else SEPARATOR).join(NUMBER if w == "{n}" else re.escape(w) for w in words)


def words_pattern(term, plural=True):
    ending = "(?:s|es)?" if plural else ""
    return re.compile(r"%s%s%s%s|#\w*?%s" % (BEFORE, phrase(term), ending, AFTER, phrase(term, tag=True)),
                      re.IGNORECASE)


def allowed_pattern(term):
    return re.compile(r"(?<![\w#])%s%s|(?<=#)%s(?!\w)" % (phrase(term), AFTER, phrase(term, tag=True)),
                      re.IGNORECASE)


def masked(text, rules):
    for term in rules.get("lint_allow_phrases") or []:
        text = allowed_pattern(term).sub(lambda m: " " * len(m.group(0)), text)
    return text


def paragraphs(text):
    return [b for b in re.split(r"\n\s*\n", text) if b.strip()]


def invented_proof(text, rules):
    found = []
    terms = rules.get("invented_proof_terms") or []
    quantities = rules.get("invented_proof_quantities") or []
    if terms:
        term = "|".join(phrase(w) for w in terms)
        tag_term = "|".join(phrase(w, True) for w in terms)
        amount = "|".join([NUMBER] + [phrase(w) for w in quantities])
        tag_amount = "|".join([NUMBER] + [phrase(w, True) for w in quantities])
        near = re.compile(r"%s(?:%s)%s(?:%s+%s){0,2}(?:%s)(?:s|es)?%s|#\w*?(?:%s)\w*?(?:%s)\w*"
                          % (BEFORE, amount, SEPARATOR, LETTER, SEPARATOR, term, AFTER, tag_amount, tag_term),
                          re.IGNORECASE)
        found += ["unsourced proof %r" % m.group(0) for m in near.finditer(text)]
    for pattern, what in ((r"\d+(?:\.\d+)?\s*(?:%|percent\b)", "percentage"),
                          (r"(?<!\w)\d+(?:\.\d+)?x(?!\w)", "multiplier")):
        found += ["unsourced %s %r" % (what, m.group(0)) for m in re.finditer(pattern, text, re.IGNORECASE)]
    return found


def lint_copy(text, rules, hook=False, full=True):
    """Return findings for one piece of copy. full=True applies every rule
    gr0wthlab applies to a post; full=False only the rules that hold for any
    page a stranger reads (characters, stock phrases, scarcity, loss framing,
    [NEED:] markers), since the claim audit covers a page's sourced numbers."""
    found = []
    words_text = masked(plain(text), rules)
    if hook:
        cap = rules.get("hook_max_words")
        if isinstance(cap, int) and len(text.split()) > cap:
            found.append("the Hook has %d words; at most %d" % (len(text.split()), cap))
    if full and rules.get("hook_must_not_be_question") and "?" in text:
        found.append("asks a question")
    if full:
        for key, label in (("banned_words_in_hook", "banned word"), ("banned_social_proof_in_hook", "social proof")):
            for term in rules.get(key) or []:
                if words_pattern(term).search(words_text):
                    found.append("%s %r" % (label, term))
    for ch in rules.get("banned_characters_anywhere") or []:
        if ch in text:
            found.append("banned character %r" % ch)
    if full and rules.get("no_emoji_in_hook"):
        symbols = sorted({c for c in text if ord(c) > EMOJI_ABOVE})
        if symbols:
            found.append("non-text symbol " + ", ".join(repr(s) for s in symbols))
    if full and rules.get("no_all_caps_words_in_hook"):
        allowed = set(rules.get("all_caps_allowlist") or [])
        for word in text.split():
            bare = word.strip(".,!:;\"'()#?")
            if len(bare) > 1 and bare.isupper() and bare not in allowed:
                found.append("all-caps word %r" % bare)
    for term in rules.get("stock_phrases") or []:
        if words_pattern(term, plural=False).search(words_text):
            found.append("stock phrase %r" % term)
    if full and rules.get("capped_words") and isinstance(rules.get("capped_words_per_paragraph"), int):
        cap = rules["capped_words_per_paragraph"]
        for paragraph in paragraphs(words_text):
            hits = [t for t in rules["capped_words"] for _ in words_pattern(t).finditer(paragraph)]
            if len(hits) > cap:
                found.append("%d capped words in one paragraph (%s); at most %d" % (len(hits), ", ".join(hits), cap))
    if full:
        found += invented_proof(words_text, rules)
    for key, label in (("fake_scarcity", "scarcity or urgency"), ("loss_framing", "loss-framed phrase")):
        for term in rules.get(key) or []:
            if words_pattern(term, plural=False).search(words_text):
                found.append("%s %r" % (label, term))
    marker = NEED_MARKER.search(text)
    if marker:
        found.append("still asks for proof: %s" % marker.group(0))
    return found


def hooks(pkg):
    out = []
    angles = pkg / "05-social-pmf" / "angles.md"
    if angles.is_file():
        table = gc.find_table(angles.read_text(encoding="utf-8"), ("ID", "Hook"))
        if table:
            header, rows, idx = table
            for row in rows:
                if len(row) == len(header) and re.fullmatch(r"P\d+", row[idx["ID"]]):
                    m = re.fullmatch(r"\"([^\"]+)\"", row[idx["Hook"]].strip())
                    out.append(("angles.md %s" % row[idx["ID"]], m.group(1) if m else row[idx["Hook"]]))
    pairs = pkg / "05-social-pmf" / "ab-pairs.md"
    if pairs.is_file():
        for number, line in enumerate(pairs.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"- Leg ([AB]) hook: (.*)", line)
            if m:
                q = re.search(r"\"([^\"]+)\"", m.group(2))
                out.append(("ab-pairs.md:%d" % number, q.group(1) if q else m.group(2)))
    return out


SOCIAL_GLOBS = ("10-launch-set/**/*.md", "05-social-pmf/week-1-drafts.md")
PAGE_GLOBS = ("03-site/*.html", "10-launch-set/**/*.html", "04-video/script.md", "09-extras/**/*.md",
              "09-extras/**/*.html")


def files_for(pkg, globs):
    seen = []
    for pattern in globs:
        for path in sorted(pkg.glob(pattern)):
            if path.is_file() and path.name not in COPY_SKIP and not path.name.startswith(".") and path not in seen:
                seen.append(path)
    return seen


COPY_FIELD_RE = re.compile(
    r"^\s*(?:[-*]\s+)?\*\*(hook|caption|title|description|hashtags|alt text|on-screen text|post|"
    r"bio|name|display name|thread|reply|text)(?: \d+)?:\*\*\s*(.*)$", re.IGNORECASE)
FIELD_END_RE = re.compile(r"^\s*(?:#|(?:[-*]\s+)?\*\*[^*]+:\*\*)")


def social_units(text):
    """Yield (line, copy) for each labeled copy field of a social Markdown file:
    `**Caption:**`, `**Title:**`, `**Alt text:**`, and the like. A field runs to
    the next blank line, label, or heading. Production notes outside those
    fields are not post copy and are not linted, as gr0wthlab lints only the
    fields a platform shows."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = COPY_FIELD_RE.match(lines[i])
        if not m:
            i += 1
            continue
        start, parts = i + 1, [m.group(2)]
        i += 1
        while i < len(lines) and lines[i].strip() and not FIELD_END_RE.match(lines[i]):
            parts.append(lines[i])
            i += 1
        copy = "\n".join(p for p in parts if p.strip())
        if copy.strip():
            yield start, copy


def copy_units(path, social=False):
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        return [(0, unit) for unit, _, _ in gc.read_html(text).page_copy()]
    if social:
        return list(social_units(text))
    return list(gc.markdown_units(text))


def lint_files(pkg, rules, globs, full):
    problems = []
    for path in files_for(pkg, globs):
        for number, unit in copy_units(path, social=full):
            for finding in lint_copy(unit, rules, full=full):
                where = gc.rel(pkg, path) + (":%d" % number if number else "")
                problems.append("%s: %s: %s" % (where, finding, " ".join(unit.split())[:100]))
    return problems


def check(pkg, source_tags=None):
    pkg = Path(pkg)
    path = pkg / RULES_PATH
    if not path.is_file():
        return {"hooks": 0, "problems": ["%s is missing" % RULES_PATH]}
    try:
        rules = gc.read_json(path)
    except ValueError as exc:
        return {"hooks": 0, "problems": ["%s is not valid JSON: %s" % (RULES_PATH, exc)]}
    problems = ["%s: %s" % (RULES_PATH, p) for p in validate_rules(rules, source_tags)]
    found = hooks(pkg)
    for where, hook in found:
        problems += ["%s: %s: %s" % (where, f, hook) for f in lint_copy(hook, rules, hook=True, full=True)]
    problems += lint_files(pkg, rules, SOCIAL_GLOBS, full=True)
    problems += lint_files(pkg, rules, PAGE_GLOBS, full=False)
    return {"hooks": len(found), "problems": problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Brand-rules lint for a Candidate Package")
    parser.add_argument("package")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: %d hooks linted, %d problem(s)" % ("PASS" if not result["problems"] else "FAIL",
                                                     result["hooks"], len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
