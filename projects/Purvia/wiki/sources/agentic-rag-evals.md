---
type: source
tags: [agentic-rag, evals, retrieval, ci, ragas]
date: 2026-06-15
title: "Retrieval Evals: measuring vector, keyword, and hybrid search"
author: "Agentic_RAG project docs"
url: "https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/evals.md"
concepts: [hybrid-retrieval-rrf, retrieval-eval-suite, ci-eval-gating, ragas-metrics, security-correctness-eval]
---

# Retrieval Evals: measuring vector, keyword, and hybrid search

This project document explains the Agentic RAG retrieval evaluation suite: why retrieval quality needs numeric measurement, how the fixed corpus and 50-question golden set are constructed, which retrieval metrics are reported, how optional generation and RAGAS scoring fit in, and what a CI-caught chunk-size regression looked like. It frames the suite as infrastructure for making vector, keyword, hybrid, reranker, and future vector-store changes falsifiable.

## Key claims

- The `search_documents` tool exposes vector-only, keyword-only, and hybrid retrieval, with hybrid search fusing vector and keyword candidates through Reciprocal Rank Fusion; the eval exists so claims about those modes are measured rather than asserted.
- The corpus is a fixed set of 7 markdown policy documents seeded through the production chunking and embedding path, producing stable chunk IDs that make golden references reproducible across CI cold starts.
- The golden set contains 50 hand-curated questions across `single_chunk`, `multi_hop`, `adversarial`, and `paraphrase` categories so the suite can test basic plumbing, multi-chunk recall, lexical-vs-semantic confusion, and synonym/OOV behavior.
- Retrieval quality is measured with `recall@k`, MRR, and nDCG@5; the metrics separate "is a gold chunk present" from "how high does the first gold chunk rank" and "are gold chunks ranked ahead of noise."
- Retrieval-only runs do not measure generated-answer correctness, tool-routing quality, latency, cost, or robustness to corpus drift; optional generation adds faithfulness and helpfulness scoring with a Claude judge.
- RAGAS is added as a standardized vocabulary layer for Faithfulness, Answer Relevancy, Context Precision, and Context Recall, but only for selected hybrid pre-filter cells and alongside the custom cross-family Claude judge.
- RAGAS score gates use fixed absolute drops and rolling 4-week medians, while red alerts for faithfulness/relevancy require corroboration from the independent Claude judge; this separates score drift from single-judge noise.
- A throwaway PR that changed chunk size from 500 to 100 demonstrated the CI loop: vector and hybrid `recall@5` dropped from 0.860 to 0.350, with the largest category drops on multi-hop and paraphrase questions.
- The document is explicit about limitations: the golden set is small, LLM-drafted questions may inflate scores, the seeded corpus may not generalize, gold labels have no second-rater calibration, and embedding model versions are not strictly pinned.

## Connections

- [[hybrid-retrieval-rrf]] - defines the evaluated retrieval modes and makes hybrid-vs-vector-vs-keyword quality an empirical comparison rather than an architectural claim.
- [[retrieval-eval-suite]] - specifies the corpus, golden set, categories, metrics, runner output, and limitations.
- [[ci-eval-gating]] - shows how PR and baseline runs turn the suite into a regression gate, including the chunk-size regression demonstration.
- [[ragas-metrics]] - documents why RAGAS is added, which cells it scores, how thresholds work, and how it relates to the custom Claude judge.
- [[security-correctness-eval]] - draws a boundary between graded answer-quality metrics and hard permission/security cells such as `no_access`, which the source treats as separately characterized by the security table.

## Source

- **Author:** Agentic_RAG project docs
- **Title:** Retrieval Evals: measuring vector, keyword, and hybrid search
- **URL:** https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/evals.md
- **Raw:** `raw/agentic-rag-evals.md` (fetched from upstream GitHub and saved verbatim, immutable)
- **Ingested:** 2026-06-15
