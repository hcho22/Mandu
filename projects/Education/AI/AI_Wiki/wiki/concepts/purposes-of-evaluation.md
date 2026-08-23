---
type: concept
tags: [evals, methodology, benchmarks, leaderboards]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# The Three Purposes of Evaluation

From [[lets-talk-about-llm-evaluation]] ([[clementine-fourrier]]): people conflate three very different reasons to evaluate, and each answers a separate question with different requirements.

## The three purposes

1. **Non-regression testing** - "is my training method sound / did I break something?" You care about score *trajectories* (improving?) and *ranges* (within expected bounds?), NOT the exact number. A 7B model should land ~50-65 on MMLU; 20-30 means no learning. Borrowed straight from software non-regression testing.
2. **Leaderboards / rankings** - "which model is best?" Because scores are unstable to minute prompting changes, the trustworthy signal is *rankings* over robust groups of evaluations, not absolute scores - though even major leaderboards aren't fully stable to perturbation.
3. **Capability measurement** - "can my model do X?" We essentially can't do this yet: there's no agreed definition of a "capability," so the honest claim is "best on a task we *hope* proxies X, without guarantee."

## Synthesis

This is the most clarifying mental model in the [[evals]] area: it explains why eval arguments talk past each other (a non-regression number is not a capability claim) and why "the best model on the leaderboard" may not be best for your use case.
It maps onto hcho's world directly: purpose #1 is literally non-regression testing from QA, and it is the purpose an eval harness in CI serves ([[eval-driven-development]], the Agentic RAG gate).
Purpose #2 connects to [[benchmark-sensitivity]] (rankings over scores), and purpose #3 is the honest counter to capability hype.
