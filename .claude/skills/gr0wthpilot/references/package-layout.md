# Package layout and the formats gr0wthlab reads

A Candidate Package mirrors RepToday's Go-To-Market Package (`projects/RepToday/gtm/`), so that at Handoff a new Product's entry in gr0wthlab's registry (`config/products.json`) is RepToday's with the name changed and its paths pointing into the package's own folder (`gtm/`, or a dated `gtm-candidate-<date>/`).
`registry-template.json` here is that entry, from gr0wthlab at commit `6776dd0`; `scripts/check_layout.py` prefers gr0wthlab's live registry when it can read one (`~/gr0wthlab`, or `GR0WTHLAB_DIR`).
One path differs from RepToday's: the launch checklist is `launch-checklist.md` inside the package, because a run writes only inside the package, while RepToday's sits beside its package.

## The tree

```
<package>/
  recap.html               the single front door
  README.md                open the recap, serve the site, play the video, in three commands
  run-journal.json         gates passed, sessions, workflows (scripts/journal.py)
  decisions-log.md         every [DECIDED BY AGENT] decision, with the alternative rejected
  sources.md               every URL cited, with its fetch time (rebuilt from sources.d/)
  sources.d/               per-agent source fragments
  sources-exempt.md        URL prefixes that are not claims, each with a reason (optional)
  screens-manifest.md      every real screen used, with its repo path and commit
  self-grade.md
  launch-checklist.md      the Founder's ordered path to the first post (gr0wthlab reads it)
  run-audit.md             tool calls, refusals, questions asked (none), workflows, simulators
  run-evidence/            copies of the guard's logs and the simulator ledger
  handoff/README.md        what Handoff does and what the gr0wthlab change must still set
  handoff/registry-entry.json
  01-research/             product-facts-brief.md, competitor-<slug>.md, pain-points.md,
                           review-mining.md, category-economics.md, pricing.md, aso-landscape.md,
                           channel-evidence.md, creator-landscape.md, name-collisions.md, last30days/
  02-brand/                positioning.md, naming-decision.md, brand-guidelines.md, logo SVGs,
                           tournament/ (rubric-*, pitch-*, judge-*, scorecard.md),
                           gate-test-asset*.html|png, gate-test-report.md, screens/
  03-site/                 index.html, index-b.html, assets, screenshots/, screenshot-gate.md,
                           cro-review.md, ai-seo-review.md
  04-video/                walkthrough.mp4, script.md, build/, gate.json, ffprobe-report.txt,
                           frames/, frame-strip.png, gate-report.md
  05-social-pmf/           the Test Kit: angles.md, ab-pairs.md, cadence-14-day.md,
                           platform-assignment.md, read-the-results.md, creative-log.json,
                           week-1-drafts.md
  06-channels/             channel-plan.md, event-metric-schema.md, creator shortlist
  07-thesis/               investment-thesis.md (and any rubric its kill criteria need)
  08-redteam/              redteam-<persona>.md, claims-ledger.md, dossier.md,
                           critic-phase-<n>.md, pre-publication-checklist.md
  09-extras/               marketing-agent/brand-rules.json and BUILD-SPEC.md (gr0wthlab reads both),
                           every extra, the invented deliverable
  10-launch-set/           instagram/, x/, tiktok/, manifest.json
```

## Files gr0wthlab parses with code

These rules come from gr0wthlab's parsers (`src/gr0wthlab/kit.py`, `results.py`, `weekly_changes.py`, `lint.py`, `shots.py` at `6776dd0`); `check_layout.py` and `brand_lint.py` enforce them.
A table is found by its header: a header cell matches a wanted column when it equals it, starts with it, or contains it, case-insensitively, so keep headers unambiguous.

### 05-social-pmf/angles.md

A table with the columns ID, Angle, pain, Hook, Format, Platform, signal, Kill, for example:

