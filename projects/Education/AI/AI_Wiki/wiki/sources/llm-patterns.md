---
type: source
title: "Patterns for Building LLM-based Systems & Products"
source-type: blog
author: "Eugene Yan"
url: "https://eugeneyan.com/writing/llm-patterns/"
date-ingested: 2026-07-08
date-created: 2023-07-29
tags: [production-llm, evals, rag, fine-tuning, caching, guardrails, defensive-ux, feedback]
---

# Patterns for Building LLM-based Systems & Products

Eugene Yan's ([[eugene-yan]]) landmark synthesis of seven practical patterns for turning LLMs into products, organized on two axes: improving performance vs reducing cost/risk, and closer to the data vs closer to the user.
The seven: Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, and Collect user feedback.
The framing quote (Karpathy) sets the theme: demos are easy, products are hard.

## Key claims

### Evals ([[evals]])
- Evals are the differentiator between "rushing out hot garbage" and seriously building; without them you fly blind. Treat it as **Eval-Driven Development** ([[eval-driven-development]]): collect task-specific evals first, then let them guide prompting, model choice, and fine-tuning.
- **[[reference-based-metrics]]** (BLEU, ROUGE, BERTScore, MoverScore) have three pitfalls: poor correlation with human judgment, poor adaptability across tasks, and poor reproducibility.
- **[[benchmark-sensitivity]]:** the same model scores differently across MMLU implementations (HELM vs EleutherAI vs original) because prompts and scoring differ; scores aren't comparable unless the implementation is identical.
- **[[llm-as-judge]]** (G-Eval, Vicuna, QLoRA) can match human agreement, but has position, verbosity, and self-enhancement biases with concrete mitigations; prefer comparison over direct scoring; don't grade with the same model family.

### RAG ([[rag]])
- RAG grounds the model on retrieved context to cut hallucination, and it's cheaper to update an index than to re-train. History: DPR, FiD, RETRO, HyDE.
- **[[embeddings]]:** text as fixed-size vectors; MTEB leaderboard; E5/Instructor/GTE beat `text-embedding-ada-002` for retrieval; ANN indices (LSH, FAISS, HNSW, ScaNN) trade a little recall for big speed.
- **[[hybrid-retrieval]]:** combine keyword search (BM25) with semantic search - each covers the other's failures (names, acronyms, IDs vs synonyms); use metadata to filter and rank.

### Production patterns ([[production-llm]])
- **[[fine-tuning]]:** continued pre-training / instruction / single-task / RLHF; LoRA and QLoRA as efficient starts; the alignment tax; reach for it last (after prompting and retrieval).
- **[[semantic-caching]]:** cache responses keyed on input embedding to cut latency and cost, but cache *safely* (item IDs, constrained inputs, precompute) rather than trusting semantic similarity alone.
- **[[guardrails]]:** validate output (structural via Guidance, syntactic, safety, semantic/factuality) and input; use another LLM for nuanced checks (NeMo, SelfCheckGPT).
- **[[defensive-ux]]:** anticipate model errors - set expectations, enable efficient dismissal, provide attribution/citations, anchor on familiar UI (Microsoft/Google/Apple human-AI guidelines).
- **[[data-flywheel]]:** collect explicit and implicit user feedback; data (evals, demonstrations, preferences) is one of the few LLM moats.
- Also: cascade (decompose tasks), monitoring (one anecdote: an LLM support bot lost 12x more than the human team in an A/B test).

## Connections

- [[production-llm]] area - this source opens it: [[fine-tuning]], [[guardrails]], [[semantic-caching]], [[defensive-ux]], [[data-flywheel]].
- [[evals]] area - deepened: [[eval-driven-development]], [[reference-based-metrics]], [[benchmark-sensitivity]]; extended [[llm-as-judge]] (biases, G-Eval, comparison-over-scoring).
- [[rag]] area - deepened: [[embeddings]], [[hybrid-retrieval]]; corroborates [[retrieval-is-the-bottleneck]] (DPR: higher retrieval precision -> higher end-to-end accuracy).
- [[single-call-workflow-or-agent]] / [[retrieval-augmented-generation]] - the prompt -> retrieve -> fine-tune ladder (fine-tune last) is shared with [[zero-to-hireable-ai-engineer]].
- [[ml-metrics]] ([[precision-recall]]) - the classification-metric foundations under eval choice.
- [[eugene-yan]] - author entity.
- This is the canonical broad reference; Purvia-specific decisions remain in that project's wiki.

## Source

- **Author:** Eugene Yan (Ziyou Yan), eugeneyan.com
- **Title:** Patterns for Building LLM-based Systems & Products
- **Published:** 2023-07-29 · **URL:** https://eugeneyan.com/writing/llm-patterns/
- **Note:** dated (2023); model/tooling specifics (ada-002, Falcon, MTEB rankings) are of their time, but the patterns are durable. Read alongside newer eval sources for current practice.
- **Raw:** [[Patterns for Building LLM-based Systems & Products]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
