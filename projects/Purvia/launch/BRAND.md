# BRAND.md - the Purvia identity and voice book

Purpose: a stranger with this file and the repo can produce a new on-brand asset without asking anyone anything.
Scope: identity + voice only. The name is settled by `docs/adr/0011-product-name.md` and is not revisitable here.

## 1. Name

- **Purvia**, always capitalized as a proper noun in prose ("Purvia"), lowercase in the wordmark ("purvia").
- Coined from *purview*: "the scope of what one is authorized to see and know" (`docs/adr/0011-product-name.md:30-33`). When you explain the name, use exactly that etymology; never invent another.
- The technical namespace stays `agentic-rag`/`ar` everywhere it already exists; never "fix" it in marketing screenshots (`docs/adr/0011-product-name.md:53-61`).
- **The white-label rule is absolute:** the support widget renders the buyer's brand, never Purvia's. No Purvia logo, name, or link may ever appear on a widget surface or in widget copy (`docs/adr/0011-product-name.md:63-66`).

## 2. The brand idea

**Purvia is the vendor that shows you its red days.**
The product enforces who may see what; the brand earns belief by measuring itself in public - including 42 days of its own benchmark reading 0.000 under a green table (`README.md:41-77`).
Every asset should feel like an engineer's lab notebook, not a launch video: dated, numbered, falsifiable, a little dry, quietly confident.

Three brand pillars, each anchored to the ledger (`launch/CLAIMS.md`):

1. **The predicate, not a filter.** Authorization lives inside the SQL retrieval predicate (C1). This is the *what*.
2. **Numbers travel with denominators.** Every quality number is stated with its n and corpus (C3, C14 cap). This is the *how we talk*.
3. **The failure that mattered.** We lead with the measured failure and its fix, because a harness you can trust is worth more than a table that is always green (C4, C29). This is the *why believe us*.

## 3. Voice

Write like the repo's own docs (`docs/evals.md` is the house style reference): plain declaratives, concrete nouns, numbers with denominators, limitations stated adjacent to strengths - never in a footnote.

Rules:

- Every quality adjective is replaced by a number and its denominator, or deleted. "Fast" -> "12.6s for the 60-question run" (C15 source).
- The name-swap test: if a sentence still works with a competitor's name swapped in, rewrite it around a fact only Purvia can cite (a file path, a date, a measured value).
- Confess before the reader can accuse. State the 16-chunk corpus before showing the 1.000 table, not after.
- No exclamation marks. No rhetorical questions in headlines. At most one metaphor per asset, and never in the same sentence as a number.
- First person plural ("we measured", "our benchmark lied to us for 42 days") for the story; second person ("your corpus", "your viewers") for instructions.
- Present tense for what ships; past tense with dates for what happened; future tense only inside clearly-labeled planned items.
- Banned vocabulary: everything in `launch/bin/claimlint.sh` (marketing superlatives, "proven secure", "zero-trust", etc.). Also banned: "AI-powered", "magic", "instantly", "just works".
- "Open-core" is the packaging word; "kit" is the product-shape word; "platform" is allowed only when both surfaces are in frame (ADR-0011 uses it).

Voice calibration pairs:

| Off-brand | On-brand |
|---|---|
| "Enterprise-ready security you can trust" | "The no_access table reads 1.000 in every cell - 60 questions, 3 modes, 3 viewers, on a 16-chunk demo corpus. Here is what that does and does not prove." |
| "Battle-tested evals" <!-- CLAIMLINT-ALLOW: off-brand example --> | "The harness caught a Δ -0.510 recall@5 regression from a one-line change and posted the red table on the PR in 4 minutes." |
| "Blazing-fast hybrid retrieval" <!-- CLAIMLINT-ALLOW: off-brand example --> | "The harness caught our hybrid stack losing to its own vector leg - keyword recall@5 was 0.140 - and measured the fix." |
| "We take security seriously" | "A viewer with no grant retrieves zero gold chunks, or CI fails. That gate cannot be configured off; the only way to silence it is to delete the eval, which is a tracked diff." |
| "Trusted by developers" | (delete - no customers may be implied that do not exist) |

## 4. Story architecture (use in this order)

