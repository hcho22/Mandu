# Building 5 AI Products Solo, with Agents

**Video Tutorial · Detailed Summary**

An interview with solo founder **Josh Pigford** (sold Baremetrics for $4M) walking through his AI-assisted build workflow — research → plan → implement in isolated git worktrees, multi-model adversarial review, self-updating config, design, and a launch-fast philosophy. Interviewed by Peter.

`8 chapters` · `Speaker: Josh Pigford (@Spigford)` · `Host: Peter` · `Topic: AI-assisted solo building`

---

## Overview

Josh Pigford builds at least five AI products in parallel as a solo founder. His central thesis: **ship fast and learn from real users instead of over-planning**. The mechanics behind that speed are a library of reusable, mostly open-source "skills" that orchestrate AI coding agents — a **build skill** (research → plan → implement in small, testable phases), a cross-model **adversarial code review** (Claude Opus builds, GPT-5.5 reviews), a **learnings skill** that updates his config automatically, and a **but-for-real skill** that forces the model to re-check its own work. He also covers hand-crafted branding to avoid "AI slop," monetization rules, support automation, and advice for new builders: fail fast and ship in days, not months.

> **How to read this:**
> - **`[Opinion]`** = the speaker's personal take / preference
> - **`[General rule]`** = a broadly-applicable principle
> - **🟡 Tips & Tactics** callout = actionable advice
> - **🔵 Tools & Skills** callout = named tools to scan

---

## Table of Contents

