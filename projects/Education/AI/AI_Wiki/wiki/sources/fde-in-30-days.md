---
type: source
title: "Forward Deployed Engineering: The Complete Playbook (FDE in 30 Days)"
source-type: podcast
author: "Vas (founder, Varick Agents), interviewed by Greg"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [ai-career, fde, forward-deployed-engineer, evals, deployment, enterprise, consulting, agents, job-search]
concepts: [forward-deployed-engineer, deployment-is-the-moat, audit-eval-deployment, real-workflow-not-documented, two-kinds-of-judgment, solve-for-the-exceptions, build-on-existing-systems, do-the-job-before-the-title, phased-autonomy, eval-driven-development, evaluation-pipeline]
---

# Forward Deployed Engineering: The Complete Playbook

A podcast interview with **Vas**, founder of **Varick Agents**, on the Forward Deployed Engineer (FDE) role - what it is, why it pays $150K to $1M/year, and a 30-day roadmap to break into it.

This is the most **directly career-actionable** source in the wiki for hcho.
The other career sources ([[zero-to-hireable-ai-engineer]], [[ai-era-50-career-tips]]) describe a general AI-engineer path.
This one describes a specific, well-paid role whose two required capabilities - deployment judgment and eval rigor - map unusually cleanly onto a hardware-validation background, and it supplies a 30-day plan for manufacturing the proof before you have the title.

**The core argument:** AI intelligence is now commoditized, because every company can access similar frontier models.
The competitive edge has therefore shifted to **deployment** - knowing *where, how, and why* to apply that intelligence inside a specific business.

## Key claims

### Intelligence is commoditized; deployment is the moat

- Frontier models release constantly, and the same foundational capability is available to any company that can pay for it.
Across ~50 enterprise clients Vas observes the same stack repeatedly: [[claude-code]], Cursor, GitHub Copilot.
- **"The edge is no longer who has the intelligence. It's where, how, and why they use it."**
- The FDE's core job is bridging general-purpose AI capability with a specific company's unique processes, systems, and context, because every business runs differently even for the "same" function - accounts payable can be a 10-step or 30-step process depending on the company.
- The term was **popularized by Palantir**, which built a software **ontology** (connectors and data links piping enterprise data into a unified interface) and deployed FDEs **on-site** at enterprise and government clients to learn workflows and then build workflows, dashboards, and agents.
Palantir essentially reinvented **consulting for the software space**.

### The three stages of an engagement

**Stage 1 - understanding the business reality.**
Going deep into *how work actually happens today*, not the documented process.
Interviews, observation, and access to systems (ERPs, CRMs).
Communication and analytical ability are **critical**, and "this is where the bulk of the time goes in my opinion."
FDE work is usually best done **on-site**: being present for a full 8-10 hour day rather than a 1-hour interview surfaces undocumented exceptions and edge cases people forget to mention.

**Stage 2 - FDE judgment.**
Deciding **where intelligence belongs and where it doesn't.**
Early in the AI wave teams over-applied AI to everything, which led to token maxing and hallucinations.
Cited stat: **95% of generative AI pilots fail** (an MIT figure as referenced by Vas).
Of a 10-step workflow, maybe only **2-3 steps genuinely need LLM judgment**; the rest can be if/else logic and API calls.
Not every workflow needs AI - sometimes it's too risky, not high-ROI enough, or already automated.

**Stage 3 - building the deployed system.**
Highly variable: at Palantir some FDEs mostly configure workflows and dashboards within the ontology (light coding, mostly SQL), while other companies require full production code.
Regardless of coding depth, FDEs need strong technical understanding because **they're accountable when something breaks in production** - "it's basically your ass on the line."

### Why FDEs are rare: two kinds of judgment

- **Commercial/business judgment:** workflows, cost, incentives, risk, adoption, business value, internal politics.
Strong in consultants (McKinsey, BCG, Bain engagement managers).
- **Technical judgment:** models, systems, APIs, data, code reliability, evals, guardrails, harnesses, post-training, fine-tuning.
Strong in software engineers.
- An FDE must be the **best combination of both** - not an average, not "good enough" at either side.
"That is the million-dollar hire where the FDE can turn business understanding into working software end to end."
- **Caution:** as FDE hiring accelerates, many entrants are strong in only one dimension - good communicators who can't code, or good engineers who can't communicate.
Vas "strongly urges" people to actively strengthen whichever side is weaker.
- Compensation: **$150,000 base with considerable equity**, up to **as high as $1 million/year** for top performers who combine consulting and technical skill.

### The real workflow, not the documented one

