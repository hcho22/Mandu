---
type: concept
tags: [infrastructure, managed-agents, sandboxes, durable-execution, sessions, observability]
date: 2026-07-03
source-count: 3
status: seeded
---

# Production Agent Infrastructure

The runtime plumbing needed to run agents in production - sessions and event streams, sandboxed compute, durable execution, credential handling, and observability - whether provided as a managed service or assembled from cloud building blocks.

## From the sources

[[claude-managed-agents]] is the managed-service view:

- Four primitives: Agent (system prompt + skills + tools + MCP + per-tool permissions), Environment (sandbox behavior), Session (an ongoing user-Claude conversation started from an agent + environment ID), and Events (sessions are SSE event streams).
- Self-hosted sandboxes bring your own containers (Cloudflare/Vercel/Modal/your fleet) so private data stays in your perimeter; MCP tunnels reach private MCP servers without exposing them; credential vaults inject tokens without Claude seeing them; agents are versioned and rollbackable.
- Span events bracket long operations so users do not think the system is stuck; the console gives live observability. The closing argument lists what you would otherwise build yourself: an agent loop, remote hosting, context management and recovery, durable event storage, a sandbox fleet, and secure end-user auth.

[[building-robust-applications-with-ai]] shows the assembled-from-components view:

- An AI agent cannot stop when the user closes the tab, so Convex provides durable processes (Workflow, with retries/delays) and queues/parallel tasks (Workpool) out of the box; each agent also gets its own sandbox computer with a browser (Daytona) that self-heals.
- Observability is set up early (Sentry + PostHog) so you know exactly what happened when a build or agent fails.

[[one-person-company-with-ai-agents]] runs engineering entirely in the cloud:

- Devin spins up a configured production VM per task (no local dev), eliminating environment headaches and giving reliable in-cloud browser testing.

## Synthesis

Once an agent leaves the demo, a common set of runtime concerns appears no matter who is building, and the two framings here - buy it managed (CMA) or assemble it from abstraction layers (Convex/Daytona/Devin) - solve the same list. **Durable execution** is the load-bearing one: an agent must keep running when the user closes the tab, which classic request/response backends do not do, so you need durable processes with retries (Convex Workflow) or a managed session/event stream (CMA). **Sandboxed, disposable compute** per agent (Daytona, CMA environments, Devin VMs) gives each run an isolated computer that can self-heal, which is also a safety boundary tied to [[agent-permissions-and-safety]] (self-hosted sandboxes and credential vaults keep private data and secrets out of reach). **Sessions as event streams** make the run inspectable, which is why observability recurs everywhere - CMA's console, Sentry/PostHog - and connects directly to production tracing like [[observability-langsmith]] in the Agentic RAG wiki. The CMA "what you'd otherwise build" list is the clearest statement of the boundary between prototype and product: an agent loop is easy, but remote hosting, durable state and recovery, a reacting sandbox fleet, and secure end-user auth are not, and they are exactly where [[agentic-system-design]] earns its keep. The interview point: shipping an agent is a systems problem - durability, isolation, and observability - not a prompting problem.
