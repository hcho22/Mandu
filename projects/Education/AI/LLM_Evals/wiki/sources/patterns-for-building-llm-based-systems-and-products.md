---
type: source
tags: [evals, metrics, llm-as-judge, benchmarks, rag, guardrails, hallucination, data-flywheel]
date: 2026-06-08
title: "Patterns for Building LLM-based Systems & Products"
author: "Eugene Yan"
url: "https://eugeneyan.com/writing/llm-patterns/"
concepts: [classification-metrics, rag-evaluation, hallucination-safety-redteam, llm-as-judge, llm-benchmarks-contamination, offline-vs-online-evals, ci-eval-gates-and-drift, error-analysis]
---

# Patterns for Building LLM-based Systems & Products

Eugene Yan surveys seven practical patterns for shipping LLM systems, organized from data-to-user and defensive-to-offensive: **evals, RAG, fine-tuning, caching, guardrails, defensive UX, and collecting user feedback**. For this evals wiki the load-bearing sections are evals (benchmarks, classical metrics, and LLM-as-judge), RAG (retrieval and embedding evaluation), guardrails (output validation and hallucination detection), and user feedback (the data flywheel). The recurring thesis is that off-the-shelf benchmarks and classical metrics are unreliable for real products, so teams should build task-specific evals and treat evaluation as the starting point of development.

## Key claims

- Evals (benchmark data + metrics) are how you measure system performance and catch regressions; without them you fly blind. "How important evals are" separates serious builders from those shipping "hot garbage."
- Notable benchmarks: **MMLU** (57 tasks), **HELM** (multi-metric, multi-domain), the **EleutherAI lm-evaluation-harness** (200 tasks), and **AlpacaEval** (win-rate vs a reference, validated against 20k human annotations).
- Benchmarks are **implementation-sensitive**: the same model scores differently across MMLU implementations (original vs HELM vs EleutherAI) because prompts, tokenization, and answer-scoring differ. Absolute scores and rankings are not comparable unless the implementation is identical.
- **Classical reference-based metrics** split into context-dependent and context-free. Matching-based: **BLEU** (precision-oriented, n-gram, machine translation), **ROUGE** (recall-oriented, summarization). Embedding-based: **BERTScore** (cosine similarity, handles synonyms) and **MoverScore** (soft many-to-one alignment).
- These classical metrics have three pitfalls: **poor correlation with human judgment**, **poor adaptability** to other tasks (n-gram overlap is meaningless for dialogue/abstractive summarization), and **poor reproducibility** (high variance, incorrect ROUGE implementations across 2,000 studies).
- For metric selection: classification-like tasks (toxicity, categorization, extractive QA) use standard **precision/recall/PR-AUC**; reference tasks (translation, extractive summarization) use BLEU/ROUGE or BERTScore/MoverScore; open-ended tasks lean on a strong LLM as judge.
- **LLM-as-judge** (reference-free): G-Eval (CoT + form-filling, Spearman 0.514 with humans), the Vicuna setup (GPT-4 single-answer grading agreed with humans 85%, above the 81% human-human agreement), and QLoRA (GPT-4 vs gpt-3.5-turbo, Spearman 0.55 with humans). LLM judgments are less noisy than humans but more biased; the bias is systematic so it can be mitigated.
- LLM-judge biases and mitigations: **position bias** (favors first response; swap order and require both orders to agree), **verbosity bias** (favors longer answers; match lengths), **self-enhancement bias** (favors own outputs - GPT-4 +10%, Claude-v1 +25%; don't judge with the same model family). Asking for a reference-based comparison instead of an absolute score reduces noise.
- The best eval is sometimes a human "vibe check" (Frankle/MosaicML: watching a fixed prompt's answer change over training was more informative than metrics). Build a set of task-specific evals (prompt, context, expected output) and run them on every change - "Eval-Driven Development."
- **RAG evaluation:** retrieval quality drives end-to-end quality - DPR (dense retrieval) beat BM25 (65.2% vs 42.9% top-5) and higher retrieval precision raised QA accuracy. Evaluate embedding models on the **MTEB leaderboard**; evaluate ANN indices on **recall vs exact, latency/throughput, memory footprint, and ease of adding items**. Hybrid (keyword + semantic) retrieval beats either alone.
- **Guardrails** validate output: single-value, syntactic (valid URLs, runnable SQL/code), semantic/factuality (cosine similarity to source), safety (moderation classifiers, banned-word lists), and input guardrails (block adversarial/NSFW prompts). NeMo-Guardrails and **SelfCheckGPT** detect hallucination by sampling multiple completions and flagging disagreement. Microsoft's Guidance steers output to a grammar by injecting structural tokens.
- **User feedback** (explicit thumbs-up/down, implicit accept/edit/ignore) builds the **data flywheel** that feeds evals, fine-tuning, and guardrails, and gives a direct measure of user satisfaction beyond offline evals. Production monitoring matters: one team found an LLM support bot caused 12x more losses in an A/B test.

## Connections

- [[classification-metrics]] - classification metrics (precision/recall/PR-AUC) for classification-like LLM tasks, plus the classical reference-based generation metrics (BLEU, ROUGE, BERTScore, MoverScore) and their three pitfalls.
- [[rag-evaluation]] - retrieval precision driving end-to-end accuracy, embedding evaluation (MTEB), ANN index evaluation factors, and the reference-based vs reference-free metric split.
- [[hallucination-safety-redteam]] - the guardrail taxonomy (syntactic/semantic/safety/input), self-consistency hallucination detection (SelfCheckGPT), and input guardrails against adversarial prompts.
- [[llm-as-judge]] - the canonical source for the three judge biases (position, verbosity, self-enhancement) and their mitigations, plus G-Eval/Vicuna/QLoRA evidence that LLM judges align with humans.
- [[llm-benchmarks-contamination]] - the major benchmark families and the implementation-sensitivity problem (same model, different scores).
- [[offline-vs-online-evals]] - Eval-Driven Development and task-specific evals as the starting point; user feedback and monitoring as the online signal.
- [[ci-eval-gates-and-drift]] - running task-specific evals on every change to catch regressions, plus the data flywheel and production monitoring.
- [[error-analysis]] - the human "vibe check" (MosaicML's fixed-prompt watching) and Eval-Driven Development, both of which start from a human reading real outputs.

## Source

- **Author:** Eugene Yan
- **Title:** Patterns for Building LLM-based Systems & Products
- **URL:** https://eugeneyan.com/writing/llm-patterns/
- **Published:** 2023-07-29
- **Raw:** `raw/Patterns for Building LLM-based Systems & Products.md` (clipped markdown copy, immutable)
- **Ingested:** 2026-06-08
