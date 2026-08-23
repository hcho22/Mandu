---
type: concept
tags: [rag, retrieval, debugging, evals, quality]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Retrieval Is the Bottleneck

From [[zero-to-hireable-ai-engineer]]: most RAG failures are retrieval failures, not model failures - when a [[retrieval-augmented-generation|RAG]] system gives a bad answer, check what got retrieved before you blame the model.

## The common failure modes

- The question and the relevant chunk don't match in vector-space even though the info is there - fix by rewriting the query.
- The relevant info is split across two chunks - fix with more chunk overlap.
- The right chunk exists but didn't make the top results - fix by retrieving more, then reranking down.

## Key points

- This one habit - inspect the retrieved chunks first - saves enormous frustration.
- Grounding with citations makes this debugging far easier, because you can see which source each claim came from.

## Synthesis

This is the validation principle at the heart of the [[rag]] area: measure the intermediate artifact (what retrieval returned), not just the final output.
It is [[looking-at-your-data]] applied to RAG and the reason a RAG system needs an eval set focused on retrieval quality ([[evals]], Ragas) rather than only end-to-end answer grading.
For hcho this is directly his edge and the spine of Agentic RAG's eval harness: treat retrieval as the unit under test, build a labeled question/chunk set, and gate changes on it.
