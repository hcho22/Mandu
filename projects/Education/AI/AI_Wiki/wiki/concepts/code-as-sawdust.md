---
type: concept
tags: [future, prompts, strategy, agents]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Code as Sawdust

The forward-looking thesis from [[inside-conductor-workflow]]: code used to be the thing you crafted; now you craft the *description* of what you want, and code is the byproduct - so prompts (and specs) are the durable artifact.

## Key points

- Implication: rerun your prompts on next-generation models to regenerate the code; the old code "didn't really matter."
- Pairs with a "malleable software" vision (moddable-game metaphor: a crafted shared core plus user-level mods/workflows).
- Caveat in tension: this coexists with [[slop-free-zones]] and [[dont-let-ai-be-your-architect]] - not everything is regenerable sawdust; the core and its contracts are still crafted.

## Synthesis

Code-as-sawdust is the strong form of [[build-for-the-model-of-the-future]]: if prompts are the durable asset, you invest in the prompt/spec/eval layer and treat implementation as disposable.
The honest reading for hcho is that it is partly true and partly aspirational - which is exactly why [[slop-free-zones]] exist. The durable artifacts worth crafting are the spec, the eval suite, and the architecture; those are validation-adjacent, so the thesis, taken carefully, favors his skill set.
