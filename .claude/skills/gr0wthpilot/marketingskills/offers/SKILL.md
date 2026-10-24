---
name: offers
description: "When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, naming, and payment structure. Also use when the user mentions 'offer,' 'offer design,' 'build an offer,' 'grand slam offer,' 'irresistible offer,' 'value stack,' 'bonus stack,' 'guarantee,' 'risk reversal,' 'money-back guarantee,' 'scarcity,' 'urgency,' 'high-ticket offer,' 'productize a service,' 'naming an offer,' 'payment plan,' 'down-sell,' 'upsell offer,' or 'why isn't my offer converting.' Best for services, agencies, courses, coaching, info products, high-ticket B2B, and direct-response. If you run pure self-serve SaaS, read pricing first — tiers and packaging do more work there. In Gr0wthPilot this copy shapes tournament pitch material and the offer framing in the Candidate Package's positioning; every offer term is the run's own proposal and never changes the Product. For price level itself (tiers, freemium, value metric), see pricing. For the page that presents the offer, see copywriting. For the launch moment, see launch. For sales collateral, see sales-enablement."
metadata:
  version: 1.0.2
---

# Offer Design

## Gr0wthPilot copy: read first

- **Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `skills/offers/` at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b`, MIT License, Copyright (c) 2025 Corey Haines.
  The license and the list of changes from upstream are in this folder's `LICENSE.md`.
- **Called by Gr0wthPilot only.** This copy is a phase skill of Mandu's `gr0wthpilot` skill and sits inside its folder, so no other Mandu session lists it.
- **What this copy is for:** phase 1, "Market the brand", reads it for the value equation, the six-part offer anatomy, and honest guarantee and scarcity choices.
  The output is tournament pitch material in `02-brand/tournament/` and the offer framing in `02-brand/positioning.md`.
- **Never ask anything.** Where this skill says to ask the user or gather context, answer from the Candidate Package first (its `01-research/product-facts-brief.md`), then the Product's own repository (read only) and `projects/<Product>/` in Mandu. Where nothing answers a question, decide, and log the decision `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`.
- **The Candidate Package is the only context.** Never read for, create, or update `.agents/product-marketing.md` or any other context or strategy file outside the Candidate Package, and add no Learnings rows or results tables; a Product has no results before its Test Kit runs.
- **Publish nothing.** Every output is a local file in the Candidate Package. Nothing here posts, sends, schedules, submits, uploads, deploys, registers, or signs up for anything, and nothing contacts a real person; the Founder does any of that himself after Handoff.
- **No new spending.** Use a paid tool or API only when its key is already in the Product's `.env`, and never print, copy, or commit a key's value. Without one, build images from HTML and SVG and video with Remotion or ffmpeg.
- **Invent nothing factual.** Names, taglines, visuals, and copy are invented freely; every fact, number, quote, and competitor detail carries a URL fetched during this run and listed in the Candidate Package's `sources.md`, and every guess is labeled `[ASSUMPTION]` with its reasoning.
- **Every offer term is the run's own proposal.** Price, payment structure, bonuses, guarantee, and scarcity are labeled as the run's pick and never change the Product.
- **No invented proof.** Never invent a customer, case study, testimonial, or result; where this skill calls for proof the Product does not have, use sourced product facts or name the gap.
- **Worked examples are leads, not sources.** The companies, prices, and lifts in `references/` (the four SaaS offers in `saas-offers.md`, for example) and the 10-40% lift in "The Diagnostic Loop" are upstream's.
  Cite one only with a source fetched during this run, and label a projected lift `[ASSUMPTION]`.
- Related skills named below are upstream skills; only the copies in Gr0wthPilot's `marketingskills/` folder and Mandu's installed skills exist here.

You are an expert in offer construction. Your goal is to help the user build offers that move — not by writing better copy on a worse offer, but by improving the offer itself.

## Before Starting

**Read the Candidate Package first:**
Read its `01-research/product-facts-brief.md` (see "Gr0wthPilot copy: read first") before answering this skill's questions. Use that context, and answer what it does not cover as "Never ask anything" says.

---

## Core Philosophy

**The offer is the thing, not the page.** Better copy on a weak offer compounds slowly. A stronger offer with average copy converts immediately. Most "we need better copy" requests are actually "we need a better offer" requests in disguise.

This skill exists because the rest of the repo handles the *expression* of an offer — `copywriting` writes the sales page, `cro` optimizes the conversion path, `pricing` sets the tier structure, `launch` orchestrates the moment, `paywalls` shapes the upgrade prompt. None of them ask the deeper question: **is the offer underneath any of that actually good?**

### When this skill matters

You sell:
- **Services** — consulting, freelance, agency retainers, productized services
- **Courses** — async, cohort-based, live
- **Coaching** — 1:1, group, mastermind
- **Info products** — guides, swipe files, templates, communities
- **High-ticket B2B** — $5K+ ACV with a sales conversation
- **Direct-response** — e-com promo offers, infomercial-style, paid-traffic-to-VSL

### When `pricing` does more of the work

You sell:
- **Self-serve SaaS** with tiered subscriptions — the levers are mostly tier structure, value metric, and packaging; offer construction (bonuses, guarantees) is secondary
- **Marketplaces** — the offer is structural, not constructed

Skim this skill in those cases for the value equation framing, then go to `pricing`.

---

## The Value Equation

The single most useful frame for offer design. Originally from Alex Hormozi's *$100M Offers* — internalized broadly across direct-response and creator-economy training since.

```
              Dream Outcome  ×  Perceived Likelihood of Achievement
  Value  =  ─────────────────────────────────────────────────────────
              Time Delay     ×   Effort & Sacrifice
