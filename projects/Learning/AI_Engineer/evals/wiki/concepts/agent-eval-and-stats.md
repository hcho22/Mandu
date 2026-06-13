---
type: concept
tags: [evals, agents, statistics]
date: 2026-06-08
source-count: 2
status: seeded
session: "S9 - Agent evaluation + statistical rigor"
---

# Agent Evaluation and Statistics

Evaluating multi-step agents (task completion, tool-call correctness, trajectory) with statistical rigor (confidence intervals, sample size, noise).

## From the sources

Clémentine Fourrier, [[lets-talk-about-llm-evaluation]], makes the case for treating evaluation as a statistically noisy measurement (the "statistical rigor" half of this concept, not the agent-trajectory half):

- LLM **scores** on automated benchmarks are extremely sensitive to minute changes in prompting and normalization; they are unstable measurements.
- **Rankings** built from robust evaluations are more stable than raw scores. Citing the ImageNet-era lesson, the more reliable way to compare models is to find broad groups of evaluations that give consistent, stable rankings.
- Perturbation experiments (Moritz Hardt, ICLR 2024): small within-range score changes on the Open LLM Leaderboard, and adding a weak contender to the Chatbot Arena, both disturbed rankings, showing neither was fully stable.
- Aggregating many **noisy human votes** can approximate the truth via a "wisdom of the crowd" effect (Galton): individual estimates form a distribution centered on the real answer, so scale can smooth subjectivity (relevant to arena-style eval; see [[llm-as-judge]]).

Chip Huyen, [[evaluate-ai-systems]], adds task/turn structure and statistical checks:

- Multi-turn applications should be evaluated both **per turn** and **per task**. Turn-based evaluation grades each output; task-based evaluation asks whether the user goal was completed and how many turns it took.
- Task boundaries are hard in chat-like applications, but task success is usually closer to what users care about than per-message quality. The BIG-bench `twenty_questions` task is an example where the score depends on completing the task and the number of questions needed.
- Evaluation sets should be large enough for reliable comparisons. Bootstrap resampling can reveal whether a set is too small or noisy by showing whether repeated samples produce similar scores.
- Smaller differences require much larger samples: OpenAI's rough table estimates about 10 examples to detect a 30% difference, 100 for 10%, 1,000 for 3%, and 10,000 for 1% at 95% confidence.
- Slice-based evaluation prevents aggregate metrics from hiding failures and helps avoid Simpson's paradox, where one model can look better overall while losing in every subgroup.
- Evaluation pipelines should be tested for reproducibility, metric correlation, and sensitivity to configuration. Judge temperature, data version, rubrics, prompts, sampling settings, and model versions should be tracked.

## In my own words (hcho)
