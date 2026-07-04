# Inside Conductor: Charlie's Voice-First Agent-Orchestration Workflow

*How the Conductor co-founder runs many coding agents in parallel — and where he thinks software is heading*

**Speaker:** Charlie, co-founder of **Conductor** (YC Summer 2024) · **Format:** Setup walkthrough + interview · **Core tools shown:** Conductor, Claude Code, Codex

---

## Overview

A behind-the-scenes tour with Charlie, co-founder of **Conductor** — a Mac app for orchestrating many coding agents (Claude Code and Codex) at once. Charlie demos a near-zero-typing, voice-first workflow where he "conducts" agents like an orchestra: kicking off parallel tasks, reviewing PRs in-app, and dispatching work from his phone. He shares the customizations that actually matter (`CLAUDE.md`, fast mode, "slop-free zones"), Conductor's own tech stack, his product/design philosophy ("don't let the AI be your architect"), when he reaches for Claude vs. Codex, his views on "token maxing," and a closing thesis that **code is becoming "sawdust"** — a byproduct of prompts that matter more than the code itself.

**Callout legend:** `TIP` = actionable advice · `TOOL` = app / setting / command · `RULE` = general principle · `OPINION` = personal / gut-feel view · `CAUTION` = pitfall to avoid.

---

## Contents

