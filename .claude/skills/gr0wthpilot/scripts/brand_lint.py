#!/usr/bin/env python3
"""Brand-rules lint for a Candidate Package.

`09-extras/marketing-agent/brand-rules.json` is the brand lint's one rule
source, and gr0wthlab's post-Draft lint reads the same file after Handoff, so
this script first validates it against the schema gr0wthlab's lint accepts
(an unknown key there blocks every Draft), then applies it with the rule
semantics of gr0wthlab's lint (src/gr0wthlab/lint.py, Rules.check_one and
Rules.sponsorship), word and phrase rules matching after lint_allow_phrases
are masked:

- to every Hook in `05-social-pmf/angles.md` and `ab-pairs.md`, and to each
  labeled copy field of the social copy (the Launch Set's Markdown and the
  week-1 drafts), every rule gr0wthlab's lint applies to a post:
  hook_max_words (Hooks and `**Hook:**` fields only), hook_must_not_be_question,
  banned_words_in_hook, banned_social_proof_in_hook,
  banned_characters_anywhere, no_emoji_in_hook, no_all_caps_words_in_hook
  with all_caps_allowlist, stock_phrases, capped_words with
  capped_words_per_paragraph, invented_proof_terms with
  invented_proof_quantities (and any percentage or multiplier, when
  invented_proof_terms is set), fake_scarcity, loss_framing, and [NEED:]
  markers; long_sentence_words and long_sentence_commas are warnings, as in
  gr0wthlab, and skip alt text;
- frozen_hooks_exempt_from as gr0wthlab honors it: a Hook that is one of the
  kit's frozen Hooks word for word skips hook_max_words, and
  banned_words_in_hook does not count inside a frozen Hook's own words, a
  whole Hook or one of its sentences, wherever a field repeats them (every
  frozen Hook of the kit, since a draft field may show any day's Hook);
- to each `**Message:**` or `**Subject:**` field (a message to a creator,
  in the social copy or in `06-channels/`): every post rule above, plus
  sponsorship_asks, which gr0wthlab reads in a message to a creator only;
- to any page a stranger reads (the site, the Launch Set's HTML, the video
  script, and the extras, whose sourced numbers the claim audit covers):
  banned_characters_anywhere, stock_phrases, fake_scarcity, loss_framing, and
  [NEED:] markers; a page's copy is its words and the attributes and JSON-LD
  a reader, search result, or share card shows.

required_sections and required_disclosure are reported as not applicable,
because gr0wthlab's lint applies neither to a post (lint.py NOT_FOR_POSTS);
a rule type whose keys brand-rules.json lacks is reported as pending, as
gr0wthlab reports it. gr0wthlab's own post-Draft lint, which also checks each
platform's character and hashtag limits, stays the authority.

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
# How gr0wthlab's lint applies each kind of key (lint.py NOT_FOR_POSTS, NEW_RULE_TYPES, LOSS_FRAMING).
NOT_FOR_POSTS = {
    "required_sections": "the layout of the dry-run creative briefs; a post Draft has its own format",
    "required_disclosure": "screens shown as simulated; the kit's posts are real-device recordings",
}
RULE_TYPES = {
    "stock phrases": ("stock_phrases",),
    "capped words per paragraph": ("capped_words", "capped_words_per_paragraph"),
    "long sentences (warning)": ("long_sentence_words", "long_sentence_commas"),
    "invented proof": ("invented_proof_terms", "invented_proof_quantities"),
    "fake scarcity": ("fake_scarcity",),
    "allowed phrases": ("lint_allow_phrases",),
    "loss framing": ("loss_framing",),
}


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


# Matching ported from gr0wthlab's src/gr0wthlab/lint.py (commit 6776dd0), for
# the rules this script applies; gr0wthlab's own lint stays the authority.
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


def sentences(text):
    found = []
    for block in paragraphs(text):
        found += [part for part in re.split(r"(?<=[.!?])\s+|\n", block) if part.strip()]
    return found


def unfrozen(text, frozen):
    """The text with the frozen Hooks' own words blanked out, each whole Hook
    and each of its sentences, wherever the text repeats one as whole words
    (gr0wthlab's Rules.unfrozen)."""
    for part in [part for hook in frozen for part in (hook, *sentences(hook))]:
        words = plain(part).split()
        if words:
            pattern = re.compile(BEFORE + r"\s+".join(re.escape(word) for word in words) + AFTER)
            text = pattern.sub(lambda m: " " * len(m.group(0)), text)
    return text


def exempt_rules(rules):
    value = rules.get("frozen_hooks_exempt_from")
    return set(value) if isinstance(value, list) else set()


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


def lint_copy(text, rules, hook=False, full=True, frozen=(), message=False):
    """Return the blocking findings for one piece of copy, as gr0wthlab's
    Rules.check_one finds them. full=True applies every rule gr0wthlab's lint
    applies to a post; full=False only the rules that hold for any page a
    stranger reads (characters, stock phrases, scarcity, loss framing, [NEED:]
    markers), since the claim audit covers a page's sourced numbers. frozen
    holds the frozen Hooks the copy may show, whose own words are exempt from
    the rules frozen_hooks_exempt_from names; message=True also reads a
    message to a creator for sponsorship_asks (Rules.sponsorship)."""
    found = []
    words_text = masked(plain(text), rules)
    exempt = exempt_rules(rules)
    frozen = tuple(h for h in frozen if h.strip()) if full else ()
    if frozen and "banned_words_in_hook" in exempt:
        banned_text = masked(unfrozen(plain(text), frozen), rules)
    else:
        banned_text = words_text
    verbatim = any(plain(text).split() == plain(h).split() for h in frozen)
    if hook and not (verbatim and "hook_max_words" in exempt):
        cap = rules.get("hook_max_words")
        if isinstance(cap, int) and len(text.split()) > cap:
            found.append("the Hook has %d words; at most %d" % (len(text.split()), cap))
    if full and rules.get("hook_must_not_be_question") and "?" in text:
        found.append("asks a question")
    if full:
        for key, label, among in (("banned_words_in_hook", "banned word", banned_text),
                                  ("banned_social_proof_in_hook", "social proof", words_text)):
            for term in rules.get(key) or []:
                if words_pattern(term).search(among):
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
    if full and "capped_words" in rules and isinstance(rules.get("capped_words_per_paragraph"), int):
        cap = rules["capped_words_per_paragraph"]
        for paragraph in paragraphs(words_text):
            hits = [t for t in rules["capped_words"] or [] for _ in words_pattern(t).finditer(paragraph)]
            if len(hits) > cap:
                found.append("%d capped words in one paragraph (%s); at most %d" % (len(hits), ", ".join(hits), cap))
    if full and "invented_proof_terms" in rules:
        found += invented_proof(words_text, rules)
    for key, label in (("fake_scarcity", "scarcity or urgency"), ("loss_framing", "loss-framed phrase")):
        for term in rules.get(key) or []:
            if words_pattern(term, plural=False).search(words_text):
                found.append("%s %r" % (label, term))
    marker = NEED_MARKER.search(text)
    if marker:
        found.append("still asks for proof: %s" % marker.group(0))
    if message:
        for term in rules.get("sponsorship_asks") or []:
            if words_pattern(term).search(words_text):
                found.append("sponsorship ask %r" % term)
    return found


def sentence_warnings(text, rules, description=False):
    """gr0wthlab's long-sentence findings, which warn and never block, and
    skip a description such as alt text."""
    found = []
    if description:
        return found
    for key, unit, measure in (("long_sentence_words", "words", lambda s: len(s.split())),
                               ("long_sentence_commas", "commas", lambda s: s.count(","))):
        limit = rules.get(key)
        if isinstance(limit, int) and not isinstance(limit, bool):
            for sentence in sentences(text):
                if measure(sentence) > limit:
                    found.append("%s: %d %s, over %d" % (key, measure(sentence), unit, limit))
    return found


def statuses(rules):
    """How each key of brand-rules.json applies to a post, and each rule type
    that waits for keys it lacks, as gr0wthlab's Rules.statuses reports them."""
    rows = []
    for key in rules:
        if key in ("comment", "notes"):
            continue
        if key not in KNOWN:
            rows.append((key, "unknown", "gr0wthlab cannot check this rule yet, so it blocks every Draft"))
        elif key in NOT_FOR_POSTS:
            rows.append((key, "not applicable", NOT_FOR_POSTS[key]))
        elif key == "sponsorship_asks":
            rows.append((key, "applied", "to a message to a creator only; a post is not read for them"))
        else:
            rows.append((key, "applied", ""))
    for name, keys in RULE_TYPES.items():
        missing = [k for k in keys if k not in rules]
        if missing:
            rows.append((name, "pending", "brand-rules.json has no " + ", ".join(missing) + " yet"))
    return rows


def hooks(pkg):
    """(where, Hook, frozen) for every Hook of the kit; a Hook is frozen when
    gr0wthlab can read it as one: an angles.md Hook cell that is exactly one
    quoted line, or the first quoted text on an A/B pair's leg line."""
    out = []
    angles = pkg / "05-social-pmf" / "angles.md"
    if angles.is_file():
        table = gc.find_table(angles.read_text(encoding="utf-8"), ("ID", "Hook"))
        if table:
            header, rows, idx = table
            for row in rows:
                if len(row) == len(header) and re.fullmatch(r"P\d+", row[idx["ID"]]):
                    m = re.fullmatch(r"\"([^\"]+)\"", row[idx["Hook"]].strip())
                    out.append(("angles.md %s" % row[idx["ID"]], m.group(1) if m else row[idx["Hook"]], bool(m)))
    pairs = pkg / "05-social-pmf" / "ab-pairs.md"
    if pairs.is_file():
        for number, line in enumerate(pairs.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"- Leg ([AB]) hook: (.*)", line)
            if m:
                q = re.search(r"\"([^\"]+)\"", m.group(2))
                out.append(("ab-pairs.md:%d" % number, q.group(1) if q else m.group(2), bool(q)))
    return out


SOCIAL_GLOBS = ("10-launch-set/**/*.md", "05-social-pmf/week-1-drafts.md")
CREATOR_GLOBS = ("06-channels/**/*.md",)
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
    r"bio|name|display name|thread|reply|text|message|subject)(?: \d+)?:\*\*\s*(.*)$", re.IGNORECASE)
