---
type: concept
tags: [agent-operations, cost, observability, prompting, analytics]
status: seed
source-count: 1
last-updated: 2026-08-21
---

# Make the Agent Report Its Cost

**Ask for the dollar cost on every single generation, as part of the prompt, every time.**

From [[one-person-marketing-team]], where it is the least glamorous instruction in the source and the one with the widest applicability.

## The four-part prompt pattern

Every asset-generation prompt in that source states four things, and lets the project supply the rest:

1. The **motivation** - why this exists.
2. The **end goal** - what the deliverable is.
3. **Where to save the output** - the exact folder.
4. **Report the cost at the end.**

Points 3 and 4 are the ones people skip, and they are the ones that make the run auditable afterwards.
Without a destination the output scatters; without a cost line the spend is invisible until the invoice arrives.

## What it buys

The source's payoff is concrete.
Because every run reported its cost, an 8-minute follow-up prompt could assemble a **creative tracker** workbook with a real cost summary: ID, date, generation type, campaign, channel, primary angle, deliverables, tool and model, credits, dollar cost, status.
That table could not have been reconstructed after the fact.

The resulting numbers are the most transferable content in the whole source:

| Deliverable | Produced | Cost |
|---|---|---|
| Static ad creatives | 18 images | $3.43 |
| Instagram carousels | 5 carousels | $9.56 |
| Sizzle reel | 2 formats, music and edits | $17.55 |
| UGC video ads | 4 characters + boards + QA + video | **Not stated** |

The shape of that table is the finding, more than the figures: **static generation is nearly free at this volume and video is two orders of magnitude more expensive per deliverable.**
Any creative loop's economics are dominated by how much video it makes, and nothing else.

Note also what the missing row demonstrates.
The most expensive item is the one the source failed to quote, which is precisely the failure this practice exists to prevent, occurring inside the source that recommends it.

## Synthesis

This is [[agent-observability]] at the smallest possible scale, done with a sentence instead of infrastructure.
The wiki's cost material is otherwise about *deciding* - [[anchor-cost-in-real-pricing]] says make the agent look up real prices before it recommends an architecture, [[loop-cost-discipline]] says tie a loop's stop condition to unit economics, [[reasoning-effort-discipline]] and [[model-routing]] are levers for lowering the bill.
All of them assume you know what things cost.
This page is the prerequisite that supplies the number, and it is nearly free to adopt.

The relationship to [[anchor-cost-in-real-pricing]] is worth stating because they are easily confused.
That page is about **prices looked up before a decision**, and it exists because a stale recalled number silently drives architecture.
This one is about **spend recorded after an action**, and it exists because unrecorded spend cannot be analyzed at all.
Together they close both ends: verify the price going in, log the cost coming out.

The larger point is that per-run cost is the cheapest column in a [[unified-data-warehouse-for-agents]] and the one nobody instruments, because it feels like accounting rather than engineering.
It is the join key between what an agent did and what it was worth.
[[leading-metric-over-vanity-metric]] wants a number a single iteration can move; cost-per-deliverable is that number for any generative loop, available on day one, before there is any performance data at all.

For hcho the immediate application is not marketing.
It is that any long-running agent loop he builds should emit its own cost line into the worklog by default, so that [[loop-cost-discipline]]'s stop conditions can be set from measurement rather than estimate.
