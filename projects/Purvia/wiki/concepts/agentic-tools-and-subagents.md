---
type: concept
tags: [agentic-rag, agents, tools, subagents]
date: 2026-06-15
source-count: 1
status: seeded
component: "chat loop tools (query_database, web_search, spawn_document_agent)"
---

# Agentic Tools and Subagents

The tool-using chat loop and delegated document agents that extend retrieval with database queries, web fallback, and isolated subtask context.

## From the sources

[[structured-rag]] informs the database-tool side of the agent loop:

- The structured data path is exposed as ordered tool use: first `plan_query(question)`, then `sql_search(plan)`.
- Tool schemas enforce the flow. `sql_search` requires a structured `plan`, so the agent cannot call the SQL execution step without planner output.
- The LLM's job is semantic resolution rather than SQL generation. It chooses declared metrics, dimensions, filters, and time grains from the semantic layer.
- The deterministic compiler and SQL safety validator execute after the LLM planning step, which keeps the tool result reproducible and inspectable.
- When the semantic layer cannot answer, the planner returns `no_match` with a suggested fallback such as file search or web search, keeping out-of-scope questions from becoming invented SQL.

## Synthesis

The agent tool design matters because constraints live in the tool boundary, not just in prompts. For structured data, `plan_query` and `sql_search` make the safe path the only expressible path. That same pattern is the broader agentic design lesson: give the model useful choices, but make unsafe or underspecified actions impossible to call.