1. **Cold open:** the failure. "For 42 days our scale benchmark measured 0.000. The table on our README stayed green. The alarm fired every night." (C4)
2. **The turn:** the reporting was the failure; the fix made "measured nothing" unpublishable (C7).
3. **The point:** this is the harness you get for *your* corpus, with the leak matrix derived free from your gold labels (C9, C10).
4. **The product:** permissions in the predicate, two surfaces, readable raw-SDK code (C1, C19).
5. **The boundaries:** who should not buy (POSITIONING.md list), read-only grants, flat groups, unmeasured 100k+ scale (C26, C27).
6. **The ask:** MIT core on GitHub; Pro tier $199 one-time when its deliverables exist (C24, C25).

## 5. Visual identity

Built for zero-spend, system-font, self-contained assets.

### Color

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#101A2B` | Primary text, dark backgrounds |
| `--paper` | `#F7F5F0` | Light backgrounds |
| `--predicate` | `#1E4FD8` | Primary accent: links, the wordmark dot, CTAs |
| `--alarm` | `#C8372D` | The red of the failure story, regression deltas, "who should not buy" |
| `--measured` | `#1F7A45` | Green table cells, passing gates - only ever used for *measured* results |
| `--slate` | `#5B6472` | Secondary text, captions, denominators |
| `--grid` | `#D8D4CC` | Rules, table borders on paper; `#243247` on ink |

The signature move: **red and green appear together.** Green is never shown without the denominator in slate beside it; the failure-story red block is part of the brand, not a warning to hide.
Contrast floors: body text pairs must clear WCAG AA (ink-on-paper and paper-on-ink both do; never set slate on predicate).

### Type

- **Numbers, tables, code, dates, file paths:** the system monospace stack `ui-monospace, "SF Mono", "Cascadia Code", Menlo, Consolas, monospace`. Numbers are the product; they get the mono voice.
- **Prose and headings:** the system sans stack `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. Headings weight 650-700, tracking normal; no all-caps except tiny table labels.
- Headline scale on the site: 44/32/24/18px desktop, 32/26/20/16px mobile; body 17px/1.6.

### Wordmark and mark

- Wordmark: lowercase `purvia` set in the heading sans at weight 700, ink (or paper on dark), with the dot of no letter altered - restraint is the brand.
- The **mark** is the *scope bracket*: a square-bracket aperture `[ ]` in `--predicate` containing a filled square in `--measured`, representing "the scope of what one is authorized to see."
  Drawn as SVG: outer bracket stroke 2.5 at 24px grid, inner square 8x8 centered.
  On red-story assets the inner square may be `--alarm` - the mark showing a red day is on-brand.
- Never: gradients, glows, 3D, mascots, shield icons, padlock icons (padlocks imply certification we do not claim).

### Layout grammar

- Tables are a first-class visual element; style them like the README's own markdown tables, ruled with `--grid`, mono numerals, denominator caption in slate underneath. Every metric table must render its caption; a table without its denominator caption is off-brand and fails review.
- Long-form pages read as a single column, max 720px prose width; evidence blocks (tables, quotes from docs) may break to 880px.
- Blockquotes render the "confession" register: 3px `--alarm` left rule for failure content, `--predicate` for doc citations.
- Footer of every asset: `MIT core - github.com/hcho22/Purvia` plus the asset's claim-ledger row IDs in slate mono (e.g. `claims: C1 C4 C9`). This is the visible receipt system.

## 6. Asset checklists

Any new asset ships only when:

1. Every claim maps to a `launch/CLAIMS.md` row and stays within its wording cap.
2. Every number has its denominator visible in the same visual unit.
3. `launch/bin/claimlint.sh <asset>` exits clean.
4. The name-swap test passes on the headline and subhead.
5. Widget surfaces shown in screenshots carry the *buyer's* demo brand (e.g. "FitSnack Support"), never Purvia's (white-label rule).
6. If the asset mentions hybrid retrieval, it is framed as "the harness caught the dead leg", never as a retrieval-superiority claim (DECISIONS.md D3).

## 7. Boundaries and edge cases

- Do not use customer logos, testimonials, star counts, or "as seen on" - none exist.
- Do not show the parked `purvia.com` or promise `purvia.ai` as live; domain references in local assets use relative links or name the GitHub repo.
- Do not translate the repo's internal invariant names ("E4", "P1b", "US-107") into customer copy without a plain-English gloss on first use.
- The face-swap-app trademark collision (`docs/adr/0011-product-name.md:69-71`) is never mentioned in customer copy and never joked about.
