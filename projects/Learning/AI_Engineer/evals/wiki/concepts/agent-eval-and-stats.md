---
type: concept
tags: [evals, agents, statistics]
date: 2026-06-08
source-count: 1
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

## In my own words (hcho)
