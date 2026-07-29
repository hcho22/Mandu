---
type: source
title: "Designing Loops & Workflows in Claude Code - with Tharic (Claude Code Team)"
source-type: video
author: "Tharic (Anthropic, Claude Code team), interviewed by Peter Yang"
url: "local"
date-ingested: 2026-07-28
date-created: unknown
tags: [claude-code, agentic-engineering, workflows, loops, sub-agents, verification, context-engineering, prompting, anthropic]
concepts: [verification-signal-picks-the-mechanism, self-referential-bias, planning-is-removing-unknowns, principles-over-constraints, read-what-the-agent-writes, sub-agents, agentic-engineering, plan-code-validate, get-out-of-the-loop, building-skills]
---

# Designing Loops & Workflows in Claude Code

A podcast interview (Peter Yang hosting) with Tharic, a member of Anthropic's [[claude-code]] team, on how Anthropic thinks about getting an agent to work autonomously for longer stretches with less hand-holding.
It covers the three orchestration mechanisms (`/loop`, `/goal`, and workflows), a live demo of a video-editing pipeline built in one prompt, a reframing of what "planning" means in agentic work, the shift in how specs are written now that agents read them, Tharic's split between [[claude-code]] and Claude in Slack, and his habits around context hygiene and multi-tasking.

This is the first primary-source Claude Code material in the wiki.
Every prior account of loops, goals, and workflows came from outside practitioners ([[working-with-fable-5]], [[every-claude-feature-ranked]]); this one comes from the team that builds the tool.
Its recurring theme, stated by Tharic up front, is that as models have gotten smarter they need less direction, fewer constraints, and fewer examples.

## Key claims

### The three mechanisms

- **`/loop`** is the general mechanism for iterative, orchestrated agent work: a way of giving the agent feedback so it can run for long periods.
- **`/goal`** reminds the agent of its exit condition and prevents it from stopping early.
Use it when the spec and exploration are already done and you just want execution, including filling in gaps when the agent hits something unexpected.
It pushes the agent to power through instead of pausing to ask whether it should keep going.
- **Workflows** are described as the most powerful of the three.
They spin up [[sub-agents]] to do work in parallel *and* to verify it, which turns a non-deterministic task into something closer to deterministic.
Tharic calls this especially useful for non-technical work.
- **The selection rule is the shape of the verification signal, not the size of the task.**
If you have a deterministic way to check success (for example, checking a rendered UI against a Figma file via the Figma MCP), use `/goal`.
If verification is squishier and requires subjective judgment (for example, comparing against a screenshot), use a workflow with a rubric and a dedicated verification agent.
- Outcomes are "very dependent on the task"; there is no single correct mechanism, only the question of what feedback signal is available.

### Workflows, sub-agents, and verification

- Applied to a podcast-production example: the main agent decides which five segments to cut shorts from, the workflow spins off a sub-agent per segment, and each sub-agent verifies its own clip against a supplied rubric for what a good clip looks like.
- **Give each parallel workflow task a maximum compute budget.**
Without one, Claude puts less verification effort into any individual output when producing several at once, and quality degrades.
- Workflows are implemented as a **JS file**, and that file can be saved into a skill, producing a reusable "skill plus workflow" package.
- Two reasons to use a workflow rather than a single skill: **context management** (sub-agents keep context clean instead of bloating one long session) and **avoiding self-referential bias**.
- **Self-referential bias**, named as a concept: "When a model prefers its own outputs, it's going to be more lenient at verifying it."
The mitigation is to use a separate Claude instance to verify rather than having the instance that did the work also grade it.
- Tharic's recommended structure is three distinct roles: one coordinating, one doing the work, one verifying, each with different context and different models.
He notes this also means each puts more compute in and is less likely to stop early.

### Planning as continuous exploration

- Tharic pushes back on planning as a single one-shot step: "I'm starting to feel like the word 'planned' is maybe too broad right now... I like to say [it's about] getting rid of your unknowns."
He flags this as his personal framing, not a formal Anthropic rule.
- The loop he describes: human request, agent does technical exploration, mockups and explainers to surface unknowns, refine the spec, hand to the agent to implement, agent keeps **implementation notes** on unexpected findings, re-spec if those notes warrant it.
- **Interrogate a dependency before building on it.**
Before building the transcription pipeline he had Claude explain how Whisper works and where it fails: silence can be mis-transcribed as phrases like "thanks for watching," a single word can be split into two chunks, and it has no built-in speaker recognition.
The point is to surface unknown unknowns before rather than during the build.
- **Prototype cheaply first.**
He treats HTML overlay mockups as disposable prototypes and only moves to the expensive step (rebuilding in React, which forces re-rendering video) once a design direction is validated.
- Specs and planning are now "very tied together"; there is no clean one-time handoff from spec to implementation.
- **Failure mode both speakers flag:** users get lazy, stop reading long AI-generated markdown plans, and just say "just do it."
Tharic warns this backfires and costs more time and money later.

### The live demo

- A single prompt produced the whole pipeline: transcribe a sample video with Whisper, use Remotion to build a UI showing the transcript with per-word highlighting and overlays, `/goal` to not stop until the video is fully rendered.
- It executed in one shot.
The transcript needed correction because Claude did not know Tharic's name, and Tharic says he is not yet happy with where the overlay landed.
- His suggested fix for overlay placement is to give the agent more metadata (finger-tracking or face-tracking data) rather than the raw video alone.
- He had not yet packaged the workflow as a skill, preferring to first fully understand what he wants and surface edge cases before packaging.
- HTML artifacts are used broadly at Anthropic for sharing plans, PRs, status reports, and incident reports.
At time of recording they were available on Team and Enterprise plans, not Max or Pro.

