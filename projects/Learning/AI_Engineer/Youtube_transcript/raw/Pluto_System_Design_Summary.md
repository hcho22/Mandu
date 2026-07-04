# Building Robust Applications with AI

**Agentic system design, explained through the architecture of Pluto — by Ross (Hey Fabrica agency)**

*YouTube Tutorial Summary*

---

## Overview

AI makes it easy to build prototypes, but most "vibe-coded" apps break the moment they get real users — because the builder never learned system design. This walkthrough uses the real architecture of Ross's app **Pluto** (an AI agent product aimed at businesses) to show how to design a robust, production-ready system in the age of AI.

The through-line: modern **abstraction layers** (Convex, Vercel, WorkOS, etc.) hide the hard infrastructure work, and because they're "everything-as-code," AI agents can operate them well. The recommended pattern is a **monorepo** containing every client, a unified backend, and standalone services — giving the agent full context over one codebase. Engineering is framed throughout as **trade-offs**: no system is perfect; you optimize for scalability, reliability, performance, and cost.

---

## Contents

1. [What System Design Means (in the Age of AI)](#1-what-system-design-means-in-the-age-of-ai)
2. [The Four Trade-Offs Every System Balances](#2-the-four-trade-offs-every-system-balances)
3. [A Short History of Infrastructure & Abstraction](#3-a-short-history-of-infrastructure--abstraction)
4. [Planning Pluto: Requirements Up Front](#4-planning-pluto-requirements-up-front)
5. [The Client Layer & the Monorepo](#5-the-client-layer--the-monorepo)
6. [The Server + Database Layer (Convex)](#6-the-server--database-layer-convex)
7. [Durable Processes, Queues & Components](#7-durable-processes-queues--components)
8. [Services: Segmenting the Codebase](#8-services-segmenting-the-codebase)
9. [The Full Pluto Stack & Supporting Tools](#9-the-full-pluto-stack--supporting-tools)
10. [Trade-Offs Ross Actually Made](#10-trade-offs-ross-actually-made)
11. [Key Takeaways](#11-key-takeaways)

**Callout legend:** 🟢 Tip / Actionable · 🔵 Tool · 🟠 General Rule · 🟣 Speaker Opinion · 🔴 Caution

---

## 1. What System Design Means (in the Age of AI)

System design is the process of planning the architecture, components, modules, interfaces, and data flow of a software system to meet specific requirements. Pre-AI, this meant manually deciding on storage, load balancers, alerting services, and CI/CD pipelines. Today, many tools abstract that complexity away, making these decisions far easier to implement.

The core reason a developer who uses AI ships a more robust app than a non-developer using AI is that the developer understands how to design a system in the first place.

> 🟠 **GENERAL RULE**
> If you plan to ship an app to production that real people will use, you need a deliberate system design — otherwise it crashes once it gets even ~10 users.

---

## 2. The Four Trade-Offs Every System Balances

The foundational principle: **engineering is all about trade-offs.** There is no perfect system, stack, tool, or infra provider — everything has trade-offs. When designing, weigh four things:

- **Scalability** — Can the system handle growing traffic/data by adding resources? Is it a simple dashboard change, or does it autoscale?
- **Reliability** — What's the chance of going down? Is the provider known for outages?
- **Performance** — Does the tool / architecture keep the app fast?
- **Cost (money)** — Can you afford it? "An arm," "an arm and a leg," or nothing?

> 🟠 **GENERAL RULE**
> No system handles every scenario. Design by consciously choosing which trade-offs you're willing to accept across scalability, reliability, performance, and cost.

> 🟣 **SPEAKER OPINION**
> "Nothing is perfect except Jesus" — Ross's tongue-in-cheek framing that every tool and provider you pick carries downsides.

---

## 3. A Short History of Infrastructure & Abstraction

Ross frames the whole video around **abstraction**: hiding complex implementation details so you focus only on essential high-level features. The evolution came in layers:

- **Own metal (self-hosted servers).** Companies ran physical server racks in-office with IT and DevOps staff. Expensive, hard to predict, hard to scale, and risky either way — too little hardware and you're "cooked" under traffic; too much and you wasted money.
- **Cloud providers.** **AWS** (Amazon), **GCP** (Google), **Azure** (Microsoft), and **Cloudflare** bought the metal and rented it out. This abstracted away physical servers and setup — you deploy straight to them. This is when the web/backends exploded. Powerful, but poor developer (and agent) experience.
- **The higher abstraction layer.** Companies like **Convex**, **Vercel**, **Supabase**, **Neon**, and **PlanetScale** wrap the cloud providers, delivering excellent developer/agent experience and easy scaling.

> 🔵 **TOOLS NAMED**
> **Infra / cloud:** AWS, GCP, Azure, Cloudflare. **Abstraction layer:** Convex, Vercel, Supabase, Neon, PlanetScale.

> 🟣 **SPEAKER OPINION**
> - Azure is "terrible to use" (Ross holds an Azure certificate); GCP is also "terrible to use." He doubts anyone can deploy a React app on Azure in under 5 minutes.
> - Ross's personal defaults: deploy on **Vercel** (occasionally Cloudflare); use **Convex** for backend; use **PlanetScale** when he needs a Postgres database. He avoids deploying directly on AWS/GCP/Azure.
> - Using your own metal today is not recommended.

> 🟠 **GENERAL RULE**
> The abstraction layer isn't just about ease — because these tools are "everything-as-code," AI agents know how to use them well, which is central to agentic engineering.

---

## 4. Planning Pluto: Requirements Up Front

Before building, Ross defined what Pluto needed. Pluto targets **businesses** (small-to-medium, ~15–60 employees) where a manager sets it up and invites employees, though individuals may also use it.

- **Auth** — needed enterprise-grade "big boy" auth supporting things like SOC 2 compliance, plus a manager-invites-employees flow.
- **Billing** — chose a **credit-based / top-up (pay-as-you-go)** model over a subscription, reasoning people are tired of subscriptions.
- **Agent hosting** — since Pluto is an AI agent, it needs a deployment target that is affordable, scalable, and reliable (won't go down).

> 🟢 **ACTIONABLE**
> Start by listing your app's hard requirements (auth model, billing model, hosting constraints) *before* picking tools — the requirements drive the stack choices.

---

## 5. The Client Layer & the Monorepo

Every app decomposes into three concerns: the **client** (where people interact), the **server**, and the **database**. Pluto has **four client surfaces**: a web app, a desktop app, a mobile app (built in one "fable run"), and an internal admin site.

### Client tech choices

- **Web app:** **SvelteKit** (described as "the Next.js for Svelte").
- **Mobile app:** **Expo + React Native** (for cross-platform incl. Android).
- **Desktop app:** **Electron**, wrapping the website.

> 🟣 **SPEAKER OPINION**
> Ross loves SvelteKit — minimal, fast, easy to build performant sites. For mobile he *likes* Swift, but uses Expo + React Native when he needs Android too. Pick the tool **you're familiar with** for the client.

### The monorepo

Rather than three separate repos for web/mobile/desktop, Ross uses a **monorepo**: one giant repository holding every client, the unified backend, all services, and even a shared component/UI library.

> 🟢 **WHY A MONOREPO (ACTIONABLE)**
> - The AI agent gets access to the **entire codebase** at once — no fragmented, separated contexts that are hard for both the human and the agent to manage.
> - One unified backend and one shared component library can serve all client surfaces.
> - Ross **almost always starts a new app with a monorepo.**

> 🔵 **TOOLS**
> **Turborepo** is Ross's monorepo tool of choice (pairs well with Vercel deployment). Clients: SvelteKit, Expo, React Native, Electron. Agent model referenced: **Fable 5** ("it's finally back").

---

## 6. The Server + Database Layer (Convex)

The server must read from the database, write to it, and interact with external services (e.g., calling a weather API) — and it must not be slow or fail.

> 🔴 **CAUTION — HARD RULE**
> **Never read data from the client directly to the database.** The client should never talk to the database. If it does, someone can inspect element → Network tab → read your API key, and "you're absolutely cooked." The secure flow: *client → server → database → server → client.*

> 🟣 **SPEAKER OPINION**
> This client-to-DB pattern is a big reason Ross isn't a fan of **Supabase**. Supabase does offer a server library, but most people query the DB from the client and rely on RLS (row-level security) — which he considers "a fool's game."

### Why Convex

Traditionally you'd deploy a Node.js backend on AWS and set up a separate Postgres instance, then wire them together. **Convex** is an abstraction above AWS that "marries" the backend and database into one box:

- You get a backend + database as one managed infrastructure — one thing to manage instead of two.
- Everything is **real-time** and fast.
- Convex primitives: **queries** (read data), **mutations** (write/mutate data), **actions** (interact with external services).
- **Everything is code** — including the database — so the agent can build features end-to-end.

> 🔵 **TOOL — CONVEX AS PLUTO'S "CONTROL PLANE"**
> Convex is Pluto's main orchestrator / source of truth / bridge — it handles everything and Ross leans heavily on Convex components (see next section).

---

## 7. Durable Processes, Queues & Components

An AI agent can't stop working just because a user closes the tab. Two backend concerns Convex solves out-of-the-box that you'd otherwise have to build yourself:

- **Durable processes** — a process that keeps running even if the user closes the tab, refreshes, or leaves. Convex provides this via its **Workflow** component (durable execution with configurable retries and delays). Vibe-coded apps that don't understand chat streams will typically fail here.
- **Queues & parallel tasks** — e.g., a Ticketmaster-style queue when thousands hammer the site, or coordinated tasks running in parallel. Convex provides the **Workpool** component. (The raw AWS equivalents would be **SQS** for queues, **RDS** for a database, EC2-style virtual servers, etc. — powerful but poor developer/agent experience.)

> 🟢 **ACTIONABLE — CONVEX COMPONENTS WORKFLOW**
> Go to **Convex Components**, search the component you need (e.g., *Workflow*, *Workpool*, *R2* storage, *Autumn*), copy the component link, and hand it to your agent to integrate. Non-technical builders can just tell the AI what they need in plain English.

> 🔵 **TOOLS / COMPONENTS**
> **Convex components used:** Workflow (durable processes), Workpool (queues / parallel tasks), Cloudflare **R2** (storage), Autumn (payments). Raw AWS equivalents mentioned: SQS, RDS, EC2.

---

## 8. Services: Segmenting the Codebase

A **service** is a self-contained, reusable block of software that performs one specific task for other parts of the app or for external clients. Pluto has two services:

- **iMessage** — lets users talk to their agent via iMessage (alongside internal chat, Telegram, Slack, and Discord "soon"). It's substantial code that doesn't have a big foothold elsewhere, so it belongs in its own contained box.
- **Inference / Payments** — Pluto plans its own inference system, tightly coupled with payments (users fund credits, credits pay for inference across different models). Separated because the Convex backend was getting big, and because a dedicated person would likely own this area long-term.

> 🟠 **GENERAL RULE — WHAT MAKES A GOOD SERVICE**
> A block of code that touches **one surface area**, does **one specific thing**, doesn't have a foothold across the entire codebase, but can be cleanly architected on its own.

> 🟣 **SPEAKER OPINION**
> Deciding what becomes a service is "more experience and vibes than a specific formula." iMessage might be "too small" to warrant its own service, but it's genuinely self-contained so it made sense to Ross. He also poses the question to **Fable 5** when deciding.

### Service tech choices

- **Inference/Payments:** **Effect (Effect TS)** + **Postgres** (via **PlanetScale**, but any provider works).
- **iMessage:** **Effect (Effect TS)** only.

> 🟣 **SPEAKER OPINION — WHY EFFECT TS**
> (a) AI is very good at writing Effect code; (b) it needs strong error handling — for inference and payments, when something goes wrong Ross needs to know, cleanly. "Nothing is as good as Effect" for error handling.

### Payments choice

> 🟠 **GENERAL RULE — PICKING A PAYMENTS PROVIDER**
> For **straight subscriptions**, use **Stripe**. For a **credit-based system**, use **Autumn** (handles credits, top-ups, free tiers, and consumables — e.g., giving your agent a card funded by credits). Convex has an Autumn component, so integration is copy-the-link-to-the-agent. Options mentioned: Stripe, Polar, Autumn.

---

## 9. The Full Pluto Stack & Supporting Tools

| Layer | Choice | Notes |
|---|---|---|
| Web client | SvelteKit | Minimal, fast, performant |
| Mobile client | Expo + React Native | Cross-platform incl. Android |
| Desktop client | Electron | Wraps the website |
| Monorepo | Turborepo | All clients + backend + services in one repo |
| Backend + DB (control plane) | Convex | Queries / mutations / actions; real-time; source of truth |
| Durable processes | Convex Workflow | Retries + delays |
| Queues / parallelism | Convex Workpool | — |
| Storage | Cloudflare R2 | Via Convex component |
| Services language | Effect (Effect TS) | Strong error handling; AI-friendly |
| Service DB | Postgres via PlanetScale | For inference/payments wallet ledger |
| Payments | Autumn | Credit-based; Convex component |
| Inference provider | OpenRouter | Underlying inference; ledger built with Effect |
| Agent | OpenClaw | The agent Pluto deploys |
| Agent sandbox / compute | Daytona | Sandbox + a computer (browser) per agent; self-heals |
| Auth | WorkOS | Enterprise-ready; easy company auth + compliance |
| Deployment | Vercel | Staging + prod, inference service, admin site |
| Analytics / error logging | Sentry + PostHog | Robust logging |
| Code review | Greptile | Summaries + confidence score (sponsor segment) |

> 🟢 **ACTIONABLE — LOGGING & OBSERVABILITY**
> Set up robust logging so you know exactly what happened when the app goes down or a build fails. Ross uses **Sentry** and **PostHog**. Non-technical builders can simply instruct the AI: "whenever an error happens, I need to track it — use Sentry and PostHog."

> 🔵 **TOOL — GREPTILE (sponsored segment)**
> Used for code review on PRs. Gives a summary plus a **confidence score**. Ross's personal rule: anything **below 4 out of 5** isn't worth personally reviewing or merging. Example PR cited: 4,341 lines on his open-source project "Ralphie." Offer mentioned: a 2-week free trial (rosmike.link/greptile). *Note: this is a paid promotion.*

> 🔵 **TOOL — DAYTONA (agent compute)**
> Great sandbox provider; every agent also gets its own computer with a browser. Ross's Pluto agent took a screenshot, something broke, it **self-healed**, then delivered the screenshot — behavior he "can't build myself" without this abstraction layer.

> 🟣 **SPEAKER OPINION — WHY WORKOS**
> It's "pretty good" and **enterprise-ready**. Since Pluto targets businesses (~15–60 employees, manager-invites model), WorkOS makes company auth and specific compliance easy — "and the agents love it."

---

## 10. Trade-Offs Ross Actually Made

- **Cost is the deliberately deferred trade-off.** Ross hasn't optimized cost yet — he wants people to try Pluto and love it first ("a problem for later"). Priority: the app doesn't break and every agent is fast (even the Daytona boxes are medium-to-large).
- Generous free tiers help (WorkOS, Convex). To save money he could put everything in Convex, but he chose separate services intentionally.
- On **Vercel** he's on the $20/month plan but has spent **over $100** so far across Pluto, staging, the inference service, and the admin site — "we ball."

> 🟠 **GENERAL RULE**
> Architect so that adding new features/tools won't break the app. Every tool Ross uses is "tried and true" and can handle scale (Vercel, Convex, Autumn). When 1,000 users join, mostly you just upgrade the plan and use AI to optimize — the app won't go down on solid infra unless the code itself is bad.

---

## 11. Key Takeaways

> 🟢 **THE PLAYBOOK IN BRIEF**
> - **Start every app as a monorepo** (Turborepo) so the agent has full-codebase context.
> - **Never let the client touch the database** — always client → server → DB.
> - **Use "everything-as-code" abstraction layers** (Convex, Vercel, WorkOS, Autumn) — they scale, and agents know how to operate them.
> - **Lean on Convex components** (Workflow, Workpool, R2, Autumn) — copy the link to your agent to integrate.
> - **Segment self-contained functionality into services** (one surface, one job, no deep foothold).
> - **Use Effect TS** where strong error handling matters (payments, inference); it's also AI-friendly.
> - **Add observability early** (Sentry + PostHog).
> - **Remember it's all trade-offs** — optimize consciously across scalability, reliability, performance, and cost.

> 🟣 **CLOSING SPEAKER NOTE**
> Ross explicitly says this isn't presented as "the greatest way" to build — it's how he thinks about apps and how he builds them at his agency, **Hey Fabrica**. Treat the specific tool picks as informed preferences, not universal law.

---

*__Caption corrections applied:__ OOTH → Auth; sock two → SOC 2; spelt kit / Spelkit / Felt → SvelteKit; nex.js → Next.js; mono repo / monor repo / monorreo → monorepo; Turbo Repo → Turborepo; Versel / Verscell / forcell → Vercel; Superbase → Supabase; convex / Convix → Convex; Postgress → Postgres; planet scale → PlanetScale; effect TS → Effect TS; Gretile / Gravile / Greile → Greptile; Post Hog / post talk → PostHog; Sentry (kept); work OS → WorkOS; open router → OpenRouter; open claw / openclaw → OpenClaw; Daytona (kept); Tanstack star → TanStack Start; Autumn / Reset / Polar / Stripe (kept as named); Fable 5 (kept as named). Some proper nouns (OpenClaw, Ralphie, Hey Fabrica, Pluto) are transcribed as heard.*