MESSAGE_FIELDS = ("message", "subject")
FIELD_END_RE = re.compile(r"^\s*(?:#|(?:[-*]\s+)?\*\*[^*]+:\*\*)")


def social_units(text):
    """Yield (line, copy, label) for each labeled copy field of a social Markdown file:
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
        start, parts, label = i + 1, [m.group(2)], m.group(1).lower()
        i += 1
        while i < len(lines) and lines[i].strip() and not FIELD_END_RE.match(lines[i]):
            parts.append(lines[i])
            i += 1
        copy = "\n".join(p for p in parts if p.strip())
        if copy.strip():
            yield start, copy, label


def copy_units(path, social=False):
    """(line, copy, label) for each piece of copy in a file; label is the
    field's label in social copy, else None."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        return [(0, unit, None) for unit, _, _ in gc.read_html(text).page_copy()]
    if social:
        return list(social_units(text))
    return [(number, unit, None) for number, unit in gc.markdown_units(text)]


def lint_files(pkg, rules, globs, full, frozen=(), only=None):
    problems, warnings = [], []
    for path in files_for(pkg, globs):
        for number, unit, label in copy_units(path, social=full):
            if only is not None and label not in only:
                continue
            where = gc.rel(pkg, path) + (":%d" % number if number else "")
            excerpt = " ".join(unit.split())[:100]
            findings = lint_copy(unit, rules, hook=label == "hook", full=full, frozen=frozen,
                                 message=label in MESSAGE_FIELDS)
            problems += ["%s: %s: %s" % (where, finding, excerpt) for finding in findings]
            if full:
                warnings += ["%s: %s: %s" % (where, finding, excerpt)
                             for finding in sentence_warnings(unit, rules, description=label == "alt text")]
    return problems, warnings


