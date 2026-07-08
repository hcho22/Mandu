---
type: source
title: "Building 5 AI Products Solo, with Agents"
source-type: tutorial-summary
author: "Josh Pigford (interviewed by Peter)"
url: "https://everydayisayear.ai"
date-ingested: 2026-07-08
date-created: unknown
tags: [solo-building, agentic-engineering, code-review, worktrees, skills, ship-fast]
---

# Building 5 AI Products Solo, with Agents

A summarized interview with solo founder [[josh-pigford]] (sold Baremetrics for $4M) on his AI-assisted build workflow: research to plan to implement in isolated git worktrees, cross-model adversarial review, self-updating config, hand-crafted branding, and a ship-fast philosophy.

## The workflow (a library of open-source skills)

- **Build skill:** [[phased-implementation]] - research produces a high-level doc, then work is broken into small, individually testable phases where each phase = one PR = one git branch (some plans run 30+ phases). A progress/decisions file carries context forward.
- **Isolated worktrees:** each phase runs in a fresh git worktree with no prior context, which reduces [[context-rot]] (so the model hallucinates less), and each worktree is a shippable unit and a rollback checkpoint. Managed by [[conductor]] (model switching + automated worktree setup: unique ports, env vars, ~10 in parallel).
- **Adversarial code review:** Claude Opus ([[anthropic]]) builds; GPT-5.5 ([[openai]]) reviews the worktree and "invariably finds 3-5 bugs Opus overlooked." See [[adversarial-code-review]].
- **but-for-real skill:** a forced self-critique that assumes the model broke something and makes it re-check - finds another 3-5 bugs, separate from the GPT review. Also filed under [[adversarial-code-review]].
- **Learnings skill:** [[self-updating-config]] - after a phase ships, it mines the worktree plus the actual chat transcript (including his repeated corrections) and appends the lessons to `CLAUDE.md` so the config improves automatically.
- Config is auto-generated from a shared template (stack: Rails + Inertia + Postgres), not hand-typed.

## Key claims

- **Ship fast, learn from real users** ([[ship-fast-learn-from-users]]): launch in days not months, often within 24 hours; build the whole product rather than an email-capture landing page (cheap now with AI); real users reveal edge cases you cannot predict.
- **A second, different model reliably catches bugs the first missed** - the core of adversarial review; treat the AI like a PR reviewer.
- **Brand first, by hand:** name to logo (~99% hand-done in Illustrator) to colors, all before any code; the marketing site comes after the app is built so copy reflects real features. This is deliberate anti-[[ai-slop]] craft.
- **Monetization:** keep a paid tier for anything with hosting costs ("it's not a charity"); ultra-cheap plans create disproportionate support load, so price higher to filter (ties to [[outcome-based-pricing]]).
- Advice for non-technical builders: fail fast, recognize each mistake, ship in days.
- His edge is 25 years of pre-AI experience: AI levels the field, but judgment about what will work still separates him.

## Connections

- [[phased-implementation]], [[context-rot]], [[adversarial-code-review]], [[self-updating-config]] - the workflow mechanics.
- [[skill-eval-loop]] / [[evals]] - adversarial review and self-critique are the same verify-your-AI-output discipline at the code level; hcho's validation edge.
- [[building-skills]] - his ~dozen open-source skills are a worked instance; the learnings skill is [[building-skills|skills that improve themselves]] applied to config.
- [[ai-slop]] / [[taste-as-moat]] - brand-first design as slop avoidance.
- [[ship-fast-learn-from-users]] connects to [[minimal-useful-agent]] and [[build-in-public]].
- [[conductor]], [[josh-pigford]], [[openai]], [[anthropic]], [[claude-code]] - tools and people.

## Source

- **Author:** Josh Pigford (@Spigford; blog everydayisayear.ai), interviewed by Peter
- **Title:** Building 5 AI Products Solo, with Agents
- **Products cited:** Proxy User, Rumored, Reply/Reply Social, Clearly, a family health tool; former Baremetrics (sold $4M) and BotBlock.
- **Tools cited:** Claude Opus, GPT-5.5, Conductor, Context7, Chops (skill editor), Adobe Illustrator; Rails + Inertia + Postgres.
- **Raw:** [[AI_Solo_Building_Tutorial_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
