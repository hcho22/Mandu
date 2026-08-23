---
type: concept
tags: [rag, retrieval, search, embeddings]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Hybrid Retrieval

From [[llm-patterns]]: combine traditional keyword search (BM25) with embedding-based semantic search, because each covers the other's failure modes.
Eugene Yan found hybrid beat either alone in his Obsidian-Copilot.

## Why hybrid

- **Semantic search alone fails on** exact tokens: a person/object name, an acronym or phrase (RAG, RLHF), or an ID (`gpt-3.5-turbo`).
- **Keyword search alone fails on** meaning: it models word frequencies only, so it misses synonyms and hypernyms.
- **Metadata** (from the keyword index) adds date/category filters and downstream ranking signals (citations, sales volume).

## Synthesis

Hybrid retrieval is a concrete refinement in the [[rag]] area and a direct lever on [[retrieval-is-the-bottleneck]]: many "the model got it wrong" failures are really "semantic search missed the exact term," fixed by adding a keyword leg.
It generalizes to a validation heuristic - don't trust one retrieval signal any more than one eval metric; ensemble complementary methods and measure the combination.
For hcho's flagship (whose stack uses pgvector) this is the argument for pairing vector search with a lexical index rather than going embedding-only.
