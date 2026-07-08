---
type: source
title: "Building Robust Applications with AI (Agentic System Design via Pluto)"
source-type: tutorial-summary
author: "Ross (Hey Fabrica)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [system-design, architecture, agents, production, convex, monorepo, abstraction]
---

# Building Robust Applications with AI (Agentic System Design via Pluto)

A summarized YouTube walkthrough by Ross ([[ross-hey-fabrica]], of the Hey Fabrica agency) using the real architecture of his AI-agent product **Pluto** to teach production-grade [[system-design]] in the AI era.
Core thesis: AI makes prototypes easy, but "vibe-coded" apps break at ~10 real users because the builder never learned system design; a developer using AI ships more robust apps than a non-developer using AI precisely because they can design a system.

## Key claims

- **[[engineering-trade-offs]]:** every design balances scalability, reliability, performance, and cost; no system is perfect, so choose consciously which trade-offs to accept.
- **[[everything-as-code-abstractions]]:** modern abstraction layers (Convex, Vercel, WorkOS, Autumn) hide the hard infra AND, because they are "everything-as-code," agents already know how to operate them - central to [[agentic-engineering]]. History: own metal to cloud (AWS/GCP/Azure) to the higher abstraction layer.
- **[[monorepo-for-agent-context]]:** start every app as a monorepo (Turborepo) so the agent has full-codebase context across all clients, one backend, and shared components. Pluto has four client surfaces (SvelteKit web, Expo/RN mobile, Electron desktop, admin).
- **[[client-never-touches-the-database]]:** the client must never query the DB directly (key leaks via the Network tab); the secure flow is client -> server -> DB -> server -> client. Ross distrusts the Supabase-RLS-from-client pattern for this reason.
- **[[durable-agent-processes]]:** an agent can't stop when the user closes the tab, so you need durable execution (Convex Workflow: retries + delays) and queues/parallelism (Convex Workpool; raw AWS equivalents SQS/RDS/EC2). Vibe-coded apps fail here.
- **Services:** segment self-contained functionality (one surface area, one job, no deep foothold) into its own service; Pluto splits out iMessage and Inference/Payments, both in Effect TS (strong error handling, AI-friendly).
- **Requirements first:** list hard requirements (enterprise auth via WorkOS, credit-based billing via Autumn, agent hosting) before picking tools; requirements drive the stack.
- **Observability early:** Sentry + PostHog from the start; see [[agent-observability]].
- **Code-review gate:** Greptile gives a PR summary + confidence score; Ross won't personally review/merge anything below 4/5 - an automated review gate akin to [[adversarial-code-review]].
- **Agent compute:** Daytona gives each agent its own sandbox + browser that self-heals (took a screenshot, something broke, it recovered) - infrastructure Ross "can't build myself."

## Connections

- [[system-design]] - this source opens and anchors that area.
- [[engineering-trade-offs]], [[everything-as-code-abstractions]], [[monorepo-for-agent-context]], [[client-never-touches-the-database]], [[durable-agent-processes]] - the five concepts it introduces.
- [[agentic-engineering]] - abstraction layers are why agents can build production systems at all.
- [[agent-observability]] - Sentry/PostHog/Daytona extend the observability thread.
- [[adversarial-code-review]] - Greptile's confidence-score merge gate is the same review-gate pattern.
- [[open-claw]] - OpenClaw is the agent Pluto deploys.
- [[ross-hey-fabrica]], [[convex]] - entities.
- Cross-wiki: general RAG/agent-infra craft lives here; product-specific decisions belong in the Agentic RAG wiki.

## Source

- **Author/Speaker:** Ross, of the Hey Fabrica agency; case study is his app Pluto (AI agent for businesses of ~15-60 employees)
- **Title:** Building Robust Applications with AI
- **Format:** YouTube tutorial, condensed to a reference summary; contains one sponsored segment (Greptile)
- **Stack cited:** SvelteKit, Expo/React Native, Electron, Turborepo, Convex (Workflow/Workpool + R2/Autumn components), Effect TS, Postgres/PlanetScale, Autumn, OpenRouter, OpenClaw, Daytona, WorkOS, Vercel, Sentry, PostHog, Greptile
- **Raw:** [[Pluto_System_Design_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
