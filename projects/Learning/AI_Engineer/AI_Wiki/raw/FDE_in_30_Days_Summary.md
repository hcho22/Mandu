# Forward Deployed Engineering: The Complete Playbook (FDE in 30 Days)

**Guest:** Vas, founder of Varick Agents
**Host:** Greg
**Topic:** What a Forward Deployed Engineer (FDE) is, why the role pays $150K–$1M/year, and a 30-day roadmap to break into it.

---

## Overview

Vas, founder of **Varick Agents**, breaks down the Forward Deployed Engineer (FDE) role — a term popularized by **Palantir** — and gives a complete playbook for becoming one in 30 days. The core argument: AI intelligence is now commoditized (every company can access similar frontier models), so the real competitive edge has shifted to **deployment** — knowing *where, how, and why* to apply that intelligence inside a specific business. FDEs sit at the intersection of business/consulting judgment and technical/engineering judgment, and Vas walks through the 3-phase engagement loop (Audit → Eval → Deployment) plus a detailed 4-week roadmap for building your own FDE case study from scratch.

> 💬 **OPINION (Vas):** "I think this is the clearest episode... the clearest master class" — this framing is the host's opinion, but the FDE definitions and the 30-day plan structure are presented by Vas as his team's original framework, developed at Varick Agents.

---

## Table of Contents

