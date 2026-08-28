# Phase 1 research checkpoint - fetched external evidence

All external claims below cite the URL fetched on 2026-08-27.

## Landscape

- **Onyx (formerly Danswer)**, the leading open-source enterprise-search RAG: "Onyx's context retrieval respects user level permissions which is only configurable via the Enterprise Edition."
  Fetched: https://docs.onyx.app/overview/core_features/internal_search
  Consequence: the flagship OSS alternative paywalls exactly the property Purvia ships MIT.
  Onyx's job is different (40+ SaaS connectors mirroring source ACLs for internal search); Purvia's job is the retrieval predicate inside a product you are building.
- **Supabase's official "RAG with Permissions" guide** provides RLS + pgvector schema patterns but omits: evaluation/testing frameworks for access-control correctness, tenant isolation beyond basic RLS, permission-management UI, and warns "RLS is latency-sensitive."
  Fetched: https://supabase.com/docs/guides/ai/rag-with-permissions
  Consequence: the DIY path ends where Purvia begins - the guide hands you the predicate pattern, not the proof harness, the share UI, the workspace boundary, or the escalation pipeline.
- **Pinecone** teaches RAG access control via an external permissions service (SpiceDB), pre- and post-retrieval: https://www.pinecone.io/learn/rag-access-control/ (search result; pattern-level, not a kit).
- **Truto (2026 enterprise architecture guide)**: "Document-level permission enforcement is the single feature that will get flagged in an enterprise security review." https://truto.one/blog/how-to-maintain-document-level-rbac-in-enterprise-rag-pipelines/ (search result).

## Framework-RAG complaints (why "readable raw-SDK code" resonates)

- GitHub community discussion: "Is LangChain becoming too complex/bloated for simple RAG applications?" - abstraction overhead, debugging pain, dependency churn. https://github.com/orgs/community/discussions/182015
- Comparison pieces summarize the folk wisdom: chains-within-chains debugging, breaking changes, "over-abstraction ... feels like magic"; plain SDK calls are easier to debug. https://www.morphllm.com/comparisons/langchain-vs-llamaindex , https://www.statsig.com/perspectives/llamaindex-vs-langchain-rag
- Purvia's hook into this: `README.md:10` - "Raw OpenAI SDK + Pydantic (no LLM frameworks)".

## Kit pricing comps (one-time, engineer-buyer)

| Kit | Model | Price (fetched) |
|---|---|---|
| ShipFast | one-time, closed | $199 Starter / $249 All-in / $299 bundle - https://shipfa.st/ |
| SaaS Pegasus | **open-core**: free OSS core + paid | $449 Professional / $649 Unlimited one-time - https://www.saaspegasus.com/pricing/ |
| Makerkit / Supastarter | one-time | $249-999 / $349+ (search-level only, not fetched; do not cite in customer copy) |

Consequence: the captain's $149-249 band sits at the accessible end of the verified market; SaaS Pegasus proves the open-core + one-time-paid-tier shape exists and clears $449.
