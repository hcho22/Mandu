---
type: concept
tags: [agentic-web, agents, mcp, interfaces, web]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Agent-Readable Website

From [[startups-for-agents]]: to sell to agents you must be machine-usable, so the homepage's job changes from persuading a human to exposing capability to a program.

## Human-readable vs agent-readable

- **Human homepage:** brand, video, copy, social proof, a demo, pricing.
- **Agent-readable homepage:** structured docs, schemas, policies, examples, endpoints.
- In practice "agent-readable" means: **MCP tools, SDKs, OAuth, checkout, a sandbox, and receipts**, plus a dedicated agent entry point (e.g. `yourwebsite.com/agents`).

## Key point

If an agent can't understand what you do and can't safely take an action with you, you are effectively **invisible to that agent** - the agent-web equivalent of not ranking in search.

## Synthesis

This is the interface layer of the [[agentic-web]] and the concrete output of [[aeo-answer-engine-optimization]]: being discoverable is necessary, being *actionable* (safe tool calls, checkout, sandbox) is what actually converts an agent.
It connects the area to [[system-design]] (exposing MCP tools/SDKs/OAuth is an architecture decision, not a marketing one) and to [[everything-as-code-abstractions]] (agents act through code-shaped interfaces, not rendered pages).
The reframe worth keeping: "marketing" work here is really engineering a safe, structured capability surface - builder-favorable, and validation-relevant (the sandbox and receipts are test and audit surfaces).
