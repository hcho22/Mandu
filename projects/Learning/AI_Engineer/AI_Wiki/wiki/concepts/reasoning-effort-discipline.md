---
type: concept
tags: [models, cost-control, claude, reasoning-effort]
status: developing
source-count: 2
last-updated: 2026-07-28
---

# Reasoning-Effort Discipline

From [[working-with-fable-5]]: the single biggest cost lever is keeping reasoning effort in the low-to-high range and refusing the settings above it (x-high, max, "Ultra Code").
Theo ([[theo-t3]]) estimates this one change alone halves many people's bills.

## Key points

- **High is the best value** and the default for a reason; low/medium/high can still run for a long time and do things a cheaper model cannot.
- **The top settings over-reason:** x-high and max second-guess themselves, loop, and over-engineer - far more changes than a simple request warrants, at drastically higher cost. They are visually tempting ("a slot-machine gradient"); resist.
- **Effort is per-step, not more steps:** higher effort makes the model overthink each individual tool call; it does not grant a longer horizon or the ability to solve harder problems. A 500-step task does not get more steps from max.
- **A tell:** Ultra Code reportedly runs many "high" passes under the hood - read as the vendor itself agreeing high is the sweet spot. Nearly everyone blowing through usage was on x-high/max/Ultra Code.

## The parallel-work analogue: budget compute per task

[[designing-loops-and-workflows]] adds the same lever pointed at fan-out rather than at a single session.
**Give each parallel workflow task a maximum compute budget.**
Without one, the model spreads verification effort thin across simultaneous outputs, so generating five things at once yields five worse-verified things rather than five equivalent ones.

This is a different failure mode than the one this page opened with and worth keeping distinct.
Theo's case is *too much* effort on a single step producing over-engineering.
Tharic's case is *too little* effort per output when many run at once, silently, because nothing signals that verification was skimped.
Together they say effort is a budget you allocate explicitly in both directions, which is also why [[sub-agents]] fan-out needs a cap rather than being free throughput.

## Synthesis

This is one of the two cost levers in the source, alongside [[model-routing]]; together they are why a month-scale agent run cost ~$150 rather than thousands.
It is a useful counter to the intuition that "more thinking = better output": beyond a point, more effort buys over-engineering, not correctness - which is itself a validation observation ([[cost-of-being-wrong]] cuts both ways: over-changing simple code has a cost too).
Note the specific settings are Theo's read of the current Claude 5 family, not a vendor benchmark; treat as a working default, not a law.
