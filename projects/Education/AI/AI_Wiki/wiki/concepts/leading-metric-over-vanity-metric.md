---
type: concept
tags: [agent-operations, loops, metrics, evals]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Leading Metric Over Vanity Metric

**Pick a metric the loop can actually move.**

From [[loops-to-run-your-business]]: choose a **leading, achievable** objective metric (impressions or views per post per week) rather than a **lagging** vanity number (total follower count).
Follower growth is a downstream result and is hard to move directly.

## The test

A metric is usable by a loop if a single iteration can change it enough to read a signal.

| Lagging / vanity | Leading / usable |
|---|---|
| Total followers | Impressions or likes per post |
| Revenue | Conversion rate on one step of the funnel |
| "Users are happier" | Eval pass rate at a fixed threshold |
| Total installs | Store-listing impressions per week |

The failure mode is not that the lagging metric is wrong to care about - it is usually the thing you actually want.
It is that **it does not respond on the loop's timescale**, so the loop cannot tell a good experiment from a bad one and never converges.

## Key points

- The ads version of the same rule: give each variant **enough budget** to produce a statistically meaningful read before deciding whether it worked.
Insufficient sample is the same failure as an unresponsive metric - no signal.
- The eval version: an explicit threshold (Inbox Zero's **≥90%** categorization accuracy) is a leading metric that closes a loop cleanly, which is why [[eval-driven-development]] and [[business-loops]] fit together so naturally.
- **Split loops by metric type** rather than by feature area: a bug loop on uptime, a feature loop on retention.
Mixing them gives you one loop with two gradients pulling against each other.

## Activity versus signal (2026-10-14)

[[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]] (Marketing wiki) states the rule for outbound and content agents: messages sent is activity, qualified replies is the signal.
Its weekly cockpit example shows why the choice matters: one angle drew fewer clicks than another but twice as many demo requests from the target segment.
Clicks would have picked the wrong angle.
Its [[projects/Education/Marketing/wiki/concepts/customer-truth-file|customer truth file]] adds the counterpart caution this page already holds: weekly counts from a handful of calls need a denominator and enough cases before they move positioning.

## Synthesis

This is the same statistical instinct that runs through the [[ml-metrics]] area, arriving from the business side.
[[classification-threshold]] is about picking an operating point you can actually act on; [[precision-recall]] is about not being fooled by an aggregate that hides the slice you care about.
A vanity metric is the aggregate case - too coarse and too slow to distinguish anything.

The connection worth making explicit is that **an eval threshold is a leading metric**, which is why evals turn out to be such good loop stop conditions.
That is a genuinely useful reframe of what an eval is *for*: not only a quality gate but the only reliably fast-responding number most AI products have.
[[evals-saturate-and-get-replaced]] is the caveat - a saturated eval stops being leading and becomes decorative, because it no longer discriminates.

For hcho this is the sharpest available critique of how the current goals are phrased.
"10 buyer interviews," "~50 waitlist signups," and "income by end of 2026" are all lagging.
They are the right things to want, but none of them can steer a weekly decision, and the leading metrics underneath them - conversations started per week, landing-page conversion rate, applications sent per week - are the ones a loop or a habit can act on.
