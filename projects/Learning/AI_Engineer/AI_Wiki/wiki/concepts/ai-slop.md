---
type: concept
tags: [quality, writing, taste, craft]
status: developing
source-count: 3
last-updated: 2026-07-28
---

# AI Slop

The characteristic low-quality signature of unedited AI output, named in [[ai-skill-from-scratch]]: em dashes, "this is not X, this is Y" phrasing, filler words ("leverage," "delve"), and strings of very short sentences.
[[building-5-ai-products-solo]] extends it to design: generic AI-generated branding is visual slop, avoided by doing name, logo, and colors by hand (in Illustrator) before any code, then generating the marketing site from those brand assets.

## Key points

- Skills accumulate slop over time because the AI writes most of the text; a "skill editor" skill should periodically audit for it.
- Slop is best caught by explicit pass/fail checks (see [[skill-eval-loop]]) plus a final human pass.
- Removing slop is mostly cosmetic but is the visible line between "AI output" and work with [[taste-as-moat|taste]].

## A tempering, on code specifically ([[designing-loops-and-workflows]], 2026-07-28)

[[tharic]] is more relaxed than the earlier sources about repo slop, and the distinction he draws is useful:

- **Acceptable cleanliness is use-case dependent.** If you only care about the outputs (rendered videos, in his example), code quality matters less, because the agent is persistent enough to work through mess.
- **Workspace tidiness is often for the human.** Organizing it is "more for the human's peace of mind than the agent's needs."
- The remedy is cheap and on-demand: `simplify`, a tool by [[boris-cherny]], or simply asking Claude to simplify or organize the workspace periodically.

Note the scope.
This tempers slop-anxiety about *internal code and workspace structure*, where the artifact is disposable and the reader is a machine.
It does not touch the original claim, which is about *output people read* (writing, branding, public work), where slop is the visible line between AI output and work with [[taste-as-moat|taste]].
Read alongside [[slop-free-zones]] and [[code-as-sawdust]], the wiki's position is converging on a boundary rather than a rule: regenerable internals tolerate mess, while durable contracts and human-facing surfaces do not.

## Synthesis

AI slop is the concrete, checkable face of the [[taste-as-moat]] argument: the last 10-20% of human review is largely slop removal and judgment.
It is directly relevant to hcho's own standards - his global instructions already ban em dashes and marketing fluff, which is an anti-slop rule set - and it is a natural thing to encode as reusable eval checks across his skills and public writing.
The third source keeps that intact for anything a person reads while removing the guilt from messy internals, which is a genuinely useful permission: cleanup effort is better spent on the surfaces where taste is visible than on tidying code an agent will regenerate anyway.
