---
type: source
tags: [solo-building, skills, worktrees, adversarial-review, design, monetization]
date: 2026-07-03
title: "Building 5 AI Products Solo, with Agents"
author: "Josh Pigford (@Spigford), interviewed by Peter"
url: ""
concepts: [agentic-coding-workflow, agent-skills, evals-for-agents, parallel-agent-orchestration, context-engineering, agents-as-labor, human-taste-and-ai-slop]
---

# Building 5 AI Products Solo, with Agents

An interview with solo founder Josh Pigford (sold Baremetrics for $4M) on his AI-assisted build workflow: research -> plan -> implement in isolated git worktrees, cross-model adversarial review, self-updating config, hand-crafted branding, and a launch-fast philosophy.
The mechanics run on a library of mostly open-source "skills" that orchestrate coding agents.

## Key claims

- Ship fast and learn from real users instead of over-planning; he has launched products within 24 hours, sometimes same-day, and builds the full product rather than testing demand with an email-capture landing page.
- The open-source build skill has research, planning, and implementation phases. Implementation is broken into small, individually user-testable phases, each one phase = one PR = one git branch; some plans run 30+ phases.
- Each phase runs in a fresh worktree with no prior context; a running progress/decisions file lets fresh sessions avoid repeating mistakes. Fresh context per phase reduces "context rot" so the model hallucinates less; worktrees double as rollback checkpoints.
- Cross-model adversarial review: Claude Opus builds, then GPT-5.5 runs an adversarial review of the worktree and "invariably finds 3-5 bugs Opus overlooked." This runs inside Conductor, which lets you set the review model and auto-manages worktrees (unique ports, env vars) for ~10 parallel agents.
- The learnings skill mines the worktree plus the actual chat transcript (including his repeated corrections) and appends lessons to CLAUDE.md, so the config improves automatically.
- The but-for-real skill "bullies" the model into re-reviewing its own work and reliably finds 3-5 more bugs, separate from the GPT review; much of the value is simply forcing a second pass. He iterates skill prompts in Chops ("be meaner").
- Branding is hand-made first: name -> logo (99% by hand in Illustrator) -> color scheme, all before any code; the marketing page is generated after the app is built, from brand assets plus the real feature set, to avoid "AI slop."
- Monetization rule: keep a paid tier for anything with hosting costs ("it's not a charity"); ultra-cheap plans generate the most support load, so price higher to filter.

## Connections

- [[agentic-coding-workflow]] - the research -> plan -> implement build skill, phase = PR = branch, and progress/decisions files.
- [[agent-skills]] - his ~dozen open-source skills (build, research, learnings, but-for-real, ui.sh, support) and Chops for iterating skill prompts.
- [[evals-for-agents]] - cross-model adversarial review and the but-for-real forced self-critique as bug-finding passes.
- [[parallel-agent-orchestration]] - Conductor's automated worktree setup (unique ports/env vars) running ~10 agents in parallel.
- [[context-engineering]] - fresh-worktree context per phase, "context rot," progress files, and the learnings skill auto-updating CLAUDE.md.
- [[agents-as-labor]] - running five products solo as a "garden," and the monetization/pricing discipline for AI products.
- [[human-taste-and-ai-slop]] - brand-first design, building marketing copy from real features, and 25 years of judgment as the real edge.

## Source

- **Author / channel:** Josh Pigford (@Spigford, blog everydayisayear.ai), interviewed by Peter
- **Title:** Building 5 AI Products Solo, with Agents
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/AI_Solo_Building_Tutorial_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
