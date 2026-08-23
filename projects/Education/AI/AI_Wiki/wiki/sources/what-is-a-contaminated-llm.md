---
type: source
title: "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide"
source-type: article
author: "Jonathan Chavez (llm-stats.com)"
url: "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
date-ingested: 2026-07-08
date-created: 2026-04-30
tags: [evals, contamination, benchmarks, detection, saturation, validity]
---

# What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide

A focused 2026 guide (Jonathan Chavez, llm-stats.com) on benchmark contamination: how it happens, the five detection methods that work, the famous cases, and the 2026 benchmarks built to resist it.
It is the dedicated deep-dive behind the [[data-contamination]] concept the eval sources kept pointing at.

## Key claims

- **The Codeforces cliff (the origin story):** four days after GPT-4 launched, Horace He found it solved 10/10 easy Codeforces problems from *before* its Sep-2021 cutoff and 0/10 from after. The formal study (Roberts et al., NeurIPS 2024) confirmed pass rate rose with a problem's GitHub presence, but only pre-cutoff (+47.8% odds per unit of log-presence; nil after). "The model is better at problems it has seen, in proportion to how often it has seen them."
- **Two definitions:** textbook = test data in the training set; functional (ConStat) = any process that inflates benchmark performance without matching real-world capability. The second is the useful one - a model scoring 60 on GSM8K but 47 on rephrased GSM8K is contaminated regardless of literal leakage.
- **[[contamination-detection|Three flavors]]:** direct (exact test item in corpus), indirect (paraphrase/solution discussion), and **latent** (the model was *selected* for its benchmark score - "Goodhart's Law in checkpoint selection"; the moment a number becomes a target it stops being a measurement).
- **[[contamination-detection|Five detection methods]]:** time-based partition, Min-K% Prob (reference-free membership inference), Time Travel (guided-instruction completion), ConStat (rephrased-sample performance gap with a reference-model panel), and canary GUIDs.
- **Famous cases:** phi-CTNL (a 1M-param model trained only on benchmarks got perfect scores - Schaeffer's satire); GSM8K->GSM1K (worst models dropped 13pp, Phi/Mistral overfit, frontier barely moved, r=0.32 memorization correlation); phi-1.5's perplexity tell; ConStat detecting Mistral-7B/Llama-3-70B/Llama-2-70B (3-8% effects); GPT-4 completing AG News/WNLI/XSum test partitions; the BIG-Bench canary reproduced by GPT-4-base, Claude 3.5 Sonnet, and Gemini (public chat models refuse - RLHF suppression, not absence).
- **The canary backfired twice:** labs didn't honor it uniformly, and the "too important to memorize" marker may make models memorize the doc *harder*.
- **Dose-response (2026):** contamination effect scales with model capacity and memorization incentive; overtraining on fresh data dilutes the dose toward zero (Bordt et al.: little effect for overtrained frontier models). But a single test replica can beat infinite clean compute on short-form answers; long generative solutions are exponentially harder to memorize - so short MCQ degrades worse than long reasoning.
- **The 2026 fix:** contamination retired MMLU, HumanEval, HellaSwag, and original GSM8K. Replacements follow three principles - time-gate the questions (LiveCodeBench, LiveBench), keep answers private (FrontierMath), and make the test harder than memorization (MMLU-Pro's 10 options). And: evaluate on your own data.

## Connections

- [[contamination-detection]] - the concept this source introduces (three flavors + five methods).
- [[data-contamination]] - deeply extended (functional definition, latent/Goodhart flavor, the Codeforces cliff, dose-response, retired benchmarks).
- [[benchmark-saturation]] - the retired-benchmark story and the contamination-resistant 2026 stack.
- [[benchmark-sensitivity]] / [[score-reproducibility]] - the same "a leaderboard number may not mean what it claims" theme.
- [[eval-driven-development]] / [[evaluation-pipeline]] - "evaluate on your own data the labs can't have seen" is the application-layer defense.
- [[anthropic]] / [[openai]] / [[google]] - GPT-4, Claude, Gemini all reproduce the BIG-Bench canary.
- Cross-wiki: sharpens the test-set-hygiene rigor hcho's Agentic RAG eval harness embodies.

## Source

- **Author:** Jonathan Chavez, llm-stats.com · **Published:** 2026-04-30
- **URL:** https://llm-stats.com/blog/research/what-is-a-contaminated-llm
- **Note:** well-sourced secondary synthesis of the 2023-2026 contamination literature (Roberts, Shi, Golchin & Surdeanu, Dekoninck/ConStat, Scale AI/GSM1K, Schaeffer/phi-CTNL).
- **Raw:** [[What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
