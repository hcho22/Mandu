---
type: concept
tags: [evals, data-splits, leakage, cross-validation]
date: 2026-06-06
source-count: 2
status: seeded
session: "S3 - Data splits, leakage, baselines, cross-validation"
---

# Data Leakage and Splits

Train/validation/test discipline, cross-validation, and the leakage failures (including benchmark contamination) that inflate scores.

## From the sources

Chip Huyen, [[evaluate-ai-systems]], frames public benchmark contamination as the LLM version of training-on-test-set leakage:

- **Data contamination** happens when a model was trained on evaluation data, so benchmark scores can reflect memorization rather than generalization. This is also called data leakage, training on the test set, or cheating.
- Contamination can be direct, indirect, accidental, or intentional. Public benchmark examples can be scraped into training corpora; training data and eval data can come from the same upstream source; teams may also continue training on benchmark data after using the benchmark to select a model.
- Detection methods include **n-gram overlap** against training data and unusually low **perplexity** on evaluation examples. N-gram overlap is more accurate but expensive and usually requires access to training data; perplexity is cheaper but less precise.
- Better reporting would disclose what share of a benchmark appears in training data, and report performance on both the overall benchmark and the clean subset.
- Evaluation data should be split and sliced by meaningful attributes: production distribution, known failure cases, typo-heavy inputs, out-of-scope requests, user tier, traffic source, usage pattern, and other risk slices. Slice-based evaluation avoids hiding failures behind aggregate scores and helps catch Simpson's paradox.
- Bootstrap resampling can test whether an evaluation set is large enough: if repeated bootstraps of the same set produce wildly different scores, the set is too small or too noisy.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], adds a taxonomy and several leakage tests that do not require access to the training corpus:

- Contamination can be **direct** (exact eval item in training), **indirect** (solution discussions, paraphrases, or derived material in training), or **latent** (model/checkpoint selection optimized against the benchmark even if the pretraining corpus did not include the test set).
- **Time-based partitioning** is a split discipline for public benchmarks with timestamps: compare pre-cutoff and post-cutoff examples of similar difficulty. A sharp cutoff-aligned gap is stronger evidence than a fuzzy similarity match.
- **Min-K% Prob** is a membership-inference check: if the least likely tokens in a sample are not very surprising to the model, the sample may have been memorized.
- **Time Travel** probes leakage by giving a model dataset metadata plus the first half of an instance and measuring whether it reconstructs the held-out remainder better than a generic completion baseline.
- **ConStat** treats leakage as an unusual benchmark-specific lift relative to matched/rephrased samples and reference models, producing both a significance test and an estimated contamination effect size.
- Canary strings can identify exact leakage, but the BIG-Bench canary story shows that canaries are not a process guarantee. Private or gated holdouts and post-cutoff/rotating data are stronger split controls.

## In my own words (hcho)
