---
type: concept
tags: [ai-career, fde, evals, framework, consulting, deployment]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Audit → Eval → Deployment

The three-phase engagement loop from [[fde-in-30-days]], which Vas calls the single most important framework in the conversation:
"If I had to put one page cemented, burned in everyone's brain, it's this one."

**Each stage is a prerequisite for the next.**

## Phase 1: Audit

Collect context, trace findings, identify bottlenecks, repetitive work, and judgment points.
Produce an **operating map** showing current-state and future-state workflows.

- **Sell the audit; don't give it away as a throwaway step.**
Vas says some clients told him the audit alone was worth **10x** what they paid, and that it's "better than McKinsey because it's so telling."
- **Naming caution:** the host's agency found clients had an "allergic reaction" to the word *audit* - they associate it with a tax audit.
Rebranding it as a **"sprint"**, framed like a design sprint, tested better.

## Phase 2: Eval

- Prioritize **high-volume** workflows where improvement is large enough to matter.
- Build a **decision matrix**: is this safe to act on autonomously, or should it route to a human?
- Produce a formal **evaluation report** with pass/fail rates and **categorized failure reasons**.

The worked example: run 50 test cases, 41 pass and 9 fail, then categorize the failures - 5 had missing data, 4 pulled the wrong record - and use that categorization to drive system improvements.

For non-deterministic tasks, build a **golden dataset** from historical data: 5,000 past presentations yield rules like "always put the logo top-left."
Even with a strong golden dataset you still need **human-in-the-loop feedback** as an ongoing mechanism.

## Phase 3: Deployment

- **Build on top of existing systems, never force a migration** ([[build-on-existing-systems]]).
- Roll out gradually: sandbox/controlled testing → shadow mode → increasing autonomy → full production.
- Deployment includes **client handholding and adoption**, not just technical monitoring (KPIs, SLAs).

## The loop repeats

Once one workflow improves, the next bottleneck becomes obvious.
This is why AI adoption tends to spread across an entire organization rather than staying isolated to one workflow - and why the engagement model is a subscription rather than a project.

## Synthesis

The structurally important claim is that **eval is the load-bearing middle stage of a commercial engagement**, not a quality step at the end.
You cannot deploy without it because the eval report *is* the artifact that earns the client's trust to grant autonomy.

That reframes evals from an engineering practice into a **sales instrument**, which the wiki has seen once before - [[agents-are-the-new-saas]] frames an eval set of 50 real examples as the agent's "gym" *and* a sales asset.
Two independent sources converging on that is worth noting: the eval suite is what you show the buyer.

The pass/fail-with-categorized-failures format is also exactly [[pass-fail-over-score-evals]] plus a failure taxonomy, which is what [[looking-at-your-data]] produces when done properly.
The framework is therefore not new eval science; it is the wiki's existing eval discipline packaged into a commercial motion with a price attached.

For hcho the immediate use is as a **structure for the Agentic RAG buyer interviews**.
The 10 interviews currently sit as an undifferentiated goal; running them as free Phase-1 audits gives the conversation a reason to exist from the buyer's side, produces an artifact they value, and generates exactly the deployment knowledge [[deployment-is-the-moat]] says the product needs.
The "permission-RAG teardown" on-ramp already in the validation plan is this, unnamed - and per the naming caution, "teardown" is likely a better word than "audit" anyway.
