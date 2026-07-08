---
type: concept
tags: [quality, taste, ai-slop, human-in-the-loop, judgment, review]
date: 2026-07-03
source-count: 5
status: seeded
---

# Human Taste and AI Slop

Keeping human judgment in the loop as the guarantor of quality: AI gets output most of the way, but the last stretch - taste, review, and deliberately protected human-owned zones - is what separates good work from "AI slop."

## From the sources

[[building-an-ai-skill-from-scratch]] quantifies the ceiling:

- Even after all five steps, a skill's output is only ~80-90% there; the final 10-20% is human review and taste, and every skill needs human eyes. A dedicated "skill editor" strips AI slop (em dashes, "this is X, not Y" patterns, filler) but the human still does the last pass.

[[building-5-ai-products-solo]] locates the edge in taste and judgment:

- Branding is hand-made first (name -> logo in Illustrator -> colors) before any code, so the product does not look like AI slop; marketing copy is generated only after the app exists, from real features.
- His real edge is 25 years of pre-AI experience letting him quickly judge whether an approach will work - AI levels the playing field, but judgment does not.

[[inside-conductor-agent-orchestration]] defends human-owned zones structurally:

- "Don't let the AI be your architect": humans own the core concepts, APIs/contracts, and interface; AI-made UI tends not to feel "crafted." "Slop-free zones" are human-written sections where every line must be read by a human, some marked "do not touch if you are an AI." Without boundaries the AI enters a vicious cycle - it sees bad code and writes more.

[[building-your-own-ai-operating-system]] keeps judgment in the loop as a principle:

- Treat the system as a mentor, not an oracle; grant autonomy in phases (the "bike method") only after a skill earns trust. "You can outsource your thinking, but you cannot outsource your understanding" - you still read everything and add your own spin.

[[ai-era-50-career-moves]] names taste as the moat in the age of cheap code:

- Fully AI-generated writing, images, and video are "still usually obvious," so the most human part is taste - and encoding your taste so the machine reproduces your judgment is the central agentic-engineering skill. Actively study the greats to build it.
- When code becomes cheap, value migrates to judgment: "own the problem, not the code." The advice pairs with a warning not to let AI atrophy the underlying skills that let you tell good from slop.

## Synthesis

This is the quality-control concept, and it is the one most aligned with hcho's validation-first positioning. The shared claim across four very different builders is that **AI output asymptotes below "good," and the remaining gap is human taste** - stated as a number (the 80-90% ceiling), as an architecture (slop-free zones and human-owned APIs), as a hiring-of-yourself (25 years of judgment), and as a principle (outsource thinking, not understanding). Two mechanisms operationalize it. **Bounded human-owned zones**: mark the core - APIs, contracts, sensitive code, the brand - as human-guaranteed and let AI have free rein only in clearly separated non-core areas, because unbounded AI amplifies whatever quality it already sees (a vicious or virtuous cycle). **A deliberate final pass**: the workflow explicitly reserves the last 10-20% for a human read-through, which is also what the fresh-context and adversarial techniques in [[evals-for-agents]] automate up to the point where only judgment remains. This is the counterweight to every throughput concept in the wiki ([[parallel-agent-orchestration]], [[agentic-coding-workflow]], [[scheduled-agent-autonomy]]): scale the machine, but keep a human gate on taste and correctness. The interview framing writes itself - "AI slop is a quality problem, and a decade of QA is exactly about where to put the human gate and how to prove the rest" - which is the same instinct that makes [[agent-permissions-and-safety]] and [[evals-for-agents]] load-bearing rather than optional.
