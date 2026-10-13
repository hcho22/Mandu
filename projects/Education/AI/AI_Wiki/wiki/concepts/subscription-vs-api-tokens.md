---
type: concept
tags: [cost, economics, subscriptions, api, agent-operations, terms-of-service]
status: seed
source-count: 1
last-updated: 2026-10-02
---

# Subscription vs API Tokens

Flat-rate agent subscriptions and metered API billing are different economic regimes, and the right cost behavior flips between them.
On the API every token is a marginal cost to minimize.
On a flat-rate subscription with a resetting limit, unused tokens are the waste, so the binding constraint becomes the rate window and the human's attention rather than the bill.
Introduced by [[token-maxing-with-agents]].

## The claimed gap

[[theo-t3]]'s estimates, unverified and dated only by the undated video (ingested 2026-10-02):

| Plan | Token value he claims |
|---|---|
| API, $200 | $200 |
| Claude subscription, $200/month | about $8,000, of which about $4,000 is Fable (separate limit) |
| Claude subscription, $100/month | about half the total but about a quarter of the hourly limit; he does not recommend it |
| Codex subscription, $200/month | about $12,000, more with frequent limit resets |

He says only the Claude and Codex subscriptions carry discounts of this size; resold access through other tools is subsidized far less.
Vendor-specific figures live on [[anthropic]] and [[codex]].

## The line he draws

- **Subscriptions are for your own work:** prompts on your codebase, agents triaging your issues, personal operations.
- **The API is for anything user-facing or public.** Serving end users from a subscription is, in his words, when you deserve a ban.
- **Subscription access is tool-bound.** He says Claude subscriptions should be used only inside [[claude-code]].
- **Multiplying accounts is a terms-of-service risk.** His multi-account proxy setup is recorded on the source page, together with his own warning that it may violate provider terms and get accounts banned. This wiki does not adopt it as a practice.

## Spending an expiring allowance

The behavioral consequence is "use it or lose it": a subscription is an allowance that disappears at reset, not savings.
His prescription is to spend leftover limit on useful low-stakes work - triaging PRs, sweeping old repositories, the "silly" offloads in [[delegate-the-problem-not-the-solution]] - rather than letting it expire.
The scarce resources that remain are the rate window (the five-hour limit he says to slow down for if you hit it across accounts) and the operator's attention ([[agent-threads-as-inbox]]).

## Synthesis

This page resolves an apparent contradiction rather than adding one.
[[reasoning-effort-discipline]] and [[loop-cost-discipline]] tell you to minimize tokens; this source tells you to burn them.
Both are right inside their billing model: per-token pricing rewards thrift, and an expiring flat allowance rewards utilization.
What does not flip is the cost of bad output.
Over-reasoned, over-engineered changes still cost review attention, which is the resource token-maxing makes scarce, so effort discipline survives the move to subscriptions for quality reasons even when the dollars disappear.

The durable rule is to **know which regime each workload is in before deciding how to economize it**.
Interactive development on your own code sits in the subscription regime; production traffic, scheduled evals in CI, and anything that serves users sits in the metered regime and keeps the full discipline of [[make-the-agent-report-its-cost]] and [[anchor-cost-in-real-pricing]].

The subsidy is also the fragile part.
The speaker's own closing advice is to burn tokens "before the subsidization ends, if it ever does," and he reports new $200 Codex sign-ups already paused.
A workflow or a business plan that only works at subsidized prices is exposed to a pricing change outside your control, which is the vendor-dependence point [[independent-agent-lab-vs-frontier-lab]] makes about stacks.

For hcho, pre-revenue and on a runway, the speaker's own caveat is the operative one: do not stack subscriptions until there is income.
A single subscription for interactive work, metered API calls for Rep Today's Coach and Purvia's evals, and no account multiplication is the conservative position.

## Source

- [[token-maxing-with-agents]] - Theo's undated video; all value figures are his estimates, partially checked against published API pricing on the source page.
