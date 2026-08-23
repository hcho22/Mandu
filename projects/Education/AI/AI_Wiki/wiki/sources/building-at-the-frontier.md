---
type: source
title: "Building at the Frontier: Boris Cherny on Claude Opus 5, Ablation, and Unhobbling"
source-type: video
author: "Boris Cherny (Anthropic, creator of Claude Code), live fireside interview"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [claude-code, anthropic, opus-5, ablation, elicitation, prompt-injection, evals, long-horizon-agents, workflows, agentic-engineering]
concepts: [ablation-driven-development, product-overhang, elicitation-over-prompt-engineering, evals-saturate-and-get-replaced, long-horizon-agent-runs, self-maintaining-codebase, dynamic-workflows-as-test-time-compute, principles-over-constraints, verification-signal-picks-the-mechanism, red-team-your-agent, build-for-the-model-of-the-future]
---

# Building at the Frontier

A live fireside interview with [[boris-cherny]], creator of [[claude-code]], recorded the day after Claude Opus 5 shipped.

This is the second primary-source [[anthropic]] account in the wiki, after [[designing-loops-and-workflows]], and it is the more radical of the two.
Where Tharic described how to use the orchestration primitives, Boris argues that the frontier is eating them: the model now runs for days or weeks on its own, and most of the harness you built to keep it alive is dead weight.

The through-line is **deletion**.
Claude Code shipped Opus 5 with **over 80% of its system prompt removed**, because instructions written to correct older models get in the way of a smarter one.
From there the argument generalizes into a standing development method ([[ablation-driven-development]]), a theory of where the unclaimed value is ([[product-overhang]]), and two long-running agentic rewrites as the evidence.

## Key claims

### What changed in Opus 5

- On **ARC-AGI-3** it reached **30%**, against a prior best in the low single digits to low teens.
- The headline behavioral change is **duration**.
Opus 5 runs for very long periods without stopping, especially paired with **auto mode**, and it keeps going because it understands the task needs finishing rather than because scaffolding forces it to.
Boris describes runs lasting "days, weeks, months," and singles out long-horizon execution as something "no other model has done."
- Boris frames model training honestly: you try to teach a whole set of new capabilities, most attempts fail, some subset lands, and occasionally the model shows up with abilities nobody trained for.

### Prompt injection resistance

- The capability that surprised him most: **Opus 5 does not appear to be prompt-injectable.**
A year ago a model reading a web page that told it to do X, Y, Z *and* delete everything on the user's computer would have complied.
It no longer does.
- The trend runs across generations: noticeable from **Opus 4.7 / 4.8**, good in **Sonnet 5**, strong in **Fable**, and Opus 5 is described as a new frontier.
- The defense is **three stacked layers**: a well-aligned model (roughly three years of alignment research), a **prompt-injection classifier** run on all traffic built on **Chris Olah's** mechanistic-interpretability work (it inspects the neurons that activate when injection occurs, so the activation is visible even when the model says nothing), and the **auto-mode classifier**.
- With all three, Anthropic can no longer demonstrate a successful prompt injection.
- Boris's own caveat is preserved: "we cannot demonstrate it" is a statement about Anthropic's red-teaming, not a guarantee, and two of the three layers are properties of the **serving stack**, not the raw weights.

### Deleting 80% of the system prompt

- Every model is different; something tuned for a model three months ago may not transfer at all.
Much of the old Claude Code system prompt existed to correct behaviors Opus 5 now gets right unaided, so **over 80% was deleted** for the release.
- What remains in the harness is mostly **safety, permissions, static analysis, and UI code**.
- An undocumented **"simple mode"** (`CLAUDE_CODE_SIMPLE=1`) strips *all* system prompts including tool prompts; Anthropic uses it internally as an ablation to test whether prompts are earning their place.
- **The surprising finding:** with those prompts removed the model is *slightly more intelligent*.
They stay in the shipped product anyway, because they make Claude Code behave like a coherent product for a human user.
That is a product decision, not a capability one.

### Ablation as standing practice

- The method borrows the research term: delete the whole system prompt, then bring it back **line by line** to measure each line's impact.
An eval measures; an ablation *removes* things to measure.
- The rebuild sequence is **delete, use it, observe, add back only what repeatedly fails** (the same failure seen more than once).
- Don't guess what instructions the model needs, because you will predict wrong, and don't add too early: every instruction is re-read on *every* invocation, so it has to earn its cost.
- Asked whether everyone building AI products should run ablations on every model release and be brave enough to delete: **"100%."**
- For people who merely *use* Claude Code: every six months delete your `CLAUDE.md`, your skills, and your hooks and see what the model does.
He recommends this specifically for Opus 5.
- **The mental model:** the model is "a living creature," something organic.
Each generation has a slightly different personality; you get to know it, then adjust the harness to fit.
Traditional engineering (big up-front design, extensive unit tests, multi-year re-architectures) does not describe this.

### Evals as a semi-durable asset