```

You move the four levers like this:

| Lever | What it means | How to increase value |
|-------|---------------|-----------------------|
| **Dream outcome** ↑ | What the customer actually wants | Connect to the bigger goal behind the surface ask. Specify and name it. |
| **Perceived likelihood** ↑ | Do they believe they'll get it | Proof (case studies, named customers, data), guarantees, methodology specificity |
| **Time delay** ↓ | How long until result | Faster onboarding, faster first win, faster end-to-end timeline |
| **Effort & sacrifice** ↓ | What it costs them in time/work/risk besides money | Done-for-you, simpler process, fewer decisions, lower learning curve |

**Implication for offer construction**: most "lower the price" requests are actually "raise the numerator or lower the denominator" requests. Price is the comparison, not the value.

**For the full framework, examples, and how to diagnose which lever is broken:** see [references/value-equation.md](references/value-equation.md)

---

## The Anatomy of a Complete Offer

A complete offer has six components. Skip any one and conversion suffers.

| # | Component | Question it answers |
|---|-----------|---------------------|
| 1 | **Core deliverable** | What do they get? |
| 2 | **Bonus stack** | What else do they get that makes the core feel undervalued? |
| 3 | **Guarantee** | What happens if it doesn't work? |
| 4 | **Scarcity / urgency** | Why now, not later? |
| 5 | **Name** | What is this thing called? |
| 6 | **Price + payment structure** | What do they pay and how? |

Most weak offers fail on bonuses (none), guarantees (none or wrong type), or scarcity (none, or fake). Most aggressive-to-the-point-of-cringe offers fail on guarantee (over-promising) or scarcity (fake countdown timers).

**For the full anatomy with worked examples:** see [references/offer-anatomy.md](references/offer-anatomy.md)

---

## Reference Library

| Reference | When to read |
|-----------|--------------|
| [value-equation.md](references/value-equation.md) | Diagnosing which lever is broken on a stuck offer |
| [offer-anatomy.md](references/offer-anatomy.md) | Building a complete offer from scratch |
| [guarantee-design.md](references/guarantee-design.md) | Picking the right type of guarantee for your business model |
| [bonus-stacking.md](references/bonus-stacking.md) | Adding bonuses that raise perceived value without devaluing the core |
| [scarcity-urgency.md](references/scarcity-urgency.md) | Creating *real* scarcity (and avoiding the fake patterns that destroy trust) |
| [offer-formats.md](references/offer-formats.md) | Format playbooks by business type — service, course, coaching, info product, SaaS lead magnet, agency retainer, high-ticket B2B |
| [saas-offers.md](references/saas-offers.md) | SaaS specifically — the discount trap (why discounting to acquire backfires) + four SaaS worked offers (AudienceTap, SaberSim, Teachable, Kit) |
| [examples.md](references/examples.md) | Anonymized worked examples — before/after for each business type |

---

## The Diagnostic Loop

When the user says "my offer isn't converting" or "I want to improve my offer":

1. **Identify the business type** — service, course, coaching, info product, SaaS, agency, B2B. The right playbook is type-specific.
2. **State the current offer in plain language** — name, price, what they get, guarantee, deadline. Write it down even if it lives in scattered places now.
3. **Run the value equation** — score each of the four levers 1–10. The lowest is the binding constraint.
4. **Audit the anatomy** — which of the six components is missing or weak?
5. **Pick one lever to fix this iteration** — don't rebuild everything. The biggest lever is usually the one currently scoring lowest.
6. **Draft the changed component** — new bonus, new guarantee, new scarcity, new name, new payment plan
7. **Project the lift, honestly** — plan on 10–40% relative lift from one component change. Multiply the lifts, don't add them: +20% then +30% = `1.20 × 1.30 = 1.56` (2% → 3.12%, +1.12 percentage points). Two iterations rarely reach 2–3x; anyone promising 5x is selling something. Confirm the combined offer with a test (see ab-testing).

---

## When NOT to Use Offer-Design Tactics

Some offer patterns work but cost more than they're worth:

- **Manipulative scarcity** — fake countdown timers, "only 3 spots left" lies. Short-term lift, long-term trust collapse. Don't.
- **Over-promising guarantees** — "double your revenue or refund + $1,000." Refund risk eats margin; the few cases that fail nuke your reputation publicly.
- **Bonus inflation** — stacking $50K of "bonuses" on a $497 product so it "feels like a steal." Sophisticated buyers see this. Treat bonuses as additive, not exaggerated.
- **Course-bro aesthetic on a serious product** — Gold logos, "secret method," fake urgency. Pattern-matches to scam. Wrong room.
- **Discounting to acquire** — discount-*askers* churn at ~2× the rate of full-price customers, and a coupon anchors the product as cheap. Discount only for upgrades/cross-sells (rewarding existing customers) or real seasonal windows — never to win a new one. Raise value with an offer instead. See [saas-offers.md](references/saas-offers.md).

The repo voice: opinionated, but honest. Building offers well doesn't mean building offers loud.

---

## Banned Vocabulary

When drafting offer language (sales pages, emails, headlines), avoid:

- **"Game-changing," "revolutionary," "disruptive," "next-level," "10x"** — pattern-matches to AI slop / course-bro
- **"Secret," "hidden," "what they don't want you to know"** — clickbait
- **"Limited time" with no actual time limit** — lying
- **"Worth $X" or "$Y value" with no comparable** — inflation
- **"100% guaranteed" without specifying conditions** — legally and brand-wise risky

Use specific numbers, named customers, concrete outcomes, real timelines. Specificity beats superlatives.

---

## Related Skills

- **pricing** — for price levels, tier structure, value metric, packaging, freemium
- **copywriting** — for the page that presents the offer
- **cro** — for optimizing the conversion path the offer travels through
- **launch** — for the moment you ship the offer
- **paywalls** — for in-app upgrade-prompt versions of an offer
- **sales-enablement** — for the deck and one-pager that carry the offer into a sales conversation
- **emails** — for the email sequence that warms up the offer
- **marketing-psychology** — for the cognitive biases that make offers land or bounce
