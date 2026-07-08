---
type: concept
tags: [observability, agents, debugging, evals]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Agent Observability

Live visibility into what an agent is doing, from [[production-agent-with-cma]] and [[building-robust-apps-with-ai]]: the CMA developer console lets you drill into events, watch tool-call timing, see multi-agent coordination, and track span events.

## Key points

- Drill into individual events (e.g. a web search's inputs and outputs) to debug behavior.
- Monitor how long tool calls take to find slow operations.
- **Span events** mark the start and end of known long-running operations so users do not think the system is stuck.
- Presented as central to the workflow, not an afterthought - you live-debug agents the way you would a running service.
- **Wire it early, at the app level too** ([[building-robust-apps-with-ai]]): Ross treats Sentry (error logging) + PostHog (analytics) as day-one [[system-design]], not a later add - "whenever an error happens, I need to track it." Daytona-hosted agents that self-heal are only debuggable because the traces exist.

## Synthesis

Observability is [[looking-at-your-data]] applied to agent execution: the same "remove all friction from inspecting what happened" principle, now over traces, tool calls, and multi-agent chatter.
It is the runtime complement to [[evals]] (evals grade outputs; observability explains behavior) and directly relevant to hcho's Agentic RAG stack, which already uses LangSmith for observability.
Expect the deeper evals sources to connect observability to production monitoring and regression detection.