1. [Why launching fast beats months of planning](#1-why-launching-fast-beats-months-of-planning) *(0:00)*
2. [A tour of the 5 AI products Josh built solo](#2-a-tour-of-the-5-ai-products-josh-built-solo) *(1:02)*
3. [The *build* skill: research, plan, track, implement](#3-the-build-skill-research-plan-track-implement) *(5:22)*
4. [The *adversarial-code-review* skill: GPT reviewing Opus' code](#4-the-adversarial-code-review-skill-gpt-reviewing-opus-code) *(10:52)*
5. [The *learnings* skill: making AI update its own CLAUDE.md](#5-the-learnings-skill-making-ai-update-its-own-claudemd) *(16:02)*
6. [The *but-for-real* skill: making AI fix its own mistakes](#6-the-but-for-real-skill-making-ai-fix-its-own-mistakes) *(16:47)*
7. [Live demo: designing non-"AI slop" websites](#7-live-demo-designing-non-ai-slop-websites) *(19:11)*
8. [Advice for builders without technical experience](#8-advice-for-builders-without-technical-experience) *(28:55)*
- [Appendix: Tools, skills & resources reference](#appendix--tools-skills--resources-reference)

---

## 1. Why launching fast beats months of planning
*Chapter 1 · 0:00*

**Key points**

- Josh has been building and launching for **25 years** and has shipped **hundreds of products**. Every launch still triggers the same fear: "what if zero people care?"
- He calls himself "textbook ADHD," which suits running many projects at once — agents let him "feed the beast a little bit more."
- His core loop: **Claude Opus** does the bulk of the work, then **GPT-5.5** does a review pass that "invariably finds three to five bugs that Opus overlooked," and finally his **but-for-real** skill pushes the model to re-check itself.
- He has launched products **within 24 hours — sometimes same-day**.

> **🟡 Tips & Tactics**
> - Don't spend months building before exposing a product to real users. **`[Opinion]`** (stated as a firm rule of thumb)
> - Always run the builder model's output past a *different* model — a second model reliably catches bugs the first missed.

> **🔵 Tools & Skills:** Claude Opus · GPT-5.5 · but-for-real skill

---

## 2. A tour of the 5 AI products Josh built solo
*Chapter 2 · 1:02*

**Key points — the products**

- **Proxy User** (launched the day of recording) — synthetic users that drive *real browsers* to QA your app; returns a screen recording of it working or breaking so you can fix issues fast.
- **Rumored** (launched the prior Friday) — catches LLMs hallucinating about your brand so you can correct it: updating website copy, publishing blog posts, or adding schema markup. It monitors continuously and alerts you when something needs fixing.
- **Reply** (a.k.a. Reply Social; launched earlier in the year) — aggregates the replies and mentions of his products into one place so he can stay on top of them.
- **Family health tool** (built ~a month earlier) — built after his mother was diagnosed with stage 4 pancreatic cancer; lets relatives stay updated and chat with the medical documents. He built it because dumping everything into Claude Code didn't give family members access.
- **Clearly** (mentioned later) — an open-source Markdown editor that supports mermaid diagrams.

**On juggling many products**

- His ADHD means his brain "ping-pongs" naturally; agents let him run more at once. Trade-off: more mental fatigue from context-switching, but more *fulfillment*.
- **Baremetrics** (a business-analytics company) took ~**7 years** on a single product and he burned out on doing one thing.
- He concedes spreading thin may not be the optimal *business* move ("there's an argument that it's a terrible idea") but he optimizes for fulfillment and constant learning. **`[Opinion]`**
- Analogy he and Peter share: tending a garden of many plants ≈ growing many products at once.

> **🔵 Tools & Skills:** Proxy User · Rumored · Reply / Reply Social · Clearly · Claude Code

*Sponsor break (clearly marked, not tutorial content): **Whisperflow** — voice dictation to AI that removes filler words and formats text; works on Mac, Windows, iPhone, Android. Code **"peter whisperflow"** at whisperflow.com gives 6 months free.*

---

## 3. The *build* skill: research, plan, track, implement
*Chapter 3 · 5:22*

**Key points**

- The **build skill** is open source on **GitHub**. It has distinct phases — **research, planning, implementation** — each with its own instruction set.
- **Research** produces a high-level research document. Example: adding **BotBlock** into Reply Social. It pulled in his old codebase from the now-defunct BotBlock product (originally a **Chrome extension**), conceptually merged it with the Reply Social codebase, and researched the technical approach: needed API calls, pros/cons, what to ignore from the old extension, what to port, and how the systems interact.
- **Implementation** breaks the work into phases. In the example, **4 phases = 4 pull requests = 4 git branches** — never one massive pass, so each chunk is contained and verifiable.
- Phases are deliberately **user-testable**. Some implementation docs run to **30+ phases** because he wants to personally test each step. The build process can open a browser and run its own tests, but he is the final check — it has to "feel right" (speed, UX matching his mental picture).
- He scans generated docs quickly, focusing on the **objectives** more than the individual tasks.
- "Building a phase" (e.g., **"build phase one BotBlock"**) triggers *deeper* research for that chunk: web search, competitor analysis (who has the feature, how they built it), latest docs (often via **Context7**), plus a design pass using the **ui.sh** skill (colors, components).
- A **progress file** is updated after each step — what was done, decisions made, and lessons learned during iteration (it is never a one-shot).

**Why a fresh worktree per phase**

- Each new worktree starts with **no prior context**; the progress file lets it reference past and future phases and avoid repeating mistakes.
- He treats a worktree as a **shippable unit** and as a **rollback checkpoint** ("save points").
- Fresh context per phase reduces "**context rot**," so the model hallucinates much less.
- Every phase is "**100% a PR**."

> **🟡 Tips & Tactics**
> - Break features into small, individually **testable phases** — each one = a single PR / branch. Don't one-shot a large feature. **`[General rule]`**
> - Keep a running **progress / decisions file** so fresh agent sessions don't repeat past mistakes and know where they are in the plan.
> - Use isolated worktrees as **rollback checkpoints** and to avoid context rot.
> - Review the **objectives** of generated plans, not just the task lists.

> **🔵 Tools & Skills:** build skill (open source, GitHub) · Context7 · ui.sh skill · git worktrees / branches / PRs · agent browser

---

## 4. The *adversarial-code-review* skill: GPT reviewing Opus' code
*Chapter 4 · 10:52*

**Key points**

- Workflow: **Claude Opus** does the bulk and the first pass (planning + initial build). After code is built in a worktree, **GPT-5.5** runs an **adversarial review** of everything in the worktree and reliably finds **3–5 bugs** Opus overlooked; then it's merged.
- This runs inside **Conductor**, which exposes a "review" button and lets you set the **review model**. Using GPT-5.5 as the reviewer is simply what works best for him. **`[Opinion]`**
- Why Conductor over Codex / Claude Code: easy **model switching** + **automated worktree management**. Opening a worktree runs a setup command that assigns a **unique port** (so he can run ~**10 simultaneously**, each in its own browser), copies environment variables, and starts the needed processes.
- He uses this build/plan process for essentially **every feature**. For one-off requests (e.g., Clearly is open source with many GitHub feature requests via a **GitHub integration**), he uses a lighter **research skill** — e.g., a request to add a zoom feature to mermaid diagrams: attach the issue, the skill ingests the GitHub context + web/UI/doc search, proposes a plan, and he approves.
- The agent will browse competitor sites, browse Reddit, and take screenshots when it decides that's useful.
- **CLAUDE.md / config:** he keeps a project config generated from a shared template during setup (not hand-typed). His stack is **Rails + Inertia + Postgres**, so it's heavily Rails-focused: best practices, his testing approach (uses an agent browser), and project specifics like Conductor's unique ports. For a monorepo (web app + iOS app) it states where things live, which commands to use and when, and how to run tests.

*Peter's parallel anecdote: Substack has no public API, so to add "Sign in with Substack" (OAuth) to his own site, he had Codex research how others did it and figure it out.*

> **🟡 Tips & Tactics**
> - Have a **second, different model** adversarially review the primary model's code — it consistently catches missed bugs. **`[General rule]`**
> - Use a tool that **automates worktree setup** (unique ports, env vars, processes) so many agents run in parallel.
> - **Auto-generate your CLAUDE.md / agents file from a template**: include the stack, commands, test instructions, and tool-specific gotchas (e.g., Conductor ports).
> - For one-off feature requests, a lighter research skill that ingests the GitHub issue + web/UI research can produce an approvable plan.

> **🔵 Tools & Skills:** Claude Opus · GPT-5.5 · Conductor · Codex · Claude Code · GitHub integration · research skill · CLAUDE.md / agents.md · Rails + Inertia + Postgres · agent browser

---

## 5. The *learnings* skill: making AI update its own CLAUDE.md
*Chapter 5 · 16:02*

**Key points**

- A separate **learnings skill**, run after a phase is shipped. It reviews everything done in the worktree *plus the actual chat sessions* — including the repeated corrections he had to give ("no, that didn't work, try this") — and distills them into additions for the **CLAUDE.md** so the model stops repeating the same mistakes.
- Result: the CLAUDE.md is **continuously updated**. The skill is open source.

> **🟡 Tips & Tactics**
> - After finishing a phase, run a skill that **mines your correction history and session transcript**, then appends the lessons to CLAUDE.md — your config improves automatically over time.

> **🔵 Tools & Skills:** learnings skill (open source) · CLAUDE.md

---

## 6. The *but-for-real* skill: making AI fix its own mistakes
*Chapter 6 · 16:47*

**Key points**

- The **but-for-real** skill is run after plan + implement. It "bullies" the model — telling it that it almost certainly broke something and to go back over it — and reliably finds **3–5 bugs**, *separate* from the GPT-5.5 review. Much of the value is simply forcing the model to re-examine its own work.
- Mental model: like a human teammate reviewing a PR — a second set of eyes always finds something or suggests a different approach; here the AI plays the reviewer role.
- He manages skill files in **Chops**, an open-source Mac app. Chops has a built-in **AI iterator**: you can tell it "be meaner" and it rewrites the whole skill. He iterated on but-for-real this way rather than writing it by hand.
- Peter calls this his favorite skill — "shocking how good it is" — and notes you sometimes have to be blunt/"mean" with the model. **`[Opinion]`**

> **🟡 Tips & Tactics**
> - Add a **self-critique skill** that explicitly assumes the model made mistakes and forces a re-review — it catches bugs *beyond* a normal review pass.
> - Treat the AI like a **PR reviewer**: a forced second pass reliably surfaces issues. **`[General rule]`**
> - Use Chops' AI iterator to refine skill prompts (e.g., "be meaner") instead of hand-editing.

> **🔵 Tools & Skills:** but-for-real skill (open source) · Chops (open-source Mac app) · Chops AI iterator

---

## 7. Live demo: designing non-"AI slop" websites
*Chapter 7 · 19:11 — also covers launch & monetization*

**Key points — the design process**

- It starts with a **name**, then a **logo**. ~**99% of logos are done by hand in Adobe Illustrator** (pen tool, trying many fonts); he hasn't found a good shortcut. The **color scheme is decided here, before any code**.
- Walkthrough (**Rumored**): concept = LLMs quoting you out of context, so "quoting" became the theme → he hunted for typefaces with interesting **quotation marks**, tried many fonts (they "all run together"), and picked one. Then he tested colors (light/dark, black/white), landed on a **deeper orange**, and tried it across textures and a favicon/avatar scenario. At this point: **zero code — just brand**.
- He hands code the chosen colors + **logo SVG files**, then jumps into building.
- The **marketing page comes after the app is built**, because building reveals what the app actually does (translating idea → features takes multiple days of iteration). He then generates a marketing site from the brand assets + a desired vibe ("urgent," edgy/techy, "not soft typical") and has AI read the **full feature set** to generate marketing copy.

**Key points — launch & business**

- He **builds the full product first** rather than testing demand with an email-collection landing page — he considers that a "distraction." He'd rather build it and ship it. **`[Opinion]`** (Caveat: building the whole thing is cheap now with AI; it wasn't always.)
- Distribution is via **social media** — ~**60,000 Twitter followers** helps get a launch started.
- Launches do flop. His admitted weakness: he moves on so fast that he stops talking about a product and people forget it — he should promote existing products more, not only build new ones.
- **Monetization:** he tries to always have a paid tier. Free/no-hosting-cost tools (e.g., the Clearly editor) may stay free; anything with **hosted infrastructure must cover its costs** — "it's not a charity." If it can't pay for its servers after he's fronted thousands, he rethinks or shuts it down (refunding recent months to paying customers when he does).
- **Pricing insight:** very low-cost plans generate the **highest support overhead** (refund requests, etc.). Peter raised his newsletter from ~**$20** to a **couple hundred dollars** for this reason. **`[General rule]`**
- **Support across 5 products:** one email alias per product all routed to a single inbox, plus a self-built **in-app chat support skill** (an Intercom replacement living inside each app) that gives him the user's account context and lets him batch support per product.
- Why he's fast: AI levels the playing field, but his **25 years of pre-AI experience** let him quickly judge whether an approach will work, won't work, or will become a problem in a few months. **`[Opinion]`**

> **🟡 Tips & Tactics**
> - **Lock brand first:** name → logo (Illustrator) → colors, before writing any code. Build the marketing site *after* the app so the copy reflects real features.
> - **Ship the whole product** instead of an email-capture landing page; get real users' perspectives ASAP.
> - Keep a **paid tier** for anything with hosting costs; make each product cover its own server costs or shut it down.
> - **Avoid ultra-cheap plans** — they create disproportionate support load; price higher to filter.
> - As a solo builder, **automate the parts you dislike by building a skill for them** (e.g., in-app support).

> **🔵 Tools & Skills:** Adobe Illustrator (pen tool) · SVG logo files · in-app chat support skill · Twitter / X · Rails + Inertia + Postgres

---

## 8. Advice for builders without technical experience
*Chapter 8 · 28:55*

**Key points**

- His core advice: **fail a lot**. "Vibe coding" gets used as a slur, but it's great that anyone can build now; the only way to learn what *not* to do is to do it wrong. AI-assisted coding **reduces** mistakes, but mistakes always existed pre-AI. **`[Opinion]`**
- Make mistakes **as fast as possible** and recognize each one so you don't repeat it. There's no substitute for jumping in and shipping.
- Don't spend months before releasing — throw it out there now. He's shipped within **24 hours / same-day**; not always possible, but as fast as he can. **`[Opinion]`**
- You build for *your* assumption of the problem; other people's version looks slightly different, and you can't discover that until real users hit edge cases ("what about this use case?"). Get outside perspectives as fast as possible. **`[General rule]`**

> **🟡 Tips & Tactics**
> - Learn by **shipping and failing fast**; recognize each mistake so you don't repeat it.
> - Release in **days, not months** — real users reveal use cases you can't predict.

*Where to find Josh: Twitter/X **@Spigford** (posts frequently; bio links to ~50 projects) and his blog **everydayisayear.ai** (practical writing on building).*

---

## Appendix · Tools, skills & resources reference

**Models**
Claude Opus — bulk building & planning. · GPT-5.5 — adversarial code review.

**Orchestration & tooling**
**Conductor** — model switching + automated worktree setup (unique ports, env vars, processes; ~10 in parallel). Compared against **Codex** and **Claude Code**. **Context7** — latest documentation. **agent browser** — automated UI testing.

**Josh's skills (open source on GitHub — ~a dozen total)**
build skill (research → plan → implement) · research skill (one-off features) · learnings skill (updates CLAUDE.md) · but-for-real skill (forced self-review) · ui.sh skill (design pass) · in-app chat support skill (Intercom replacement).

**Skill management**
**Chops** — open-source Mac app for editing skill files, with a built-in AI iterator ("be meaner").

**Stack & design**
Ruby on **Rails** + **Inertia** + **PostgreSQL**; config via **CLAUDE.md / agents.md**. Branding hand-made in **Adobe Illustrator** (SVG logos).

**Products mentioned**
Proxy User (browser-based synthetic QA) · Rumored (brand-hallucination monitoring) · Reply / Reply Social (mention aggregation) · Clearly (open-source Markdown editor) · a family health-tracking tool · former: Baremetrics (sold for $4M) and BotBlock (defunct Chrome extension).

**People & links**
Speaker: **Josh Pigford** — X/Twitter **@Spigford**, blog **everydayisayear.ai**. Host: **Peter**. Sponsor: **Whisperflow** (whisperflow.com; code "peter whisperflow" = 6 months free).

---

*Caption corrections applied to the source transcript: barometrics → Baremetrics; clawed code → Claude Code; botlock / "bot block" → BotBlock; context 7 → Context7; UI.sh → ui.sh; "butt for real" → but-for-real; "every day is a year.ai" → everydayisayear.ai. Model name "GPT-5.5" preserved as spoken. A garbled tool name in the Conductor comparison was read as "Codex and Claude Code."*
