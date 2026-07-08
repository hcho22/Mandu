---
type: concept
tags: [agents, context-engineering, agentic-engineering, parallelism]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Sub-Agents

Delegating work to child agents, primarily to protect the main session's context, from [[building-products-with-agents]].

## Key points

- **Models rarely self-delegate.** Today's harnesses do not proactively spawn sub-agents, except built-ins like Claude Code's explore agent; usually you must prompt for them explicitly.
- **The real reason to use them is context management:** carve out heavy, exploratory work that would not be meaningful to the main session, and return only the conclusion - keeping the main context small.
- Also good for many isolated tasks in parallel (e.g. spin up 10 sub-agents for 10 independent experiments; a ~200x8 benchmark run).

## Sub-agents vs agent teams

[[every-claude-feature-ranked]] draws the key contrast: sub-agents work in parallel and only report to the main session, whereas [[agent-teams]] talk to each other and debate. Parallel throughput vs deliberation.

## Synthesis

Sub-agents are the practical defense against [[context-rot]] and a building block of [[get-out-of-the-loop]] scale (many parallel workstreams).
They are part of [[agentic-engineering]]'s "compound engineering" pillar: structuring work across agents so the main thread stays clean and the human supervises breadth rather than depth.
