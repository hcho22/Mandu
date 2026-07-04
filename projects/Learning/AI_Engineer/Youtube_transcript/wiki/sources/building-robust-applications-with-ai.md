---
type: source
tags: [system-design, architecture, convex, monorepo, observability, trade-offs]
date: 2026-07-03
title: "Building Robust Applications with AI (Pluto System Design)"
author: "Ross (Hey Fabrica agency)"
url: ""
concepts: [agentic-system-design, production-agent-infrastructure]
---

# Building Robust Applications with AI (Pluto System Design)

A tutorial that uses the real architecture of Ross's agent product Pluto to show how to design a robust, production-ready system in the age of AI, since most "vibe-coded" apps break the moment they get real users.
The through-line is that modern "everything-as-code" abstraction layers hide hard infrastructure and, because they are code, AI agents can operate them well.

## Key claims

- System design (planning architecture, components, interfaces, and data flow to meet requirements) is why a developer using AI ships a more robust app than a non-developer using AI; without it, an app crashes at ~10 users.
- Engineering is all about trade-offs across four axes - scalability, reliability, performance, and cost - and no system, stack, or provider is perfect; you consciously choose which trade-offs to accept.
- Infrastructure evolved by abstraction: own metal -> cloud providers (AWS/GCP/Azure/Cloudflare) -> higher abstraction layers (Convex, Vercel, Supabase, Neon, PlanetScale) with excellent developer and agent experience because they are everything-as-code.
- Start every app as a monorepo (Turborepo) holding all clients, a unified backend, services, and a shared component library, so the AI agent has full-codebase context instead of fragmented, separated contexts.
- Never let the client talk to the database directly (client -> server -> DB -> server -> client), or an API key can be read from the network tab; this is his objection to the common Supabase-from-the-client + RLS pattern.
- Convex is Pluto's "control plane": a merged backend + database (queries read, mutations write, actions call external services), real-time, everything-as-code, with components like Workflow (durable processes that survive tab close) and Workpool (queues/parallel tasks).
- Segment self-contained functionality into services (one surface area, one job, no deep foothold), using Effect TS where strong error handling matters (payments, inference) because AI writes Effect well; pick payments by model (Stripe for subscriptions, Autumn for credits).
- Add observability early (Sentry + PostHog); an agent gets its own sandbox/computer (Daytona) with a browser that self-heals; enterprise auth via WorkOS. It is all informed preference, not universal law.

## Connections

- [[agentic-system-design]] - the four trade-offs, abstraction layers, monorepo-for-agent-context, client -> server -> DB, services, and early observability.
- [[production-agent-infrastructure]] - Convex durable processes/queues, per-agent self-healing sandboxes (Daytona), and OpenClaw as the deployed agent.

## Source

- **Author / channel:** Ross (Hey Fabrica agency; product: Pluto)
- **Title:** Building Robust Applications with AI (Pluto System Design)
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Pluto_System_Design_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
