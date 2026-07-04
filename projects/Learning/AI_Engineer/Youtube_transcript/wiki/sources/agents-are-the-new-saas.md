---
type: source
tags: [agents, agent-as-labor, business-model, evals, gtm]
date: 2026-07-03
title: "Agents Are the New SaaS"
author: "Startup Ideas Podcast"
url: ""
concepts: [agents-as-labor, evals-for-agents, agent-permissions-and-safety]
---

# Agents Are the New SaaS

A Startup Ideas Podcast episode arguing that software is shifting from "help me do the work" to "do the work with me," so the sellable unit becomes a completed job rather than a tool.
It lays out an 8-part playbook for finding a repetitive paid workflow, shadowing the human who does it, building the smallest useful agent, wrapping it in a trust-building product layer, and selling pilots as labor, capped by a 30-day build plan.

## Key claims

- SaaS sells software; agent SaaS sells work. The buyer is offloading a task, not buying capability, and the addressable market is labor (human capital) rather than software seats.
- Pick a workflow with a paycheck attached, scored on five traits: it happens constantly, has a clear finish line, touches existing software, has annoying-but-learnable edge cases, and the buyer can feel the loss.
- Shadow the human across 10-20 real jobs before building; the hidden detail is the product. Distill it into a 7-part agent spec: trigger, context, tools, allowed actions, where approval is needed, when to escalate to a human, and what success looks like.
- Build the Minimal Useful Agent (MUA), not a fully autonomous "employee." The ladder is draft -> triage -> coordinate -> act; per Anthropic guidance, start as a predictable workflow and earn autonomy.
- The product wrapper (logs, approvals, handoff rules, a test surface) is what makes it SaaS: the agent does the work, but the "control room" creates trust.
- Evals are the agent's "gym": take ~50 real examples of the job, mark the right answers, and score the agent (e.g., 42 correct / 6 flagged / 2 wrong). Every prompt/model/tool change sends it back through the gym, and the results double as a sales asset.
- Sell pilots like labor first (run it manually with AI for three customers in one niche), then productize the repeated pattern; move toward outcome-based pricing only once value is understood.
- Distribution runs on "workflow teardowns": show the painful old way, then the agent way. Sell painkillers, not vitamins.

## Connections

- [[agents-as-labor]] - the core "sell work, not software" thesis, the MUA ladder, the product wrapper, and outcome pricing.
- [[evals-for-agents]] - the 50-example "gym," pass/flag/fail scoring, re-running on every change, and evals as a trust/sales artifact.
- [[agent-permissions-and-safety]] - the 7-part spec's allowed-actions, approval, and escalation boundaries as a human-in-the-loop control model.

## Source

- **Author / channel:** Startup Ideas Podcast
- **Title:** Agents Are the New SaaS
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Agents-Are-the-New-SaaS_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
