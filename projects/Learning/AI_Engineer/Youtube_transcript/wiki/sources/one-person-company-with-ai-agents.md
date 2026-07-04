---
type: source
tags: [solo-founder, cron, skills, agent-identity, cloud-dev, gtm]
date: 2026-07-03
title: "Running a One-Person Company with AI Agents"
author: "Ryan Carson (Untangled)"
url: ""
concepts: [agentic-coding-workflow, agent-skills, scheduled-agent-autonomy, agent-permissions-and-safety, production-agent-infrastructure, agents-as-labor]
---

# Running a One-Person Company with AI Agents

A walkthrough of how solo founder Ryan Carson runs an entire startup - engineering, marketing, sales, ops - using AI agents instead of employees, built on the mantra that agents are "cron jobs and markdown files."
It covers a self-built EA/chief-of-staff layer, cron-driven skills, Slack as the control surface, scoped agent identity, and a Devin-based cloud engineering stack.

## Key claims

- An agent = a good cron (when it runs) + a good skill file (how it works). Nail those two and the agent can do a lot; he ships "at least 10 PRs a day, sometimes a lot more." Onboarding agents is far easier than humans, but the setup is genuinely hard and fiddly.
- He open-sourced "Claw Chief," a set of markdown files plus crons that turns his agent into an EA. The most important file is the priority map (long-term projects and people), alongside an auto-resolver and an agents.md.
- Crons vs. heartbeats: heartbeats are not reliably time-triggered ("whenever I think about it"); a cron is deterministic and repeatable. He builds a custom "heartbeat" as a 15-minute cron pointing at one skill, following DRY (the cron is minimal, all detail lives in the skill).
- Treat the agent like a real employee with its own scoped identity: its own email address and GitHub account, read access to email/calendar, and write access "as itself," never impersonating him. He red-teamed it (even asked his sisters to hack it) and it resisted prompt injection.
- Engineering runs on Devin with no local development: Devin spins up a configured production VM per task, eliminating local environment headaches, and provides reliable in-cloud browser testing. Schedules run playbooks (skill-like docs) - e.g., a weekly full user-journey run and smoke tests.
- Everything is a PR: he runs a full SDLC "designed for a very large team" though solo, because agents need reproducible processes that do not depend on him; he reads PRs and markdown, rarely code.
- Go-to-market is now the hard part: a daily prospecting skill finds and emails verified prospects (logged in a Google Sheet CRM via Firecrawl), and a nightly content playbook chops interviews and publishes via Publer.
- Build the machine first: invest heavily up front in SDLC, docs, and reference files wired into crons and skills, then augment with more agents or an agent-augmented human. This inverts old "bare-minimum MVP" advice.

## Connections

- [[agentic-coding-workflow]] - "everything is a PR," a solo-run full SDLC, voice-brain-dump -> PRD skill -> build, and the land-PR playbook.
- [[agent-skills]] - "agents are markdown files," Claw Chief skills, priority map / auto-resolver, and playbooks as skills.
- [[scheduled-agent-autonomy]] - crons vs. heartbeats, the 15-minute EA sweep, DRY crons, and Devin schedules running playbooks.
- [[agent-permissions-and-safety]] - scoped agent identity (own email/GitHub, write-as-itself), red-teaming, and check-if-you-emailed-before guardrails.
- [[production-agent-infrastructure]] - Devin's per-task cloud VMs, reliable in-cloud browser testing, and cloud-only engineering.
- [[agents-as-labor]] - the one-person-company thesis, doing the work of ten people, and build-the-machine-then-hire.

## Source

- **Author / channel:** Ryan Carson (founder, Untangled)
- **Title:** Running a One-Person Company with AI Agents
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/AI-Agent-Solo-Founder-Tutorial-Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
