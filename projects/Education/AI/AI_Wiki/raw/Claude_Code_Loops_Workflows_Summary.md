# Designing Loops & Workflows in Claude Code — with Tharic (Claude Code Team)

**Source:** Peter Yang podcast interview with Tharic, Anthropic's Claude Code team
**Topic:** How to design loops and workflows to get Claude to work autonomously for longer periods, plus Tharic's personal Claude Code / Claude in Slack ("cloud tag") workflow

---

## Overview

Tharic from the Claude Code team joins Peter Yang to explain how Anthropic thinks about getting Claude to work for extended periods with less hand-holding. The conversation covers the three core mechanisms — `/loop`, `/goal`, and **workflows** — then moves into a live demo of an AI-powered video-editing pipeline (transcription + Remotion overlays), a deep dive on what "planning" really means in agentic work, and closes with Tharic's personal habits around multi-tasking, context management, and becoming more technical.

> 💬 **Speaker Opinion:** Tharic's overarching theme — "as the models have gotten smarter, they need less direction, fewer constraints, and fewer examples" — shapes nearly every recommendation in this video.

---

## Table of Contents

1. [The Three Mechanisms: /loop, /goal, and Workflows](#1-the-three-mechanisms-loop-goal-and-workflows)
2. [Live Demo: AI Video Editing Workflow](#2-live-demo-ai-video-editing-workflow)
3. [Rethinking "Planning" as Iterative Exploration](#3-rethinking-planning-as-iterative-exploration)
4. [Specs Are Now Written for Agents Too](#4-specs-are-now-written-for-agents-too)
5. [Claude Code vs. "Cloud Tag" (Claude in Slack)](#5-claude-code-vs-cloud-tag-claude-in-slack)
6. [Workflows Explained: Sub-Agents, Verification & Self-Referential Bias](#6-workflows-explained-sub-agents-verification--self-referential-bias)
7. [Tharic's Personal Habits: Focus & Multi-Clotting](#7-tharics-personal-habits-focus--multi-clotting)
8. [Keeping Context Clean](#8-keeping-context-clean)
9. [Becoming More Technical](#9-becoming-more-technical)
10. [Appendix: Caption Corrections & Uncertain Terms](#appendix-caption-corrections--uncertain-terms)

---

## 1. The Three Mechanisms: /loop, /goal, and Workflows

Tharic frames "loops" as a general term for different ways of giving the agent feedback so it can work for long periods in an orchestrated way.

- **`/loop`** — general mechanism for iterative, orchestrated agent work.
- **`/goal`** — reminds the agent of its exit condition and prevents it from stopping early. Best used when the task is complex and you need to make sure it's fully done — it pushes the agent to "power through" instead of pausing to ask "should I keep going?"
- **Workflows** — described as the most powerful mechanism. They let you spin up **sub-agents** to both do the work in parallel *and* verify the work, turning a non-deterministic task into something closer to deterministic — especially useful for non-technical work.

> 📏 **General Rule:** Use `/goal` when the user has already done enough spec/exploration and just wants the agent to execute and fill in gaps if it hits something unexpected.

> 📏 **General Rule:** Use workflows when a task can be parallelized and needs independent verification (e.g., generating multiple video clips, each checked against a rubric).

> 💡 **TIP:** If you have a deterministic way to verify success (e.g., checking a rendered UI against a **Figma** file via the **Figma MCP**), use `/goal` — e.g., "make sure the rendered design matches the Figma MCP." If verification is "squishier" (e.g., comparing to a screenshot with subjective judgment), use a **workflow** with a rubric and a dedicated verification agent instead.

> 💬 **Speaker Opinion:** Tharic notes that outcomes are "very dependent on the task" — there's no single right mechanism; it depends on what kind of feedback signal is available.

---

## 2. Live Demo: AI Video Editing Workflow

Tharic recorded a short video of himself (as a guest on the Peter Yang podcast) pointing at where he wanted an overlay and saying "fade to black" — then fed it to Claude Code in a single prompt.

### The exact prompt used:
> "This is a repo for the Peter Yang podcast. There's a sample video here called **Peter Yang recording**. Transcribe it using **Whisper**. Then use **Remotion** to create a UI that shows the transcript with each individual word being highlighted, and different overlays. **/goal** — don't stop until the video is fully rendered."

### Result
One-shot execution: Claude transcribed the audio with Whisper, built the caption/overlay UI in Remotion, and rendered a fade-to-black ending. It did not know Tharic's name, so the transcript needed correction.

> 🛠️ **TOOLS USED:** Whisper (transcription), Remotion (video UI/overlay rendering), `/goal` (to prevent early stopping)

> 💡 **TIP:** To improve overlay placement accuracy (e.g., tracking where a hand or face is pointing), Tharic suggests giving the agent more metadata — e.g., finger-tracking or face-tracking data — rather than relying on the raw video alone.

> 💬 **Speaker Opinion:** Tharic says he isn't personally thrilled yet with where the overlay appeared — this is presented as an unresolved, ongoing refinement, not a finished feature.

**On skills:** At the time of the demo, Tharic had *not yet* turned this workflow into a reusable skill — he says he prefers to first fully understand what he wants and surface edge cases before packaging something as a skill.

---

## 3. Rethinking "Planning" as Iterative Exploration

Tharic pushes back on the idea that planning is a single, one-shot step ("plan, then execute"). Instead, he frames it as continuous exploration.

> 💬 **Speaker Opinion:** "I'm starting to feel like the word 'planned' is maybe too broad right now... I like to say [it's about] getting rid of your unknowns." This is explicitly Tharic's personal framing, not a formal Anthropic rule.

### Example: Redesigning the video overlays
Tharic asked Claude to:
> "I want to update the UI of these overlays. I want to use Peter Yang's style — here's his blog — create an HTML artifact for exploring different designs for the overlays and captions, design variations."

> 🛠️ **TOOL:** HTML artifacts — used at Anthropic broadly for sharing plans, PRs, status reports, and incident reports. (Currently available on **Team** and **Enterprise** plans; not yet on Max/Pro at time of recording.)

> 🛠️ **TOOL:** The **front-end design plugin** was used to generate the polished, image-rich plan Peter noticed.

### Example: Understanding Whisper's edge cases before building
Before building the transcription workflow, Tharic had Claude explain how Whisper works and its failure modes, including:
- Silence can be mis-transcribed as phrases like "thanks for watching"
- A single word can be split into two chunks
- Whisper has no built-in speaker recognition

> 💡 **TIP:** Prompt the agent to explain the tool/library you're about to depend on and surface its known edge cases *before* building on top of it — this avoids discovering "unknown unknowns" mid-build.

> 📏 **General Rule:** Planning is iterative — human request → agent does technical exploration → mockups/explainers to find unknowns → refine → hand back to agent → agent implements and keeps notes on issues found along the way → re-spec if needed.

> ⚠️ **CAUTION (Speaker Opinion):** Tharic and Peter both flag a common failure mode: users (including Peter) get "lazy" and stop reading long AI-generated markdown plans, just telling Claude to "just do it." Tharic warns this backfires — skipping careful plan review tends to cost more time and money later.

> 💡 **TIP:** Prototype cheaply first. Tharic treats the HTML overlay mockups as disposable prototypes — only once a design direction is validated does he move to the more expensive step (e.g., rebuilding in React, which requires re-rendering video and code changes).

---

## 4. Specs Are Now Written for Agents Too

Peter raises that traditional product specs (problem, solution, goal) were written for humans — but now agents read them too, prompting a discussion on how spec-writing has changed.

> 💬 **Speaker Opinion:** Tharic says specs are "very tied together" with planning now — there isn't a clean one-time handoff from spec to implementation anymore; it's a back-and-forth process.

**Workflow Tharic describes:**
1. Human request
2. Agent does technical exploration
3. Mockups/explainers to clarify unknowns
4. Refine the spec
5. Hand to agent to implement
6. Agent keeps **implementation notes** along the way, surfacing unexpected findings
7. Re-spec if needed based on those notes

> 💡 **TIP:** Ask the agent to keep implementation notes as it works — this creates a record of what wasn't anticipated and enables "re-speccing" mid-project instead of only at the start.

> 💡 **TIP:** Build the smallest/cheapest version first (e.g., HTML prototype) to validate the spec before investing in a more expensive implementation (e.g., full React rebuild).

---

## 5. Claude Code vs. "Cloud Tag" (Claude in Slack)

Peter asks what percentage of Tharic's work happens in "cloud tag" (tagging Claude in Slack) vs. the terminal/app.

> 💬 **Speaker Opinion (Tharic's personal workflow):**
> - **Parallel / background work** ("multi-clotting") happens in Slack via cloud tag — initial explorations, PR specs, understanding a problem.
> - Once he's focused on **one specific thing**, that happens in Claude Code, in a more iterative back-and-forth style.
> - Previously he ran ~5 parallel Claude Code sessions; now it's typically **one active Claude Code session** plus multiple cloud-tag Slack sessions.

### Example use case: "Babysitting" a PR
Tharic asks Claude (via Slack) to babysit a PR — fix tests and tag a reviewer — who then gets tagged into the same Slack channel for discussion.

> 🛠️ **TOOL:** Claude in Slack ("cloud tag") — used both via private DM channel (Tharic has a personal "Thoric Claude" Slack channel) and shared team/project channels (e.g., a feedback channel, project-specific engineering channels).

> 💡 **TIP:** To trigger a skill in cloud tag/Slack, you don't need special syntax — you can simply tell Claude in natural language to use the skill.

> 💬 **Speaker Opinion:** Tharic says Slack is where Anthropic already lives, calling it "a very natural way to explore," and notes some people do almost all of their coding entirely through Claude in Slack.

### On agent identity and memory
Every agent/channel in cloud tag has its own memory. Tharic is cautious about over-applying the "coworker" metaphor to Claude:

> 💬 **Speaker Opinion:** "I think these metaphors can sometimes be helpful but also limiting... it is kind of helpful to think of an agent that has persistence and memory, but I think they're also different from co-workers in some ways." He adds Claude's memory is "better and worse sometimes... it's spiky."

---

## 6. Workflows Explained: Sub-Agents, Verification & Self-Referential Bias

Applied to Peter's own "podcast production skill" (which generates YouTube thumbnails, clip ideas, and rendered short clips from a transcript), Tharic explains when and how to use a workflow instead of a single skill.

### Example: Generating multiple short video clips
> "The main agent decides which five areas of the clip you want to create a short for, then the workflow spins off a sub-agent for each one. You also give it a rubric for what a good clip looks like — each one is verifying against it."

> 📏 **General Rule:** Give each parallel workflow task a **maximum compute budget** so quality doesn't degrade when generating multiple outputs simultaneously (Tharic notes that without this, Claude may put less verification effort into any individual clip when doing several at once).

> 🛠️ **TOOL:** Workflows are implemented as a **JS file**; Tharic notes you can save this JS file into a skill, creating a reusable "skill + workflow" package.

### Why use a workflow instead of just a skill?
1. **Context management** — sub-agents keep context clean rather than bloating one long session.
2. **Avoiding self-referential bias** — a model reviewing its own output tends to be too lenient.

> 📏 **General Rule (named concept — "self-referential bias"):** "When a model prefers its own outputs, it's going to be more lenient at verifying it." Use a **separate Claude instance to verify** work rather than having the same instance that did the work also grade it.

> 💡 **TIP:** Structure it as three separate Claude "roles": one coordinating, one doing the work, one verifying — each with different context/models — for genuinely less-biased evaluation, and this also means each puts more compute in and is less likely to stop early.

---

## 7. Tharic's Personal Habits: Focus & Multi-Clotting

Peter admits to feeling exhausted running five Claude threads simultaneously — "worse than back-to-back meetings."

> 💬 **Speaker Opinion:** "My goal for this year is to be more productive, but work less." Tharic frames this as a personal goal, not a company mandate.

> 💡 **TIP (Tharic's personal practice):** Focus on **one primary project** at a time, even while other background tasks (builds, merges, exploration) run in parallel. He says his biggest time-waster is being "a little bit lazy," giving a weak prompt, and then having to redo the work.

> 💬 **Speaker Opinion:** "There's an optimal amount of multi-clotting depending on who you are and what you're doing" — Tharic is explicit that this varies by person.

### On repo/workspace "slop"
Peter worries that if he doesn't carefully review everything the agent produces, the repo could degrade into "slop."

> 🛠️ **TOOL:** **`simplify`** — a tool built by Boris (Anthropic) that simplifies/cleans up a repo.

> 💬 **Speaker Opinion:** Tharic says the acceptable level of code "cleanliness" depends on the use case — if you only care about outputs (e.g., rendered videos), code quality matters less, since the agent is persistent enough to work through mess. But organizing the workspace is often more for the *human's* peace of mind than the agent's needs.

> 💡 **TIP:** You can always just ask Claude to "simplify" or "organize" the codebase/workspace periodically.

---

## 8. Keeping Context Clean

Peter asks whether Tharic minimizes MCPs, keeps `CLAUDE.md` short, etc.

> 📏 **General Rule / Anthropic Finding:** As models have gotten smarter, they need **less direction, fewer constraints, and fewer examples**. Anthropic **cut the Claude Code system prompt by 80%** for this reason.

Why fewer examples/constraints help:
- Excessive examples can over-constrain the model — it starts mimicking the exact example pattern instead of generalizing.
- Hard "never do X" constraints are often actually "usually don't do X" — stating it as an absolute can misfire.
- **Explaining the *reason*** behind a constraint tends to be more effective than a bare prohibition.

> 💡 **TIP:** Trim your `CLAUDE.md` files — Tharic believes most are currently too long. The same applies to skills, which he thinks are often too long as well.

> 💬 **Speaker Opinion (on MCPs):** "It depends on the MCP" — some take up significant context, but Tharic notes the MCP team has invested heavily in reducing this via tool search and related improvements.

### Prompting style shift: constraints → principles
Using a Twitter/X post as an example:

> 💡 **TIP:** Instead of rigid rules ("must be exactly 280 characters, never do X"), give the agent **context about yourself and your principles** (e.g., "I work on Claude Code at Anthropic, here are principles we follow") plus flexible framing (e.g., "I'd prefer one tweet, but a two-tweet thread might work better for this") — this gives the model room to find a better solution than a rigid constraint would.

> 📏 **General Rule:** Hard numeric constraints that are truly non-negotiable (e.g., a 280-character limit that's a platform limit) should still be stated explicitly — the shift is away from *unnecessary* rigid constraints, not all constraints.

---

## 9. Becoming More Technical

Peter asks how a less-technical person can "learn to work with agents" in a deeper way — not syntax, but understanding.

> 💬 **Speaker Opinion:** "The first step is motivating yourself to learn things... that is honestly really hard." Tharic admits he struggles with this too when something isn't strictly required to finish a task.

> 📏 **General Rule (Tharic's framing):** The goal of becoming more technical is to know your **"unknown unknowns"** — e.g., understanding trade-offs between backend services, video encoding libraries, or local vs. remote transcription — not memorizing syntax like TypeScript specifics.

> 💡 **TIP:** Push Claude to brainstorm and teach you the constraints of a system (what's possible, how it currently works, how it could be better) — but Tharic stresses "you really do have to push it."

> 💬 **Speaker Opinion (citing Andrej Karpathy):** "Education should feel like work more than fun" — attributed by Tharic to Karpathy, used to argue that real learning requires deliberate effort, not just prompting Claude and looking at outputs.

**Practical takeaway discussed:** Peter notes that generating and actually reading detailed HTML reports/explainers (as Tharic does) is likely the exception, not the norm — most people just prompt and look at the output without engaging with the reasoning. Tharic frames this practice as key to leveling up from "good" outputs to "best-in-class" outputs.

> 💡 **TIP:** Consider adding a custom instruction to your Claude setup (e.g., CLAUDE.md) asking it to generate an HTML report/explainer for significant tasks, specifically so you're prompted to read and learn from it.

---

## Appendix: Caption Corrections & Uncertain Terms

The following corrections were made to likely auto-caption errors from the original transcript:

| Original Caption Text | Corrected To | Confidence |
|---|---|---|
| "reotion" | Remotion | High — matches known video-creation React framework |
| "cloud code" / "cloud" (referring to the product) | Claude Code / Claude | High — consistent brand reference throughout |
| "cloud tag" | Claude in Slack (Anthropic's internal term for tagging Claude in Slack channels) | Medium — kept as "cloud tag" in quotes since this appears to be the actual internal nickname used, not a mis-transcription |
| "Slashloop, slashgoal" | `/loop`, `/goal` | High — clearly slash-commands |
| "multiclouding" / "multiling" / "multi-clotting" | Left as spoken ("multi-clotting" / "multi-clouding") — likely Tharic's own coined term for running multiple Claude sessions in parallel; exact intended spelling is **[?]** unclear from audio | Low — flagged as uncertain |
| "Boris put out... simplify" | `simplify` (tool name) | Medium — tool name inferred from context |
| "Kaparthi" | Andrej Karpathy | High — well-known AI researcher |
| "respspec" | re-spec | High — clear meaning from context |
| "antfooding" | "ant fooding" (Anthropic's internal version of "dogfooding") | Medium — inferred pun on "Anthropic" + "dogfooding" |

> ⚠️ **Note:** A few informal/coined terms (e.g., "multi-clotting," "cloud tag") appear to be Tharic's own internal shorthand rather than official Anthropic product names, and are preserved as spoken rather than replaced with guesses.
