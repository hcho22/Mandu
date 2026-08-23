# Building at the Frontier: Boris Cherny on Claude Opus 5, Ablation, and Unhobbling

> **Format:** Live fireside interview with Boris Cherny, creator of Claude Code, recorded the day after Claude Opus 5 shipped.
> **Callout key:** 💡 Tip · 🛠 Tool · 📏 General Rule · 🗣 Speaker Opinion · ⚠️ Caution

---

## Overview

Boris Cherny walks through what changed with Claude Opus 5 and — more importantly — what that means for how you should build on top of it. The through-line is deletion: Claude Code shipped with **over 80% of its system prompt removed**, because instructions written to correct older models now get in the way of a smarter one. From there he argues for an empirical, ablation-driven development loop (delete everything, use the product, add back only what repeatedly fails), explains "product overhang" and "hobbling," and demonstrates the payoff with two long-running agentic rewrites: **Bun's Zig codebase rewritten to Rust in 11 days**, and the Claude desktop app being rewritten from Electron to Swift by a session that has been running **over two weeks**. He closes on orchestration primitives (dynamic workflows, loops, routines), Anthropic's self-maintaining codebases, and what still separates exceptional builders now that most code is agent-written.

---

## Table of contents

1. [What's new in Claude Opus 5](#1-whats-new-in-claude-opus-5)
2. [Prompt injection: a new frontier](#2-prompt-injection-a-new-frontier)
3. [Deleting 80% of the Claude Code system prompt](#3-deleting-80-of-the-claude-code-system-prompt)
4. [Ablation as a standing development practice](#4-ablation-as-a-standing-development-practice)
5. [Rebuilding the prompt, piece by piece](#5-rebuilding-the-prompt-piece-by-piece)
6. [Evals: the only semi-durable asset](#6-evals-the-only-semi-durable-asset)
7. [Unhobbling and product overhang](#7-unhobbling-and-product-overhang)
8. [Case study: Bun from Zig to Rust in 11 days](#8-case-study-bun-from-zig-to-rust-in-11-days)
9. [Case study: Electron to Swift, still running](#9-case-study-electron-to-swift-still-running)
10. [Elicitation has replaced prompt engineering](#10-elicitation-has-replaced-prompt-engineering)
11. [Orchestrating thousands of agents](#11-orchestrating-thousands-of-agents)
12. [Claude maintaining its own codebase](#12-claude-maintaining-its-own-codebase)
13. [Is coding solved? What separates the best](#13-is-coding-solved-what-separates-the-best)
14. [Advice for CS students](#14-advice-for-cs-students)
15. [Closing announcement](#15-closing-announcement)
16. [Appendix: corrections to the auto-captions](#appendix-corrections-to-the-auto-captions)

---

## 1. What's new in Claude Opus 5

Opus 5 shipped the day before the interview. On **ARC-AGI-3** it reached **30%**, against a prior best in the low single digits to low teens.

Boris frames model training honestly: you try to teach a whole set of new capabilities, most attempts fail, some subset lands — and occasionally the model shows up with abilities nobody trained for.

The headline behavioral change is **duration**. Opus 5 runs for very long periods without stopping, especially combined with **auto mode**. It keeps going because it understands the task needs finishing, rather than because scaffolding forces it to.

> 🛠 **Tool — auto mode**
> Pairing Opus 5 with auto mode is what produces multi-day and multi-week runs. Boris describes runs lasting "days, weeks, months."

> 💡 **Tip — drop the scaffolding**
> You no longer need orchestration scaffolding to keep long tasks alive. Boris explicitly says you don't need `/go` [?] or `/loop` [?] — they help, but the model will run without them.

> 🗣 **Speaker opinion**
> Boris singles out long-horizon execution as something "no other model has done."

---

## 2. Prompt injection: a new frontier

The capability Boris says surprised him most: **Opus 5 does not appear to be prompt-injectable.** A year ago, a model reading an instruction on a web page telling it to do X, Y, Z *and* delete everything on the user's computer would have complied. It no longer does.

This has been improving across generations — noticeable from **Opus 4.7 / 4.8**, good in **Sonnet 5**, and **Fable** was strong at it — but Opus 5 is described as hitting a new frontier.

The defense is three layers stacked:

1. **A well-aligned model** — roughly three years of alignment research.
2. **A prompt-injection classifier** run on all traffic, built on **Chris Olah's** mechanistic interpretability work. It inspects the neurons inside the model that activate when prompt injection occurs — the model may not say anything, but the activation is visible and diagnosable.
3. **The auto mode classifier.**

With all three, Anthropic can no longer demonstrate a successful prompt injection.

> 📏 **General rule — this changes harness design**
> The "lethal trifecta" concern has shaped harness, agent, and product design for years. If injection resistance holds, a large amount of defensive scaffolding in agent products becomes unnecessary. Re-examine yours.

> ⚠️ **Caution**
> "We cannot demonstrate it" is a statement about Anthropic's own red-teaming, not a guarantee. Note also that the resistance is partly a property of the *serving stack* (two of the three layers are classifiers), not the raw model weights alone.

---

## 3. Deleting 80% of the Claude Code system prompt

Claude Code as a harness is under constant change: prompts added, prompts deleted, tools shipped and unshipped, tool prompts rewritten. Every new model release triggers another round.

The reason is simple — **every model is different**. Something tuned for a model three months ago may not transfer at all.

Much of the old system prompt existed to correct behaviors Opus 5 now gets right on its own. So **over 80% of it was deleted** for this release.

> 💡 **Tip — override the system prompt yourself**
> When you run Claude Code you can pass `--system-prompt` [?] and set whatever system prompt you want, to experiment.

> 🛠 **Tool — undocumented "simple mode"**
> Set the environment variable `CLAUDE_CODE_SIMPLE=1` [?] and run `claude`. This strips *all* system prompts, including the ones attached to tools. Anthropic uses it internally as an ablation to test whether the prompts are earning their place.

> 🗣 **Speaker opinion — a genuinely surprising finding**
> With those prompts removed, Boris says the model is *slightly more intelligent*. The prompts stay in the shipped product anyway, because they make Claude Code behave like a coherent product for a human user — that's a product decision, not a capability one.

---

## 4. Ablation as a standing development practice

The interviewer's framing: for each model release you effectively press delete on the prompt and start over — something no normal product team would do every six months. Boris confirms the spirit, with a correction: the entire codebase isn't deleted, but a lot is.

The method borrows the research term **ablation**: delete the whole system prompt, then bring it back **line by line** to measure the impact of each individual line. An eval measures; an ablation *removes* things to measure.

What's left in the Claude Code harness today is mostly **safety, permissions, static analysis, and UI code**. Much of the rest has already been unshipped.

> 📏 **General rule — for builders of agentic products**
> Asked whether everyone building AI products should run ablations on every model release and be brave enough to delete: **"100%."**

> 💡 **Tip — for people who just *use* Claude Code**
> Every six months, delete your `CLAUDE.md`, your skills, and your hooks, and see what the model does. Boris specifically recommends this for Opus 5 — the model may not need instructions that older models required.

---

## 5. Rebuilding the prompt, piece by piece

The rebuild sequence:

1. **Delete.**
2. **Use it.** Run the real product or your real codebase against the new model.
3. **Observe** where it does well and where it stumbles.
4. **Add back only what repeatedly fails** — the same failure, seen more than once.

Don't guess at what instructions the model needs; you'll predict wrong. And don't add too early: every instruction is re-read on *every* invocation, so it has to earn its cost.

> 📏 **General rule — models aren't systems**
> Traditional engineering means big up-front system design, extensive unit tests, and re-architectures measured in months or years. Models don't work that way.

> 🗣 **Speaker opinion — the mental model**
> Boris describes the model as "a living creature," something organic. Each generation behaves differently and has a slightly different personality; you take time to get to know it, then adjust the harness to fit. It's an empirical, scientific discipline: try, observe, iterate.

---

## 6. Evals: the only semi-durable asset

Code and system prompts get deleted at the frontier. Evals are the closest thing to a durable asset — you keep appending to them.

But Boris walks back the strength of that claim himself: evals **outlive the harness, but not by much**. An eval might survive one, two, or three model generations. On the current exponential, evals saturate quickly and get thrown away, and a new set has to be built.

> 📏 **General rule — how to source a new eval set**
> Same loop as everything else: use the product, use the model, find where it actually struggles, and build the eval from those observed failures.

> ⚠️ **Caution — don't over-invest in an eval suite**
> Treat saturation as the expected end state, not a failure. Budget for replacing evals rather than maintaining them indefinitely.

---

## 7. Unhobbling and product overhang

Two sides of one idea:

- **Product overhang** — today's model can already do things nobody has built a product for. The capability exists; nothing elicits it.
- **Hobbling** — your product actively gets in the model's way and prevents the correct behavior from being elicited.

**The origin story of Claude Code.** Roughly 18–24 months earlier, **Sonnet 3.5** was the best coding model available (and, Boris notes, a fairly terrible one by today's standards). The coding products of that moment did single-line autocomplete, sometimes multi-line, and read-only chat about a codebase — no write access. Nothing was eliciting the model's actual ability to write whole functions and whole files.

Claude Code's bet: strip the scaffolding, give the model the **simplest possible harness** and full terminal access, and let it write an entire file — an entire feature. That was the product overhang of the time.

> 🗣 **Speaker opinion**
> With modern models there is *so much* product overhang left that Boris thinks there's a huge amount of unclaimed, commercially valuable opportunity. His hypothesis: dozens to hundreds of undiscovered elicitations exist in today's models.

> 📏 **General rule — how to hunt for overhang**
> 1. **Give the model tasks slightly harder than you think it can handle.**
> 2. **Keep re-throwing your standing hard problem at each new model** — the previous one failing says nothing about the next one.
> 3. **Play with no commercial goal.** The OpenCV drawing discovery (below) came from exactly that.

> ⚠️ **Caution — over-specifying is the common failure**
> The frequent mistake is prescribing *how*: "do this, in this way, step one, then two, then three." For modern models that's the wrong register. Go higher-level: describe the **task**, the **guardrails**, and the **exit criteria**, then let the model cook and check back later.

> 🛠 **Tool — OpenCV as a drawing surface**
> Internally viral at Anthropic: give Opus 5 **OpenCV** and ask it to draw. It produces credible portraits, animals, and landscapes. The model was never trained to draw — it's a pure elicitation gap, found by accident while playing.

---

## 8. Case study: Bun from Zig to Rust in 11 days

Claude Code is built on **Bun**, the open-source JavaScript runtime and faster alternative to **Node.js**. Bun was written in **Zig**, a low-level systems language in the family of C — including manual memory management, which makes memory leaks easy to hit.

The Bun team had been using Claude to **fuzz the codebase** and trigger memory leaks, finding many of them one case at a time. That was the model's capability ceiling at the time.

Then **Jarred** [?] on the Bun team tried the harder version of the problem — a test he re-ran with each model generation. Starting with **Fable**, the model could do it (and Opus 5 can too).

The setup:

- **A test suite as the verifier.** Bun is very well tested, and Node.js has a large test suite too — so correctness is cheap to check.
- **One prompt**, run as a **dynamic workflow**.
- **11 days** of runtime.
- Result: the entire codebase rewritten from **Zig to Rust**.

Not one-shot — there *was* steering. But previous models couldn't have done it even with steering. Human equivalent, per the panel: definitely over a year with the best engineers, for a JavaScript runtime of over 100,000 [lines].

> 📏 **General rule — verification is the enabling ingredient**
> This worked because a mature test suite made "did you do the right thing?" answerable automatically. Pick problems where the oracle already exists, or build the oracle first.

> 💡 **Tip**
> The rewrite is **in production** — it's what Claude Code runs on today.

---

## 9. Case study: Electron to Swift, still running

The Claude desktop app is built with **Electron**. It was sluggish and unreliable six months ago; it's now fast enough that most of the team uses it. Boris wanted to know what a **native** version would feel like.

He ran the whole thing through **Claude Tag** — Claude running inside Slack — bootstrapping the environment conversationally:

1. *"Do you have access to a macOS runner on GitHub?"* → **No.** So he hooked one up, giving it the ability to start a macOS VM via GitHub.
2. *"Can you access this codebase?"* (an empty repo for the Swift rewrite) → **No.** So he granted access.
3. Then the actual prompt: **rewrite the Electron app in Swift; run the Electron app in the macOS VM; screenshot it; compare pixel by pixel against the Swift version; don't stop until you're done.**

That was the entire prompt. At the time of the interview it had been running **a little over two weeks — 14 to 15 days — and was still going.** Nobody in the audience raised a hand for a task running longer.

> 💡 **Tip — the shape of a long-running prompt**
> Three ingredients only: a hard task, a **verification loop** the model can execute itself (run it → screenshot → compare pixel by pixel), and a **stopping condition** ("don't stop until you're done"). No fancy scaffolding.

> 🗣 **Speaker opinion**
> "You don't need the fancy stuff." Boris again names `/go` [?] and `/loop` [?] as helpful but not required.

> 🛠 **Tool — Claude Tag**
> Claude running in Slack. Notably, Claude decided on its own to **live-blog the run**: it created an internal Slack channel and posted progress screenshots every few minutes.

---

## 10. Elicitation has replaced prompt engineering

The job title went from *prompt engineer* to *context engineer*; Boris expects these waves to keep coming and going. The durable skill today is narrower:

1. **Give Claude a task that seems a little too hard.**
2. **Make it possible for Claude to verify its own work along the way.**

> 🗣 **Speaker opinion — the single biggest gap**
> **Verification** is "probably the single most important thing that people do not get right."

> ⚠️ **Caution — there is no one weird trick**
> Boris's advice on where *not* to learn this: "Maybe don't listen to the LinkedIn influencers. Don't read Twitter." People keep hunting for a trick that doesn't exist.

> 📏 **General rule — the full debugging loop**
> Give it a hard task → give it the tools to verify its work, the same way you'd verify yours → watch where it struggles → fix that specific thing with **better prompting**, a **skill**, or — if the model is missing context — an **MCP** server so it can pull the context in. That's the whole method.

> 🗣 **Speaker opinion — who struggles most**
> Engineers with years or decades of experience have the hardest time, because over-specifying is what previous systems demanded. Unlearning it is a journey. The target mental model: **treat the model like a coworker** — that's the level of intelligence it's at now.

---

## 11. Orchestrating thousands of agents

The Electron→Swift run has spawned an unknown number of agents; Boris guesses **thousands to tens of thousands**. Two mechanisms produce that scale:

### Dynamic workflows

A fairly new Claude Code feature. **Invocation is literally: "use a workflow."** That's it — Claude triggers the dynamic workflow itself.

Mechanically: Anthropic uses the **Bun** runtime as a sandbox, starts a VM inside Bun, and lets Claude start and orchestrate many agents inside it. It isn't one agent, or ten parallel agents. For a task like a codebase rewrite, deep data analysis, or a multi-stage feature spanning dozens of pull requests, it will:

- fan out a set of agents for a first pass,
- run a second stage of agents that **verify or summarize** that work,
- fan out again for a third stage — and so on.

Boris's background is functional programming, so the design is **an algebra for agents**: primitives for running agents in sequence and in parallel, with tools for Claude to orchestrate them inside the sandbox token-efficiently.

> 📏 **General rule — this is a new axis of test-time compute**
> Scaling laws historically ran on neural net size, training data, and training FLOPs. Test-time compute (how many tokens are generated) was added recently. Dynamic workflows are a **new way to orchestrate and dramatically ramp up test-time compute** on a single hard task. Boris notes it hasn't been written about much.

### Loops and routines

- **Loop** — essentially a cron job running **locally** for Claude.
- **Routine** — the same thing running **in the cloud**, so you can close your laptop.

> 📏 **General rule — which primitive to use**
> **Dynamic workflow:** *one* task, broken into chunks, sharing context.
> **Loop / routine:** *one repetitive* task, run over and over — every 5 minutes, every hour, every day — that does **not** share context, though it may share memory.

---

## 12. Claude maintaining its own codebase

Anthropic now has Claude maintaining its own products. From a Slack channel, Claude was told to start a set of routines across the codebases for the **CLI, the iOS app, the Android app, and the desktop app**.

Live routines include:

| Routine | What it does |
|---|---|
| **Clean up dead code** | A one-sentence prompt. Runs daily, finds dead code across all codebases using **static and dynamic analysis** — the analysis approach was *not* prompted, Claude figured it out — and opens a PR to delete it. |
| **Ship finished experiments** | Finds experiments already rolled out to 100%, deletes the flag from the codebase, ships it. |
| **Write missing tests** | Adds coverage for areas that need it. |
| **Delete useless tests** | Removes tests that shouldn't be there — junk added by older models or by people at some point. |
| **"Abstraction police"** | Finds nearly-duplicated abstractions that drifted apart across a large codebase and unifies them. |

There are now roughly **20 or 30 routines running daily** across all codebases — hundreds of agents a day, sometimes thousands. Boris frames the output as the work of dozens or hundreds of engineers, freeing people to ship new products and talk to users.

> 💡 **Tip — routine prompts are one sentence**
> Both the dead-code and abstraction routines are single-sentence prompts. The sophistication (which analyses to run, how to detect near-duplicate abstractions) came from the model, not the prompt.

> ⚠️ **Caution**
> "It's not totally there yet" — Anthropic is *on the path* to fully automated app maintenance, not finished.

---

## 13. Is coding solved? What separates the best

Boris has said coding is solved; here he adds the caveat himself: **solved for the kind of coding he does**, not for everyone. Still hard for Claude:

- very deep systems codebases,
- distributed systems,
- fine-grained UI verification — something off by a pixel. Opus 5 was a big leap in **vision and computer use**, but it isn't perfect.

Audience check: a solid show of hands for **100% of code written by agents**; slightly fewer, roughly comparable, for **more than 50%**.

> 🗣 **Speaker opinion — the differentiating mindset**
> Being **empirical**. Forget what you learned about past models. Forget the computer science theory from class. Watch the model attempt a task, see where it struggles, adjust from that. It's no longer a theoretical science — it's an empirical one, and the people who are best at **letting go of their priors** and retrying ideas that failed before are the ones succeeding.

---

## 14. Advice for CS students

Boris learned to code practically, always in service of a concrete problem:

- First language: **BASIC**, on **TI-83** calculators, in middle school — written to solve algebra problems and cheat on math tests. He got good grades, then passed the programs to classmates over a **serial cable**.
- When the math got to **calculus**, BASIC wasn't enough, so he learned **assembly** to write a better solver.
- He also wrote a guide to programming TI-83 calculators that's still online somewhere.

> 🗣 **Speaker opinion — what to still learn the hard way**
> Not just the computer science — learn how to **apply** it. Build startups. Build products. Develop your own **design sense** and **business sense**. Learn **data science**. Learn **how to talk to users**. Those are the skills that, combined with CS and engineering, become really valuable — and the ones he'd still do by hand.

> 💡 **Tip — the summarized arc**
> Build something *you* want first, then level up and build something *people* want.

---

## 15. Closing announcement

Everyone in the room received **Max 20x** accounts — a code sent to their email. The closing challenge from the hosts: someone in the room should build something that runs for **multiple months** and **thousands of agents**.

---

## Appendix: corrections to the auto-captions

Auto-generated captions garbled a number of proper nouns and commands. Corrections applied throughout this document:

| As transcribed | Corrected to | Note |
|---|---|---|
| Cloud Code / clock code / quad code / Clocko | Claude Code | |
| cloud / quad / clot / cla | Claude | |
| Enthropic | Anthropic | |
| hardness | harness | |
| aentic | agentic | |
| Arc AGI 3 | ARC-AGI-3 | |
| Chrisola | Chris Olah | Anthropic mechanistic interpretability researcher |
| SA 3.5 / sonet 3.5 | Sonnet 3.5 | |
| Zigg | Zig | |
| memory weeks | memory leaks | |
| unchip tools | unship tools | |
| dynamic referrals | dynamic workflows | |
| Open CV | OpenCV | |
| cloudmd | `CLAUDE.md` | |
| unhubble / unhobbling | unhobble / unhobbling | |
| Morris (closing thanks) | Boris | |
| Jared (Bun team) | Jarred [?] | Likely Jarred Sumner, Bun's creator — not stated in the transcript |
| SLGO / slashgo | `/go` [?] | Slash command; exact name inferred from audio |
| sloop | `/loop` [?] | Slash command; "loop" is confirmed elsewhere as a feature name |
| "d-system prompt" | `--system-prompt` [?] | CLI flag; exact form inferred |
| "claude code simple equals 1" | `CLAUDE_CODE_SIMPLE=1` [?] | Environment variable; exact name inferred |
| "over 100,000" (Bun codebase) | over 100,000 [lines] [?] | Unit cut off mid-sentence |

**`[?]` marks a restoration inferred from unclear audio — verify against the video or official docs before relying on it.**
