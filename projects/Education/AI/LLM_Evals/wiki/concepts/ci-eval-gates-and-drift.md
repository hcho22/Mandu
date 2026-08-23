---
type: concept
tags: [evals, ci, drift, llmops]
date: 2026-06-08
source-count: 5
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

Chip Huyen, [[evaluate-ai-systems]], connects CI-style gates to model selection and production iteration:

- Evaluation criteria should be defined before development, including **hard requirements** and **ideal targets** for cost, scale, latency, quality, and task-specific capabilities. Those targets become the gates that decide whether a model or system variant is useful.
- Model selection is iterative: filter impossible models by hard attributes, use public data to narrow the pool, run private evals on the survivors, and then monitor production to detect failure and collect feedback.
- Production monitoring should test whether evaluation scores map to business outcomes. For example, a factual-consistency threshold should correspond to what share of support requests can safely be automated.
- Evaluation should include human review when necessary, even in production. A sampled daily review process can serve as a North Star when automated metrics are weak.
- Iteration is expected, but evaluation changes must be tracked. Log the eval data, rubric, judge prompt, sampling configuration, and model/system version so score changes are attributable.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], explains why CI gates need fresh and protected eval data:

- A stale public benchmark is a weak regression gate if the model or provider may have seen the test set. The gate can pass memorization rather than the behavior the product needs.
- Gate quality improves when eval sets are private, versioned, post-cutoff where relevant, and rotated over time. LiveCodeBench/LiveBench-style freshness and GSM1K/FrontierMath-style private holdouts are the pattern.
- Saturated benchmarks should not be treated as hard gates for frontier work. When top models cluster near the ceiling, small score changes may be contamination, noise, or formatting sensitivity rather than capability movement.
- Regression dashboards should distinguish public benchmark orientation from private product gates, and should track benchmark provenance, release dates, model cutoffs, and eval-set versions alongside scores.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], formalize what makes a benchmark a good *training-time* regression signal (the model-builder's CI):

- **Ablations** are the builder's non-regression test: train under a setup, evaluate on chosen tasks, compare to a baseline to confirm a change (data, architecture, params) did not break - or improved - expected performance. Evals also run on intermediate **checkpoints** to catch regressions/spikes during training.
- **The FineWeb team's four criteria** for selecting tasks that give signal even on weak mid-training models (derived from training 49 models, 73k GPU-hours): **monotonicity** (Spearman score-vs-steps >= 0.5 - does the task improve as training progresses?), **low noise** (signal-to-noise ratio > 20, measured across seeds), **non-random performance** (max score sits >= 3 std above the random baseline), and **model-ordering consistency** (Kendall's tau - do rankings at 30B tokens predict rankings at 300B?).
- These properties sharpen Fourrier's high-SNR / watch-trajectories-and-ranges guidance already on this page, and connect to reward-model practice: tracking **win-rate or win-probability over training** can detect model degradation and select the optimal checkpoint (see [[llm-as-judge]]).

## In my own words (hcho)
