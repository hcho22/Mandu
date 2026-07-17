---
type: concept
tags: [agentic-rag, tools, text-to-sql, semantic-layer]
date: 2026-06-15
source-count: 1
status: seeded
component: "docs/structured-rag.md"
---

# Text-to-SQL Semantic Layer

A text-to-SQL path that separates semantic planning from deterministic SQL compilation so business metrics are explicit and reproducible.

## From the sources

[[structured-rag]] defines the semantic-layer approach:

- Naive text-to-SQL can produce runnable SQL while choosing the wrong business definition, especially for ambiguous terms like revenue.
- `backend/semantic_layer.yaml` defines entities, dimensions, metrics, joins, SQL fragments, grains, and synonyms. The LLM sees this semantic layer, not a raw schema dump.
- The agent uses `plan_query(question)` to map natural language onto a structured plan, then `sql_search(plan)` to compile and execute SQL deterministically.
- The `sql_search` tool schema requires a structured plan argument, so the agent cannot directly skip planning and execute free-form SQL.
- Planner validation rejects hallucinated metrics by downgrading invalid matches to `no_match`.
- The compiler traverses the join graph, chooses a deterministic root, attaches joins in stable order, splices metric fragments and dimensions, parameterizes filters, and runs the existing SQL safety validator.
- Scalar metrics such as `net_revenue` cannot be combined with dimensions; the compiler raises a tool error instead of emitting invalid-but-plausible SQL.
- The 30-question eval reports naive 10.0% vs semantic 100.0% accuracy across metric ambiguity, join/dimension, and time/filter categories.
- Out-of-scope questions reveal semantic-layer gaps rather than prompt gaps: novel metrics, raw-row inspection, multi-step reasoning, and undefined grains need new layer definitions or planner capabilities.

## Synthesis

The semantic layer makes text-to-SQL production-shaped by moving the LLM away from SQL generation and toward semantic choice. Once the model chooses `gross_revenue`, `net_revenue`, or another declared metric, the deterministic compiler owns correctness. This is less flashy than free-form SQL generation, but it is what makes the result auditable, evaluable, and safe enough to expose through [[agentic-tools-and-subagents]].
