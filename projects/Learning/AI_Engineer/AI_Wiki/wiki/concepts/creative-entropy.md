---
type: concept
tags: [agent-operations, agents, failure-mode, creativity, loops]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Solving for Entropy

**An agent left alone gets stuck thinking in the same way.**
Creative ideation stagnates over time, and nothing in the loop notices.

From [[building-marketing-agents]], and the most generalizable finding in that source.
Cody stresses that **this problem is rarely discussed publicly** - most people describe these systems as "set it up once and it's just good," which he directly disputes.

## The failure mode

A feedback loop that generates variants, measures them, and generates more like the winners is a **hill climber**.
It converges, and once converged it keeps producing minor variations of a local optimum while its own metrics look stable.
There is no signal inside the loop that says "you stopped exploring," because by the loop's own measure nothing is wrong.

## The fix: inject new DNA from outside

Two mechanisms he uses:

1. **Competitors' public ad libraries** (the Facebook Ads Library) - pull real ads from outside your own system and use them as fresh source material for research.
2. **Niche YouTube channels and podcast transcripts** - extract insights from category-specific content to seed new angles.

He also mentions a TikTok/Reels trend-scraping API for surfacing the most viral posts in a category, to inform creative trend direction.

The common structure: **the diversity has to come from outside the loop's own output**, because anything generated inside it is already downstream of the current optimum.

## Synthesis

This deserves to be lifted out of marketing, because it is a general property of any self-reinforcing agent loop and the wiki has been accumulating loop pages without it.

[[business-loops]], [[self-improving-agent-loop]], and [[self-maintaining-codebase]] all describe loops that improve against a metric.
Every one of them is exposed to this.
A rubric-graded self-improvement loop will converge on the rubric; an SEO loop will converge on the tactics that worked last quarter; a dead-code routine will keep finding the same class of dead code.
None of them will report a problem.

It is also the loop-shaped cousin of [[self-referential-bias]].
That page says a model grades its own output too leniently, and the fix is a *different* model or context doing the verifying.
This says a loop feeds on its own output and narrows, and the fix is *external* material entering the generation step.
Both are failures of a closed system evaluating itself, at different points in the cycle, with the same shape of fix: **break the closure.**

The practical instruction is to build the injection in deliberately rather than hoping for it - a scheduled step that pulls competitor material, outside sources, or human input into the loop, on the assumption that convergence is the default and not an edge case.

Worth flagging against [[evals-saturate-and-get-replaced]] too: a saturating eval and a converging loop are the same phenomenon seen from the measurement side and the generation side.
