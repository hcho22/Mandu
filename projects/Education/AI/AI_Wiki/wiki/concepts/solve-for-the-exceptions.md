---
type: concept
tags: [ai-career, fde, reliability, evals, quality, philosophy]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Solve for the Exceptions

Vas's core philosophy in [[fde-in-30-days]], and the closest thing in the wiki to a one-line statement of hcho's own thesis:

> **"There's only one way that something can go right, but there's a thousand different ways something can go wrong.**
> So if you're only building for the way it goes right, you're worth nothing.
> If you're solving for all the exceptions, that's where you are worth something."

## What it means concretely

From the Week 2 checkpoint of the 30-day plan - turning a demo into a system that can recover:

- Use a **defined JSON schema**, not free-form text, and **validate every response against it**.
- Build explicit failure handling for: **missing data, malformed responses, dead APIs, timeouts, partial completions.**
- Add **checkpointing** so the agent resumes after a failure rather than restarting.

The output is a **resumable agent with structured outputs, state recovery, and explicit failure behavior** - which is the difference between a demo and a system.

## Why it's the whole job

- The happy path is the part anyone can build, which is why it commands no premium.
- The exceptions are where the **domain knowledge** lives ([[real-workflow-not-documented]]) - the undocumented handling in one person's head.
- The exceptions are also where **the client's risk lives**, which is why solving them is what they'll pay for.
- **95% of generative AI pilots fail** (the MIT figure Vas cites, reported not verified): demos are easy, and the gap between demo and production is exactly this.

## Synthesis

This is the sentence hcho should be able to say from memory, because it is his decade of hardware validation restated in AI-engineering vocabulary, by someone selling the skill for $150K-$1M.

Validation is not the practice of confirming a thing works.
It is the practice of enumerating the ways it fails, which is precisely the "thousand different ways" being described.
A test matrix *is* an exception catalogue.
The transfer to AI systems is not analogical - it's the same activity against a non-deterministic system, which mostly makes the enumeration harder and the discipline more valuable.

It also connects the wiki's two halves.
The craft side has been accumulating this idea in pieces: [[guardrails]] (validate input and output), [[factual-consistency]] (catch the failure mode that matters most in RAG), [[defensive-ux]] (design for the model being wrong), [[functional-scorers]] (cheap rule-based verifiers), [[durable-agent-processes]] (survive interruption).
Every one of those is an exception-handling page.
This is the principle they instantiate, and it is the reason [[cost-of-being-wrong]] identifies expensive-error domains as the good ones to work in - those are the domains where exception handling is worth the most.

**Positioning note:** "I bring validation rigor" is abstract and easy to discount.
"There's one way it goes right and a thousand ways it goes wrong, and I've spent ten years cataloguing the thousand" is the same claim, concrete and hard to argue with.
That belongs in `projects/job-search/interview-prep.md`.