- Illustrative example: "an email arrives" sounds like a simple trigger, but in reality it arrives from 40+ senders with no consistent formatting, the data comes as PDF / screenshot / Excel / buried in a forwarded thread, many steps are exceptions ("ignore the second attachment," "Sarah already signed off on this one"), there's no consistent subject line to route by, and **the real logic often lives in one person's head and isn't written down anywhere**.
- The same complexity repeats at every downstream step.
- **A useful probe:** ask people how easy it would be for *them* to write down every exception in their own job.
Vas uses his own experience at Meta - his official job description ("I code all day") omits meetings, production incidents, and firefighting.
- Once the real workflow is understood, the FDE decides: where does deterministic software live, where does the agent act, where does a human approve, and where does the record get updated?
- **Recommended architecture:** deterministic software handles the majority of steps, LLM/API calls provide judgment where needed, and **human-in-the-loop approval** is inserted before the agent proceeds to the back half of the workflow.
Vas "strongly recommends" all his FDEs push for that approval step: intake, validation, agent drafting, **human approval**, remaining steps execute.

### Audit → Eval → Deployment

Described by Vas as the single most important framework in the conversation: "If I had to put one page cemented, burned in everyone's brain, it's this one."
Each stage is a **prerequisite** for the next.

**Phase 1 - Audit.**
Collect context, trace findings, identify bottlenecks, repetitive work, and judgment points.
Produce an **operating map** showing current-state and future-state workflows.
**Sell the audit, don't give it away** - Vas says some clients told him the audit alone was worth **10x** what they paid for it, and it's "better than McKinsey because it's so telling."
Note the host's rebranding tip: his agency found clients had an "allergic reaction" to the word *audit* (they associate it with a tax audit), and rebranding it as a **"sprint"** tested better.

**Phase 2 - Eval.**
Prioritize high-volume workflows where improvement is large enough to matter.
Build a decision matrix: is it safe to act on autonomously, or should it route to a human?
Produce a formal **evaluation report** with pass/fail rates and categorized failure reasons.
Example framework: run 50 test cases, 41 pass and 9 fail, then categorize the failures (5 had missing data, 4 pulled the wrong record) and use that categorization to drive system improvements.

**Phase 3 - Deployment.**
**Build on top of existing systems - never force a migration.**
His concrete example: a client spent multiple years and several million dollars migrating to **NetSuite**; telling them they now need to move *off* NetSuite would fail immediately ("they're going to tell you to get lost").
Instead integrate with NetSuite, Salesforce, SAP, Concur, Expensify, Gong, Workday.
Roll out gradually: sandbox/controlled testing, shadow mode, increasing autonomy, full production.

- **The loop repeats continuously.** Once one workflow improves, the next bottleneck becomes obvious, which is why AI adoption tends to spread across an organization rather than staying isolated.

### Building evals for non-deterministic tasks

- For deterministic tasks ("was this email categorized correctly") evals are easier, because you can validate against historical data - e.g. 10,000 past emails.
- For creative tasks ("create a presentation") success is subjective.
The move is to use as much historical data as possible to build a **golden dataset** of what good output looks like - e.g. 5,000 past presentations, from which you derive rules like "always put the logo top-left" and consistent font sizing.
- Even with a strong golden dataset and good evals you still need **human-in-the-loop feedback** as an ongoing mechanism, to improve the harness and/or fine-tune the model over time.
- **On model agnosticism, Vas gives deliberately opposite advice to companies and individuals.**
Varick Agents as a company is model agnostic, believing value comes from switching models to improve accuracy and lower cost.
But **for an individual starting out: pick one model and one agent-building platform and get very good at it first**, then branch out.
"Don't put the cart ahead of the horse."
Your real value transfers across any model anyway.

### The 30-day roadmap

Vas's condensed version of what he learned over a year: build a complete FDE case study from scratch, **before** you have the job title, in order to get hired.

**Week 1 - build a working agent.**
An agent that completes **one real enterprise workflow** end to end (finance, HR, procurement, logistics, IT, sales - any back-office function).
Core building blocks, roughly one per day: agent looping, tool usage, guardrails, context and memory, and an **audit trail** logging every prompt, response, tool call, and error.
**"If you can't show the client what the agent is doing, they will never trust you."**
Checkpoint: a working agent with tools, guardrails, deliberate memory, and a full audit trail for one task.

**Week 2 - make it production-ready (recoverable).**
Use a **defined JSON schema**, not free-form text, and validate every response against it.
Build explicit failure handling for missing data, malformed responses, dead APIs, timeouts, and partial completions.
Add **checkpointing** so the agent resumes after a failure rather than restarting.
**His core philosophy:** "There's only one way that something can go right, but there's a thousand different ways something can go wrong. So if you're only building for the way it goes right, you're worth nothing. If you're solving for all the exceptions, that's where you are worth something."
Checkpoint: a resumable agent with structured outputs, state recovery, and explicit failure behavior.

