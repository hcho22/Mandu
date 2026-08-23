---
type: concept
tags: [evals, benchmarks, reproducibility, leaderboards]
status: developing
source-count: 3
last-updated: 2026-07-08
---

# Benchmark Sensitivity

From [[llm-patterns]], [[lets-talk-about-llm-evaluation]], and [[evaluate-ai-systems]]: the same model can score very differently on the same benchmark depending on how the benchmark is implemented, so leaderboard scores are not comparable unless the implementation is identical down to prompts and tokenization.

## The MMLU example

HuggingFace compared three MMLU implementations and found both the prompts and the scoring differed:

- **Original MMLU** - compares predicted probabilities on the answer letters (A/B/C/D) only.
- **HELM** - takes the highest-probability next token, even if it isn't one of the options.
- **EleutherAI** - computes the probability of the full answer sequence, then picks the highest.

Result: both absolute scores and model rankings fluctuate widely by implementation. (The QLoRA author's blunt take: "do not work with/report or trust MMLU scores.")

## Rankings over scores ([[lets-talk-about-llm-evaluation]])

Because scores are so unstable, Fourrier argues the more trustworthy signal is *rankings* over robust groups of evaluations, not absolute numbers - the ImageNet-era lesson. But even that has limits: perturbation experiments (Moritz Hardt) show neither the Open LLM Leaderboard nor the Chatbot Arena gives fully stable rankings. So prefer rankings to scores, but don't over-trust either.

## Also from [[evaluate-ai-systems]]

- **MCQ formatting sensitivity:** an extra space or an added "Choices:" phrase can flip a model's multiple-choice answers (Alzahrani et al.).
- **Benchmark correlation matters:** don't aggregate two perfectly-correlated benchmarks (they exaggerate a bias); HF's six-benchmark leaderboard shows ARC-C/MMLU/WinoGrande strongly correlated (all reasoning), TruthfulQA only moderately (truthfulness is separable).
- **Aggregation is unclear:** HF averages benchmark scores (treating 80% on TruthfulQA = 80% on GSM-8K); HELM uses mean win rate. Neither weighting is obviously right, and leaderboards rarely explain their benchmark choice.

The full checklist of what makes a *specific reported score* irreproducible (code base, seeds, metric definition, normalization, prompt format, few-shot order, hardware, batch size, precision) is its own concept: [[score-reproducibility]] ([[llm-evaluation-guidebook]]).

## Synthesis

This is the eval-hygiene concept that makes public leaderboards suspect and is the natural bridge to data contamination (see the forthcoming contaminated-LLM source): if implementation details silently move scores, so does test-set leakage.
It reinforces [[eval-driven-development]] - build your own task-specific eval with a pinned implementation rather than trusting an off-the-shelf benchmark number - and it is a validation instinct: an unreproducible measurement isn't a measurement.
For hcho it is a sharp interview point: "I don't trust a benchmark score I can't reproduce end to end," which is exactly the rigor the AI-quality roles screen for.
