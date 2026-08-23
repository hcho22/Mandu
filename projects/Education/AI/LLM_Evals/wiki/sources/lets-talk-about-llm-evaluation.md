---
type: source
tags: [evals, benchmarks, contamination, llm-as-judge, human-eval, ranking-stability]
date: 2026-06-08
title: "Let's talk about LLM evaluation"
author: "Clémentine Fourrier"
url: "https://huggingface.co/blog/clefourrier/llm-evaluation"
concepts: [llm-benchmarks-contamination, llm-as-judge, offline-vs-online-evals, ci-eval-gates-and-drift, agent-eval-and-stats]
---

# Let's talk about LLM evaluation

Clémentine Fourrier (Hugging Face evaluation and leaderboards team) gives a survey of how and why LLM evaluation is done. She splits the "how" into three methods (automated benchmarks, humans as judges, models as judges), each with its own uses and failure modes, and the "why" into three distinct purposes people tend to conflate (non-regression testing, leaderboards/rankings, and capability claims). The throughline is that scores are fragile and "general capability" is not yet definable, so evaluation gives bounded signal rather than ground truth.

## Key claims

- There are three main ways to evaluate LLMs, each with distinct uses and limits: **automated benchmarks**, **humans as judges**, **models as judges**.
- A benchmark is a collection of **samples** (sometimes with a gold reference) plus a **metric**; for LLMs the two main task shapes are generation (compare to a reference after normalization) and multiple-choice (compare log-probabilities of continuations).
- The point of benchmarking on held-out data is to test **generalization**, not memorization; a model that only scores on seen data is **overfitting**.
- Benchmarks have known failure modes: models favoring choices by presentation **order** in multiple-choice, and **unfair normalization** in generative eval.
- **Contamination** (eval data leaking into the training set) inflates benchmark scores without real generalization; mitigations include canary strings, gating, encryption, and **dynamic benchmarks** (regularly refreshed data), though refresh is costly. Closed black-box APIs give no guarantee submitted eval data is not later trained on.
- For well-defined **tasks** performance is easy to measure; for broad **capabilities** ("good at math") people use holistic proxies (e.g. GSM8K) whose success and failure are hard to interpret.
- **Human judges** handle open-ended tasks and reduce contamination, but carry biases: preference for **sycophantic/assertive** answers, underestimating errors stated confidently, and **culturally bound** preferences. Forms span vibes-checks → **arenas** (Elo, e.g. LMSYS) → paid **systematic annotation**.
- **Model-as-judge** is cheaper than humans but has subtle, hard-to-interpret biases: **self-preference**, inconsistent score ranges (improved by asking for reasoning before the score), and weak correlation with human rankings. Generalist judges correlate with human preference but are closed and drift; small specialist judges may carry less subtle bias.
- Evaluation serves three distinct purposes people conflate: (1) **non-regression testing** — watch score *trajectories* and *ranges*, not precise values; (2) **leaderboards/rankings** — rankings are more robust than scores; (3) **capability claims** — mostly not rigorously possible, since "capability" is undefined for models.
- Scores are highly sensitive to minute prompt changes; **rankings** built from robust evaluations are more stable than raw scores (perturbation experiments by Moritz Hardt on the Open LLM Leaderboard and Chatbot Arena). Aggregating many noisy human votes can approximate truth via a "wisdom of the crowd" (Galton) effect.

## Connections

- [[llm-benchmarks-contamination]] - the core of the piece: benchmark anatomy (samples + metric), generalization vs overfitting, task vs capability, multiple-choice order bias, normalization unfairness, and the full contamination story (canary strings, gating, dynamic benchmarks).
- [[llm-as-judge]] - the "model as judge" section: generalist vs specialist judges and their biases (self-preference, inconsistent score ranges, reason-before-score mitigation, weak human-ranking correlation).
- [[offline-vs-online-evals]] - the "how do we evaluate" taxonomy of three methods (benchmarks, human judges, model judges) and the three distinct purposes evaluation serves.
- [[ci-eval-gates-and-drift]] - non-regression testing framed from software: confirm a change has not broken expected behavior by watching score trajectories and ranges, using high signal-to-noise benchmarks.
- [[agent-eval-and-stats]] - statistical fragility of evaluation: scores shift under minute prompt changes while rankings are more stable; perturbation experiments and wisdom-of-the-crowd aggregation of noisy votes.

## Source

- **Author:** Clémentine Fourrier
- **Title:** Let's talk about LLM evaluation
- **URL:** https://huggingface.co/blog/clefourrier/llm-evaluation
- **Published:** 2024-05-23
- **Raw:** `raw/Let's talk about LLM evaluation.md` (clipped markdown copy, immutable)
- **Ingested:** 2026-06-08
