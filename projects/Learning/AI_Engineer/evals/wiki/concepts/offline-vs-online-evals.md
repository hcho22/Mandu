---
type: concept
tags: [evals, offline-evals, online-evals, fundamentals]
date: 2026-06-08
source-count: 5
status: seeded
session: "S1 - What evals are and why they matter"
---

# Offline vs Online Evals

The distinction between evaluating a model on a fixed dataset before deploy (offline) versus on live traffic after deploy (online), plus human-in-the-loop grading.

## From the sources

Hamel Husain, [[your-ai-product-needs-evals]], frames evals as a three-level progression that spans the offline-to-online boundary:

- **Level 1 (offline):** fast, cheap unit-test assertions run in CI on every change.
- **Level 2 (offline and sampled):** human and model-graded review of logged traces; align the LLM judge to human labels.
- **Level 3 (online):** A/B testing on live traffic, deferred until product-market fit is clearer.

The takeaway for this concept: offline evals (Levels 1-2) are where iteration speed comes from, and online evaluation (Level 3) is a later-stage validation, not the starting point.

Clémentine Fourrier, [[lets-talk-about-llm-evaluation]], gives the complementary "what evals are" taxonomy: the methods you can use and the reasons you would use them.

- **Three methods** (each with distinct uses and limits): automated **benchmarks**, **humans as judges** (vibes-checks → Elo arenas → paid systematic annotation), and **models as judges**. See [[llm-benchmarks-contamination]] and [[llm-as-judge]] for each method's failure modes.
- **Three purposes people conflate:** (1) **non-regression testing** — has a change broken expected behavior? Watch trajectories and ranges, not precise scores (see [[ci-eval-gates-and-drift]]); (2) **leaderboards/rankings** — which model is best? Rankings are more robust than scores (see [[agent-eval-and-stats]]); (3) **capability claims** — can the model do X? Mostly not rigorously answerable, since "capability" is undefined for models.
- The unifying caution: scores give bounded signal, not ground truth, and "general capability" cannot yet be measured because it is not yet defined.

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], adds the practical bookends of the offline-to-online span:

- **Offline starting point - "Eval-Driven Development":** build a set of task-specific evals (prompt, context, expected output) and run them on every change to measure improvements or regressions, rather than relying on off-the-shelf benchmarks. Sometimes the most useful offline check is still a human "vibe check."
- **Online signal - user feedback and monitoring:** explicit (thumbs up/down) and implicit (accept/edit/ignore) feedback give a direct measure of user satisfaction that offline evals cannot, and feed the data flywheel (see [[ci-eval-gates-and-drift]]). Production monitoring is the real test - one team found an LLM support bot caused 12x more losses in an A/B test.

Chip Huyen, [[evaluate-ai-systems]], turns the same split into an end-to-end application workflow:

- **Evaluation-driven development** means defining evaluation criteria before building. The criteria should be specific to the application: domain capability, generation quality, instruction following, cost, latency, scale, safety, factual consistency, and business impact.
- Public benchmarks and leaderboards are useful only as an **offline filter** for model candidates. The decisive step is running the candidates through your own evaluation pipeline with your own prompts, metrics, rubrics, and data.
- Production monitoring closes the loop: after deployment, the system should collect actual user feedback, detect failures, and test whether offline metrics correspond to business metrics. A/B testing is necessary when business outcomes can be confounded by promotions, product launches, or other external changes.
- The same application may need evaluation at multiple levels: component, turn, task, and end-to-end. Task-level evaluation matters most to users, while component and turn-level evaluation explain where a failure came from.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], sharpens the caution around public offline benchmarks:

- Public benchmark scores are only trustworthy when the benchmark is still discriminative and plausibly unseen. Saturated tests such as original MMLU, HumanEval, HellaSwag, and GSM8K lose value when top models cluster near the ceiling or when contamination evidence accumulates.
- Contamination-resistant offline evals use post-cutoff items, rotating fresh questions, private holdouts, or harder answer formats. Examples in the article include LiveCodeBench/LiveBench, FrontierMath, GSM1K-style private replacement sets, and MMLU-Pro.
- For product work, the practical answer is the same as in the broader evals workflow: use public benchmarks to orient, but evaluate model candidates on private application data, prompts, and failure modes that providers could not have seen.
- Online monitoring remains necessary because even a clean offline benchmark measures abstract capability, not whether the model handles the product's users, codebase, tone, edge cases, or business outcomes.

## In my own words (hcho)
