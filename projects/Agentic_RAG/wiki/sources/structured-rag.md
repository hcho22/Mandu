---
type: source
tags: [agentic-rag, structured-rag, text-to-sql, semantic-layer, evals]
date: 2026-06-15
title: "Structured RAG: a semantic-layer query planner for text-to-SQL"
author: "Agentic_RAG project docs"
url: "https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/structured-rag.md"
concepts: [text-to-sql-semantic-layer, agentic-tools-and-subagents]
---

# Structured RAG: a semantic-layer query planner for text-to-SQL

This project document explains why naive text-to-SQL is unsafe for business questions with ambiguous metrics, then describes Agentic RAG's semantic-layer approach: an LLM planner maps user questions to structured metric/dimension/filter plans, and a deterministic compiler turns validated plans into parameterized read-only SQL. It also reports a 30-question eval where the semantic path scores 100% against a 10% naive baseline.

## Key claims

- Naive text-to-SQL can produce runnable SQL while still choosing the wrong business definition, such as treating "revenue" as billed amount, expected collectible amount, net of refunds, or pre-tax merchandise revenue.
- The semantic layer in `backend/semantic_layer.yaml` defines entities, dimensions, metrics, joins, SQL fragments, grains, and synonyms so the LLM resolves business meaning before SQL generation.
- The agent uses two tools in order: `plan_query(question)` for LLM semantic resolution and `sql_search(plan)` for deterministic compilation and execution.
- `sql_search` requires a structured plan argument, so the agent cannot skip the planner and directly execute free-form SQL.
- The planner prompt renders the semantic layer and requires function-calling; validation downgrades hallucinated metrics to `no_match`.
- The compiler is a graph traversal over the join graph, not an LLM generator. It chooses a deterministic root, attaches joins, splices metric fragments and dimensions, binds filters as parameters, and runs through the existing SQL safety validator.
- Scalar metrics such as `net_revenue` and `repeat_customers` cannot be combined with dimensions; the compiler refuses invalid combinations instead of producing plausible but wrong SQL.
- The structured eval has 30 hand-authored questions across metric ambiguity, join/dimension, and time/filter categories. The naive baseline scores 10%, while the semantic path scores 100%.
- The system is explicit about scope: free-form row inspection, novel metrics, multi-step reasoning, and undefined aggregation grains return `no_match` or need semantic-layer expansion rather than prompt-engineering.

## Connections

- [[text-to-sql-semantic-layer]] - defines the semantic layer, two-step planner/compiler path, compiler constraints, and structured SQL eval.
- [[agentic-tools-and-subagents]] - shows how the agent's database tool surface is constrained by tool schemas and ordered calls, with deterministic execution after the LLM planning step.

## Source

- **Author:** Agentic_RAG project docs
- **Title:** Structured RAG: a semantic-layer query planner for text-to-SQL
- **URL:** https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/structured-rag.md
- **Raw:** `raw/structured-rag.md` (fetched from upstream GitHub and saved verbatim, immutable)
- **Ingested:** 2026-06-15
