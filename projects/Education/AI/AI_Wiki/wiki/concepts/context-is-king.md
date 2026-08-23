---
type: concept
tags: [context-engineering, ai-operating-system, craft]
status: developing
source-count: 2
last-updated: 2026-08-21
---

# Context Is King

The claim from [[ai-operating-system-tutorial]] that the model is not your edge - everyone has the same models - so the differentiator is the context you feed it.

## Key points

- Mental model: the **model is the engine, your context is the fuel.** Good fuel produces useful, non-generic output.
- Models are **stateless**: a fresh session knows only global rules + `CLAUDE.md` + the files you provide; without context it is a beginner every time.
- **Treat tokens like money.**
- Self-test: ask your system "based on our business, what should I do next week?" A generic answer means your context (and the "hands" that pull data) need work.

## The file structure it implies ([[one-person-marketing-team]], 2026-08-21)

The second source is the same idea applied to a business rather than to personal work, and it is concrete where this page is abstract.

**Separate the operating doc from the context.**
`CLAUDE.md` stays short and does two jobs only: say what the project is, and point at the files to read before writing anything.
The actual material - positioning, customer avatar, product facts, voice and copy, message bank, playbooks - lives as individual markdown files in a `context/` directory.
Generated assets land in `output/`, source material in `assets/`.

That routing structure is what makes the claim operational.
An agent that must load everything to know anything is not curating context, it is dumping it, and it collides directly with [[principles-over-constraints]].
A short router plus fat leaf files is progressive disclosure applied to business context.

The source also treats `CLAUDE.md` as **a living document changed daily or weekly**, updated in passing with "add that to the CLAUDE.md, this is important" rather than in a dedicated maintenance pass.
That is the low-ceremony version of [[self-updating-config]].

## Competitive form: [[own-the-context-layer]]

The same source pushes this page's claim one step further, into a strategic position rather than a technique.
If the model is rented and the generation tool is rented, **the context layer is the only part you own** - which makes the question not "which tool" but "what am I accumulating."
That is filed separately as [[own-the-context-layer]], with the important caveat that a context layer guarantees consistency and not quality; [[taste-as-moat]] supplies the rest.

## Synthesis

This is the "why" behind [[agentic-engineering]]'s context-engineering pillar and behind the whole [[ai-operating-system]] idea: the leverage is in curating and connecting context, not in the raw model.
For hcho it is also a positioning point - a validation-minded builder who structures context and data well has an edge that does not depend on model access.
