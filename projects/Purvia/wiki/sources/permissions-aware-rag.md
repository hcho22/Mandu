---
type: source
tags: [agentic-rag, permissions, retrieval, security, hnsw, evals]
date: 2026-06-15
title: "Permission-aware RAG: how Module 11 handles document sharing without breaking retrieval"
author: "Agentic_RAG project docs"
url: "https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/permissions-aware-rag.md"
concepts: [permissions-aware-retrieval, security-correctness-eval, retrieval-eval-suite, hybrid-retrieval-rrf]
---

# Permission-aware RAG: how Module 11 handles document sharing without breaking retrieval

This project document explains how Agentic RAG implements per-document sharing without relying on post-hoc filtering after retrieval. It covers the ACL data model, the SQL predicate inside `match_chunks`, granting-principal display precedence, the interaction between selective permission filters and pgvector HNSW, the correctness and scale evals, and the deliberate v0 scope cuts.

## Key claims

- Post-filtering top-k retrieval collapses recall for sparse permissions: if a viewer can see 5% of a corpus, top-10 retrieval returns only 0.5 visible chunks in expectation, which makes multi-hop retrieval unreliable.
- The fix is to push the permission predicate into SQL so the planner ranks among visible candidates from the start; the source calls this pre-filter retrieval.
- The ACL model uses `principals`, `principal_membership`, `chunk_acl`, and `profiles`; ownership remains additive and does not require owner rows in `chunk_acl`.
- `chunk_acl` is the sole source of truth for grants. Document-level sharing materializes per-chunk ACL rows, and re-chunking uses a snapshot-and-replay journal in document metadata to keep grants consistent.
- `match_chunks` restates the visibility predicate inside the function, even though RLS also applies, for self-documentation and defense in depth.
- `granting_principal_display` explains why a chunk is visible, with deterministic precedence: owner, direct user grant, then group grant.
- Selective permission filters can hurt HNSW recall because the graph walk may exhaust its `ef_search` budget before finding enough visible candidates; `match_chunks` accepts an optional `ef_search` override for benchmarking and tuning.
- At the current 10k benchmark size, Postgres chooses exact nearest-neighbor sorting over the filtered visible set instead of walking HNSW, so the permission-scale table is 1.000 across selectivities; a 100k+ benchmark is the natural follow-up.
- The correctness eval's load-bearing result is the security property: no-access viewers return zero gold chunks for vector, keyword, and hybrid modes under pre-filter and post-filter strategies.
- v0 deliberately defers per-chunk UI, autocomplete, bulk sharing, audit UI, role hierarchies, write-vs-read tiers, nested groups, and workspace scoping.

## Connections

- [[permissions-aware-retrieval]] - defines why permissions belong in the retrieval predicate, how ACLs are represented, and what pre-filter retrieval changes.
- [[security-correctness-eval]] - provides the no-access security table and explains why permission correctness is a hard property, not a soft RAG-quality score.
- [[retrieval-eval-suite]] - extends the eval apparatus with viewer setups, pre-vs-post filter strategies, non-regression checks, and a permission-scale benchmark.
- [[hybrid-retrieval-rrf]] - shows how vector, keyword, and hybrid modes are all evaluated under the permission filter, and where HNSW-specific behavior can matter.

## Source

- **Author:** Agentic_RAG project docs
- **Title:** Permission-aware RAG: how Module 11 handles document sharing without breaking retrieval
- **URL:** https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/permissions-aware-rag.md
- **Raw:** `raw/permissions-aware-rag.md` (fetched from upstream GitHub and saved verbatim, immutable)
- **Ingested:** 2026-06-15
