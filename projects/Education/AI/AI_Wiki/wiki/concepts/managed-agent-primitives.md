---
type: concept
tags: [agent-infrastructure, anthropic, claude-managed-agents, production]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Managed Agent Primitives

The four building blocks of Claude Managed Agents (CMA), from [[production-agent-with-cma]] - a useful mental model of production agent infrastructure regardless of vendor.

## The four blocks

| Block | What it is |
|---|---|
| **Agent** | A template: system prompt, skills, tools, MCP connections, and per-tool permissions. |
| **Environment** | A sandbox template: network access, pre-installed packages, self-hosted option. |
| **Session** | An ongoing user-Claude conversation (agent ID + environment ID; can attach repos/files). |
| **Events** | The session's stream: user events, agent events, session lifecycle, span events. |

## Why it matters

What you would otherwise build yourself: the agent loop and remote hosting, context management and state recovery, skills/MCP integration, durable event storage, a sandboxing fleet, and secure end-user auth.

## Synthesis

This is a concrete reference architecture for the abstract [[agents-as-cron-plus-markdown]] and [[agentic-engineering]] ideas: an Agent template is the "skill file," an Environment is the sandbox, and Events are the observable stream.
It also shows where the wiki's safety and eval concepts become platform features - [[credential-vaults]], per-tool permissions ([[capabilities-not-instructions]]), [[outcome-rubric-iteration]], and [[agent-observability]] are all primitives here.
