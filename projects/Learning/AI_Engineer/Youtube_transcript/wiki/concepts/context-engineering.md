---
type: concept
tags: [context, claude-md, compaction, context-rot, statelessness]
date: 2026-07-03
source-count: 5
status: seeded
---

# Context Engineering

Managing what an agent knows and how much of its context window is spent: loading the right project context (CLAUDE.md / AGENTS.md), keeping context fresh to avoid drift, and using sub-agents and compaction to protect the main window.

## From the sources

[[building-your-own-ai-operating-system]] makes context the thesis:

- The model is the engine, context is the fuel; everyone has the same model, so context is the differentiator. Models are stateless - a fresh session is a beginner until it loads global rules, CLAUDE.md, and your files. Treat tokens like money.
- The self-test: ask a fresh session "based on our business, what should I do next week?" - a bad answer means you need better context and better "hands" to pull data.

[[inside-conductor-agent-orchestration]] tunes context as the customization that matters:

- A few-hundred-line CLAUDE.md plus skills files carrying tuned engineering practices ("we're a startup - don't write enterprise code"), always fast mode for token-maxing, and Context7 MCP for pulling docs.

[[building-5-ai-products-solo]] fights "context rot":

- Each build phase runs in a fresh worktree with no prior context; a running progress/decisions file carries only what the next phase needs. Fresh context per phase reduces context rot so the model hallucinates much less, and the learnings skill mines the transcript to append lessons to CLAUDE.md automatically.

[[building-products-with-coding-agents]] uses sub-agents to protect the window:

- The main reason to use a sub-agent is to keep the main session's context window from blowing up: carve heavy exploratory investigation out to a sub-agent that returns only its conclusion. AGENTS.md carries per-project structure and testing instructions.

[[every-claude-feature-ranked]] makes context visible and reversible:

- The status line's context percentage (e.g., 27%, 274k/1M tokens) tells you when to hand off, /clear, or /compact; /rewind rolls code and conversation to a checkpoint (better than piling corrections on); auto-memory and prompt caching work in the background.

## Synthesis

Every builder treats the context window as the scarce resource to be engineered, and the practices fall into three moves. **Load the right context** - CLAUDE.md / AGENTS.md plus skills are how a stateless model stops being a beginner each session, which is why "context is king" and why editing these files is a near-daily habit. **Keep context fresh** - long sessions accumulate "context rot" that raises hallucination, so fresh worktrees per phase, a compact progress file that carries only the essentials, and /rewind over piled-on corrections all trade breadth of history for signal. **Offload context** - sub-agents (see [[sub-agents-and-multi-agent]]) exist largely to keep exploratory work out of the main window by returning only conclusions, and compaction/caching reclaim space silently. The unifying principle is a token economy: context is fuel you pay for, so you spend it on signal and reclaim it aggressively. This connects outward - the config that context engineering maintains is what the [[agentic-coding-workflow]] plans run against, persistent knowledge that should survive a session belongs in [[agent-memory]] rather than the window, and at the architecture level the monorepo choice in [[agentic-system-design]] is itself a context-engineering decision (give the agent one codebase it can see whole). Note the boundary this wiki keeps: domain knowledge like this compounds in the wiki, while the running context that agents load lives in CLAUDE.md and skills.
