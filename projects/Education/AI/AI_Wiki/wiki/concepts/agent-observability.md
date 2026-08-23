---
type: concept
tags: [observability, agents, debugging, evals]
status: established
source-count: 4
last-updated: 2026-08-01
---

# Agent Observability

Live visibility into what an agent is doing, from [[production-agent-with-cma]] and [[building-robust-apps-with-ai]]: the CMA developer console lets you drill into events, watch tool-call timing, see multi-agent coordination, and track span events.

## Key points

- Drill into individual events (e.g. a web search's inputs and outputs) to debug behavior.
- Monitor how long tool calls take to find slow operations.
- **Span events** mark the start and end of known long-running operations so users do not think the system is stuck.
- Presented as central to the workflow, not an afterthought - you live-debug agents the way you would a running service.
- **Wire it early, at the app level too** ([[building-robust-apps-with-ai]]): Ross treats Sentry (error logging) + PostHog (analytics) as day-one [[system-design]], not a later add - "whenever an error happens, I need to track it." Daytona-hosted agents that self-heal are only debuggable because the traces exist.

## "Observability is the hard part, not the automation" (2026-08-01)

[[running-teams-of-ai-agents]] promotes this from a debugging convenience to **the actual engineering work** of running scheduled agents.

[[ryan-carson]]'s framing: writing the automation is the easy half.
The real questions are *how do you know it failed? did the agent silently fail and self-fix? what happened to the PR it opened?*
His advice is to work this out **with** the agent - ask it "I understand it runs Mon/Wed/Fri and triggers a triage session on failure; how do I find out about it?" - and the answer chain (post to Slack → connect the MCP → which channel do I watch) is the machinery you have to build.

Two design patterns from the same source:

- **Compress and route, don't judge** ([[production-watchdog]]): an agent reads every event for paid customers and produces a daily digest, with **each line linking back to the live production UI**. Humans are extraordinarily good at spotting "that's weird" at a glance, so the agent's job is to make that glance possible.
- **The audit trail is a trust artifact, not a debugging one** ([[fde-in-30-days]]). Week 1 of the FDE roadmap requires logging every prompt, response, tool call, and error, and the reason given is commercial: **"If you can't show the client what the agent is doing, they will never trust you."**

Related but distinct: [[agentic-full-stack-build]] deliberately *hides* tool calls in a "calm mode," on the grounds that with current models the noise is not worth reading.
That is not a contradiction - it is the difference between watching an agent work in real time (low value now) and being able to reconstruct what it did afterward (higher value than ever).

## Synthesis

Observability is [[looking-at-your-data]] applied to agent execution: the same "remove all friction from inspecting what happened" principle, now over traces, tool calls, and multi-agent chatter.
It is the runtime complement to [[evals]] (evals grade outputs; observability explains behavior) and directly relevant to hcho's Agentic RAG stack, which already uses LangSmith for observability.
Expect the deeper evals sources to connect observability to production monitoring and regression detection.
