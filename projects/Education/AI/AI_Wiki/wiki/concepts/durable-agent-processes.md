---
type: concept
tags: [system-design, agents, infrastructure, reliability]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Durable Agent Processes

From [[building-robust-apps-with-ai]]: an AI agent can't stop working just because the user closed the tab, refreshed, or left - so an agent product needs backend primitives that vibe-coded apps typically lack.

## The two primitives

- **Durable execution** - a process that survives the client disconnecting, with configurable retries and delays. Ross uses the Convex ([[convex]]) **Workflow** component; the raw equivalent would be hand-built on cloud primitives.
- **Queues / parallelism** - handle bursts (a Ticketmaster-style rush) and coordinate parallel tasks. Ross uses the Convex **Workpool** component (raw AWS equivalents: SQS for queues, RDS for the DB, EC2 for compute).

## Key points

- These are the failure points where "chat-stream" prototypes break under real use.
- On an everything-as-code platform they are copy-the-component-link installs rather than infrastructure projects ([[everything-as-code-abstractions]]).

## Synthesis

This is the reliability axis of [[engineering-trade-offs]] made concrete for agent products: long-running, user-independent work is the norm for agents, so durability and queuing are table stakes, not extras.
It connects to [[managed-agent-primitives]] and [[agent-observability]] in the production-agent-infra thread - the same "agents are long-lived processes that must be observable and recoverable" reality, seen from the app-architecture side.
For hcho's agent bets (Agentic RAG), this is a checklist item: where does the work continue if the user leaves, and what retries it?
