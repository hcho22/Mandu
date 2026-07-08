---
type: concept
tags: [evals, benchmarks, saturation, lifecycle]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Benchmark Saturation

From [[llm-evaluation-guidebook]] and [[what-is-a-contaminated-llm]]: a benchmark is saturated when model performance passes human level or clusters near the ceiling, so it loses discriminative power between models.
"It's like evaluating high school students on pre-school problems: success tells you nothing (though failure is still indicative)."

## Key points

- Saturation is one of the two lifecycle threats to a benchmark, alongside [[data-contamination]] - together they mean "a benchmark stops being useful as soon as it becomes public."
- It drives the constant churn of new benchmarks: MMLU -> MMLU-Pro, GSM8K -> MATH-500/AIME, HumanEval -> LiveCodeBench/SWE-Bench, etc.
- Counter-tactics: harder graduate-level sets (GPQA, Humanity's Last Exam), procedurally-regenerated sets (GSM-Symbolic, ZebraLogic), and contamination-resistant designs (LiveCodeBench dates problems; forecasting can't be contaminated).
- **Practical read ([[what-is-a-contaminated-llm]]):** distrust scores clustered near saturation - "when the top three models are within 1.5 points of each other above 90, the benchmark has stopped measuring anything for the frontier; the information is in the long tail of harder tests." Contamination retired MMLU, HumanEval, HellaSwag, and original GSM8K precisely because they saturated.

## Synthesis

Saturation is the "measurement decays over time" half of the [[evals]] area's validity story (contamination is the other), and it is why [[eval-driven-development]] favors your own evolving task-specific set over a fixed public benchmark.
It reframes evaluation as never finished - "as models improve, benchmarks saturate" - which is a maintenance discipline, not a one-time setup, and a natural fit for hcho's ongoing-validation instinct.
The move toward saturation-resistant designs (procedural generation, dated problems, forecasting) is the same idea as a refreshed regression suite that keeps catching new failure modes.
