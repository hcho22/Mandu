---
type: concept
tags: [agent-operations, loops, cost, economics]
status: seed
source-count: 2
last-updated: 2026-10-02
---

# Loop Cost Discipline

The answer to the obvious objection: if an agent loops indefinitely, what stops it from quietly running up an unbounded bill?

From [[loops-to-run-your-business]], where the host raises the skeptic's case directly - **the people who get rich from loops are the token providers**, because people just burn tokens.

## The guardrail

**Attach real economic values so the loop can stop itself.**

A click is worth 3 cents. A customer is worth $100.
Give the loop those numbers and a spend cap, and the stop condition becomes economic rather than arbitrary.
Loops may run $50 / $100 / $200 a month depending on scope.

## The scale correction

Most of the fear is a category error about what "infinite loop" means:

- These loops are **infinite over time**, not an agent trapped in a real-time infinite loop.
- **One shallow run every month for years.** Each individual run is small.
- The SEO loop specifically: likely **under $5 in tokens per run**, running about once a month.
Against the cost of an SEO agency, cost should not be the deciding worry.

## Plan-based strategy

| Plan | Posture |
|---|---|
| Max ($100-200/month) | You effectively get thousands of dollars of tokens; don't sweat cost for something like this |
| Tight $20 plan | Be much more careful; consider cheaper open-source models for this kind of task |

## The expiring-allowance view (2026-10-02)

[[token-maxing-with-agents]] pushes the Max-plan row of the table above further: on a flat plan, unspent limit expires at reset, so its speaker treats leftover allowance as something to spend on low-stakes work rather than conserve.
That is a statement about subscription workloads only ([[subscription-vs-api-tokens]]).
Loops that serve users or run as unattended production automation belong on metered billing, where this page's unit-economics stop condition applies in full.

## Synthesis

Two useful ideas sit underneath this, and the second is the durable one.

First, **cost scales with run frequency, not with loop lifetime**, which is the thing people get wrong when they hear "runs forever." A monthly loop running for three years is 36 cheap runs.

Second, and more interesting: **tying the stop condition to unit economics makes the loop's exit criterion the same thing as its business justification.** A loop that knows a customer is worth $100 does not need a separately-invented budget cap, because it can reason about whether continuing is worth it. That is a strictly better design than a spend limit bolted on top, and it is the loop version of what [[fde-in-30-days]] means by measuring impact in revenue uplift, risk mitigation, and cost savings.

The contrast with the rest of the batch is worth holding.
[[running-teams-of-ai-agents]] reports ~$20,000/month in tokens and argues you should spend first and engineer cost down later; this source argues a well-scoped loop is a rounding error.
Both are right at their own scale, and the difference is whether the loop is *running a company's engineering* or *tending one metric*.
For hcho, at a $20-200/month plan with no revenue, the second framing applies and the cost objection to starting a first loop does not really hold.
See [[reasoning-effort-discipline]] and [[model-routing]] for the per-run cost levers.
