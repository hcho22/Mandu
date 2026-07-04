---
type: source
tags: [managed-agents, anthropic, sandboxes, multi-agent, credentials, observability]
date: 2026-07-03
title: "Build a Production-Ready Agent with Claude Managed Agents"
author: "Code with Claude workshop (Anthropic)"
url: ""
concepts: [production-agent-infrastructure, agent-skills, agent-permissions-and-safety, agent-memory, sub-agents-and-multi-agent, evals-for-agents]
---

# Build a Production-Ready Agent with Claude Managed Agents

A hands-on Code with Claude workshop introducing Claude Managed Agents (CMA): a set of API endpoints (usable with any API key) that hand you production-ready, scalable agent infrastructure so you pick the primitives you need and build your product on top.
It live-builds a contrived M&A deal-analysis app, then tours newer capabilities (self-hosted sandboxes, MCP tunnels, multi-agent, credential vaults, memory stores) and the developer-console observability views.

## Key claims

- CMA has four core primitives: Agent (a template of system prompt, skills, tools, MCP servers, and per-tool permissions), Environment (sandbox behavior - network access, packages, self-hosted), Session (an ongoing user-Claude conversation started from an agent ID + environment ID), and Events (sessions are SSE event streams).
- Per-tool permission controls: a file-read tool can auto-execute while running bash or a database MCP call requires explicit end-user approval; some agents should be denied web access entirely so they cannot be prompt-injected.
- Outcomes let you pass Claude a file/blob that acts as a spec/rubric; Claude does a first pass, then iterates and checks its own work against the rubric repeatedly until it satisfies it.
- Events are typed: user events (messages, interrupts, tool results, confirmations, outcomes), agent events (messages, compaction, tool executions, multi-agent coordination), session lifecycle events, and span events that bracket long operations so users do not think the system is stuck.
- Self-hosted sandboxes let you bring your own containers (Cloudflare, Vercel, Modal, or your own fleet) so private data never leaves your perimeter; MCP tunnels let Claude reach private MCP servers inside your network without exposing them.
- Credential vaults store MCP auth tokens with Anthropic and inject them without Claude ever seeing them (they never enter its context window). Memory stores let Claude read/write persistent memory across sessions, and you can read and manually edit what it remembered.
- The harder streaming endpoint is handed to Claude Code, which ships with the Claude API skill that makes it "really good" at the Managed Agents APIs - "Claude can help you build your own Claude." Agents are versioned and can be rolled back.
- In the live run Claude spawns four sub-agents, each with its own context window, coordinating and passing updates; the console shows each agent as a line with drill-down into events and tool-call timing, ending with an outcome evaluation against the rubric.

## Connections

- [[production-agent-infrastructure]] - the CMA primitives (agents/environments/sessions/events), sandboxes, MCP tunnels, versioning, and the "what you'd otherwise build" argument.
- [[agent-skills]] - agents are configured with skills, and Claude Code's built-in Claude API skill drives CMA integration.
- [[agent-permissions-and-safety]] - per-tool permissions, denying web access to prevent injection, and credential vaults that keep tokens out of context.
- [[agent-memory]] - persistent memory stores that are readable and manually editable across sessions.
- [[sub-agents-and-multi-agent]] - multi-agent coordination events and the live four-sub-agent fan-out with per-agent context windows.
- [[evals-for-agents]] - outcomes as a rubric the agent iterates against, and console observability for live debugging.

## Source

- **Author / channel:** Code with Claude workshop (Anthropic)
- **Title:** Build a Production-Ready Agent with Claude Managed Agents
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Claude_Managed_Agents_Production_Agent_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
