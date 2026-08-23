---
type: concept
tags: [agentic-engineering, cost, architecture, failure-mode]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Anchor Cost Decisions in Real Pricing

**Make the agent search actual current pricing before it recommends an architecture.**
Its default cost estimates can be wrong by an order of magnitude and quietly drive the decision.

This is the single failure that survived an entire full-stack build in [[agentic-full-stack-build]].

## What happened

The plan recommended hosted Supabase Pro at **$25/month** and estimated a self-hosted VPS at **$30-60/month** - which, on those numbers, makes the managed service the obvious call.

Kun pushed back on both.
Three users (him, his wife, his son) don't justify paying for SaaS, and the VPS estimate contradicted his direct experience with Hetzner.
He queued feedback that a low-cost VPS should land around **$5/month**.

The agent then **searched real cloud pricing, re-anchored, and came back recommending a budget VPS at ~$5.50/month**, plus roughly 20% more for backups.
The provisioned Hetzner server came in well below the original estimate.

## Why this is the dangerous class of error

- **The wrong number never surfaces as a wrong number.** It surfaces as an architecture recommendation, which is much harder to audit.
- The reasoning on top of it was sound. Kun explicitly liked the agent's framing - "buy operational simplicity before buying infrastructure" - while overriding its conclusion.
**Good reasoning over bad data produces a confident wrong answer**, and confidence is exactly what makes it slip through.
- Cost is a domain where the model's training data goes stale fast and where it has no way to notice.
- His closing assessment of the whole session: the single place the model wasn't good enough was this decision, **and that was because it reasoned from wrong pricing data, not because it reasoned badly.**

## Synthesis

The transferable rule is broader than pricing: **any recommendation resting on a number the model recalled rather than looked up should be treated as unverified.**
Pricing is the clearest case because it changes monthly and is trivially checkable, but the same shape applies to rate limits, model context windows, library API surfaces, and free-tier boundaries.

The practical instruction is a one-liner in the prompt - *search current pricing before recommending* - and it is cheap insurance against the most expensive category of agent error, the one that doesn't look like an error.

Note how this interacts with [[review-plans-as-artifacts]]: Kun caught it because the decision was surfaced as an explicit, annotatable line item in an artifact rather than buried in paragraph 12 of a 351-line report.
The format is what made the number visible enough to challenge.

It also pairs with [[agent-over-engineering]] as the two places human judgment still earned its keep across an entire session where the human never read source code.
Both are **scope and cost** judgments, not correctness judgments - which is a fair summary of where the human's remaining edge sits.
