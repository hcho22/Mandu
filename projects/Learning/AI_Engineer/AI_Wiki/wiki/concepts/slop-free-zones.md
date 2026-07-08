---
type: concept
tags: [code-quality, agent-safety, ai-slop, boundaries]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Slop-Free Zones

Clearly bounded, human-guaranteed sections of a codebase or docs where every line is read by a human, from [[inside-conductor-workflow]].
Some lines are marked "do not touch if you are an AI - human eyes only."

## Key points

- AI may contribute, but nothing in the zone ships unread by a human.
- The rationale is a vicious cycle: an AI that sees bad code writes more bad code (and the compounding runs positive too, so protect the good parts).
- Pairs with keeping AI out of the architectural core (see [[dont-let-ai-be-your-architect]]).

## Synthesis

Slop-free zones are the deliberate counterweight to [[get-out-of-the-loop]]: you automate review everywhere you can, but you explicitly keep a human in the loop on the parts that must not degrade.
They are the structural version of [[ai-slop]] avoidance and [[taste-as-moat]] - drawing a line around where human taste is non-negotiable.
For hcho this is a clean, defensible practice: not "review everything" or "review nothing," but "mark what must stay human and guarantee it."
