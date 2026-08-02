---
type: concept
tags: [agentic-engineering, product, opportunity, elicitation, anthropic]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Product Overhang and Hobbling

Two sides of one idea, from [[boris-cherny]] in [[building-at-the-frontier]]:

- **Product overhang** - today's model can already do things nobody has built a product for. The capability exists; nothing elicits it.
- **Hobbling** - your product actively gets in the model's way and prevents the correct behavior from being elicited.

## The origin story as proof

Roughly 18-24 months before the interview, **Sonnet 3.5** was the best coding model available and, Boris notes, fairly terrible by today's standards.
The coding products of that moment did single-line autocomplete, sometimes multi-line, and read-only chat about a codebase, with **no write access**.

Nothing was eliciting the model's actual ability to write whole functions and whole files.

[[claude-code]]'s bet was to strip the scaffolding, give the model the **simplest possible harness** plus full terminal access, and let it write an entire feature.
That was the product overhang of the time, and capturing it built the product.

## How to hunt for overhang

1. **Give the model tasks slightly harder than you think it can handle.**
2. **Keep re-throwing your standing hard problem at each new model.** The previous one failing says nothing about the next one. (The Bun Zig-to-Rust rewrite in [[long-horizon-agent-runs]] was exactly this: a test re-run every generation until one passed.)
3. **Play with no commercial goal.** The internally-viral discovery that Opus 5 can draw credible portraits given **OpenCV** came from precisely that - the model was never trained to draw, and the gap was pure elicitation, found by accident.

## Key points

- Boris's hypothesis: **dozens to hundreds of undiscovered elicitations exist in today's models**, and there is a huge amount of unclaimed, commercially valuable opportunity.
- **The common form of hobbling is over-specifying** - prescribing *how* ("do this, in this way, step one, then two, then three").
The right register is higher-level: describe the **task**, the **guardrails**, and the **exit criteria**, then let the model cook.
- Experienced engineers hobble the most, because over-specification is what every previous system demanded of them.
- Hobbling and overhang are not symmetric. Overhang is opportunity you haven't taken; hobbling is opportunity you are actively destroying.

## Synthesis

This is the wiki's best available theory of **where value comes from in an AI product**, and it reframes product strategy as a search problem rather than a design problem.
The scarce resource is not model capability and not engineering; it is the willingness to keep asking a model to do something it failed at last time.

It sits underneath several pages that previously read as unconnected advice.
[[build-for-the-model-of-the-future]] is the strategic version of the same claim.
[[ablation-driven-development]] is how you stop hobbling.
[[elicitation-over-prompt-engineering]] is the skill that finds overhang.

For hcho the operational reading is uncomfortable but useful: **a standing hard problem is an asset**, and the discipline is to keep a list of things the model recently could not do and re-test it every release, rather than filing them as settled limitations.
The Agentic RAG flagship's harder open questions (see the Agentic RAG wiki, `projects/Agentic_RAG/wiki/`) belong on that list rather than in the "not feasible" bucket.
