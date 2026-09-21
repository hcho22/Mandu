---
type: concept
tags: [agentic-engineering, prompting, planning, requirements]
status: developing
source-count: 2
last-updated: 2026-09-16
---

# Ramble, Then Let the Agent Structure It

**Dictate everything in your head, unstructured, and let the agent rationalize it.**

From [[agentic-full-stack-build]]: Kun kicks off a new project by dictating roughly **3,000 characters** of unstructured requirements in one go - the problem, the product, and the constraints as they occur to him.

> "This is typically how I kick off a new project. I just ramble, try to explain everything I have in mind to First Mate, and let the agent figure things out."

## What the ramble has to contain

Rambling is not the same as being vague.
His contained specific things that would otherwise have been silently invented for him:

- **The problem** - allowance tracked in a notebook, breaking down once there are multiple rules.
- **The educational goal** - introduce balance, loans, credit, repayments, interest, gradually.
- **The platform** - iOS only for now, and why (his son uses an iPad).
- **The modes** - parent mode writes, child mode is read-only.
- **The hard constraints** - the money is **virtual**, a tracker not real money; data must be **portable and cloud-stored** because parent and child use different devices.
- **The two workstreams he wanted** - market research and technical research, in parallel.

**State the non-negotiable constraints explicitly.**
These are exactly the assumptions that get silently invented for you if you leave them out.

## The two disciplines around it

- **Run market validation before writing code.** If the app already exists exactly as specified, install it instead of building it.
The market scout found nothing matching the full brief and recommended building.
- **Mine the research twice.** The first pass answers "should we build this?"; a second pass over the same research answers "**what should we steal?**"
That second pass produced the feature list that shaped the product - read-only kids view, money buckets, approval requests, lessons attached to real actions.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] expands the beginner prompt to include non-goals, data ownership, privacy, offline behavior, and unresolved assumptions.
The agent organizes those inputs into a product contract; its capacity to impose structure does not authorize inventing missing requirements.

## Synthesis

The claim worth extracting is that **structure is now cheap and completeness is not.**
The traditional advice - write a tight spec before you start - optimized for a reader who would follow it literally and had no capacity to reorganize.
An agent can impose structure on a rambling brain-dump trivially.
What it cannot do is guess the constraints you didn't say.

So the effort should move from *organizing* requirements to *exhausting* them, which is a different and easier task, and one that plays to dictation rather than writing.

This is the front end of [[planning-is-removing-unknowns]].
Tharic's framing is that planning is continuous exploration aimed at eliminating unknowns; the ramble is the cheapest possible first pass at surfacing what you already know, so the exploration can start from the actual gaps.
It also feeds [[review-plans-as-artifacts]]: the ramble produces a plan, and the plan gets reviewed as an artifact rather than as prose.

The "mine the research twice" habit is the underrated part and generalizes past product work - competitive research answers a go/no-go question on the first read and a design question on the second, and most people only do the first read.