**Week 3 - measure and optimize.**
Build a **golden dataset of 20+ real queries** with evals for correctness, format, tool selection, and escalation behavior.
Optimize cost by routing simpler subtasks to cheaper models.
Only add multi-agent coordination when decomposition genuinely helps.
**Measure impact across exactly three buckets: revenue uplift, risk mitigation, and cost savings** - Vas states these are the only three categories that matter to a business.
Checkpoint: an evaluated agent with known failure modes, measured cost, and a golden dataset.

**Week 4 - communicate and defend.**
Document the pain point, why AI belongs there, the architecture, and the iteration history (e.g. "accuracy went from 70% to 95%").
**Rehearse the pitch two ways: as an engineer** (architecture, decisions, tradeoffs) **and as a VP** (problem, outcome, evidence, risk).
Actually pitch it to real businesses during this week; they'll tell you directly whether your economics and framing are right.
Checkpoint: a complete FDE case study, defensible to both engineers and executives.

**The whole point:** "Do the job before you have the title."

### Selling and positioning

- People inside a company are motivated by **not wanting to look bad and wanting to get promoted** - frame the engagement around helping your internal champion get credit.
- Bringing in an FDE is inherently perceived as risk, so you must actively **de-risk** the engagement.
- **For people breaking in: do the first audit for free.**
Get your foot in the door, prove value, and only get paid once you've demonstrated measurable value.
Early customers "are genuinely worth more to you than you are to them"; after 2-3 proven engagements you can start charging.

## Connections

- [[forward-deployed-engineer]] - the role page; the source's primary contribution and a live career target for hcho.
- [[deployment-is-the-moat]] - the thesis that makes the role exist.
- [[audit-eval-deployment]] - the three-phase engagement loop, with eval as the load-bearing middle stage.
- [[real-workflow-not-documented]] - the discovery discipline; where the bulk of FDE time goes.
- [[two-kinds-of-judgment]] - commercial plus technical, and why "good enough at both" fails.
- [[solve-for-the-exceptions]] - "a thousand different ways something can go wrong"; **the closest thing in the wiki to a one-line statement of hcho's own QA thesis**.
- [[build-on-existing-systems]] - never force a migration; integrate with the ERP the client already paid millions for.
- [[do-the-job-before-the-title]] - manufacture the proof artifact before applying; sharpens [[t-shaped-portfolio]] and [[build-in-public]].
- [[eval-driven-development]] and [[evaluation-pipeline]] - the golden-dataset and categorized-failure-report method, stated from the client-facing side.
- [[phased-autonomy]] - **strong second source**: sandbox, shadow mode, increasing autonomy, full production, with human approval mid-workflow.
- [[single-call-workflow-or-agent]] - "only 2-3 of 10 steps genuinely need LLM judgment" is the same principle with a number attached.
- [[agent-observability]] - the audit trail as a *trust* requirement, not just a debugging one.
- [[agent-saas]] and [[outcome-based-pricing]] - the audit-then-implementation pricing ladder is the consulting form of that model.
- [[ai-career]] - the area this source most enriches.
- [[cost-of-being-wrong]] - enterprise back-office workflows as exactly the expensive-error domain that stays human-led longer.
- [[claude-code]], [[anthropic]], [[openai]] - entities.

**Cross-project:** this source justifies a new role page in the Job-Search Roles wiki (`projects/Job_Search/wiki/`), which as of this ingest covers Applied AI Engineer but not FDE.
FDE straddles hcho's two target buckets (AI builder and AI evals/quality) and the 30-day plan is a concrete portfolio spec.
Talking points belong in `projects/job-search/interview-prep.md` per the Mandu wikis convention, not duplicated here.

## Source

- **Author:** Vas, founder of Varick Agents; interviewed by a host addressed as "Greg"
- **Title:** Forward Deployed Engineering: The Complete Playbook (FDE in 30 Days)
- **Format:** Podcast interview, ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/FDE_in_30_Days_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix, which notes that a companion document ("FDE_Starter_Plan.pdf" / Varick's FDE in 30 Days guide) was used to confirm the spellings of Vas, Varick Agents, and NetSuite.
Two model names are flagged unresolved: "GPT 5.6 Soul" and "Muse Spark."
Captions repeatedly rendered **FDE** as "FTE," which normally means Full-Time Employee; the appendix treats this as a captioning confusion.

Two numbers should be treated as reported rather than verified: the **95% of generative AI pilots fail** MIT statistic is cited second-hand by Vas, and the **$150K-$1M** compensation range is his own characterization of the market, not survey data.
The Audit → Eval → Deployment framework is presented by Vas as his team's original framing developed at Varick Agents, not an industry standard.
