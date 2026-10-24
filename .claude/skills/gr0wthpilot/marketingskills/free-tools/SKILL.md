---
name: free-tools
description: When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as marketing," "free tool," "marketing tool," "calculator," "generator," "interactive tool," "lead gen tool," "build a tool for leads," "free resource," "ROI calculator," "grader tool," "audit tool," "should I build a free tool," or "tools for lead gen." Use this whenever someone wants to build something useful and give it away to attract leads or earn links. In Gr0wthPilot this copy generates and scores free-tool ideas for a Candidate Package's unexpected deliverable in `09-extras/`, and never deploys a tool or connects a form to a live backend. For downloadable content lead magnets (ebooks, checklists, templates), see lead-magnets.
metadata:
  version: 2.0.3
---

# Free Tool Strategy (Engineering as Marketing)

## Gr0wthPilot copy: read first

- **Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `skills/free-tools/` at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b`, MIT License, Copyright (c) 2025 Corey Haines.
  The license and the list of changes from upstream are in this folder's `LICENSE.md`.
- **Called by Gr0wthPilot only.** This copy is a phase skill of Mandu's `gr0wthpilot` skill and sits inside its folder, so no other Mandu session lists it.
- **What this copy is for:** phase 5, Package, reads this copy only when the run picks the free-tool extra.
  It generates, validates, and scores free-tool ideas for the Candidate Package's unexpected deliverable, written to `09-extras/`.
- **Never ask anything.** Where this skill says to ask the user or gather context, answer from the Candidate Package first (its `01-research/product-facts-brief.md`), then the Product's own repository (read only) and `projects/<Product>/` in Mandu. Where nothing answers a question, decide, and log the decision `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`.
- **The Candidate Package is the only context.** Never read for, create, or update `.agents/product-marketing.md` or any other context or strategy file outside the Candidate Package, and add no Learnings rows or results tables; a Product has no results before its Test Kit runs.
- **Publish nothing.** Every output is a local file in the Candidate Package. Nothing here posts, sends, schedules, submits, uploads, deploys, registers, or signs up for anything, and nothing contacts a real person; the Founder does any of that himself after Handoff.
- **No new spending.** Use a paid tool or API only when its key is already in the Product's `.env`, and never print, copy, or commit a key's value. Without one, build images from HTML and SVG and video with Remotion or ffmpeg.
- **Invent nothing factual.** Names, taglines, visuals, and copy are invented freely; every fact, number, quote, and competitor detail carries a URL fetched during this run and listed in the Candidate Package's `sources.md`, and every guess is labeled `[ASSUMPTION]` with its reasoning.
- **A built tool stays local.** If the run builds the picked tool, it is a local file in `09-extras/`; its lead capture is a form with no live backend, like the Waitlist form, and nothing is hosted or deployed.
- **Scores need sources.** Every fact behind a scorecard row, including search demand and the cases in `references/tool-benchmarks.md`, carries a URL fetched during this run and listed in `sources.md`; the upstream links are leads to fetch, not sources, and a row with no fetched source is scored as an `[ASSUMPTION]` with its reasoning.
- Related skills named below are upstream skills; only the copies in Gr0wthPilot's `marketingskills/` folder and Mandu's installed skills exist here.

You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness.

## Initial Assessment

**Check the Candidate Package first:**
Read the Candidate Package's `01-research/product-facts-brief.md` (see "Gr0wthPilot copy: read first") before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before designing a tool strategy, understand:

1. **Business Context** - What's the core product? Who is the target audience? What problems do they have?

2. **Goals** - Lead generation? SEO/traffic? Brand awareness? Product education?

3. **Resources** - Technical capacity to build? Ongoing maintenance bandwidth? Budget for promotion?

---

## Core Principles

**"Your product is my marketing opportunity."** Bezos said "your margin is my opportunity." The engineering-as-marketing version: take a capability others monetize and build a free version as an acquisition channel. Unsplash gave away the stock photos Getty sold — and Getty acquired it. See [references/tool-benchmarks.md](references/tool-benchmarks.md) for sourced cases and measurement limits.

### 1. Solve a Real Problem
- Tool must provide genuine value
- Solves a problem your audience actually has
- Useful even without your main product

### 2. Adjacent to Core Product
- Related to what you sell
- Natural path from tool to product
- Educates on problem you solve

### 3. Simple and Focused
- Does one thing well
- Low friction to use
- Immediate value

### 4. Worth the Investment
- Lead value × expected leads > build cost + maintenance

---

## Tool Types Overview

| Type | Examples | Best For |
|------|----------|----------|
| Calculators | ROI, savings, pricing estimators | Decisions involving numbers |
| Generators | Templates, policies, names | Creating something quickly |
| Analyzers | Website graders, SEO auditors | Evaluating existing work |
| Testers | Meta tag preview, speed tests | Checking if something works |
| Libraries | Icon sets, templates, snippets | Reference material |
| Interactive | Tutorials, playgrounds, quizzes | Learning/understanding |

**For detailed tool types and examples**: See [references/tool-types.md](references/tool-types.md)

**For sourced case examples (Unsplash, HubSpot Website Grader, Buffer, Shopify) and evidence requirements**: See [references/tool-benchmarks.md](references/tool-benchmarks.md)

---

## Ideation Framework

### Start with Pain Points

1. **What problems does your audience Google?** - Search query research, common questions

2. **What manual processes are tedious?** - Spreadsheet tasks, repetitive calculations

3. **What do they need before buying your product?** - Assessments, planning, comparisons

4. **What information do they wish they had?** - Data they can't easily access, benchmarks

### Validate the Idea

- **Search demand**: Is there search volume? How competitive?
- **Uniqueness**: What exists? How can you be 10x better?
- **Lead quality**: Does this audience match buyers?
- **Build feasibility**: How complex? Can you scope an MVP?

---

## Lead Capture Strategy

### Gating Options

| Approach | Pros | Cons |
|----------|------|------|
| Fully gated | Maximum capture | Lower usage |
| Partially gated | Balance of both | Common pattern |
| Ungated + optional | Maximum reach | Lower capture |
| Ungated entirely | Pure SEO/brand | No direct leads |

### Lead Capture Best Practices
- Value exchange clear: "Get your full report"
- Minimal friction: Email only
- Show preview of what they'll get
- Optional: Segment by asking one qualifying question

---

## SEO Considerations

### Keyword Strategy
**Tool landing page**: "[thing] calculator", "[thing] generator", "free [tool type]"

**Supporting content**: "How to [use case]", "What is [concept]"

### Link Building
Free tools attract links because:
- Genuinely useful (people reference them)
- Unique (can't link to just any page)
- Shareable (social amplification)

---

## Build vs. Buy

### Build Custom
When: Unique concept, core to brand, high strategic value, have dev capacity

### Use No-Code Tools
Options: Outgrow, Involve.me, Typeform, Tally, Bubble, Webflow
When: Speed to market, limited dev resources, testing concept

### Embed Existing
When: Something good exists, white-label available, not core differentiator

---

## MVP Scope

### Minimum Viable Tool
1. Core functionality only—does the one thing, works reliably
2. Essential UX—clear input, obvious output, mobile works
3. Basic lead capture—email collection, leads go somewhere useful

### What to Skip Initially
Account creation, saving results, advanced features, perfect design, every edge case

---

## Evaluation Scorecard

Rate each factor 1-5:

| Factor | Score |
|--------|-------|
| Search demand exists | ___ |
| Audience match to buyers | ___ |
| Uniqueness vs. existing | ___ |
| Natural path to product | ___ |
| Build feasibility | ___ |
| Maintenance burden (inverse) | ___ |
| Link-building potential | ___ |
| Share-worthiness | ___ |

**25+**: Strong candidate | **15-24**: Promising | **<15**: Reconsider

---

## Task-Specific Questions

1. What existing tools does your audience use for workarounds?
2. How do you currently generate leads?
3. What technical resources are available?
4. What's the timeline and budget?

---

## Common Pitfalls

- **Over-engineering** — Shipping a bloated tool before validating demand. Unsplash started as a Tumblr blog with Dropbox links, then invested in a custom site after demand emerged. Scope to one useful job and test it with your audience.
- **Poor product integration** — A tool with no natural path to your product earns traffic but not pipeline. The best cases surface the product's value (an analyzer can demonstrate the problem your paid product solves).
- **Maintenance / security debt** — Tools that scrape, call APIs, or take user input rot and become attack surfaces. Budget for upkeep before you build.
- **Vanity metrics** — Visitors and usage feel good but don't pay. Track leads, qualification rate, and trial/signup conversion — measured in your own funnel.

## Related Skills

- **lead-magnets**: For downloadable content lead magnets (ebooks, checklists, templates)
- **cro**: For optimizing the tool's landing page
- **seo-audit**: For SEO-optimizing the tool
- **link-building**: For promoting the tool to sites that link to resources like it
- **analytics**: For measuring tool usage
- **emails**: For nurturing leads from the tool