1. [Who & What: Conductor](#1-who--what-conductor)
2. [The Voice-First Setup](#2-the-voice-first-setup)
3. [Core Conductor Workflow](#3-core-conductor-workflow)
4. [On the Go & Hands-Off Editing](#4-on-the-go--hands-off-editing)
5. [Software Stack & Hardware](#5-software-stack--hardware)
6. [Customizations That Matter](#6-customizations-that-matter)
7. [Conductor's Own Tech Stack](#7-conductors-own-tech-stack)
8. [Product & Design Philosophy](#8-product--design-philosophy)
9. [Claude vs. Codex (& GUI vs. Terminal)](#9-claude-vs-codex--gui-vs-terminal)
10. [Token Maxing & Lines of Code](#10-token-maxing--lines-of-code)
11. [The Future: Cloud Agents & "Code as Sawdust"](#11-the-future-cloud-agents--code-as-sawdust)
12. [Notes on Caption Corrections & Proper Nouns](#notes-on-caption-corrections--proper-nouns)

---

## 1. Who & What: Conductor

- Charlie is co-founder of **Conductor**, a Mac app for orchestrating a fleet of coding agents at once. The company was **YC Summer 2024**.
- The team builds Conductor *with* Conductor — heavy dogfooding ("We're using Conductor to build Conductor").
- The core unit is a **workspace**, currently an abstraction around a git **work tree** (Charlie notes this is "going to change soon").

> **TOOL** — **Conductor**: Mac app to run and manage multiple coding agents (Claude Code [^1] + Codex [^3]) in parallel.

---

## 2. The Voice-First Setup

- Guiding idea: **talk to your computer more, type less.** The whole team adopted desk mics to encourage this.
- His current must-have is a **gooseneck microphone** [^2], ~**$20 on Amazon**.
- In an open-plan office you can lean over and quietly issue commands (e.g., *"merge PR 3475"*) without disrupting people nearby.

> **TOOL** — **Gooseneck microphone** (~$20, Amazon), positioned for easy, low-volume dictation.

> **TIP** — Whispering commands into a desk mic is far less disruptive in open-plan offices than speaking out loud — it lowers the social cost of voice control.

> **OPINION** — Charlie calls the gooseneck mic "a recent thing I can't live without" — a personal preference, not a requirement.

---

## 3. Core Conductor Workflow

- **Kick off tasks constantly** with `Command-N`, then dictate a prompt (e.g., *"take a look at the latest Linear [^10] issue and give me a rough pass at how you'd solve it"*) and press Enter. The task then runs in the sidebar.
- **Parallelism:** while one agent works, he switches to another chat — keeping several agents busy at once.
- Heavy **keyboard-shortcut** user (e.g., `Command-Shift-Y` to jump to a workspace that's ready to merge).
- **Reviews PRs inside Conductor**, leaving GitHub-style inline comments (*"this looks a little weird to me — why do we need this?"*) then Enter to send the agent back to work.
- **Experimentation is central:** many workspaces are throwaway ideas; if one is good it gets promoted from **internal** → **experimental**.
- **Status pipeline** in the left panel: **In progress** → **In review** (PR created) → **Done** (merged). **Archive** removes a merged workspace from the side panel.
- A **Dashboard** page (in progress) shows all agents in one place and routes each to its next action.

> **TIP** — The loop: `Command-N` → dictate → Enter → switch chats. Always keep an agent running so you're never idle while one works.

> **TIP** — Review and comment on PRs in-app with GitHub-style inline comments instead of context-switching to GitHub.

> **RULE** — Treat workspaces as **cheap, disposable experiments**; only promote the ideas that earn it (internal → experimental). Most never ship.

> **OPINION** — The aspirational feel is being "the **CEO of a little company**" whose agents bring back digestible reports you redirect or merge — a vision/metaphor, and the dashboard interface is "still being messed around with."

---

## 4. On the Go & Hands-Off Editing

- **Mobile "conducting":** dictate a request into his phone (e.g., *"add a feature to change the theme to hacker mode"*), tap **Conduct**, and his computer starts working remotely.
- He says he **basically doesn't write code by hand anymore** — only the occasional Tailwind class edit or opening an IDE to change an `.env` file.
- **Caveman mode:** a Conductor mode you click to type and edit a file directly by hand — named that way because hand-editing is now the exception.
- For small UI tweaks: highlight an element and tell the AI, or just dictate (*"that button looks a little too wide — can you make it smaller?"*).

> **TOOL** — **Caveman mode** (Conductor): direct, by-hand file editing for the rare cases the AI can't handle.

> **TOOL** — **"Conduct" button** (mobile): dictate a task on your phone and dispatch it to your machine.

> **OPINION** — Asked if he still writes code today: *"No… very occasionally."* A personal account of his own habits, not a prescription.

---

## 5. Software Stack & Hardware

- **Telegram** — used to talk to his "open claw" [^7] (a recent addition).
- **Spokenly** — dictation/speech-to-text, triggered with `Control-Space`; it runs a **local model, Parakeet**.
- Hardware: a heavily specced machine with **128 GB of RAM**, partly to run local models like Parakeet.
- As a counter-move, he just ordered a **MacBook Neo** [^8] — the lowest-spec/lowest-RAM option — deliberately, to force himself onto minimal hardware.

> **TOOL** — **Spokenly** (dictation, `Control-Space`) running **Parakeet** locally · **Telegram** as a chat interface to his agent.

> **OPINION** — Buying a deliberately low-spec MacBook Neo to "force myself to use the lowest-spec option" is a personal discipline experiment.

---

## 6. Customizations That Matter

- **`CLAUDE.md` [^9] + skills files:** a few hundred lines of tuned engineering practices, e.g. *"We're a startup — you're probably used to writing enterprise code, but that's not how we do things here."*
- **Always uses fast mode** (not the default) — considered essential for "token maxing."
- **Context7 MCP** [^6] — helpful for pulling in documentation; otherwise mostly stock settings.
- Runs Claude with **"dangerously accept all permissions"** (skip-permissions) — not the default elsewhere, but the default way Conductor runs Claude.
- **Slop-free zones** [^5]: clearly bounded, human-written parts of the codebase/docs. AI may contribute, but **every line must be read by a human**. Some lines are marked *"do not touch if you are an AI — human eyes only."*

> **TOOL** — `CLAUDE.md` & skills files · **fast mode** · **Context7 MCP** · run Claude with **"dangerously accept all permissions."**

> **RULE** — Define **slop-free zones** — human-guaranteed sections where every line is human-reviewed — and mark sensitive code "do not touch if you are an AI."

> **CAUTION** — Without clear boundaries, the AI can fall into a **vicious cycle**: it sees bad code and writes more bad code as a result (the same compounding can run in the positive direction).

> **OPINION** — "If you're trying to token max, you *have* to be in fast mode." Most other settings, he says, are fine out of the box — his personal calibration.

---

## 7. Conductor's Own Tech Stack

- Desktop app is a **Tauri** [^4] app using the native **Safari (WebKit) web renderer**.
- Backend is **technically Rust**, but the desktop app is **~90–95% TypeScript**.
- The web app is **Elixir** (a **Phoenix** app) — currently tiny, since all it does right now is log in.

> **TOOL** — **Stack:** Tauri (native Safari renderer) · Rust backend · ~90–95% TypeScript desktop · Elixir/Phoenix web app.

> **OPINION** — "I'm a huge Elixir fan" — Charlie keeps pushing for more Elixir in the codebase wherever possible. Personal preference.

---

## 8. Product & Design Philosophy

- **Humans own the architecture and interface.** The team thought through core concepts themselves — the "workspace" abstraction and the three-pane layout (**chats left, chat center, review/run right**).
- **Crafted UI matters:** they spent a long time on details like the "open in" button and whether to show app icons in the top bar.
- **Would do differently:** build the core around **human-written APIs/contracts** the AI doesn't touch much, while giving the AI "free rein" in clearly separated non-core areas. Current boundaries are "a little murky" and they're improving them.
- **Stay slightly ahead of the frontier** — push users' comfort zones. Early reaction to Conductor: *"This is crazy — I can barely manage one agent, how do I manage three or five?"*
- **Enforced workflow:** you can't edit files directly — every workspace is a work tree that **must create a PR you then merge**.

> **RULE** — **Don't let the AI be your architect.** Own the core concepts, APIs, and interface decisions yourself — AI-made UI choices tend not to feel "crafted."

> **RULE** — Keep AI **out of the core** (human-written APIs/contracts); give it free rein only in clearly separated, non-core areas so experiments can't damage core infrastructure.

> **TIP** — Enforce a PR-based workflow (work tree → PR → merge) so no change ever bypasses review.

> **OPINION** — Conviction comes from **dogfooding + gut feel**, not analytics or A/B testing: "When I click this, it feels right." (He was initially against showing app icons in the top bar, then came to like them.)

---

## 9. Claude vs. Codex (& GUI vs. Terminal)

- **Codex = the "workhorse":** powers through a specific problem, unafraid to make many tool calls, good for long debugging sessions.
- **Claude (Opus) = more of a partner:** more back-and-forth, more creative — his instinctive choice when building a new feature.
- **GUI over terminal:** we moved from CLI to GUI in the '80s for a reason; humans are spatial/visual creatures, and a GUI gives a stable spatial map plus capabilities a terminal can't offer. A CLI may suit "AI brains" better than human ones.

> **RULE OF THUMB** — Reach for **Opus** when building something new/creative; reach for **Codex** when you "just want to get stuff done" or grind through a long, specific debugging problem.

> **OPINION** — "Humans are visual, spatial creatures" — terminals feel restrictive to him; GUIs fit human cognition better. A personal design conviction.

---

## 10. Token Maxing & Lines of Code

- **Peak spend:** ~**$22,000 on tokens in July 2025** (on a previous generation of models), producing tens of thousands of lines that month.
- **Pro "token maxing":** fast mode, "think extra hard," high effort all the time.
- **Anti lines-of-code:** deliberately keep LOC minimal; he thinks about a brand-new app very differently from an established codebase like Conductor.

> **OPINION / PRACTICE** — "Token max" aggressively (fast mode, high effort everywhere) **but keep lines of code minimal** — spend on thinking, not output volume.

> **CAUTION** — Unchecked line-of-code growth can make a codebase **spiral out of control** — be deliberate about what you add.

---

## 11. The Future: Cloud Agents & "Code as Sawdust"

- **Cloud workspaces** [^1] (sneak peek): today, agents stop when you close your laptop. Conductor is investing in cloud so agents can run **~10× longer**, be "10× smarter," and run unconstrained by your machine's CPU.
- **Open collaboration questions:** Should you be able to talk to **sub-agents**? Should there be **multiplayer chats** where several people work with the AIs on the same thing?
- **"Code as sawdust":** code used to be the thing you crafted; now you craft the **description** of what you want and code is the byproduct. Implication — **prompts are the durable artifact**: rerun them on next-gen models to regenerate code; the old code "didn't really matter."
- **Malleable software:** the "submit a prompt / prompt request" feature is an early experiment. Metaphor — **video-game mods** (Call of Duty: same skeleton for everyone, but custom skins/reload speeds). He wants users to "mod" Conductor and build in their own workflows while the crafted core stays the same.

> **TOOL** — **Cloud workspaces** (in development): remote, longer-running agents that don't stop when you close your laptop.

> **OPINION / VISION** — "Code is almost like sawdust now" — a forward-looking thesis that prompts, not code, are what matter as models improve.

> **IDEA** — Think of your software like a **moddable game**: a crafted, shared core plus user-level mods and workflows that make it feel like your own.

---

## Notes on Caption Corrections & Proper Nouns

[^1]: The auto-captions repeatedly render **"Claude"** as "cloud." Corrected to **Claude** where it refers to the agent (e.g., "while Claude is working," "run Claude," `CLAUDE.md`). Kept as **Cloud** only where it clearly means remote/cloud execution ("Cloud workspaces," investing "in cloud").
[^2]: "gooseeneck" → **gooseneck**.
[^3]: "codeex / Codeex" → **Codex**.
[^4]: "towery app" → **Tauri** (cross-platform desktop framework).
[^5]: "slot free zones" → **slop-free zones** (i.e., zones kept free of AI "slop").
[^6]: "context 7 MCP" → **Context7 MCP** (documentation MCP server).
[^7]: "open claw" — transcription is unclear; preserved as spoken. Appears to be an agent/bot the speaker chats with over Telegram.
[^8]: **MacBook Neo** — preserved exactly as spoken; could not verify this as a standard product name.
[^9]: "cloud MD" → **`CLAUDE.md`**.
[^10]: Capitalization/spelling normalized: "linear issue" → **Linear** (issue tracker); "command n / command shift Y" → `Command-N` / `Command-Shift-Y`; "YC Summer 24" → **YC Summer 2024**. "GStack" and "Gary mode" (a power user named Gary and his setup) preserved as spoken.
