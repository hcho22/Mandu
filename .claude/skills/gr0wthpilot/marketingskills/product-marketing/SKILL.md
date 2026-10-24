---
name: product-marketing
description: "When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'ICP,' 'ideal customer profile,' 'brand voice,' 'tone of voice,' 'brand guidelines,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills. In Gr0wthPilot this copy gives only its section outline, as the outline of the Candidate Package's `01-research/product-facts-brief.md`, which the other copies read for product, audience, and positioning context."
metadata:
  version: 2.2.0
---

# Product Marketing Context

## Gr0wthPilot copy: read first

- **Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `skills/product-marketing/` at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b`, MIT License, Copyright (c) 2025 Corey Haines.
  The license and the list of changes from upstream are in this folder's `LICENSE.md`.
- **Called by Gr0wthPilot only.** This copy is a phase skill of Mandu's `gr0wthpilot` skill and sits inside its folder, so no other Mandu session lists it.
- **What this copy is for:** Gr0wthPilot reads it before phase 1, when the run reads the product, for its section outline only, never its own context file.
  "Sections to Capture" and the Step 3 structure are the outline of the Candidate Package's `01-research/product-facts-brief.md`, which the run drafts from the Product's own repository (read only) and `projects/<Product>/` in Mandu.
- **Never ask anything.** Where this skill says to ask the user or gather context, answer from the Candidate Package first (its `01-research/product-facts-brief.md`), then the Product's own repository (read only) and `projects/<Product>/` in Mandu. Where nothing answers a question, decide, and log the decision `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`.
- **The Candidate Package is the only context.** Never read for, create, or update `.agents/product-marketing.md` or any other context or strategy file outside the Candidate Package, and add no Learnings rows or results tables; a Product has no results before its Test Kit runs.
- **Publish nothing.** Every output is a local file in the Candidate Package. Nothing here posts, sends, schedules, submits, uploads, deploys, registers, or signs up for anything, and nothing contacts a real person; the Founder does any of that himself after Handoff.
- **No new spending.** Use a paid tool or API only when its key is already in the Product's `.env`, and never print, copy, or commit a key's value. Without one, build images from HTML and SVG and video with Remotion or ffmpeg.
- **Invent nothing factual.** Names, taglines, visuals, and copy are invented freely; every fact, number, quote, and competitor detail carries a URL fetched during this run and listed in the Candidate Package's `sources.md`, and every guess is labeled `[ASSUMPTION]` with its reasoning.
- **Auto-draft only.** The start-from-scratch path, the questions to the user after a draft, and the Learnings section are cut, because each one asks the user or records results; the brief is drafted from sources alone.
- **Open sections stay open.** Proof Points, verbatim Customer Language, and Current metrics hold only what a source shows; where none does, the section says so instead of carrying an estimate.
- Related skills named below are upstream skills; only the copies in Gr0wthPilot's `marketingskills/` folder and Mandu's installed skills exist here.

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is the Candidate Package's `01-research/product-facts-brief.md`.

## Workflow

### Step 1: Check for Existing Context

First, check if the Candidate Package's `01-research/product-facts-brief.md` already exists.

**If it exists:**
- Read it and summarize what's captured — note its current **Document version** and the last few **Changelog** entries so the user sees where the doc stands and what's changed recently
- Decide which sections need updating
- Only gather info for those sections
- On any substantive save, bump the version and add a changelog entry (see Step 4). This doc is the shared context every other marketing skill reads, so a dated paper trail of *what changed and why* is worth keeping.

**If it doesn't exist, auto-draft it:**

1. **Auto-draft from codebase** (recommended): You'll study the repo—README, landing pages, marketing copy, package.json, etc.—and draft a V1 of the context document. This is faster than starting from scratch.

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- 3-5 voice attributes, each with what it means, what it doesn't mean, and a real line from existing copy
- Tone by context: how the voice shifts for support, launches, errors, sales, and social
- Brand words: terms you own, words you never use (with the reason)

Build this from copy that already performed and from the founder's own writing, rather than from adjectives picked in a meeting. See [references/brand-voice.md](references/brand-voice.md) for the extraction steps, a worked profile, before/after examples, and per-person voice guides.

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

### 13. Paid Ads (optional, only if they run ads)
The **ads** skill reads this so the user doesn't re-explain the account every session.
- Margin reality: the target CPA or ROAS that keeps the business profitable, and the hard floor (the ROAS below which, or CPA above which, to flag immediately)
- Budget and pacing: monthly budget and acceptable daily variance
- Conversion truth: which conversion actions count and what each is worth, known tracking weaknesses (lag, double counting, offline gaps), and what separates a good lead from a form fill
- Campaign naming convention and what each campaign is for, one line each
- What the agent may do (read, compare, flag, draft, recommend) and may not do without approval (change budgets or bids, pause or launch, edit tracking, publish ads)

---

## Step 3: Create the Document

After gathering information, create the Candidate Package's `01-research/product-facts-brief.md` with this structure:

```markdown
# Product Marketing Context

**Document version:** v1
**Last updated:** [date]

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
| Attribute | Means | Doesn't mean | Example line |
|-----------|-------|--------------|--------------|
| | | | |

**Tone by context:**
- Support:
- Launch:
- Errors:
- Sales:
- Social:
**Terms we own:**
**Never use (and why):**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Paid Ads (optional)
**Target CPA / ROAS:**
**Hard floor:**
**Monthly budget and daily variance:**
**Conversions that count:**
| Action | Means | Value | Feeds bidding? |
|--------|-------|-------|----------------|
| | | | |
**Known tracking weaknesses:**
**Good lead vs. form fill:**
**Campaigns:** [name] — [what it's for]
**Agent may:** read, compare, flag, draft, recommend
**Agent may not (without approval):** change budgets or bids, pause or launch, edit tracking, publish ads

## Changelog
*Newest first. One line per revision: what changed and why.*
- v1 ([date]) — Initial context.
```

---

## Step 4: Confirm, Version, and Save

- Show the completed document
- **Set the version and changelog** — this is the paper trail for a doc every other skill reads:
  - **New document:** set `Document version: v1` and a single Changelog entry — `- v1 ([today]) — Initial context.`
  - **Updating an existing document:** increment the version (v2 → v3 …), update `Last updated` to today, and **prepend a new Changelog entry** at the top of the list (newest first) summarizing *what changed and why* in one line. Never rewrite or reorder past entries.
  - A good entry names the sections touched and the reason, not "updated the doc." Examples:
    - `- v3 (2026-07-16) — Repositioned from "email tool" to "deliverability platform"; added RevOps to the ICP.`
    - `- v2 (2026-06-02) — Rewrote value prop and objections after 5 customer interviews; added competitor Acme.`
  - Use today's date in ISO form (YYYY-MM-DD) for the entry and `Last updated`.
  - **Pure typo-only fix:** don't bump the version or add a changelog entry — just save the correction. Every other change bumps the version and gets an entry. When the change is a real repositioning, say so plainly — downstream skills will now generate against the new context.
- Save to the Candidate Package's `01-research/product-facts-brief.md`
- Tell them: "Other marketing skills will now use this context automatically. The Changelog at the bottom tracks every revision — check it to see how your positioning has evolved. Run `/product-marketing` anytime to update it."

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C, Paid Ads if they don't run ads)
