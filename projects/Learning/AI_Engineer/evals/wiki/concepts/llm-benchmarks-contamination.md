---
type: concept
tags: [evals, benchmarks, contamination]
date: 2026-06-08
source-count: 4
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

Chip Huyen, [[evaluate-ai-systems]], adds the model-selection view: public benchmarks and leaderboards help narrow the candidate set, but they cannot choose the best model for a product.

- There are thousands of benchmarks, old benchmarks saturate quickly, and evaluation harnesses such as EleutherAI's lm-evaluation-harness and OpenAI evals make it easier to run many of them. The challenge shifts from running benchmarks to deciding which benchmarks matter.
- Public leaderboards are useful but incomplete because they select a small subset of benchmarks, often under compute constraints, and benchmark choice is not always transparently tied to the capabilities a user actually needs.
- Benchmark aggregation is itself a modeling choice. Simple averages treat all scores and capabilities equally, while approaches such as mean win rate ask how often one model beats another across scenarios. Either way, a leaderboard encodes priorities that may not match the application.
- Benchmark correlation matters: highly correlated benchmarks overweight the same capability, while weakly correlated metrics may expose either a real capability separation or unreliable measurements.
- Multiple-choice benchmarks are easy to verify, but they primarily test choosing among options, not generating useful open-ended outputs. They can also be sensitive to small formatting changes.
- Contamination undermines trust in public scores. Benchmark data can appear in training data directly or indirectly, and high public scores can reflect memorization. Private holdouts, clean-sample reporting, and contamination checks are the countermeasures.
- The practical use of public benchmarks is to eliminate bad fits and pick a small group of promising candidates for private evals, not to substitute for application-specific evaluation.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], focuses the page on benchmark contamination itself: how it happens, how it is detected, and what newer benchmarks do differently.

- A useful working definition is broader than "the model trained on the test set": contamination is any process that inflates benchmark performance without matching real-world capability. The mechanisms are **direct** contamination, **indirect** contamination through paraphrases or solution material, and **latent** contamination through checkpoint/model selection against a benchmark.
- The GPT-4 Codeforces cutoff case is a clean contamination pattern: strong performance on easy pre-cutoff problems and failure on comparable post-cutoff problems. The later Codeforces/Project Euler study tied pre-cutoff pass rate to GitHub presence, with the relationship disappearing after the cutoff.
- Five detection families recur in the literature: **time-based partitioning**, **Min-K% Prob** membership inference, **Time Travel** guided completions, **ConStat** performance gaps on rephrased/reference samples, and **canary GUIDs**.
- Concrete cases include GSM8K-vs-GSM1K overfitting for Phi and Mistral families, ConStat detections on Mistral/Llama/Open LLM Leaderboard models, Time Travel findings on GPT-4 and datasets such as AG News/WNLI/XSum, and BIG-Bench canary reproduction by several frontier models.
- Contamination effects are regime-dependent. The dose-response view says capacity, contaminated-token dose, and the incentive to memorize determine how much test-set inclusion affects scores; long generative solutions can be harder to memorize than short discriminative answers.
- The 2026-style replacement stack relies on post-cutoff or rotating tests (LiveCodeBench/LiveBench), private unpublished holdouts (FrontierMath/GSM1K-style practice), harder answer formats (MMLU-Pro), and application-specific evals on data the labs could not have seen.

## In my own words (hcho)
Why this matters for LLMs: contamination
For LLMs, the "training set" is most of the internet — so the test set can accidentally leak into training. Two well-documented cases:
1. GSM8K leakage detected by ConStat (2024). Researchers at ETH Zurich built ConStat, a statistical test that compares a model's performance on a famous benchmark against its performance on a freshly rephrased or synthetic equivalent of the same difficulty. A clean model should score similarly on both; a contaminated one scores suspiciously higher on the original. Their analysis found statistically significant contamination evidence on GSM8K (a grade-school math benchmark) for several popular open models, including models in the Mistral and Phi families — suggesting the benchmark's problems (or close paraphrases) had seeped into their training data, inflating reported math ability.
2. The GPT-4 Codeforces cliff. Shortly after GPT-4's release, researchers (notably Horace He) tested it on Codeforces competitive programming problems. GPT-4 solved problems published before its training cutoff at a high rate — but its solve rate collapsed to roughly zero on problems published after the cutoff, even at comparable difficulty. If the model had genuinely learned to solve these problems, the publication date shouldn't matter. The cliff is a smoking gun for memorization: it had seen the old problems (and their public solutions) during training.
The beginner takeaway
Both failures are the same sin from the first diagram: the test set touched the training data. The detection tricks map nicely to the eval concepts:

ConStat is essentially asking "does the model do better on the exact test set than on a fresh equivalent?" — a contamination-robust validation idea.
The Codeforces cliff uses time as a natural train/test split: anything after the cutoff is guaranteed-clean test data.

This is why modern eval practice favors private held-out sets, regularly refreshed benchmarks (e.g. LiveBench, LiveCodeBench), and post-cutoff data — recreating, at internet scale, the discipline of "the test set is touched once and never trained on."