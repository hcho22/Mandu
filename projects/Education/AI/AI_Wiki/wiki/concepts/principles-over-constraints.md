---
type: concept
tags: [prompting, context-engineering, claude-code, craft, anthropic, agents-md]
status: established
source-count: 3
last-updated: 2026-08-27
---

# Principles Over Constraints

The prompting-style shift from [[designing-loops-and-workflows]]: as models get smarter they need **less direction, fewer constraints, and fewer examples**, so give the agent your context and principles rather than a rulebook.
The hard datum behind it is that Anthropic ([[anthropic]]) **cut the [[claude-code]] system prompt by 80%** for this reason.

## Why fewer examples and constraints help

- **Excessive examples over-constrain.** The model starts mimicking the exact example pattern instead of generalizing from it.
- **Hard prohibitions are usually overstated.** A "never do X" constraint is typically really "usually don't do X," and stating it as an absolute misfires.
- **Explaining the reason beats stating the rule.** A constraint with its rationale attached is more effective than a bare prohibition.

## What it looks like in practice

Rather than rigid rules ("must be exactly 280 characters, never do X"), supply:

- **Context about yourself** ("I work on Claude Code at Anthropic, here are the principles we follow").
- **Flexible framing** ("I'd prefer one tweet, but a two-tweet thread might work better for this").

This leaves the model room to find a better solution than the constraint would have allowed.

## The limit of the rule

Hard numeric constraints that are genuinely non-negotiable, such as an actual platform character limit, should still be stated explicitly.
The shift is away from *unnecessary* rigidity, not away from all constraints.

Note also that this is about **instructions**, and it does not soften [[capabilities-not-instructions]].
If anything it strengthens that page's argument: if instructions are this soft and negotiable a control surface, then anything you genuinely cannot allow must be removed from the agent's key ring rather than forbidden in prose.

## Trim what you have

- Tharic believes most `CLAUDE.md` files are currently too long, and that skills are often too long as well.
This reinforces [[building-skills]]'s existing "keep it human-reviewable, favor progressive disclosure" rule from an Anthropic insider.
- On MCPs: "it depends on the MCP."
Some consume significant context, but the MCP team has invested in reducing this through tool search and related work.

## Second primary source, and the method behind it (2026-08-01)

[[building-at-the-frontier]] confirms the 80% cut from the person who ships the harness, and supplies what this page was missing: **how you find out which 80%.**

[[boris-cherny]]'s answer is [[ablation-driven-development]] - delete the whole system prompt, bring it back line by line, and add back only what repeatedly fails.
"An eval measures; an ablation removes things to measure."
Anthropic runs this internally with an undocumented simple mode that strips *all* system prompts including tool prompts.

Three additions that sharpen the rule:

- **The reason the cut worked:** with those prompts removed the model is *slightly more intelligent*. They ship anyway because they make Claude Code behave like a coherent product for a human - a product decision, not a capability one.
- **Every instruction is re-read on every invocation**, so it has to earn its token cost. That is the mechanism behind "too long," stated as economics rather than taste.
- **The failure has a demographic:** engineers with years or decades of experience struggle most, because over-specifying is what every previous system demanded of them.

The most extreme evidence is [[self-maintaining-codebase]]: Anthropic's dead-code and abstraction-police routines are **one-sentence prompts**, and the sophistication - deciding to run static *and* dynamic analysis - came from the model rather than the prompt.

Boris's instruction to users, not just builders: **every six months, delete your `CLAUDE.md`, your skills, and your hooks and see what the model does.**

## The economics stated as a budget (2026-08-27, [[agents-md-is-a-neural-net]])

[[kun]] restates "every instruction is re-read on every invocation" as **model size**: a memory file is like the parameter count of a network, where a bigger file holds more but costs more at inference, so the budget has to be explicit.
That converts this page's qualitative "too long" into a quantitative discipline - pick a token budget for the always-loaded file, and near it every addition is zero-sum against a removal or an extraction ([[skills-as-release-valve]]).
It is the same argument this page makes ("instructions must earn their token cost") given a unit and a ceiling, and it supplies the *where does the trimmed content go* answer via [[agents-md-as-neural-net]] and skills.

## Synthesis

This is a direct corrective to a habit the wiki's own sources encouraged in an earlier model generation, where richer configuration, more examples, and longer skill files read as better engineering.
The counterintuitive claim is that instruction volume and output quality are inversely related past a threshold, because the model's default behavior is now often better than the pattern your examples pin it to.
It fits the wiki's broader arc: [[build-for-the-model-of-the-future]] says build assuming models improve, and this is that principle applied to your own prompts, where the compounding cost of over-specification is that it caps the model at your imagination.

There is a real tension worth holding rather than resolving.
[[context-is-king]] argues the context you feed the model is your differentiator, and this source argues most people feed it too much.
The reconciliation is that the two are talking about different content: [[context-is-king]] means domain data, business specifics, and connected sources, while this page means behavioral instructions and stylistic examples.
Load the first heavily, the second sparingly.

For hcho this is immediately actionable and slightly uncomfortable, since Mandu's own `CLAUDE.md` and skill files are long and rule-dense.
The test it suggests is per rule: does this encode context the model cannot infer, or is it a constraint the model would have satisfied anyway?
The second kind is costing tokens and capping quality.

With the second source that test now has a procedure attached, and the honest reading is stronger.
Mandu's configuration is not just possibly-too-long, it is **debt written against the model generation it was tuned on**, and the only reliable way to find the debt is to zero it and let the failures re-accumulate ([[ablation-driven-development]]).
Boris's demographic observation also lands close to home: a decade of engineering discipline is exactly the background that over-specifies, and unlearning it is described as a journey rather than a decision.