def check(pkg, source_tags=None):
    pkg = Path(pkg)
    path = pkg / RULES_PATH
    if not path.is_file():
        return {"hooks": 0, "problems": ["%s is missing" % RULES_PATH], "warnings": [], "statuses": []}
    try:
        rules = gc.read_json(path)
    except ValueError as exc:
        return {"hooks": 0, "problems": ["%s is not valid JSON: %s" % (RULES_PATH, exc)], "warnings": [],
                "statuses": []}
    problems = ["%s: %s" % (RULES_PATH, p) for p in validate_rules(rules, source_tags)]
    if not isinstance(rules, dict):
        return {"hooks": 0, "problems": problems, "warnings": [], "statuses": []}
    warnings = []
    found = hooks(pkg)
    frozen = tuple(dict.fromkeys(hook for _, hook, is_frozen in found if is_frozen))
    for where, hook, is_frozen in found:
        problems += ["%s: %s: %s" % (where, f, hook)
                     for f in lint_copy(hook, rules, hook=True, frozen=(hook,) if is_frozen else ())]
        warnings += ["%s: %s: %s" % (where, f, hook) for f in sentence_warnings(hook, rules)]
    for globs, full, only in ((SOCIAL_GLOBS, True, None), (CREATOR_GLOBS, True, MESSAGE_FIELDS),
                              (PAGE_GLOBS, False, None)):
        more, warned = lint_files(pkg, rules, globs, full, frozen=frozen, only=only)
        problems += more
        warnings += warned
    return {"hooks": len(found), "problems": problems, "warnings": warnings, "statuses": statuses(rules)}


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
        for warning in result["warnings"]:
            print("WARN " + warning)
        for rule, status, detail in result["statuses"]:
            if status != "applied":
                print("NOTE %s: %s (%s)" % (rule, status, detail))
        print("%s: %d hooks linted, %d problem(s)" % ("PASS" if not result["problems"] else "FAIL",
                                                     result["hooks"], len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
