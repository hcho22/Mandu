---
type: concept
tags: [agentic-rag, retrieval, permissions, security]
date: 2026-06-15
source-count: 1
status: seeded
component: "docs/permissions-aware-rag.md"
---

# Permissions-Aware Retrieval

Retrieval that applies document and chunk ACLs inside candidate selection so ranking happens only over chunks visible to the viewer.

## From the sources

[[permissions-aware-rag]] defines the problem and the v0 retrieval design:

- Post-filter retrieval fails under sparse permissions. If a viewer can see 5% of a corpus, top-10 retrieval returns only 0.5 visible chunks in expectation, so multi-hop questions often return nothing useful.
- Pre-filter retrieval pushes the permission predicate into SQL so the planner chooses among visible chunks from the start.
- The ACL model uses `principals`, `principal_membership`, `chunk_acl`, and `profiles`. Ownership remains additive through `chunks.user_id`, while `chunk_acl` grants access to additional users or groups.
- `chunk_acl` is the sole source of truth for grants. Document-level sharing writes one row per chunk, and re-chunking uses snapshot-and-replay metadata so grants survive chunk replacement.
- `match_chunks` restates the visibility rule inside the function, even though RLS applies, to make the hot retrieval predicate explicit and preserve defense in depth.
- Granting-principal display is deterministic: owner wins, then direct user grant, then group grant, with stable tie-breaking for group grants.
- The design deliberately stores grants per chunk to keep the retrieval predicate shallower; it chooses storage cost over an extra read-time join.

## Synthesis

The core insight is that permissions are part of retrieval quality, not just an authorization wrapper around retrieval. If the retriever ranks the wrong universe and filters afterward, sparse ACLs become a recall problem. By moving ACLs into the SQL predicate, Agentic RAG makes visibility and ranking a single operation, then uses [[security-correctness-eval]] and [[retrieval-eval-suite]] to prove the security property and watch the quality trade-off.