```
| ID | Angle | Sourced pain | Hook | Format | Platform | Pre-registered success signal | Kill criterion |
|---|---|---|---|---|---|---|---|
| P01 | Waiting is the point | "I miss not knowing how the photos came out" (https://www.reddit.com/r/...) | "Shoot now. See it tomorrow." | 15-20s screen record of a real roll developing | TikTok | watched-full rank in the top half of the bank once 10 posts shipped | bottom third on two reads |
```

- IDs are `P` and a zero-padded number (`P01`); at least 15 Angles.
- The Hook cell is exactly one straight-quoted string: that is the frozen Hook.
- The pain cell holds the pain's source URL (https).
- Platform is `TikTok` or `YouTube Shorts`.
- Format names a recording gr0wthlab's filming plan knows: founder on camera, screen record, time-lapse, slow motion, demo, pan, or video, optionally after a length like `15-20s`.
- The signal and Kill cells name metrics gr0wthlab collects: watched-full, viewed versus swiped, % viewed, watch time, saves, shares, likes, profile visits, comments.

### 05-social-pmf/ab-pairs.md

One section per pair:

```
## AB-1: the delay mechanic (angle P01, TikTok, same screen record)

- Leg A hook: "Shoot now. See it tomorrow."
- Leg B hook: "Your photos develop overnight."
- Belief tested: ...
```

The heading names `angle P..` and ends with a parenthesis whose second part is the platform; both `- Leg A hook:` and `- Leg B hook:` lines start at column 0 with a straight-quoted Hook.

### 05-social-pmf/cadence-14-day.md

A table with Day, Asset, Angle, and a primary-platform column; days 1 to 13 at least, each once.
A fixed day's Angle cell starts with its Angle ID; a pair leg is written `P01 / AB-1 leg A`, and the pair's Angle must be that day's Angle.
Exactly one flex day may lack a fixed Angle, and it names exactly one fallback Angle.
The platform cell is `TikTok` or `YouTube Shorts`.
An optional `## ... checklist` section lists asset checks as `- ` items; a line that names `creative-log.json` and "killed" states the kill rule.

### 05-social-pmf/platform-assignment.md

A `## The two test platforms` section holding `### 1. TikTok (primary)` and `### 2. YouTube Shorts (secondary)`, spelled exactly so.

### 05-social-pmf/read-the-results.md

It must hold the floor line, for example:
`- Any post under 200 impressions is unread, not failed; the floor counts each platform's views (TikTok Studio's video views, YouTube Studio's views).`

### 05-social-pmf/creative-log.json

Pretty-printed JSON, one key per line: an object with a `comment` and an `angles` list, one record per Angle, and only these keys: angle_id, hook, platform, hypothesis, format, preregistered_success_signal, kill_criterion, pain_rank, pain_state, verbatim_quote, pain_source_url, ab_pair, results, status.
`angle_id` is the Angle's ID alone or followed by a hyphen (`"P01"` or `"P01-waiting"`, never `"P01_waiting"`), on a line of its own, and the record's `status` line follows it within the same record, because gr0wthlab's kill edits from one to the other.
Every Angle on the same platform uses the same platform string (`tiktok`, `youtube_shorts`); `status` starts `draft` and `results` is `null`.
The file ends with a `]` line and then a `}` line.

### 09-extras/marketing-agent/brand-rules.json

The brand lint's one rule source, for this package and for gr0wthlab's post Drafts; an unknown key blocks every Draft.
Keys: `comment`, `notes`; lists of words or phrases `banned_words_in_hook`, `banned_social_proof_in_hook`, `all_caps_allowlist`, `stock_phrases`, `capped_words`, `invented_proof_terms`, `invented_proof_quantities`, `fake_scarcity`, `lint_allow_phrases`, `loss_framing`, `sponsorship_asks`; `banned_characters_anywhere` (include the em dash); whole numbers `hook_max_words`, `capped_words_per_paragraph`, `long_sentence_words`, `long_sentence_commas`; booleans `hook_must_not_be_question`, `no_emoji_in_hook`, `no_all_caps_words_in_hook`; `pain_source_url_must_start_with` (`"https://"`); `frozen_hooks_exempt_from` (only `hook_max_words` and `banned_words_in_hook`); `required_sections`, `required_disclosure`.
`caption_call_to_action` is `{"line": "Join the waitlist: {link}", "links": {"TikTok": "<site>/tiktok", "YouTube Shorts": "<site>/youtube"}}`: one line with `{link}` once, links keyed exactly by the two platforms, bare addresses whose last part is a Waitlist Source tag, a different one per platform.
Each link is a domain with its top-level domain and no scheme (`immerse.app/tiktok`, not `immerse/tiktok`), as gr0wthlab's lint reads a link; one it cannot read as a link blocks every Draft.
Every field of post copy, not only a Hook, is refused for a question mark when `hook_must_not_be_question` is true, as gr0wthlab's lint refuses it.
Derive the lists from the brand guidelines' voice rules and the category's forbidden claims.