### Claude Code versus Claude in Slack ("cloud tag")

- Tharic's split: parallel and background work (initial explorations, PR specs, understanding a problem) happens in Slack via tagging Claude; focused single-thread work happens in [[claude-code]] with iterative back-and-forth.
- He previously ran about five parallel Claude Code sessions and now runs typically **one active Claude Code session** plus multiple Slack sessions.
- Example use: asking Claude in Slack to "babysit" a PR, fix tests, and tag a reviewer, who then joins the same Slack channel.
- Every agent and channel in Slack has its own memory.
- Triggering a skill there needs no special syntax; natural language is enough.
- **Caution on the coworker metaphor:** "I think these metaphors can sometimes be helpful but also limiting... it is kind of helpful to think of an agent that has persistence and memory, but I think they're also different from co-workers in some ways."
He adds that Claude's memory is "better and worse sometimes... it's spiky."

### Context hygiene and prompting style

- **Anthropic cut the Claude Code system prompt by 80%** because as models have gotten smarter they need less direction, fewer constraints, and fewer examples.
- Why fewer examples and constraints help: excessive examples over-constrain the model into mimicking the exact example pattern instead of generalizing; hard "never do X" constraints are usually really "usually don't do X," and stating them as absolutes misfires; explaining the **reason** behind a constraint is more effective than a bare prohibition.
- Tharic believes most `CLAUDE.md` files are too long, and that skills are often too long as well.
- **Constraints to principles:** rather than rigid rules ("must be exactly 280 characters, never do X"), give the agent context about yourself and your principles plus flexible framing ("I'd prefer one tweet, but a two-tweet thread might work better here").
Hard numeric constraints that are genuinely non-negotiable (an actual platform character limit) should still be stated explicitly; the shift is away from *unnecessary* rigidity, not all constraints.
- On MCPs: "it depends on the MCP"; some consume significant context, but the MCP team has invested in reducing this through tool search and related work.

### Repo hygiene and multi-tasking

- `simplify`, a tool built by Boris ([[boris-cherny]]) at Anthropic, simplifies and cleans up a repo; you can also just ask Claude to simplify or organize the workspace periodically.
- Acceptable code cleanliness depends on the use case.
If you only care about the outputs (rendered videos), code quality matters less, because the agent is persistent enough to work through mess.
Organizing the workspace is often more for the human's peace of mind than the agent's needs.
- "My goal for this year is to be more productive, but work less."
Tharic focuses on **one primary project** at a time even while background tasks run in parallel, and names his biggest time-waster as being "a little bit lazy," giving a weak prompt, and having to redo the work.
- "There's an optimal amount of multi-clotting depending on who you are and what you're doing."
Peter, by contrast, describes running five Claude threads simultaneously as exhausting and "worse than back-to-back meetings."

### Becoming more technical

- The goal of getting more technical is to know your **unknown unknowns**: understanding trade-offs between backend services, video encoding libraries, or local versus remote transcription, not memorizing TypeScript syntax.
- Push Claude to brainstorm and teach you the constraints of a system, but "you really do have to push it."
- Citing [[andrej-karpathy]]: "education should feel like work more than fun," used to argue that real learning requires deliberate effort rather than prompting and glancing at output.
- Generating and actually reading detailed HTML reports and explainers is framed as the exception, not the norm, and as the practice that separates "good" outputs from best-in-class ones.
- Suggested habit: add a custom instruction asking Claude to generate an HTML report or explainer for significant tasks, specifically so you are prompted to read and learn from it.

## Connections

- [[verification-signal-picks-the-mechanism]] - the source's central rule; the first explicit criterion in the wiki for choosing between `/loop`, `/goal`, and workflows.
- [[self-referential-bias]] - named here in the agentic-work context; the same phenomenon [[llm-as-judge]] files as self-enhancement bias and [[fresh-context-review]] approaches from the context angle.
- [[planning-is-removing-unknowns]] - reframes planning as continuous exploration; refines [[plan-code-validate]].
- [[principles-over-constraints]] - the prompting-style shift, with the 80% system-prompt cut as its hard datum.
- [[read-what-the-agent-writes]] - the lazy-plan-reading failure mode and the explainer-reading counter-practice.
- [[sub-agents]] - second source, and the first to give a concrete reason to budget compute per parallel task.
- [[agentic-engineering]] - primary-source confirmation of the compound-engineering and context-engineering pillars.
- [[get-out-of-the-loop]] - counterweight: Tharic reduced his parallel sessions rather than increasing them.
- [[building-skills]] - workflows are a JS file that can be packaged into a skill; also "most skills are too long."
- [[reasoning-effort-discipline]] - per-task compute budgets as the parallel-work analogue of the effort lever.
- [[agent-as-employee]] - tempered here; the coworker metaphor is called helpful but limiting.
- [[ai-slop]] - tempered here; cleanliness is use-case dependent, and workspace tidiness is often for the human.
- [[claude-code]], [[anthropic]], [[tharic]], [[boris-cherny]], [[andrej-karpathy]] - entities.

## Source

- **Author:** Tharic (Anthropic, Claude Code team), interviewed by Peter Yang
- **Title:** Designing Loops & Workflows in Claude Code - with Tharic (Claude Code Team)
- **Format:** Podcast interview, ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/Claude_Code_Loops_Workflows_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-28

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Terms flagged as uncertain there and preserved as spoken: "multi-clotting" (Tharic's apparent coinage for running multiple parallel sessions, spelling unconfirmed) and "cloud tag" (the internal nickname for tagging Claude in Slack).
"simplify" as a tool name is inferred from context at medium confidence.
Speaker opinions are distinguished from general rules throughout the raw file, and that distinction is preserved above.
