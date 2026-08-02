---
type: concept
tags: [agent-operations, agents, routines, maintenance, anthropic]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# The Self-Maintaining Codebase

Anthropic now has Claude maintaining its own products.
From a Slack channel, Claude was told to start a set of routines across the **CLI, iOS, Android, and desktop** codebases ([[building-at-the-frontier]]).

## The live routines

| Routine | What it does |
|---|---|
| **Clean up dead code** | Runs daily, finds dead code across all codebases using **static and dynamic analysis**, opens a PR to delete it |
| **Ship finished experiments** | Finds experiments already rolled out to 100%, deletes the flag, ships it |
| **Write missing tests** | Adds coverage for areas that need it |
| **Delete useless tests** | Removes tests that shouldn't be there - junk added by older models or by people |
| **"Abstraction police"** | Finds nearly-duplicated abstractions that drifted apart across a large codebase and unifies them |

Roughly **20 or 30 routines running daily**, producing hundreds of agents a day and sometimes thousands.
[[boris-cherny]] frames the output as the work of dozens or hundreds of engineers, freeing people to ship new products and talk to users.

## Key points

- **The routine prompts are one sentence.**
Both the dead-code and abstraction routines are single-sentence prompts.
The sophistication - deciding to run static *and* dynamic analysis, working out how to detect near-duplicate abstractions - **came from the model, not the prompt**.
This is [[principles-over-constraints]] at its most extreme, and the strongest evidence for it in the wiki.
- **Every routine ends in a PR**, not in a direct commit. The human gate is at review, not at authorship. Compare [[everything-is-a-pr]].
- The work selected is telling: **entropy removal**, not feature work.
Dead code, stale flags, missing tests, junk tests, drifted abstractions - every routine fights the accumulation that normally requires a periodic human cleanup nobody schedules.
- Boris's own caveat: "it's not totally there yet." Anthropic is on the path to fully automated app maintenance, not finished.

## Synthesis

This is the mature form of [[agents-as-cron-plus-markdown]], and the gap between them is instructive.
[[one-person-company-with-agents]] recorded the pattern as a solo-founder trick - a cron job plus a good skill file.
Here the same primitive runs at the scale of a frontier lab's entire product surface, and what changed is not the mechanism but **how little prompt it needs**.

The deeper point is about which work to automate first.
The instinct is to point agents at feature development, where the visible value is.
Anthropic pointed them at **maintenance** - the work that is individually low-value, collectively enormous, endlessly deferred, and unusually well-specified.
[[ryan-carson]]'s [[production-watchdog]] and [[self-improving-agent-loop]] in [[running-teams-of-ai-agents]] make the same choice independently: the automation targets the paper cuts nobody would prioritize.

For hcho this is directly copyable at Mandu and repo scale.
A daily "find and delete dead code" routine is a one-sentence prompt, and the interesting part is not writing it but **building the observability to know it ran and what it did** - the exact thing [[running-teams-of-ai-agents]] names as the hard half.
