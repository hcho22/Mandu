---
type: source
title: "Running a One-Person Company with AI Agents"
source-type: tutorial-summary
author: "Ryan Carson (Untangled)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [agent-ops, solo-building, agents, cron, skills, agent-safety]
---

# Running a One-Person Company with AI Agents

A summarized walkthrough of how solo founder [[ryan-carson]] runs an entire startup (engineering, marketing, sales, ops) with AI agents instead of employees, using Open Claw ([[open-claw]]), Devin ([[devin]]), and Codex.
Central thesis: [[agents-as-cron-plus-markdown|agents are just cron jobs and markdown files]]. The honest caveat, repeated throughout: the setup is genuinely hard and fiddly.

## Key claims

- **An agent = a good cron (when it runs) + a good skill file (how it works).** He open-sourced "Claw Chief," an EA/chief-of-staff layer that is just markdown files + crons; a "priority map" file (long-term priorities, not a weekly task list) is the single most important file.
- **Crons over heartbeats:** heartbeats are not reliably time-triggered ("whenever I think about it"); a cron is deterministic and repeatable. Build your own heartbeat as a minimal cron that points at one skill (DRY: detail lives once, in the skill).
- **[[agent-as-employee]]:** give the agent its own real identity (email on your domain, its own GitHub) and scoped permissions - read access where an EA would have it, write "as itself," never impersonating you.
- **[[red-team-your-agent]]:** he had the interviewer and his sisters try to prompt-inject R2; it held up, leaking nothing.
- **Be overly specific and pedantic** in instructions (things you would never tell a human, like "always check if you've emailed this person"); do it once and never again. A stray "CC my other account" line caused a confusing hard-to-diagnose bug - the agent follows instructions literally.
- **Don't build a custom harness:** stick with out-of-the-box Open Claw + custom skills/crons, or "you end up maintaining it instead of working." "Buy a couple tools off the shelf, get a custom drill, but don't build a custom machine." Constantly switching agents to optimize them "is not real work."
- **Engineering in the cloud (Devin), no local dev:** a fresh cloud VM per task removes local headaches; "Schedules" run "playbooks" (skill-like docs) - e.g. a weekly full-journey coverage run and smoke tests.
- **[[everything-is-a-pr]]:** run a full SDLC "designed for a very large team" even solo, with reproducible processes that do not depend on you; a "land PR" playbook merges 10-20x/day. He reads PRs and markdown, rarely code.
- **[[build-the-machine-first]]:** most of the work now is building the system that does the work - the inverse of old MVP advice. Invest up front in SDLC, docs, and reference files; understand and do every job before hiring an agent-augmented human. He raised a $2M seed but plans not to hire for a while.
- **Go-to-market is the hard part:** building features is "almost trivial"; getting users and revenue is the skill. Marketing is automated too (a Google Ads CLI built by Devin; a nightly content playbook using Gemini ([[google]]) + an OpenAI ([[openai]]) image model + Publer).
- **Design:** pay a good human designer for the first cut, then reproduce the brand with a `design.md` + reference images ("instruction file + references," the same pattern used everywhere).

## Connections

- [[agents-as-cron-plus-markdown]], [[agent-as-employee]], [[build-the-machine-first]], [[everything-is-a-pr]], [[red-team-your-agent]] - the ops concepts.
- [[capabilities-not-instructions]] - agent-as-employee is the identity/permissions side of the same safety rule; the literal-instruction bug is a vivid example.
- [[building-skills]] - Claw Chief skills, Devin playbooks, and minimal crons are all skills/instruction files.
- [[phased-implementation]] / [[adversarial-code-review]] - everything-is-a-PR extends the same code-factory discipline.
- [[taste-as-moat]] / [[ai-slop]] - "pay a designer for the first cut, then reproduce with design.md + references."
- [[ship-fast-learn-from-users]] vs [[build-the-machine-first]] - two agentic-ops takes that both invert classic MVP advice (see synthesis).

## Source

- **Author:** Ryan Carson (founder of Untangled, a family-law product); interview/walkthrough
- **Title:** Running a One-Person Company with AI Agents
- **Tools cited:** Open Claw, Claw Chief, Devin, Codex (GPT-5.5), Firecrawl, Todoist, Google Sheets (CRM), Descript, Gemini, OpenAI image model, Publer, WhisperFlow, Agent Mail, Design Joy, Tailscale/SSH.
- **Raw:** [[AI-Agent-Solo-Founder-Tutorial-Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
