---
type: concept
tags: [system-design, architecture, trade-offs, monorepo, abstraction, observability]
date: 2026-07-03
source-count: 1
status: seeded
---

# Agentic System Design

Designing a production-ready application architecture in the age of AI: choosing among trade-offs, using "everything-as-code" abstraction layers agents can operate, and structuring the codebase (monorepo, services, secure data flow) so an agent has the context to build it.

## From the sources

[[building-robust-applications-with-ai]] is the anchor source, using the real architecture of Pluto:

- System design is why a developer using AI ships a more robust app than a non-developer using AI; without deliberate design an app crashes at ~10 users.
- Engineering is all about trade-offs across four axes - scalability, reliability, performance, cost - and nothing is perfect, so you consciously choose which to accept.
- Infrastructure evolved by abstraction (own metal -> cloud providers -> higher layers like Convex/Vercel/Supabase), and because the higher layers are everything-as-code, agents know how to operate them well.
- Start every app as a monorepo (Turborepo) so the agent has full-codebase context instead of fragmented ones; never let the client talk to the database directly (client -> server -> DB); segment self-contained functionality into services (one surface, one job).
- Use Effect TS where strong error handling matters (payments/inference) because AI writes it well; pick payments by model (Stripe for subscriptions, Autumn for credits); add observability early (Sentry + PostHog). It is informed preference, not universal law.

## Synthesis

This concept is the reminder that agents do not repeal system design - they raise its leverage. The load-bearing claim is that the gap between a robust app and a vibe-coded one that dies at ten users is *the builder's system-design judgment*, not the model. Two ideas make this an explicitly *agentic* discipline rather than ordinary architecture. First, **abstraction layers are chosen partly for the agent**: everything-as-code platforms (Convex, Vercel, WorkOS) are operable by agents precisely because their surface is code, so a stack decision is also an agent-capability decision. Second, **the monorepo is a context decision** - one repo gives the agent whole-codebase context instead of fragmented ones, which ties architecture directly to [[context-engineering]]. The durability and sandbox concerns the source raises (durable processes, per-agent compute) are the runtime side, covered in [[production-agent-infrastructure]]; the "never let the client touch the database" rule and the audit/observability defaults are the security-and-visibility side that connects to [[agent-permissions-and-safety]]. The framing to carry into interviews is that this is classic engineering rigor - trade-off analysis across scalability/reliability/performance/cost, secure data flow, observability from day one - reasserted for AI-built systems, which is exactly the "validation and system rigor most builders lack" angle. As more system-design talks are ingested, this single-source page is where they will accrue.
