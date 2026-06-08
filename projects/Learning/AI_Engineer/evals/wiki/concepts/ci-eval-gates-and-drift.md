---
type: concept
tags: [evals, ci, drift, llmops]
date: 2026-06-08
source-count: 2
status: seeded
session: "S10 - CI/CD evals, drift monitoring, putting it all together"
---

# CI Eval Gates and Drift

Gating merges on eval pass-rate in CI and monitoring production drift, tying offline and online evals into a flywheel.

## From the sources

Clémentine Fourrier, [[lets-talk-about-llm-evaluation]], names **non-regression testing** as one of the three distinct purposes of evaluation, borrowing the concept directly from software:

- The software analogy: when you add a feature or fix a bug, non-regression tests confirm you have not broken existing high-level behavior. For models, the analog confirms that a change (different data, architecture, parameters) has not broken expected performance for a model of that class.
- What to watch: score **trajectories** (is performance improving over training?) and score **ranges** (is it within the expected band, e.g. a 7B getting 50-65 on MMLU vs 20-30 signaling no learning?), not the precise score itself.
- Requirement: use benchmarks with a high **signal-to-noise ratio**, so a large score change reflects a real shift in the model rather than measurement noise (see [[agent-eval-and-stats]]).

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], frames the same idea at the product level:

- Evals exist to **measure system changes at scale and detect regressions**; without them you visually inspect outputs on every change. Maintain a set of task-specific evals and run them on each change ("Eval-Driven Development"; see [[offline-vs-online-evals]]).
- The **data flywheel:** user feedback feeds evals, fine-tuning, and guardrails, which improve the product, which drives more usage and more data - a virtuous cycle and a moat.
- **Drift/monitoring** is the production complement to offline gates: it demonstrates value added or lost. One team ran an LLM support bot for two weeks before an A/B test showed 12x more losses, then discontinued it.

## In my own words (hcho)
