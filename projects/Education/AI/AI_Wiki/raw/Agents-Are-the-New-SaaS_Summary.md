# Agents Are the New SaaS

**Startup Ideas Podcast · Tutorial Summary**

*A step-by-step playbook for finding a niche, building your first agent, proving it works, and selling agents as labor.*

---

## Overview

The core thesis: software is shifting from **"help me do the work"** to **"do the work with me."** Where SaaS sells software (a tool a team can use), **agent SaaS sells work** — a job the team no longer has to do by hand. The speaker argues the total addressable market is larger than SaaS because agents target **labor** (human capital), a multi-trillion-dollar market. The episode walks through an 8-part playbook — from picking a workflow with a paycheck attached, to shadowing the human, building the smallest useful agent, wrapping it as a product, and selling pilots as labor — capped by a 30-day, week-by-week execution plan.

**Callout legend:** 💚 **Tip / Actionable** · 💙 **Tool / Named Example** · 💜 **General Rule** · 🧡 **Speaker Opinion** · ❤️ **Caution / Trade-off**

---

## Table of Contents

1. [The Product Is the Job](#1-the-product-is-the-job) — SaaS sells software, agent SaaS sells work
2. [Pick a Workflow with a Paycheck Attached](#2-pick-a-workflow-with-a-paycheck-attached) — the 5 traits + scoring rubric
3. [Shadow the Human Before You Build](#3-shadow-the-human-before-you-build) — the 7-part agent spec
4. [Build the Smallest Useful Agent (MUA)](#4-build-the-smallest-useful-agent-mua) — the 4 first-version types
5. [The Product Wrapper Is What Makes It SaaS](#5-the-product-wrapper-is-what-makes-it-saas) — the control room + evals
6. [Sell the Pilot Like Labor, Then Productize](#6-sell-the-pilot-like-labor-then-productize) — pricing models
7. [Distribution](#7-distribution) — workflow teardowns & content
8. [The 0-to-100 Plan](#8-the-0-to-100-plan-build-an-agent-business-in-30-days) — a 30-day, week-by-week build
- [Appendix A: Corrections & Caption Fixes](#appendix-a--corrections--caption-fixes)

---

## 1. The Product Is the Job

The foundational mental model: **SaaS sells software; agent SaaS sells work.** A normal SaaS product says "here is a tool a team could use." An agent SaaS product says "here is a job your team no longer has to do by hand" — and then sells that service. It sounds like a small change but it's a big mindset shift, both for the customer and for the builder.

> 💜 **GENERAL RULE**
> Frame the offer as a job that disappears, not a tool that's provided. The buyer isn't purchasing capability — they're offloading a task.

### Worked examples

**Restaurants:** the phone rings during dinner service, the host is busy seating people, the same questions repeat, reservations get missed and private-dining calls get lost — all lost revenue.

> 💙 **TOOL / NAMED EXAMPLE**
> **Slang.ai** — an "AI superhost" for restaurants (speaker notes he is not affiliated; used only as an illustrative example). Answers inbound calls, handles guest questions, manages reservations, routes VIPs, alerts staff to high-priority topics (private dining, guest complaints), and integrates with systems like **OpenTable** and **Yelp**.

**Home services** (plumbing, HVAC, roofing, pest control): missed calls mean lost jobs. An agent that picks up 24/7 books jobs, follows up with customers, and eases dispatcher overload — more revenue from the same demand.

> 💙 **TOOL / NAMED EXAMPLE**
> **Same Day** — focuses on home services, selling AI dispatchers / sales agents / receptionists that answer calls, respond to texts, book jobs, and reschedule.

> 💚 **TIP / THE MENTAL MODEL FOR IDEAS**
> When generating a startup idea, ask: can I handle this **one annoying job** better than a junior employee, faster than an agency, and cheaper than adding headcount? These everyday examples matter precisely because they're easy to understand.

---

## 2. Pick a Workflow with a Paycheck Attached

Start with the paycheck. If people already pay for the work — an employee, an agency, a receptionist, a coordinator, a dispatcher — there's an opportunity to deliver it cheaper and free that person up for higher-value creative work.

> 💜 **GENERAL RULE — The 5 Traits of a Good Agent Workflow**
> 1. **It happens all the time.** Daily is good, hourly is better (every inbound lead, call, tech ticket, quote request, appointment, order, maintenance request).
> 2. **It has a clear finish line.** The job got booked, the ticket got categorized, the refund got approved, the vendor got scheduled, the customer got a useful answer.
> 3. **It touches existing software.** Gmail, Slack, Shopify, HubSpot, Zendesk, Stripe — agents need these tools to act and the context to read.
> 4. **The edge cases are annoying but learnable.** Too basic → plain automation (Zaps) already handles it. Pure human judgment → the first version breaks. The sweet spot is repetitive work with enough judgment that AI can help.
> 5. **The buyer can feel the loss.** Missed calls, slow replies, dropped leads, empty calendar slots, expensive humans doing low-value coordination.

> ❤️ **CAUTION / TRADE-OFF**
> Avoid both extremes: a workflow that's too basic gets eaten by simple automations (Zapier-style zaps), while one requiring pure human judgment will break in its first version.

### First rep: how to get started

Pick one niche and write down **20 jobs people complain about.** Examples: *Roofers* — missed calls, financing questions, insurance paperwork, appointment reminders. *Med spas* — lead qualification, no-show recovery, membership upsells. *Shopify brands* — returns, exchanges, wholesale lead follow-ups.

> 💚 **TIP / Score Each Job on 5 Things**
> - How **often** does it happen?
> - How **expensive** is the pain?
> - How **easy** is it to know when the job is done?
> - What **tools** does it need access to?
> - **Who already owns the budget?**
>
> Start with the job that has a paycheck attached — that's where agent SaaS begins.

---

## 3. Shadow the Human Before You Build

The step most people miss: once you've identified the job — before you prompt, before you code — **shadow a human who does it.** Many founders want to skip this, but it's usually what gives you an unfair advantage and the insight to build a high-quality agent.

> 💚 **TIP / How to Shadow (watch 10–20 jobs)**
> - Watch someone do the job across **10 to 20 jobs.**
> - Ask them to **screen record** it and **narrate** what they're doing.
> - Ask what makes a case **easy**, what makes a case **weird**, what they check before deciding, and where mistakes happen.
>
> You're looking for the *real* workflow. Even if you've done the task before, having it fresh is a big help.

**Why the detail matters:** a restaurant host asked "What time are you open?" is really running a deeper workflow — they know when the kitchen closes, which tables suit strollers, when the patio is closed, how to handle a VIP, and when to route a private inquiry. **The detail is the product.**

> 💜 **GENERAL RULE — The 7-Part Agent Spec**
> - What **wakes the agent up**? (trigger)
> - What **context** does it need?
> - What **tools** can it use?
> - What is it **allowed to do itself**?
> - Where does it need **approval**?
> - When should it **escalate** and bring a human into the loop?
> - What does **success** look like?

> 🧡 **SPEAKER OPINION**
> Nail these seven parts and you won't build "agent slop." The goal is agents that do the work as well as (or better than) humans and far more consistently — that's what people pay for.

---

## 4. Build the Smallest Useful Agent (MUA)

Most people hear "agent" and imagine a fully autonomous employee — the kind of demo that goes viral on Twitter but doesn't really work and makes a bad business. Start smaller. The speaker calls it the **Minimal Useful Agent (MUA)**.

> ❤️ **CAUTION / TRADE-OFF**
> Chasing the fully autonomous "employee" agent up front produces impressive demos that don't hold up and turn into weak businesses. Constrain scope deliberately.

> 💜 **GENERAL RULE — The 4 Good First Versions**
> 1. **Draft-and-approve agent** — reads context, drafts the reply / quote / summary / next step; a human approves. Best when there's workflow risk, creativity, or an approval process.
> 2. **Triage agent** — classifies inbound work and routes it (maintenance request vs. billing issue vs. refund).
> 3. **Coordinator agent** — moves between systems and people: checks availability, sends reminders, asks for missing info, keeps work moving.
> 4. **Bounded-action agent** — does a specific thing under clear rules (book an appointment, send a follow-up, process a refund under $50).
>
> The ladder: **draft → triage → coordinate → act.**

> 💙 **TOOL / NAMED EXAMPLE**
> **Uber Eats** is cited as a bounded-action agent in the wild: order a salad that never arrives and the refund is issued automatically by an agent.

> 💚 **TIP / Start as a Workflow, Not an Agent (via Anthropic guidance)**
> The speaker cites **Anthropic's agent guidance**: many agent problems should *start as workflows.* A workflow follows a predictable path; an agent decides more dynamically. **Earn autonomy** by starting predictable and adding judgment only when it creates value.

> 🧡 **SPEAKER OPINION**
> Ship **one workflow and one promise** — e.g., "we answer missed calls for roofers and book qualified jobs," or "we triage maintenance requests for property managers and schedule the right vendor." One workflow that works is enough for day one, and it builds confidence in both you and the customer — who are buying agents for the first time and don't want everything at once (especially if you're not Microsoft or Salesforce).

---

## 5. The Product Wrapper Is What Makes It SaaS

Don't just build a cool automation. What separates a cool automation from a real agent-first SaaS product: **the agent does the work, but the wrapper creates the trust.** Customers need to see what happened.

> 💜 **GENERAL RULE — What the Wrapper Provides**
> - Visibility: **logs** and a record of what happened, and **why** the agent did what it did.
> - **Approvals, controls, and handoff rules.**
> - A way to **test the agent before it goes live.**
>
> The agent lives in the phone system, inbox, Slack channel, or CRM — but the customer still needs the **"control room."** The dashboard can be simple.

**Example control rooms:** a restaurant phone agent shows call summaries, reservation outcomes, and missed human handoffs; a property-maintenance agent shows tickets created, vendor routes, tenant updates, and owner approvals.

### Evals: the agent's "gym"

Before promising autonomy, build a small test set. Take **50 real examples** of the job (50 calls, 50 leads, or 50 maintenance requests) and mark the right answers, then run the agent system against them: did it classify correctly, ask for the right missing info, use the right policy? This is an **eval**.

> 💚 **TIP / Evals Double as a Sales Asset**
> Every time you change the prompt, model, tools, or workflow, the agent goes "back through the gym." It's also persuasive: *"We tested this on 50 of your old maintenance requests. It routed **42** correctly, flagged **6** for human review, and made **2** mistakes — here are the two, and here's how we fix them."* Transparency builds trust, especially with owners of "boring" businesses.

---

## 6. Sell the Pilot Like Labor, Then Productize

The fastest path: run a **pilot where you manually do the work with AI**, then productize the repeated parts. Start with **three customers in one niche** — same niche, same workflow, same pain — and sell the outcome ("we will answer and qualify your missed calls"; "we will triage your maintenance requests"). Charge a setup fee plus a simple monthly fee; keep pricing easy to understand. Add usage- or outcome-based pricing once you understand the value.

> ❤️ **CAUTION / TRADE-OFF**
> Be very constrained in the pilot (same niche / workflow / pain) or you'll get bad results. And don't jump straight to outcome pricing — you have to earn your way there with patience.

> 🧡 **SPEAKER OPINION**
> Outcome pricing is the future of how agent-first businesses and software get priced — customers don't want to pay for "another seat." (He notes this is a recurring theme on the Startup Ideas Podcast.)

> 💚 **TIP / Example Pricing Models**
> - **$1,500 setup + $1,000/month** for one workflow.
> - **$2,000 setup + $30 per qualified appointment** (moving toward outcome-based).
> - **$3,000/month up to 500 handled tickets.**
>
> The exact price matters less than the learning: what does the customer value, where does the agent break, what needs approval, and — most important — what would they miss if you took it away?

> 💜 **GENERAL RULE — Productize the Repeated Pattern**
> Build the product around what repeats. If every roofer needs the same emergency-call script, service-area check, financing questions, and estimate follow-up — you have a product. If every med spa needs lead scoring, consultation booking, no-show recovery, and post-treatment follow-up — you have a product. This is agent SaaS: **you earn the software by doing the work first.**

---

## 7. Distribution

You need people to hear about the agent, see it, and think "I need this." The tactic working in real time: **workflow teardowns.**

> 💚 **TIP / The Workflow Teardown Format**
> **Show the old way** (painful): a call comes in, nobody answers; the customer calls the next company; or a CSR answers, asks five questions, checks the calendar and service area, books, writes notes, sends a reminder — then forgets to follow up. **Then show the agent way:** agent answers, asks the right questions, checks service area and urgency, books the appointment, updates the CRM, sends confirmation, and flags edge cases for a human. Owners and managers *feel* that pain.

> 🧡 **SPEAKER OPINION**
> Be in the business of selling **painkillers, not vitamins.** The way to get someone to book a call is to (gently) make fun of the old way, then show the new way.

> 💚 **TIP / Content Strategy**
> - **Pick one workflow and make the internet associate you with it.**
> - Make the checklist, the benchmark, the teardown, and **"50 examples of this workflow"** posts.
> - Focus on **one platform** to start; find the formats that work, then put **paid ads** behind the winners. Memes around the "old way" help.

> 🧡 **SPEAKER OPINION**
> Many listeners don't want to create content — understandable — but you have to, because that's where the opportunity is. (He notes future episodes will cover getting customers to vibe-coded apps.)

---

## 8. The 0-to-100 Plan (Build an Agent Business in 30 Days)

> 💜 **GENERAL RULE — Week 1, Day by Day**
> - **Day 1:** Pick a niche where missed work costs money (home services, property management, insurance agencies).
> - **Day 2:** Interview 10 operators; have them screen-share the workflow; keep the calls as research. (You can pay them.)
> - **Day 3:** Pick one workflow with frequency, pain, software access, and a clear success metric.
> - **Day 4:** Write the agent spec — trigger, context, tools, rules, handoffs, eval.
> - **Day 5:** Run it **manually with AI** — use Claude or ChatGPT, copy/paste the context, draft the output, ask a human to approve. You're testing whether AI helps *before* building software.
> - **Day 6:** Build the smallest useful version (draft-and-approve or triage is usually enough).
> - **Day 7:** Create the eval set from 50 real examples.

> 💜 **GENERAL RULE — Weeks 2 to 4**
> - **Week 2:** Sell two pilots in the same niche.
> - **Week 3:** Add the product wrapper (logs, approvals, settings, analytics, handoffs) and use AI to build the software.
> - **Week 4:** Publish workflow teardowns, turn the pilots into proof, and double down on the content strategy.

> 💙 **TOOL / NAMED EXAMPLE**
> For running the pilot manually: **Claude** or **ChatGPT**. For building the wrapper software in Week 3, the speaker says he'd probably use **Claude Design**, and — "assuming that Fable is live" — use **Fable** to code it up.

> 💚 **TIP / Build the Audience the Whole Time**
> Throughout the 30 days, build an audience in parallel. By the end of week 4 you should have formats that work and know where to double down. In months 2–3, focus on understanding your **LTV**, which channels work, and where to spend to acquire customers.

### Closing thesis

> 🧡 **SPEAKER OPINION**
> Agents are the new SaaS because software is moving from "help me do the work" to "do the work with me." Many people see and understand the shift but aren't building agent-first businesses. The opportunity: find the smallest painful workflow that repeats all day, in a niche you understand, and make it disappear — answering a phone, booking a job, triaging a ticket, updating the system, escalating the weird case.

> 💚 **TIP / The One-Line Playbook**
> Start with the job → **find it, shadow it, spec it, run it manually, build the smallest useful agent, sell the pilot, then productize the repeatable parts.** That's how you build an agent people will pay for.

---

## Appendix A · Corrections & Caption Fixes

Obvious caption/transcription errors were corrected silently in the summary above. The notable fixes are logged here. Items marked **[uncertain]** are best-guess interpretations of garbled or ambiguous captions — verify against the source video if precision matters.

| Caption as transcribed | Corrected to | Note |
|---|---|---|
| "the new SAS" | the new **SaaS** | Software-as-a-Service; appears throughout. *[confident]* |
| "Slang AI" | **Slang.ai** | Restaurant voice-AI company. *[confident]* |
| "Open Table" | **OpenTable** | Reservation platform (one word). *[confident]* |
| "Zenes" | **Zendesk** | Support software; inferred from context of Gmail/Slack/Shopify/HubSpot/Stripe. *[uncertain]* |
| "zaps" / "Zaps" | **Zaps (Zapier)** | Refers to basic automations. *[confident]* |
| "chatbt" / "chatgbt" | **ChatGPT** | OpenAI product. *[confident]* |
| "claude" / "Clawude" | **Claude** | Anthropic's model. *[confident]* |
| "Clawude Design" | **Claude Design** | Named build tool. *[confident]* |
| "Fable" | **Fable** | Kept as-is; speaker himself hedges ("assuming that Fable is live"). Likely a coding model/tool. *[uncertain]* |
| "same day" | **Same Day** | Home-services agent company; capitalized as a proper name. *[uncertain]* |
| "MUA" | **MUA (Minimal Useful Agent)** | Speaker's coined term; expanded on first use. *[confident]* |
| "eval" / "evals" | **eval / evals** | Evaluation test set; kept as standard term. *[confident]* |
| "rapper" | **wrapper** | Product wrapper (homophone error). *[confident]* |
| "CSR" | **CSR** | Customer service rep; kept as-is. *[confident]* |
| "LTV" | **LTV** | Lifetime value; kept as-is. *[confident]* |

**Note on figures preserved verbatim from the transcript:** pricing examples ($1,500 setup / $1,000 mo; $2,000 + $30 per appointment; $3,000/mo up to 500 tickets), the 50-example eval set (42 correct / 6 flagged / 2 mistakes), "refund under $50," 20 jobs to list, 10 operator interviews, and 10–20 shadowing sessions.
