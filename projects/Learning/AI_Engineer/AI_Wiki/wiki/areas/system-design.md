---
type: area
tags: [system-design, architecture, production, agents, infrastructure]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# System Design (in the AI era)

The durable hub for designing robust, production-ready applications when AI writes much of the code.
The premise ([[building-robust-apps-with-ai]]): AI makes prototypes trivial, but apps break at their first ~10 real users unless someone deliberately designed the system.
The developer's edge over a non-developer using the same AI is exactly this: knowing how to architect for scale, reliability, and failure.

## The governing lens

[[engineering-trade-offs]]: no perfect system exists, so every choice is a conscious balance of **scalability, reliability, performance, and cost**.
Design is choosing which trade-offs you will accept, not chasing a mythical best stack.

## Concepts in this area

- [[engineering-trade-offs]] - the four axes every design balances.
- [[everything-as-code-abstractions]] - abstraction layers agents can operate; why the modern stack is agent-friendly.
- [[monorepo-for-agent-context]] - one repo so the agent (and human) sees the whole system.
- [[client-never-touches-the-database]] - the client -> server -> DB security rule.
- [[durable-agent-processes]] - durable execution + queues, because an agent can't stop when the tab closes.

## Practices this area folds in (not yet standalone pages)

- **Requirements first:** enumerate hard requirements (auth model, billing model, hosting) before picking tools; the requirements drive the stack.
- **Services segmentation:** carve out code that touches one surface area, does one job, and has no deep foothold (Pluto's iMessage and Inference/Payments services).
- **Observability early:** wire error/analytics logging ([[agent-observability]]: Sentry + PostHog) from day one.
- **Automated review gate:** Greptile-style confidence-scored PR review ([[adversarial-code-review]]).

## Where this connects

- [[agentic-engineering]] - abstraction layers are the substrate that makes agents able to build production systems.
- [[agent-observability]] and [[managed-agent-primitives]] - the production-agent-infra thread (Daytona sandboxes, durable processes) overlaps here.
- Cross-wiki: general architecture craft lives here; the Agentic RAG wiki owns that product's specific stack decisions.

## Sources

- [[building-robust-apps-with-ai]] - Ross (Hey Fabrica): agentic system design taught through the Pluto architecture.

## Synthesis

One source in, the throughline is that **system design is the durable, non-commoditized skill under "AI can build anything."**
The abstraction layers keep rising (metal -> cloud -> everything-as-code platforms), which is what lets agents operate infrastructure, but it does not remove the need for judgment about trade-offs, security boundaries, and failure modes - it concentrates the remaining value there.
That is squarely hcho's edge: designing for reliability and failure is validation thinking applied to architecture, and it is what separates a shippable product from a demo.