### 08-redteam/pre-publication-checklist.md

Items at column 0, `- [ ] **Title** what to do (blocking: scope)`, continuation lines indented two spaces.
An open item whose scope starts "everything public" or "social" and names no claim blocks every gr0wthlab post Draft until the Founder closes it; use that scope only for what truly must come first, such as the Waitlist going live.

### 01-research/competitor-*.md

See `research.md`: each starts `# Competitor Teardown: <Name>` and cites the US App Store page.

## Files gr0wthlab reads as text

`02-brand/brand-guidelines.md`, `02-brand/positioning.md` (gr0wthlab scores Listening Fit against it, so it must define the customer plainly), `06-channels/` (the channel plan must name, by name, any creator the Founder may write to), `07-thesis/` (Beta Cohort invitations cite its lines word for word, so it holds a line giving the first session's length in minutes), `launch-checklist.md`, and `09-extras/marketing-agent/BUILD-SPEC.md`.

`BUILD-SPEC.md` describes, for gr0wthlab's post-Draft agent, how this Product's posts are made: the creative loop from Angle to Hook to Draft, the brand-rules lint as the floor, what a vision check of each asset must look for in this brand, what each platform's caption and on-screen text hold, and what must never be generated.

## Social copy the lint reads

In `05-social-pmf/week-1-drafts.md` and the Launch Set's Markdown, put every piece of post copy in a labeled field at the start of a line, as gr0wthlab lints only what a platform shows:

```
**Caption:** ...
**Title:** ...
**Hashtags:** ...
**Alt text:** ...
**On-screen text:** ...
**Bio:** ...
```

A field runs to the next blank line, label, or heading; production notes outside fields are not linted.

## 10-launch-set/manifest.json

```
{"assets": [
  {"platform": "instagram", "kind": "profile-image", "path": "instagram/profile.png", "size": "320x320",
   "size_source": "<the platform help page fetched in this run>"},
  {"platform": "instagram", "kind": "first-week-posts", "path": "instagram/week-1.md", "size_source": "..."}
]}
```

Platforms are `instagram`, `x`, and `tiktok`; each needs at least a `profile-image` and `first-week-posts`.
Every asset whose kind is not text (`first-week-posts` or `bio`) is a PNG, JPEG, or WebP image at exactly its stated size, and every `size_source` is the http(s) URL of the platform page fetched in this run that gives the size, which `sources.md` lists.

## handoff/

`registry-entry.json` is written by `check_layout.py <package> --product <Product> --write-entry` once the layout check passes; every path in it points into the package's own folder, the one that would be handed off.
`README.md` says what Handoff does (the Founder's words, the package's Handoff line from the preflight: "<Product> - hand to gr0wthlab" for `gtm/`, "<Product> - hand to gr0wthlab (<folder>)" for a dated folder; firstmate's reviewed gr0wthlab change adding the entry; the next weekly run picking it up) and what that change must still set that is not a package file: the repository block, the Waitlist view and its Source tags and Fit answers, filming, and the Beta Cohort size.
For a Candidate Package beside a live one (`beside-live`), it says a second Handoff waits for gr0wthlab to take a replacement package, and gives no ready Handoff line.
