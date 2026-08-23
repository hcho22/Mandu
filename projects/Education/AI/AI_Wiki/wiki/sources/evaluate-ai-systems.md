---
type: source
title: "Evaluate AI Systems (AI Engineering, Chapter 4)"
source-type: guidebook
author: "Chip Huyen"
url: "local"
date-ingested: 2026-07-08
date-created: 2024-12-01
tags: [evals, evaluation-pipeline, benchmarks, model-selection, contamination, factual-consistency]
---

# Evaluate AI Systems (AI Engineering, Ch. 4)

Chapter 4 of Chip Huyen's ([[chip-huyen]]) book *AI Engineering*: the authoritative practitioner treatment of evaluating models for your application.
Three parts: evaluation criteria (what to measure and how), model selection (choosing among models, including build-vs-buy and reading public benchmarks), and designing a custom evaluation pipeline.
Thesis: evaluation is the biggest bottleneck to AI adoption, so define how you'll evaluate before you build ([[eval-driven-development]]).

## Key claims

### Evaluation criteria ([[evaluation-criteria]])
- Four buckets: **domain-specific capability** (benchmarks, functional correctness, MCQs), **generation capability** (fluency, coherence, [[factual-consistency]], safety), **instruction-following** (IFEval, INFOBench, roleplaying), and **cost and latency** (Pareto optimization; time-to-first-token etc.).
- MCQs are popular (easy to create/verify) but test discrimination, not generation, and are sensitive to formatting ([[benchmark-sensitivity]]).

### Factual consistency ([[factual-consistency]])
- **Local** (against provided context) vs **global** (against open knowledge); local is much easier and is the key RAG metric.
- Methods: AI judge, self-verification (SelfCheckGPT), knowledge-augmented (SAFE: decompose -> self-contained -> search -> verify), textual entailment/NLI (entailment/contradiction/neutral), and specialized scorers (DeBERTa-NLI). Benchmark: TruthfulQA.

### Model selection ([[model-build-vs-buy]])
- Differentiate hard attributes (license, size, privacy - can't change) from soft (accuracy, latency you can improve).
- **Build vs buy** (host open-source vs commercial API) along seven axes: data privacy, data lineage/copyright, performance, functionality (logprobs, function calling, structured outputs, finetuning access), cost (API vs engineering), control/transparency, on-device.
- **Public benchmarks** filter out bad models but won't find the best for you; leaderboards aggregate an unclear small set (HF averages 6; HELM uses mean win rate), benchmarks saturate fast, correlation matters (don't include two perfectly-correlated benchmarks), and they're likely [[data-contamination|contaminated]].

### Data contamination ([[data-contamination]])
- Training on the test set: "Pretraining on the Test Set Is All You Need" (a 1M-param model beat larger ones by training on benchmarks). Mostly unintentional (web scraping), sometimes deliberate. Detect via n-gram overlap (accurate, costly) or perplexity (cheap, approximate); report clean-subset scores.

### Design your evaluation pipeline ([[evaluation-pipeline]])
1. **Evaluate all components** (per task, per turn, per intermediate output) - isolate where the system fails; task-based matters most.
2. **Create an evaluation guideline** - define good vs bad (a *correct* answer isn't always *good*), build scoring rubrics with examples validated by humans, and tie eval metrics to business metrics + a usefulness threshold.
3. **Define methods and data** - mix methods (cheap classifier on 100%, expensive judge on 1%), use logprobs when available, slice data (Simpson's paradox), size the eval set (OpenAI: ~100 for 10%, ~1000 for 3%; bootstrap to check reliability), evaluate the evaluation pipeline (temperature 0, reproducibility), and iterate with experiment tracking.

## Connections

- [[evaluation-criteria]], [[factual-consistency]], [[model-build-vs-buy]], [[evaluation-pipeline]] - concepts introduced here.
- [[eval-driven-development]] - Chip's "evaluation-driven development" is a second, deeper source for it.
- [[data-contamination]] / [[benchmark-sensitivity]] - deeply extended (detection methods, MCQ sensitivity, benchmark correlation/aggregation).
- [[three-eval-methods]] / [[llm-as-judge]] / [[pass-fail-over-score-evals]] - the methods this chapter assembles into a pipeline.
- [[retrieval-is-the-bottleneck]] / [[rag]] - factual consistency is the central RAG metric (Ch. 6 in the book).
- [[model-selection]] - build-vs-buy is the "which family/host" decision, complementary to temperament-based selection.
- Cross-wiki: this is the reference layer; hcho's own eval synthesis and Agentic RAG's harness live in their wikis.

## Source

- **Author:** Chip Huyen, from *AI Engineering: Building Applications with Foundation Models* (O'Reilly), Chapter 4
- **Title:** Evaluate AI Systems
- **Note:** the definitive practitioner eval reference; some model/benchmark specifics are of its 2024 moment, but the pipeline method is durable.
- **Raw:** [[Evaluate AI Systems]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