- Code and system prompts get deleted at the frontier; evals are the closest thing to a durable asset, because you keep appending to them.
- **But Boris walks the claim back himself:** evals **outlive the harness, but not by much**.
An eval might survive one, two, or three model generations.
On the current exponential they saturate quickly, get thrown away, and a new set has to be built.
- Treat saturation as the expected end state, not a failure, and **budget for replacing evals rather than maintaining them indefinitely**.
- Sourcing a new eval set uses the same loop as everything else: use the product, use the model, find where it actually struggles, build the eval from those observed failures.

### Unhobbling and product overhang

- **Product overhang** - today's model can already do things nobody has built a product for; the capability exists and nothing elicits it.
- **Hobbling** - your product actively gets in the model's way and prevents the correct behavior from being elicited.
- **The Claude Code origin story:** roughly 18-24 months earlier, **Sonnet 3.5** was the best coding model (and fairly terrible by today's standards).
The coding products of that moment did single-line autocomplete and read-only chat about a codebase, with no write access.
Nothing elicited the model's actual ability to write whole functions and whole files.
Claude Code's bet was to strip the scaffolding, give the model the **simplest possible harness** plus full terminal access, and let it write an entire feature.
- Boris's hypothesis: **dozens to hundreds of undiscovered elicitations exist in today's models**, and there is a huge amount of unclaimed, commercially valuable opportunity left.
- **How to hunt for overhang:** give the model tasks slightly harder than you think it can handle; keep re-throwing your standing hard problem at each new model, because the previous one failing says nothing about the next; and play with no commercial goal.
- **The common failure is over-specifying** - prescribing *how* ("do this, in this way, step one, then two, then three").
Go higher-level: describe the **task**, the **guardrails**, and the **exit criteria**, then let the model cook and check back later.
- **The OpenCV find:** internally viral at Anthropic, give Opus 5 **OpenCV** and ask it to draw, and it produces credible portraits, animals, and landscapes.
The model was never trained to draw.
A pure elicitation gap, found by accident while playing.

### Case study: Bun from Zig to Rust in 11 days

- Claude Code is built on **Bun**, which was written in **Zig** (manual memory management, easy to leak).
The Bun team had been using Claude to **fuzz the codebase** for memory leaks one case at a time; that was the capability ceiling.
- **Jarred** on the Bun team re-ran a harder standing test with each model generation.
Starting with **Fable** the model could do it, and Opus 5 can too.
- The setup: **a mature test suite as the verifier** (Bun is very well tested, and Node.js has a large suite too, so correctness is cheap to check), **one prompt** run as a **dynamic workflow**, **11 days** of runtime.
- Result: the entire codebase rewritten from Zig to Rust, **now in production** as what Claude Code runs on.
- Not one-shot; there *was* steering, but previous models could not have done it even with steering.
Human equivalent per the panel: over a year with the best engineers, for a runtime of over 100,000 lines.
- **The enabling ingredient is verification.** Pick problems where the oracle already exists, or build the oracle first.

### Case study: Electron to Swift, still running

- Boris wanted to know what a native version of the Electron-based Claude desktop app would feel like.
- He ran it through **Claude Tag** (Claude inside Slack), bootstrapping conversationally: "do you have access to a macOS runner on GitHub?" (no, so he hooked one up), "can you access this codebase?" (no, so he granted access).
- Then the entire prompt: **rewrite the Electron app in Swift; run the Electron app in the macOS VM; screenshot it; compare pixel by pixel against the Swift version; don't stop until you're done.**
- At the time of the interview it had been running **a little over two weeks** and was still going.
Nobody in the audience had a longer-running task.
- **The shape of a long-running prompt is three ingredients only:** a hard task, a **verification loop the model can execute itself**, and a **stopping condition**.
"You don't need the fancy stuff" - `/go` and `/loop` are named as helpful but not required.
- Claude decided on its own to **live-blog the run**, creating an internal Slack channel and posting progress screenshots every few minutes.

### Elicitation has replaced prompt engineering

- The job title went from *prompt engineer* to *context engineer*, and Boris expects these waves to keep coming and going.
The durable skill is narrower: **give Claude a task that seems a little too hard, and make it possible for Claude to verify its own work along the way.**
- **Verification is "probably the single most important thing that people do not get right."**
- On where not to learn this: "Maybe don't listen to the LinkedIn influencers. Don't read Twitter."
People keep hunting for a trick that does not exist.
- **The full debugging loop:** hard task, tools to verify its work the same way you would verify yours, watch where it struggles, then fix that specific thing with better prompting, a **skill**, or an **MCP** server if the model is missing context.
- **Who struggles most:** engineers with years or decades of experience, because over-specifying is what previous systems demanded, and unlearning it is a journey.
The target mental model is to **treat the model like a coworker**.

### Orchestrating thousands of agents

- The Electron-to-Swift run has spawned an unknown number of agents; Boris guesses **thousands to tens of thousands**.
- **Dynamic workflows** are invoked literally by saying "use a workflow"; Claude triggers it itself.
Mechanically, Anthropic uses the **Bun** runtime as a sandbox, starts a VM inside it, and lets Claude start and orchestrate many agents there.
For a codebase rewrite or a multi-stage feature spanning dozens of PRs it will fan out agents for a first pass, run a second stage that **verifies or summarizes** that work, fan out again, and so on.
- Boris's background is functional programming, so the design is **an algebra for agents**: primitives for running agents in sequence and in parallel, with tools for Claude to orchestrate them token-efficiently.
- **This is a new axis of test-time compute.** Scaling laws ran on net size, training data, and training FLOPs; test-time compute (tokens generated) was added recently.
Dynamic workflows are a new way to dramatically ramp up test-time compute on a single hard task, and Boris notes it has not been written about much.
- **Which primitive to use:** a **dynamic workflow** is *one* task broken into chunks that share context; a **loop** (local cron for Claude) or **routine** (the same thing in the cloud, so you can close your laptop) is *one repetitive* task run over and over that does **not** share context, though it may share memory.

### Claude maintaining its own codebase

- From a Slack channel, Claude was told to start routines across the **CLI, iOS, Android, and desktop** codebases.
- Live routines: **clean up dead code** (a one-sentence prompt; runs daily, finds dead code using static and dynamic analysis that was *not* prompted, opens a PR to delete it), **ship finished experiments** (finds experiments at 100% rollout, deletes the flag, ships it), **write missing tests**, **delete useless tests** (junk added by older models or by people), and the **"abstraction police"** (finds nearly-duplicated abstractions that drifted apart and unifies them).
- Roughly **20 or 30 routines running daily**, hundreds of agents a day and sometimes thousands.
Boris frames the output as the work of dozens or hundreds of engineers.
- **Routine prompts are one sentence.** The sophistication came from the model, not the prompt.
- His own caveat: "it's not totally there yet" - Anthropic is on the path to fully automated app maintenance, not finished.

### Is coding solved, and what separates the best

- Boris has said coding is solved and adds the caveat himself: **solved for the kind of coding he does**, not for everyone.
Still hard for Claude: very deep systems codebases, distributed systems, and fine-grained UI verification where something is off by a pixel (Opus 5 was a big leap in vision and computer use, but it is not perfect).
- **The differentiating mindset is being empirical.**
Forget what you learned about past models, forget the CS theory from class, watch the model attempt a task, see where it struggles, adjust from that.
The people best at **letting go of their priors** and retrying ideas that failed before are the ones succeeding.
- Advice for students: learn how to **apply** the CS, not just the CS.
Build startups and products, develop **design sense** and **business sense**, learn **data science**, learn **how to talk to users**.
Build something *you* want first, then level up and build something *people* want.

## Connections

- [[ablation-driven-development]] - the source's central method; delete first, add back only repeated failures.
- [[product-overhang]] - the theory of where unclaimed value sits, and its inverse, hobbling.
- [[elicitation-over-prompt-engineering]] - the durable skill: too-hard task plus self-verification.
- [[long-horizon-agent-runs]] - the 11-day and 15-day runs, and the three ingredients that make them work.
- [[evals-saturate-and-get-replaced]] - the walked-back durability claim; **tension** with the [[evals]] area's compounding-asset framing.
- [[self-maintaining-codebase]] - the 20-30 daily routines; the mature form of [[agents-as-cron-plus-markdown]].
- [[dynamic-workflows-as-test-time-compute]] - orchestration as a scaling axis, not just a convenience.
- [[principles-over-constraints]] - **second primary source** for the 80% cut, and the first to supply the *method* (ablation) behind it rather than just the finding.
- [[verification-signal-picks-the-mechanism]] - **tempered here**: Boris says `/go` and `/loop` are helpful but not required, because the model now sustains long runs unaided.
- [[red-team-your-agent]] - **contradiction flagged**: injection resistance may retire a large amount of defensive scaffolding, with Boris's own caveats attached.
- [[build-for-the-model-of-the-future]] - Boris's own prior principle, now given its operational procedure.
- [[get-out-of-the-loop]] - "describe the task, guardrails, and exit criteria, then check back later."
- [[agentic-engineering]] - the area this source most reshapes.
- [[model-selection]], [[sub-agents]], [[building-skills]], [[credential-vaults]] - touched in passing.
- [[boris-cherny]], [[anthropic]], [[claude-code]] - entities.

## Source

- **Author:** Boris Cherny (Anthropic, creator of Claude Code)
- **Title:** Building at the Frontier: Boris Cherny on Claude Opus 5, Ablation, and Unhobbling
- **Format:** Live fireside interview, recorded the day after Claude Opus 5 shipped; ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/boris-cherny-claude-code-opus-5-summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Items the appendix marks `[?]` as inferred from unclear audio, and which should be verified before being relied on: the slash commands `/go` and `/loop`, the CLI flag `--system-prompt`, the environment variable `CLAUDE_CODE_SIMPLE=1`, the Bun engineer's name (**Jarred**, likely Jarred Sumner but not stated in the transcript), and the "over 100,000" figure for the Bun codebase, where the unit was cut off mid-sentence and "lines" is an inference.

Two claims are self-limited by the speaker and should not be repeated flat:
the prompt-injection resistance is described as "we cannot demonstrate it" against Anthropic's own red-teaming, and two of the three defense layers live in the serving stack rather than the weights;
and "coding is solved" is explicitly narrowed by Boris to the kind of coding he does.
