---
type: concept
tags: [evals, contamination, detection, membership-inference, validity]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Contamination Detection

From [[what-is-a-contaminated-llm]]: how to tell whether a model's benchmark score is real capability or memorized [[data-contamination]], without needing access to the training corpus.

## The three flavors (what you're detecting)

- **Direct** - the exact test item was in the pretraining corpus.
- **Indirect** - a paraphrase or a solution discussion was.
- **Latent** - nobody trained on the test set, but the model was *selected* for its score on it ("Goodhart's Law in checkpoint selection": pick the best-MMLU checkpoint of 100 and the selection process saw MMLU even if pretraining didn't).

## The five detection methods

1. **Time-based partition** - split a timestamped benchmark at the model's cutoff; higher pre-cutoff accuracy on equally hard problems is the tell (the Codeforces cliff; LiveCodeBench is built on this).
2. **Min-K% Prob** (Shi et al., ICLR 2024) - reference-free membership inference: seen text has few very-low-probability tokens; average the bottom k% and flag unusually high values. Needs only black-box logprobs.
3. **Time Travel** (Golchin & Surdeanu, ICLR 2024) - give the dataset name, partition, and first half of an instance and ask the model to complete it; high ROUGE-L overlap vs a no-name baseline means contamination (caught GPT-4 on AG News, WNLI, XSum).
4. **ConStat** (Dekoninck et al., 2024) - compare the target's performance gap between a benchmark and a rephrased reference against a panel of reference models; an unusual lift is contamination, reported as a p-value and an effect size.
5. **Canary GUIDs** - a unique string embedded in benchmark files (BIG-Bench's `26b5c67b-...`); if the model reproduces it, it saw the benchmark. (It failed in practice - labs ignored it, and the "important" marker may worsen memorization.)

## Synthesis

This is the practitioner's toolkit for the validity threat named in [[data-contamination]], and it is validation/QA work in its purest research form: design an experiment (a time cutoff, a rephrase, a membership test) that separates recall from reasoning.
Time-based partition and Min-K% Prob are the most broadly usable (only completions or logprobs needed); ConStat gives the cleanest effect-size estimate.
For hcho this is unusually strong interview material - naming the five methods and the three flavors demonstrates exactly the measurement rigor AI-quality roles screen for, and it directly informs how to keep his own eval sets uncontaminated.
