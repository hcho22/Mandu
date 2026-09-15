# Automating AI Evals the Right Way — with Error Analysis

> **Source:** YouTube podcast interview hosted by **Peter Yang**, with guests **Hamel Husain** and **Shreya Shankar**, the instructors behind the most popular AI evals course online (they've reportedly taught **4,500+** students).
>
> **Format note:** This is a conversation/demo, not a step-by-step tutorial, so it's organized by **theme** rather than by numbered steps. Callouts are tagged so you can scan them: 💡 Tip · 🔧 Tool · 📏 General Rule · 🗣️ Speaker Opinion · ⚠️ Caution.

---

## Overview

The core message: **evals still start with looking at your own data and externalizing your taste** — that fundamental hasn't changed. What *has* changed is that **agents can now do the tedious parts with you**, running in the background while you review, then distilling your open-ended feedback into a reusable rubric.

The episode's spine is a distinction between **top-down evals** (what a domain expert would look for, derivable from the task alone) and **bottom-up evals** (failure modes you only discover by reading real outputs). AI is good at the first and bad at the second — so the human's job is to supply the bottom-up taste, and the AI's job is to scale it. The centerpiece is a live demo of Shreya's free **Error Discovery Skill**, which builds a custom review interface, watches you annotate, and turns your notes into eval criteria. The episode closes with Hamel's benchmark of "do-it-for-you" automated eval vendors: useful as a baseline, but they all miss the taste-dependent errors that actually differentiate a product.

---

## Table of Contents

1. [How evals have evolved over the past year](#1-how-evals-have-evolved-over-the-past-year)
2. [The core framework: top-down vs. bottom-up evals](#2-the-core-framework-top-down-vs-bottom-up-evals)
3. [Live critique: Peter's podcast-takeaway eval skill](#3-live-critique-peters-podcast-takeaway-eval-skill)
4. [Writing is the "final boss" — voice, workflow, and anti-slop](#4-writing-is-the-final-boss--voice-workflow-and-anti-slop)
5. [Demo: the Error Discovery Skill](#5-demo-the-error-discovery-skill)
6. [Model & tooling tangent: Codex, Claude, and orchestration](#6-model--tooling-tangent-codex-claude-and-orchestration)
7. [Do automated evals actually work?](#7-do-automated-evals-actually-work)
8. [Wrap-up, takeaways & the course](#8-wrap-up-takeaways--the-course)
9. [Appendix: caption corrections](#appendix-caption-corrections)

---

## 1. How evals have evolved over the past year

The fundamentals are unchanged: start by looking at data, do **error analysis**, and use a structured approach so you externalize your judgment *before* you start writing evals. The shift is that agents have become powerful enough to help you look at data thoughtfully — and to run in the background while you review, giving you far more leverage in that critical first stage.

Prior lessons that still hold (referenced from Hamel's earlier appearance): mainly review real customer traces and conversations to find where things go wrong, and use **yes/no, pass/fail** evals rather than inventing arbitrary numeric scores.

> 📏 **General Rule** — Externalize your taste and judgment *before* you write evals. Everything begins with structured data review and error analysis.

> 🗣️ **Speaker Opinion (Hamel)** — He's now a much bigger fan of **LLM judges** than before. They've gotten very good at evaluating narrow, well-defined criteria (e.g., "is this output too long/short?", "does it follow a particular structure?").

> 🔧 **Tool — LLM judge:** an LLM that looks at a single trace and makes a judgment about one specific, well-defined failure mode.

---

## 2. The core framework: top-down vs. bottom-up evals

This distinction is the backbone of the whole episode.

- **Top-down evals** — What you'd come up with "in a vacuum," given only the task description. A domain expert's understanding of what makes the task good. Examples for podcast takeaways: word/character length, correct use of action verbs, whether takeaways are actually actionable for humans.
- **Bottom-up evals** — Data-driven. The gut reactions and feedback you get *only* from reading lots and lots of sample outputs, then externalizing those reactions into evals. These emerge and accumulate over time as you see more failure modes.

> 📏 **General Rule** — Claude/AI is good at helping generate **top-down** evals but **very bad at bottom-up** evals. "That's all you." Bottom-up evals must come from the human looking at data.

> 💡 **Tip** — In the skill itself, **explicitly separate your evals into top-down and bottom-up** sections. It keeps you honest about whether your bottom-up coverage is actually exhaustive.

> 📏 **General Rule** — Evals are **iterative and never "done."** Seeing more examples surfaces more failure modes, which you feed back into the evals.

---

## 3. Live critique: Peter's podcast-takeaway eval skill

**What Peter built:** a skill for podcast post-production. It pulls the top ~10 takeaways from an interview transcript and drafts an initial newsletter post. Peter still manually reviews and iterates — he doesn't paste and ship.

**His evals, two kinds:**
- *Deterministic checks* — e.g., each takeaway is between **240 and 330 characters**.
- *Judgment-based checks* — e.g., "Is each takeaway understandable on its own without watching the episode?", "Does it give plain, useful advice?"

**His current loop:** run the skill on a raw transcript → go back and forth giving feedback until happy → then ask Claude to *reflect on the whole conversation and suggest updates to the skill and the evals* so the same rework isn't needed next time.

> ⚠️ **Caution — Overfitting.** Peter's worry: a note added for one episode (e.g., takeaways weren't **MECE** — mutually exclusive, collectively exhaustive) may not matter for the next interview, so blindly baking it into the evals overfits to one episode.

**Hamel & Shreya's recommendations:**

> 💡 **Tip — Fan out with sub-agents.** When you have many eval criteria, use a **sub-agent to evaluate each criterion (or group of criteria)** so you're confident every criterion is actually checked.

> ⚠️ **Caution** — If you hand a model one giant list of criteria, it tends to get "washed out" — it'll ignore some and get lazy. Focused per-criterion evaluation keeps it honest ("evaluate N2" → it really focuses on N2).

> 💡 **Tip — Generate a scorecard.** Have the skill produce a **spreadsheet / pivot table**: each criterion as a row with a yes/no (pass/fail) indicator per sample. You then eyeball the hierarchy of what matters (MECE might matter less elsewhere). You don't necessarily need to add explicit weights.

> 💡 **Tip — Mine your back catalog for bottom-up signal.** Run the skill on the raw transcripts of your **past 10–20 interviews**, compare its output against your **human-edited final** takeaways, and have the AI find patterns across all of them. Because you have the real "labels" (your edited takeaways), the AI can reflect on the *difference* between its output and your final version.

> 🗣️ **Speaker Opinion (Hamel)** — Peter's reflect-and-update-the-skill loop is "amazing" and exactly the right instinct.

---

## 4. Writing is the "final boss" — voice, workflow, and anti-slop

> 🗣️ **Speaker Opinion (Hamel & Shreya)** — They joke that **writing is the "final boss" for LLMs**: getting a model to write like *you*, in a way you're satisfied with, is extremely difficult.

> ⚠️ **Caution — Don't let it silently edit your prose.** Peter's experience: letting the AI directly edit a blog post means you don't know what it changed, and it quietly adds slop. Better workflow: have it **output its result so you can compare manually** to your own version.

> 💡 **Tip — Design the workflow, not just the prompt.** How you integrate AI feedback into writing matters as much as the feedback itself. You often "don't know whether you like it until you see it," so the interface should let you accept/reject suggestions rather than overwrite your work.

**Anti-slop skills:**

> 🔧 **Tool — "plain writing" skill (Peter's):** an anti-slop pass he runs on everything he writes. He built it up over time to strip AI slop; he plans to open-source it. (Funny demo: inverting the skill to *add* as much slop as possible produces telltale phrases like "Here's the thing" and "This is a paradigm shift.")

> ⚠️ **Caution** — Aggressive anti-slop passes can go overboard and start **removing your personality** from the writing.

> 🗣️ **Speaker Opinion (Peter)** — Current models (he name-checks **Fable** and **GPT-5.6 [?]**) "just keep producing slop," which is why he added so much to his cleanup skill.

**Slop tells to watch for** (surfaced later in the demo): **negative contrast** ("it's not X, it's Y"), **triadic parallel enumeration** (lists of threes / "three things to keep in mind"), and **staccato fragments** (very short, <4-word sentences).

---

## 5. Demo: the Error Discovery Skill

Shreya demos her **Error Discovery Skill** (free, on GitHub) live. The scenario: an AI writing assistant has generated a set of writing samples, and she wants to externalize her taste on writing into **LLM judges** without reading everything in a spreadsheet herself.

**How she launches it:**

> 🔧 **Command / setup** — Start a Claude session with `--dangerously-skip-permissions`, model set to **Opus 4.8** (deliberately *not* **Fable**, to avoid burning through her remaining Fable usage on data review). Prompt used: *"use my error discovery skill to build me an interface to help me look at my AI outputs and give feedback."*

> ⚠️ **Caution — It's not instant.** Building the interface from scratch took about **15 minutes** in the demo.

> 🗣️ **Speaker Opinion (Shreya)** — A purpose-built interface is far easier on human eyes than reviewing data in **Google Sheets**, which is "very very hard to read."

### The skill's five steps

1. **Read the dataset** and infer its *semantic* type (an article? code? traces?) — not just the string data type.
2. **Design the visual encoding** — decide how to render the data so it's easy for humans to read, using **Gestalt principles** (color, spacing, opacity) to surface what *varies* in the data (e.g., number of turns in an agent trace). This speaks to human visual processing.
3. **Build the interface** — a "review app" with a **Python backend** and an **HTML/JavaScript front end**.
4. **Choose which samples to review** — from hundreds or thousands of traces, an agent clusters the data and picks a **diverse initial sample** to label.
5. **Run an interactive loop** — the coding agent (Claude Code, Codex, etc.) watches your UI interactions, compiles them into open-ended feedback, reads that feedback in real time, and proposes new samples to label or new rubric criteria.

> 📏 **General Rule — Design philosophy.** The *human* reads and gives open-ended feedback in situ; the *agent's* job is **not** to invent feedback but to **group and distill** your notes into actionable rubric criteria, so you don't do that grouping work yourself.

### Inside the interface

Three tabs: an **article-by-article** (or trace-by-trace) view, a **map view** showing the agent's clustering into semantically meaningful categories, and a **progress view** that auto-populates with the common failure modes emerging from your annotations.

> 🔧 **Tool — the Claude "monitor tool":** runs in the background reacting to each note you give (e.g., logging "my first note from you on the sleep article…"). It lets you stay in flow reading and annotating while reflection happens behind the scenes.

**The feedback flow in practice:**
- Give feedback **in situ** as you read (e.g., "I don't like negative contrast in my writing"; "this 'humble' framing feels annoying — reflect and reason why").
- After roughly **10 reviews/notes**, the agent starts proposing a taxonomy and applying your feedback automatically across all docs. (Shreya notes the 10-note threshold is a useful "carrot" that makes you actually read samples.)

> 💡 **Tip — Reflect live, not just at the end.** Interleaving human think-time with AI think-time (reflection in the background) beats dumping all feedback and waiting for one big reflection at the end.

> ⚠️ **Caution — You still have to look at the data.** Giving feedback is genuinely tedious, and AI "can't read your mind." Voice dictation can speed it up, but you must read through the samples (or at least a real sample). Shreya advises spending a couple of hours and reviewing until you feel **saturated** (e.g., all **18** samples), not just five.

### Failure modes it found

Concrete failure modes surfaced during the demo: **negative contrast** ("not X, it's Y"), **triadic parallel enumeration** (lists of threes), **staccato fragments** (<4 words), and overuse of **colons**.

> 🔧 **Numbers from the run** — The agent generated **361 suggestions**. The "less-than-four-words staccato rule" alone produced **249**. The single *most frequent* failure mode turned out to be **staccato fragments** — surprising to the hosts, who'd expected "not X but Y" to win.

> 📏 **General Rule** — The human drives the *taste*; the AI *scales* it. AI applies the human's discovered criteria across the whole dataset (superpowers), but the human decides what's good and bad.

### What you get out of it

> 💡 **Tip — Turn annotations into a rubric → a skill.** The discovered failure modes become your **rubric**, i.e., your evals. Ask the agent: *"Write a skill that evaluates AI-assisted writing based on the failure modes found."* Each criterion can become an **LLM judge**; you can build a dashboard or monitor traces/outputs in real time.

> 📏 **General Rule** — The **hardest part of evals is error analysis** (producing the rubric). This process makes that part easy.

> 💡 **Tip — You also get a labeled dataset for free.** Because samples are annotated, you can **benchmark the rubric** (measure precision/recall) — evals aren't just a rubric, you need to measure whether the rubric is any good.

**Applying it to Peter's podcast use case:**

> 💡 **Tip** — Create a folder containing the current takeaway-generation skill, example transcripts, and the takeaways you deemed good. Then invoke: *"help me do error analysis on my podcast takeaway skill"* — apply the skill to generate takeaways and build an interface to review them, **especially compared against the good outputs (ground truth).** The interface the agent builds will be *different* from the writing demo's — it reads your data and designs an encoding to fit.

> 📏 **General Rule** — The goal of error analysis is **confidence**: knowing exactly what behavior the LLM is exhibiting.

> 🗣️ **Speaker Opinion** — Because you can just build your own flexible interface with Claude, generic eval **SaaS is "in trouble"**: a bespoke tool fits your workflow in ways off-the-shelf products won't. (Counterpoint from Shreya/Hamel: you need a *very* good idea of your own workflow/process to pull this off.)

> 🔧 **Where to get it** — The **Error Discovery Skill** is free on **GitHub** (Peter will link it in the episode description).

---

## 6. Model & tooling tangent: Codex, Claude, and orchestration

A candid detour on which tools the three are actually using.

> 🗣️ **Speaker Opinion (Shreya)** — **Fable** is exciting for meatier software-engineering tasks. She's also impressed by **Codex** / "the new Soul [?]" for hard tasks with very human-readable output. Her gripe with Claude models lately: they write with **jargon** she'd never use day-to-day, leaving her lost.

> 🗣️ **Speaker Opinion (Hamel)** — He's using **Codex** a lot more, mostly for the **Codex app's functionality**:
> - **Mobile support** on another level — a "command center" showing all sessions across all devices, with no loss of functionality (queue messages, steer, switch models, view artifacts).
> - **Codex can steer Codex** — create threads, have threads talk to each other, tag/front-run a busy thread, do research, rename threads — lightweight orchestration without going "full code factory."
> - **Economics** — fewer limits; frontier models fully within the subscription (versus a "50%" arrangement elsewhere), with limits that keep resetting.

> 🗣️ **Speaker Opinion (all)** — We're in the **"Uber/Lyft era"** of AI models — heavily subsidized cheap pricing that will stop at some point. Hamel also criticizes Anthropic's communication/PR strategy (a jab about "Dario hates Twitter").

> 🗣️ **Speaker Opinion (Peter)** — A former "total Claude fanboy" who switched: he now uses **Codex + GPT** for almost everything (Fable only for planning/bug-finding). **Codex's browser use is "incredible"** — many tools he uses have no API, so it just clicks around and figures things out.

> 🔧 **Tool — reverse-engineering skill (Hamel's):** for any website without an API, it instructs the agent to listen to all network traffic, document the API, and memorialize it as scripts — effectively turning any site into an API. (He mentions **"printing press CLI [?]"** as something similar.)

---

## 7. Do automated evals actually work?

Hamel summarizes his blog post, **"Do automated evals work?"** A wave of vendors now sell "do-it-for-you" evals: you upload your traces, chat with an AI, and say "do my evals for me."

> 🔧 **Tools benchmarked:**
> - **Braintrust** — feature called **"Loop"** (trace viewer + chat).
> - **Arize** — an equivalent feature called **"Alex."**
> - **LangSmith** — a similar capability.
> - Also benchmarked against **coding agents** (Claude, Codex, etc.).

**The experiment:** take a dataset humans had already annotated, and measure how well each automated tool recovers the same errors.

**Findings:**

> 📏 **General Rule** — Automated tools recover **a lot** of errors humans would — but they **all miss the same class of error**: the non-obvious ones requiring **product judgment and taste.**

- **Good at:** obvious failures — a failed tool call, a user expressing dissatisfaction. You don't need product expertise to see these.
- **Bad at:** taste-dependent misses. Example (a real-estate/rental sales agent): failing to handle **sales objections** — replying "we don't have that available, have a nice day" instead of offering alternatives. Also missing **multi-channel** issues, e.g., putting **markdown in text messages** where it doesn't render.

> 📏 **General Rule** — **Coding agents performed about the same** as the dedicated eval tools. The harness is thin — you're really just invoking a model behind someone else's prompt. To improve any of them, you must **steer the agent** with an idea of what's good and bad — which you can't know without doing error analysis first.

> ⚠️ **Caution — Watch precision, not just recall.** Best-case precision is ~**80–90%**, meaning **10–20% of flagged "errors" are red herrings** that can distort your product if you accept them blindly.

> 🗣️ **Speaker Opinion (Shreya)** — She was pleasantly surprised these off-the-shelf tools work as well as they do; absolutely use them — but also review the errors *they* found to confirm you agree.

> 💡 **Tip** — If your traces already live in a tool like **LangSmith**, using its built-in eval feature is a no-brainer (it's in your ecosystem). The tools' main advantage is integration, not superior judgment.

---

## 8. Wrap-up, takeaways & the course

> 📏 **The two headline takeaways:**
> 1. **Use the Error Discovery Skill** — feed it examples and let it help identify the common *themes* of errors (skips the manual theme-finding, though not the data-looking).
> 2. **Use the coding harnesses and eval tools — but also actually read the outputs.** Looking at your data yourself is the edge; the automated baseline is available to every competitor too.

> 📏 **General Rule** — There is **no future, even with AGI, where you don't look at your data** if you're building a product. You have to inject your taste somehow. "Actually reading and looking at stuff" is the durable edge (true of code review, too).

**What the course covers (5 modules, revamped for the agentic-AI era):**
1. The **error-analysis philosophy** (the foundation shown here).
2. **Productionizing & scaling** within a company — aligning multiple people on criteria, integrating into **CI/CD**, monitoring **drift** over months of deployment.
3. **Safety & adversarial evaluation** — e.g., ensuring you don't leak tenant data, evaluated over time before deploying to real customers.
4. **Improvement** — joint **cost and accuracy** improvement; putting evals in an auto-research loop. They claim to have cut cost by up to **100×** (e.g., moving off Opus/Fable while keeping accuracy).

---

## Appendix: caption corrections

The auto-generated captions garbled several names and terms. Corrections applied throughout this document (uncertain restorations flagged `[?]`):

| Caption text | Corrected to | Notes |
|---|---|---|
| "Hambo," "Haml," "Ham," "Hamill," "Hava" | **Hamel Husain** | Guest / instructor |
| "Shrea," "Treya," "Sha," "Shrey," "Straas" | **Shreya Shankar** | Guest / instructor |
| "scale" (as in "use SH's scale," "run the scale") | **skill** | Consistently mis-transcribed; refers to Claude *skills* |
| "emails" (as in "how many emails I add") | **evals** | Mis-transcribed in several places |
| "just stall principles" | **Gestalt principles** | Visual-design principles |
| "mei," "me," "MECI" | **MECE** | Mutually Exclusive, Collectively Exhaustive (consulting term) |
| "Brain Trust" | **Braintrust** | Eval vendor |
| "Arise" | **Arize** | Eval vendor |
| "Langmith" | **LangSmith** | Eval vendor |
| "codeex," "codecs," "CODEX" | **Codex** | Coding agent |
| "Opus 48" | **Opus 4.8** | Model version |
| "Uber Lift" | **Uber / Lyft** | Pricing-subsidy analogy |
| "Elyle," "by Elyle" | **AI / the LLM [?]** | Garbled; likely "AI" |
| "GBT 5.6" | **GPT-5.6 [?]** | Exact version uncertain |
| "peterwisperflow" | **peterwhisperflow [?]** | Sponsor promo code; spelling uncertain |
| "the new Soul" | **[?]** | Possibly a model/codename; unresolved |
| "printing press CLI" | **[?]** | Tool name; spelling/existence unverified |

> ⚠️ **Editorial note** — Slop-tell terminology ("negative contrast," "triadic parallel enumeration," "staccato fragments") is transcribed as spoken by the participants. The framing of some callouts as "Tip" vs. "General Rule" vs. "Speaker Opinion" is this document's editorial classification, not the speakers' own labeling.
