---
type: concept
tags: [evals, contamination, benchmarks, leakage, validity]
status: established
source-count: 4
last-updated: 2026-07-08
---

# Data Contamination

From [[lets-talk-about-llm-evaluation]] ([[clementine-fourrier]]), [[evaluate-ai-systems]] ([[chip-huyen]]), [[llm-evaluation-guidebook]], and the dedicated deep-dive [[what-is-a-contaminated-llm]]: when an evaluation dataset ends up in a model's training set (aka data leakage, "training on the test set"), the model scores high on that benchmark without the performance generalizing to the underlying task - "doing recall, not reasoning."

## Key points

- Public benchmarks in plain text very likely leak into training corpora, often accidentally.
- Mitigations: **canary strings** (a marker to find and remove, as BigBench does), **encrypted** or **gated** benchmarks, and **dynamic benchmarks** (regularly refreshed data so scores are on genuinely unseen examples) - the last is effective but costly to sustain.
- Closed black-box APIs give **no guarantee** your submitted eval data won't later be used for training/fine-tuning.

## Detection and handling ([[evaluate-ai-systems]])

- **A benchmark stops being useful as soon as it becomes public** - Rylan Schaeffer's satirical "Pretraining on the Test Set Is All You Need" trained a 1M-param model on benchmarks and beat far larger models.
- Contamination is usually **unintentional** (web scraping pulls in public benchmarks), sometimes **indirect** (train and test drawn from the same textbook), and sometimes **deliberate-but-defensible** (train the final model on high-quality benchmark data before release).
- **Detect** via n-gram overlap (e.g. a shared 13-token sequence marks a sample "dirty"; accurate but costly and needs training-data access) or perplexity (unusually low perplexity on eval data suggests it was seen; cheap, approximate).
- **Handle** by reporting the clean-subset score alongside the full-benchmark score, and by keeping part of a benchmark private as a hold-out.

## The best cure: procedural generation ([[llm-evaluation-guidebook]])

Assume any public-internet dataset is or will be contaminated. Beyond canary strings, encryption/gating, and post-hoc detection, the strongest mitigation is **rule-based procedural generation** - benchmarks that algorithmically produce unlimited fresh test cases (NPHardEval, MuSR, ZebraLogic, GSM-Symbolic, IFEval), which controls difficulty, enables automatic verification, and structurally prevents memorization. Dated benchmarks (LiveCodeBench) and forecasting are contamination-proof by construction. It pairs with [[benchmark-saturation]] as the two reasons a public benchmark decays.

## The deep-dive ([[what-is-a-contaminated-llm]])

- **Functional definition (ConStat):** contamination is *any process that inflates benchmark performance without matching real capability* - broader and more useful than "test data in the training set."
- **Three flavors:** direct, indirect, and **latent** (Goodhart in checkpoint selection - the model was *selected* for its score). Detection of all three: see [[contamination-detection]].
- **The Codeforces cliff:** GPT-4 solved 10/10 easy pre-cutoff problems and 0/10 post-cutoff - the clean natural experiment that broke the field's trust in benchmark numbers.
- **Dose-response (2026):** the effect scales with model capacity and memorization incentive; overtraining on fresh unique data dilutes the dose toward zero (so frontier models show little effect), but a single test replica can beat infinite clean compute on short answers. Short-form MCQ degrades worse than long generative reasoning.
- **It retired four benchmarks** (MMLU, HumanEval, HellaSwag, original GSM8K). The contamination-resistant 2026 stack follows three principles: time-gate questions (LiveCodeBench), keep answers private (FrontierMath), and make the test harder than memorization (MMLU-Pro).

## Synthesis

Contamination is the validity threat that undermines the whole benchmark method in [[three-eval-methods]]: a high score can be memorization, not capability, so it is the deeper cousin of [[benchmark-sensitivity]] (both mean a leaderboard number may not mean what it claims).
It is the reason human eval and your-own-task-specific evals ([[eval-driven-development]]) matter - fresh prompts can't have leaked.
This is exactly hcho's territory: contamination is a test-set-hygiene problem, the same "don't validate against data you trained/tuned on" discipline from ML and QA - now with concrete detection tools (n-gram overlap, perplexity). The dedicated contaminated-LLM source deepens this page further.
