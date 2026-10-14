---
type: concept
tags: [ai-career, role, fde, deployment, evals, job-search]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Forward Deployed Engineer (FDE)

An engineer embedded **inside a client's business** to figure out where AI belongs in their actual workflows, then build and deploy it there.

The term was **popularized by Palantir**, which built a software **ontology** - connectors and data links piping enterprise data into a unified interface - and deployed FDEs **on-site** at enterprise and government clients to learn their workflows, then build the workflows, dashboards, and agents that solve specific problems.
Palantir essentially reinvented **consulting for the software space**: a centralized platform, customized per client by engineers on the ground.

Documented in [[fde-in-30-days]] by Vas of Varick Agents.

## The three stages of an engagement

1. **Understand the business reality.**
Going deep into *how work actually happens today*, not the documented process ([[real-workflow-not-documented]]).
Interviews, observation, and access to ERPs and CRMs.
"This is where the bulk of the time goes."
Best done **on-site** - a full 8-10 hour day surfaces exceptions a 1-hour interview never will.
2. **FDE judgment.**
Deciding **where intelligence belongs and where it doesn't.**
Of a 10-step workflow, maybe only **2-3 steps genuinely need LLM judgment**; the rest is if/else logic and API calls.
Not every workflow needs AI - sometimes it's too risky, not high-ROI enough, or already automated.
3. **Build the deployed system.**
Highly variable: at Palantir some FDEs mostly configure workflows and dashboards (light coding, mostly SQL), while other companies require full production code.
Regardless of depth, FDEs need strong technical understanding because **they're accountable when it breaks in production** - "it's basically your ass on the line."

## Why the role exists now

Because [[deployment-is-the-moat]]: frontier intelligence is commoditized, so the edge moved to knowing *where, how, and why* to apply it inside a specific business.

## Why it's rare, and what it pays

The role requires [[two-kinds-of-judgment]] - commercial and technical - and the **best combination of both**, not an average.
Vas puts the range at **$150,000 base with considerable equity** up to **as high as $1 million/year** for top performers, and warns that as hiring accelerates most entrants are strong in only one dimension.
(Both figures are his characterization of the market, not survey data.)

## Method

The engagement runs on [[audit-eval-deployment]], with [[build-on-existing-systems]] as the non-negotiable deployment constraint and [[solve-for-the-exceptions]] as the philosophy of what makes the work valuable.
The entry path is [[do-the-job-before-the-title]].

## The marketing version (2026-10-14)

[[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]] (Marketing wiki) names a "forward deployed marketer," also called a [[projects/Education/Marketing/wiki/concepts/marketing-engineer|marketing engineer]]: someone who embeds with a founder's company for 30, 60, or 90 days, builds one growth system, and sells the outcome at $5K, $10K, or $30K per month.
The speaker explicitly compares the earning ceiling to today's forward deployed engineers.
The shape matches this page (embed, build one workflow next to revenue, productize what repeats), and the evidence is weaker: a forecast by [[greg-isenberg]], with no market data behind the pay figures.

## Synthesis

This is the most **directly relevant role page** in the wiki for hcho's job search, and it is worth stating why plainly.

The role's two halves are deployment judgment and eval rigor.
The eval half is hcho's declared edge and the explicit reason the pivot narrative works at all.
The other half - going on-site, watching how work actually happens, cataloguing every exception, and being accountable when it breaks in production - is a description of hardware validation and QA at a customer-facing company, which is what he did for a decade at Zebra.
**FDE is unusual among AI roles in that it rewards the non-AI half of his background rather than discounting it.**

It also straddles the two-bucket targeting rather than forcing a choice: FDE is an AI builder role *and* an evals/quality role, since [[audit-eval-deployment]] puts eval construction at the load-bearing middle of every engagement.

Honest caveats before treating this as a target:
the role is heavily client-facing and often travel-heavy, which is a real lifestyle constraint;
compensation figures come from one founder with an interest in the role sounding attractive;
and "FDE" is used loosely enough across companies that the title alone doesn't tell you whether the job is engineering or configuration.

Actions this suggests, which belong outside this wiki:
a role page in the Job-Search Roles wiki (`projects/Job_Search/wiki/`), which currently covers Applied AI Engineer but not FDE;
FDE-titled roles added to the job-hunter target list;
and the [[do-the-job-before-the-title]] case-study spec assessed against the existing Agentic RAG work, which already covers much of its Week 1-3 checklist.
