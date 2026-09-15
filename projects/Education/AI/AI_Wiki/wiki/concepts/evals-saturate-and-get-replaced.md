---
type: concept
tags: [evals, agentic-engineering, anthropic, contradiction]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Evals Saturate and Get Replaced

[[boris-cherny]] in [[building-at-the-frontier]] makes the case for evals as the durable asset and then immediately walks it back himself.

**The claim:** at the frontier, code and system prompts get deleted every model release ([[ablation-driven-development]]).
Evals are the closest thing to a durable asset, because you keep appending to them rather than throwing them away.

**The walk-back:** evals **outlive the harness, but not by much**.
An eval might survive one, two, or three model generations.
On the current exponential they saturate quickly, get thrown away, and a new set has to be built.

## Key points

- **Treat saturation as the expected end state, not a failure.**
- **Budget for replacing evals rather than maintaining them indefinitely.** This is a different posture from a regression suite, which you maintain forever.
- Sourcing a new eval set uses the same empirical loop as everything else: use the product, use the model, find where it actually struggles, and build the eval from those observed failures.
- The half-life is set by model releases, not by your product's stability.

## The contradiction to hold

This tensions with the framing across the [[evals]] area, which treats the eval system as the compounding asset that makes iteration possible ([[eval-driven-development]], [[evaluation-pipeline]], [[three-level-eval-framework]]).
It is not a refutation, and the two are reconcilable, but the reconciliation has to be stated rather than assumed:

| What saturates | What doesn't |
|---|---|
| The specific test cases and thresholds | The *method* for sourcing them from observed failures |
| The absolute scores | The failure taxonomy and the slices you learned to care about |
| Benchmarks near the ceiling ([[benchmark-saturation]]) | The instrumentation, trace review habit, and CI plumbing |

Note that this is the *same phenomenon* [[benchmark-saturation]] already documents for public benchmarks, now claimed for private product evals too.
The wiki had treated your-own-evals as immune to the decay that eats leaderboards.
This source says they are not, only slower.

## Synthesis

The honest reading is that **the eval skill is durable and the eval artifact is not**, and hcho's positioning should be stated at the level that survives.

That matters concretely, because the pitch "I bring validation rigor" is safe while "I built an eval suite" ages like a benchmark.
The transferable claim is the loop - observe failures, build the check, gate on it, replace it when it stops discriminating - and the ability to notice *when* a suite has gone blind, which is exactly the judgment [[benchmark-saturation]] and [[data-contamination]] train.

It also argues against gold-plating: an eval suite built to last three years is built for a horizon that does not exist.
Build it to be cheap to rebuild.
For the Purvia eval harness (`projects/Purvia/wiki/`), that means investing in the *generator* - the path from observed failure to new test case - over the test cases themselves.
