---
type: concept
tags: [evals, benchmarks, contamination]
date: 2026-06-08
source-count: 2
status: seeded
session: "S4 - LLM benchmarks: what they measure and what they don't"
---

# LLM Benchmarks and Contamination

The major LLM benchmark families and their saturation and training-data contamination status.

## From the sources

Clémentine Fourrier, [[lets-talk-about-llm-evaluation]], frames automated benchmarking and its main failure mode, contamination:

- A benchmark is two parts: a collection of **samples** (sometimes paired with a gold reference) and a **metric** that scores the output. For LLMs the two main task shapes are **generation** (compare generated text to a reference after normalization) and **multiple-choice** (compare the log-probabilities of candidate continuations).
- The reason to test on held-out data is **generalization**: a model that scores only on data it has seen is **overfitting**. Well-defined **tasks** (spam classification) are easy to score; broad **capabilities** ("good at math") get holistic proxies like GSM8K whose pass/fail is hard to interpret.
- Benchmark-specific biases: models can favor answers by their **presentation order** in multiple-choice, and **normalization** in generative eval can be unfair if poorly designed.
- **Contamination** is when eval data leaks into the training set; the model then scores high without generalizing. Mitigations: **canary strings** (BigBench), **gating**, **encryption**, and **dynamic benchmarks** (datasets refreshed so the data is always unseen, but costly to maintain). Closed black-box APIs offer no guarantee that submitted eval data is not later used for training.
- Scores are fragile; **rankings** built from robust evaluations are more stable than raw scores (see [[agent-eval-and-stats]]). Capability claims beyond "best on this proxy task" are mostly not rigorously supportable today.

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], names the major benchmark families and a concrete reproducibility failure:

- The major families: **MMLU** (57 knowledge/reasoning tasks), **HELM** (multi-metric, multi-domain: accuracy, calibration, robustness, fairness, bias, toxicity), the **EleutherAI lm-evaluation-harness** (unified framework, ~200 tasks, incorporates BigBench/MMLU), and **AlpacaEval** (win rate vs a reference model, validated against 20k human annotations).
- **Implementation sensitivity:** the same model gets significantly different MMLU scores across the original, HELM, and EleutherAI implementations, because the prompt, tokenization, and answer-scoring differ (compare predicted-letter probabilities vs next-token probabilities vs full-answer-sequence probabilities). Both absolute scores and rankings can shift, so scores are not comparable unless the implementation is identical down to prompts and tokenization.
- Practical consequence: off-the-shelf benchmarks like MMLU rarely fit a real product ("unless your LLM is studying for a school exam"); prefer task-specific evals (see [[offline-vs-online-evals]]).

## In my own words (hcho)
