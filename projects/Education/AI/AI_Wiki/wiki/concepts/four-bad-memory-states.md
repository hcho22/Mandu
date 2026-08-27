---
type: concept
tags: [agentic-engineering, agents-md, claude-md, context-engineering, diagnostic]
status: seed
source-count: 1
last-updated: 2026-08-27
---

# Four Bad Memory States

The diagnostic from [[agents-md-is-a-neural-net]] ([[kun]]): look at any project memory file (`AGENTS.md` / `CLAUDE.md`) older than a few months and it is in one of four states.

- **Empty.** The file exists only because a tool created it. The agent reads nothing useful and re-derives the same things every session.
- **Bloated.** Every time an agent did something dumb, someone pasted in a rule. A year later it is 900 lines, every one of which is paid for on every single session forever, and instruction-following gets diluted as the file grows - the rules that matter are buried under the rules that do not.
- **Stale.** Half the rules describe a build system replaced in March. The agent follows them anyway, or learns to ignore the file, which is the same thing.
- **Drifted.** `AGENTS.md` says one thing, `CLAUDE.md` says another, and whichever harness you use today gets a different set of instructions.

## The common root

All four come from the same habit: the file is edited **transactionally, on anecdotal observations**, and it is a lot easier to append than to consolidate and prune.
That is why the fix is not "write a better file" but a different *operation* - budgeted, batched, evidence-driven training ([[agents-md-as-neural-net]]), with skills as the release valve for what the budget cannot hold ([[skills-as-release-valve]]).

## Synthesis

A crisp failure taxonomy that names what the wiki's self-improvement pages are actually fixing.
**Bloat** is the state [[principles-over-constraints]] and [[ablation-driven-development]] attack from the volume side ("most instructions are debt against a model that no longer exists"), and it is the most expensive because it is paid on every invocation while quietly lowering quality.
**Drift** is the state [[two-level-agent-memory]] prevents by keeping user-level preferences and project-level weights separate.
**Stale** is the state a regular backward pass ([[backpass]]) catches, because a rule describing a replaced build system will show up in the transcripts as loss.
For hcho this is a ready-made lint checklist for Mandu's own configuration: is any file empty, is `CLAUDE.md` bloated past its budget, are rules stale, and do the global and project files drift?