1. [What Recently Changed: Intelligence Is Commoditized](#1-what-recently-changed-intelligence-is-commoditized)
2. [Where the Term Comes From: Palantir](#2-where-the-term-comes-from-palantir)
3. [The Three Stages of an FDE Engagement](#3-the-three-stages-of-an-fde-engagement)
4. [The Two Kinds of Judgment (Why FDEs Are Rare)](#4-the-two-kinds-of-judgment-why-fdes-are-rare)
5. [Understanding the Real Workflow (Not the Documented One)](#5-understanding-the-real-workflow-not-the-documented-one)
6. [Designing the System: Deterministic Software vs. Agent vs. Human](#6-designing-the-system-deterministic-software-vs-agent-vs-human)
7. [Building: Audit → Eval → Deployment](#7-building-audit--eval--deployment)
8. [Selling & Positioning the Engagement](#8-selling--positioning-the-engagement)
9. [The 30-Day Roadmap to Become an FDE](#9-the-30-day-roadmap-to-become-an-fde)
10. [Closing Thoughts](#10-closing-thoughts)

---

## 1. What Recently Changed: Intelligence Is Commoditized

**Key points:**
- Frontier models are being released constantly — Vas name-checks **Kimi K3**, **Fable 5**, and **GPT-5.6** as recent releases at time of recording.
- The same foundational AI capability is now available to any company that can pay for it.
- Across ~50 enterprise clients, Vas observes the same tooling stack repeatedly: **Claude Code**, **Cursor** (for model agnosticism), **GitHub Copilot**.
- Because everyone has access to the same intelligence, **intelligence itself is no longer the moat** — deployment is.

> 📏 **RULE (general principle):** "The edge is no longer who has the intelligence. It's where, how, and why they use it." — This is presented as an industry-wide reality, not just Vas's opinion.

> 💡 **TIP:** The FDE's core job is bridging general-purpose AI capability with a specific company's unique processes, systems, and context — because every business runs differently even for the "same" function (e.g., accounts payable can be a 10-step or 30-step process depending on the company).

---

## 2. Where the Term Comes From: Palantir

**Key points:**
- The term "forward deployed engineer" was **popularized by Palantir**.
- Palantir built a software **ontology** — a stack of connectors and data links that pipe enterprise data into a unified interface.
- Palantir FDEs are deployed **on-site** at enterprise or government/military clients, learn their workflows, then build workflows, dashboards, and agents to solve specific problems.
- Palantir essentially reinvented **consulting for the software space** — a centralized platform, customized per client by FDEs on the ground.

> 💬 **OPINION (Vas):** "I think the AI age is going to demand [customization] 100 times more" than the prior "data age" — this is Vas's forward-looking prediction, not an established fact.

> 🛠️ **TOOL MENTION:** Palantir's ontology/software stack (referenced as context, not something Vas endorses using directly).

---

## 3. The Three Stages of an FDE Engagement

Vas frames FDE involvement at a company in three stages:

### Stage 1 — Understanding the Business Reality
- Requires going deep into *how work actually happens today* — not the documented process.
- Involves interviews, observation, and access to systems (ERPs, CRMs).
- Communication and analytical ability are described as **critical** — arguably where the bulk of an FDE's time goes.

> 💬 **OPINION (Vas):** "This is where the bulk of the time goes in my opinion."

> 💡 **TIP:** FDE work is usually best done **on-site**, even though it's technically possible remotely. Being physically present for a full 8–10 hour day (vs. a 1-hour interview) surfaces undocumented exceptions and edge cases that people forget to mention. Vas compares this to McKenzie [McKinsey] consultants sitting with miners on-site to observe real workflows.

### Stage 2 — FDE Judgment
- Deciding **where intelligence belongs and where it doesn't.**
- Early in the AI wave, teams over-applied AI to everything ("slap AI everywhere"), which led to **token maxing** and hallucinations.
- Cited stat: **95% of generative AI pilots fail** (MIT statistic, as referenced by Vas).
- Of a 10-step workflow, maybe only 2–3 steps genuinely need LLM judgment (e.g., non-deterministic categorization); the rest can be solved with if/else logic and API calls.

> 📏 **RULE:** Not every workflow needs AI — sometimes it's too risky, not high-ROI enough, or already automated.

> 💡 **TIP:** Compensation reality — Vas states FDE roles range from **$150,000 base salary with considerable equity** up to **as high as $1 million/year** for top performers who combine consulting and technical skill.

### Stage 3 — Building the Deployed System
- Highly variable by company. At Palantir, some FDEs mostly configure workflows/dashboards within the ontology (light coding, mostly SQL); other companies require full production code.
- Regardless of coding depth, FDEs need strong technical understanding because **they're accountable when something breaks in production** — "it's basically your ass on the line."

---

## 4. The Two Kinds of Judgment (Why FDEs Are Rare)

**Key points:**
- **Commercial/business judgment**: workflows, cost, incentives, risk, adoption, business value, internal politics. Strong in consultants (e.g., **McKinsey**, **BCG**, **Bain** engagement managers).
- **Technical judgment**: models, systems, APIs, data, code reliability, evals, guardrails, harnesses, post-training, fine-tuning. Strong in software engineers.
- An FDE must be the **best combination of both** — not an average, not "good enough" at either side.

> 💬 **OPINION (Vas/Greg analogy):** Greg frames it as "understanding art and understanding science and being able to speak both" — an analogy, not a technical claim.

> 📏 **RULE:** "It is truly the best of both... that is the million-dollar hire where the FD can turn business understanding into working software end to end."

> ⚠️ **CAUTION:** Vas warns that as FDE hiring accelerates, many people entering the role are strong in only one dimension (e.g., good communicators who can't code, or good engineers who can't communicate). He "strongly urges" people to actively strengthen whichever side is weaker.

---

## 5. Understanding the Real Workflow (Not the Documented One)

**Key points:**
- Illustrative example: "an email arrives" sounds like a simple trigger, but in reality:
  - Arrives from 40+ senders, no consistent formatting.
  - Data comes in mixed formats: PDF, screenshot, Excel spreadsheet, or buried in a forwarded thread.
  - Many steps are exceptions ("ignore the second attachment," "Sarah already signed off on this one").
  - No consistent subject line to route by.
  - The real logic often lives **in one person's head** and isn't written down anywhere.
- The same complexity repeats at every downstream step (e.g., copying into a spreadsheet — stale data, manual rekeying, column drift).

> 💡 **TIP:** Ask people directly: how easy would it be for *you* to write down every exception in your own job? Vas uses his own experience as a software engineer at **Meta** — his "official" job description ("I code all day") omits the reality of meetings, production incidents, and firefighting.

> 📏 **RULE:** Once the real workflow is understood, the FDE decides: where does deterministic software live, where does the agent act, where does a human approve, and where does the record get updated?

**Recommended architecture pattern:**
- Deterministic software handles the majority of steps.
- LLM/API calls provide judgment where needed.
- **Human-in-the-loop approval** is inserted before the agent proceeds to the back half of a workflow.

> 📏 **RULE (strong recommendation):** Vas says he "strongly recommends" all his FDEs push for a human-in-the-loop approval step in agent implementations — intake → validation → agent drafting → **human approval** → remaining steps execute.

---

## 6. Designing the System: Deterministic Software vs. Agent vs. Human

**Key points:**
- The FDE's build responsibilities break into three parts:
  1. **Auditing**
  2. **Creating evaluation suites** to prove correctness
  3. **Deployment** — both client handholding/adoption and technical monitoring (KPIs, SLAs)
- Each stage is a **prerequisite** for the next.

### Building Evals for Non-Deterministic Tasks
- For deterministic tasks (e.g., "was this email categorized correctly"), evals are easier — you can validate against historical data (e.g., 10,000 past emails).
- For creative/non-deterministic tasks (e.g., "create a presentation"), success is subjective ("beauty is in the eye of the beholder").

> 💡 **TIP:** Use as much historical data as possible to build a "golden data set" of what good output looks like (e.g., 5,000 past presentations → derive rules like "always put the logo top-left," consistent font sizing).

> 📏 **RULE:** Even with a strong golden dataset and good evals, you still need **human-in-the-loop feedback** as an ongoing mechanism — to improve the harness and/or fine-tune/post-train the model over time.

**Example eval framework (from the discussion):**
- Run 50 test cases → e.g., 41 pass, 9 fail.
- Categorize failures (e.g., 5 had missing data, 4 pulled the wrong record).
- Use failure categorization to drive system improvements.

### On Model Choice / Model Agnosticism

> 💬 **OPINION (Vas, explicitly framed as advice for beginners):** Varick Agents as a company is deliberately **model agnostic** — believing value comes from being able to switch models to improve accuracy and lower cost, and not "monopolizing" your inference layer.
>
> However, Vas's advice **for individuals starting out as an FDE** is the opposite: **pick one model and one agent-building platform and get very good at it first** (e.g., OpenAI's agent building tools, or Anthropic's **Agent SDK**). Only branch out to other models/platforms (Claude, **Kimi 3**, **GLM 5.2**, open-source models) once you're already strong in one ecosystem.

> 💡 **TIP:** "Don't put the cart ahead of the horse" — build deep expertise in one model/platform before trying to become model-agnostic. Your real value as an FDE is understanding both the business and technical sides, which transfers across any model.

---

## 7. Building: Audit → Eval → Deployment

This is described by Vas as the single most important framework in the whole conversation ("If I had to put one page cemented, burned in everyone's brain, it's this one").

### Phase 1: Audit
- Collect context, trace findings, identify bottlenecks, repetitive work, and judgment points.
- Produce an **operating map** showing current-state and future-state (with AI) workflows.

> 💡 **TIP — Sell the audit, don't give it away as a throwaway step:** Vas references a related episode with guest **Corey Ganim**, who discussed selling audits as a way to learn a client's business before deploying AI, then charging separately (monthly fee or one-time fee) for implementation.

> 💬 **OPINION (Vas):** "The audit is worth so much money to a business... it's better than McKinsey [referenced in transcript as 'McKenzie'] because it's so telling." Vas states some clients told him the audit alone was worth **10x** what they paid for it.

> 💡 **TIP (rebranding):** Greg shares that his agency **LCA** found that clients had an "allergic reaction" to the word *audit* (people associate it with a tax audit). Rebranding the audit as a **"sprint"** (framed like a design sprint) tested better with clients.

### Phase 2: Eval
- Prioritize high-volume workflows where improvement is large enough to matter.
- Build a decision matrix: is it safe to act on autonomously, or should it route to a human?
- Produce a formal **evaluation report** (pass/fail rates, categorized failure reasons).

### Phase 3: Deployment
- **Build on top of existing systems — never force a migration.**

> ⚠️ **CAUTION / RULE:** Vas gives a concrete example — a client spent multiple years and several million dollars migrating to **NetSuite** (an ERP system). Telling that client they now need to move *off* NetSuite for an AI solution would fail immediately ("they're going to tell you to get lost"). Instead, build on top of and integrate with NetSuite, **Salesforce**, **SAP**, **Concur**, **Expensify**, **Gong**, and **Workday**.

- Roll out gradually: sandbox/controlled testing → shadow mode → increasing autonomy → full production.

> 💡 **TIP:** Meeting clients in person makes it easier to walk them through this gradual autonomy journey, versus being "a guy behind a computer screen" flipping a switch.

---

## 8. Selling & Positioning the Engagement

**Key points:**
- People inside a company are motivated by **not wanting to look bad / wanting to get promoted** — frame the engagement around helping your internal champion get credit for driving value.
- Bringing in an FDE is inherently perceived as risk by the client-side stakeholder — you must actively **de-risk** the engagement.

> 💡 **TIP (strong recommendation for people breaking in):** Do the **first audit for free**. Get your foot in the door, prove value, come up with a plan, and only get paid once you've demonstrated measurable value. Vas states early customers "are genuinely worth more to you than you are to them" — after 2–3 proven engagements, you can start charging.

> 💬 **OPINION (Greg, analogy):** Frames good positioning as "fishing with dynamite" — pitch improvements to the existing stack (efficiency, faster customer reach, revenue growth) rather than proposing disruptive migrations.

> 📏 **RULE:** The Audit → Eval → Deployment loop repeats continuously. Once one workflow improves, the next bottleneck becomes obvious — this is why AI adoption tends to spread across an entire organization rather than staying isolated to one workflow.

---

## 9. The 30-Day Roadmap to Become an FDE

Vas's condensed version of what he learned over a year, compressed into a 30-day plan to build a complete FDE case study from scratch — done **before** you have the job title, in order to get hired.

### Week 1 — Build a Working Agent
**Goal:** Build an agent that completes **one real enterprise workflow** end-to-end (finance, HR, procurement, logistics, IT, sales — any back-office function).

Core building blocks to learn (roughly one per day over the week):
- Agent looping
- Tool usage
- Guardrails
- Context and memory
- **Audit trail** (logging every prompt, response, tool call, error)

> ⚠️ **CAUTION / RULE:** "If you can't show the client what the agent is doing, they will never trust you." Full traceability is treated as non-negotiable, partly due to real client fear/fear-mongering around autonomous agents.

> 📏 **Vas's definition of "agent" (explicitly his own definition, not universal):** "If I give you a task, can you solve it in as much detail and as high enough accuracy as possible" — with minimal reliance on the user prompting perfectly. He states: "I can prompt like an idiot and it will still happen."

**Week 1 Checkpoint:** A working agent with tools, guardrails, deliberate memory, and a full audit trail for one task.

---

### Week 2 — Make It Production-Ready (Recoverable)
**Goal:** Turn the demo into a system that can recover from failure.

- Use a **defined JSON schema** — not free-form text — and validate every response against it.
- Build explicit **failure handling / exception handling** for: missing data, malformed responses, dead APIs, timeouts, partial completions.
- Add **checkpointing** so the agent can resume after a failure rather than restarting.

> 📏 **RULE (Vas's core philosophy):** "There's only one way that something can go right, but there's a thousand different ways something can go wrong. So if you're only building for the way it goes right, you're worth nothing. If you're solving for all the exceptions, that's where you are worth something as an agent."

**Week 2 Checkpoint:** A resumable agent with structured outputs, state recovery, and explicit failure behavior.

---

### Week 3 — Measure and Optimize
**Goal:** Make the system measurable and economically viable.

- Build a **golden dataset of 20+ real queries** with evals for correctness, format, tool selection, and escalation behavior.
- Optimize cost by routing simpler subtasks to cheaper/smaller models — Vas mentions **Gemini Flash** as an example of a lighter-weight option, and is skeptical about **Llama 4** being a good fit for this ("probably not").
- Only add multi-agent coordination when decomposition genuinely helps (implied caution against over-engineering).

> 💡 **TIP:** Measure impact across exactly **three buckets**: revenue uplift, risk mitigation, and cost savings. Vas states these are the only three measurement categories that matter to a business.

**Week 3 Checkpoint:** An evaluated agent with known failure modes, measured cost, and a golden dataset.

---

### Week 4 — Communicate and Defend
**Goal:** Defend the system like an FDE would to a real client — both technically and commercially.

- Document: the pain point, why AI belongs there, the architecture, and the iteration history (e.g., "accuracy went from 70% to 95%").
- **Rehearse the pitch two ways:**
  - **As an engineer:** architecture, decisions, tradeoffs.
  - **As a VP:** problem, outcome, evidence, risk.

> 💡 **TIP:** During this week, actually pitch your agent to real businesses. They'll tell you directly whether your economics and framing are right — and this feedback should shape your next FDE engagement.

**Week 4 Checkpoint:** A complete FDE case study, defensible to both engineers and executives.

---

### Final Note — The Whole Point of the 30 Days

> 📏 **RULE:** "Do the job before you have the title." By day 30, you won't just understand forward deployed engineering conceptually — you'll have tangible proof (a working, evaluated, documented case study) that you can do it, which materially increases your odds of getting hired.

---

## 10. Closing Thoughts

- Vas notes this kind of practical, current material isn't taught in universities — he draws a parallel to being in computer science school around **2008–2009** when the App Store launched, and being told mobile development "wasn't in the textbook." He ultimately dropped out over this gap.

> 💬 **OPINION (Vas):** He believes foundational university coursework (math, physics) was valuable for learning how to think, but that the tactical/current material is best learned via YouTube and X (Twitter) rather than formal coursework, and is skeptical universities will catch up quickly on AI/agents curricula.

- Both Vas and Greg point to **YouTube and X (Twitter)** as the best current sources for staying up to date — Vas notes even large companies (he references **Mark Zuckerberg**/Meta model announcements) now break news on X first.
- Vas confirms he'll be reading and responding to comments on the video/podcast for follow-up questions.

**Referenced companies/tools throughout:** Palantir, Varick Agents, LCA (Greg's agency), Meta, McKinsey ("McKenzie" in captions), BCG, Bain, NetSuite, Salesforce, SAP, Concur, Expensify, Gong, Workday, HubSpot, Apollo, Clay, Chili Piper, Claude Code, Cursor, GitHub Copilot, OpenAI Agent Building Platform, Anthropic Agent SDK, Kimi 3, GLM 5.2, Gemini Flash, Llama 4.

---

## Appendix: Caption Corrections

The following terms were corrected from likely auto-caption misspellings based on context and the companion reference document:

| Caption Text | Corrected To |
|---|---|
| "Voss" / "Vos" / "Foss" | **Vas** |
| "Veric Agents" | **Varick Agents** |
| "Palunteer" / "Palanteer" | **Palantir** |
| "Netswuite" | **NetSuite** |
| "McKenzie" | McKinsey *(kept as spoken/captioned reference where ambiguous; likely means McKinsey & Company)* |
| "FTE" / "FTEEs" (when referring to the role) | **FDE** / **FDEs** (Forward Deployed Engineer(s)) — "FTE" normally means Full-Time Employee, so this appears to be a captioning confusion with "FDE" |
| "Kimmy 3" | **Kimi 3** (per companion document; note the video audio also references "Kimi K3" in some AI industry naming conventions — kept as "Kimi 3" per the reference doc) |
| "GPT 5.6 Soul" | Uncertain — possibly a mis-transcription of a specific model name `[?]`; kept as heard, unconfirmed |
| "Muse Spark" | Uncertain — possibly a mis-transcription of a specific lightweight model name `[?]`; unconfirmed |

*Note: A companion source document ("FDE_Starter_Plan.pdf" / Varick's FDE in 30 Days guide) was used to confirm spellings of Vas, Varick Agents, and NetSuite, and to confirm the exact closing quote used above.*
