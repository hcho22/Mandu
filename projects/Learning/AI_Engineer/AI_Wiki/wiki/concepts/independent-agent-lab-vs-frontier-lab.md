---
type: concept
tags: [agent-operations, cost, vendor-strategy, model-routing, contradiction]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Independent Agent Lab vs Frontier Lab

[[ryan-carson]]'s sharpest strategic claim in [[running-teams-of-ai-agents]]: **don't build your engineering motion inside a frontier lab's stack.**

If your whole workflow lives inside [[claude-code]] or Codex, those vendors are not incentivized to keep it economical for you long term.
They are incentivized to lock you into their models and their process.

## The argument

- **Independent agent labs** (Amp, Devin/Cognition, Factory, and Cursor with caveats) are incentivized to give you the best result at the lowest price, so they do the hard [[model-routing]] work: a high-effort frontier model for one task, a cheap fine-tuned coding model for another, a check with a premium model at the end.
- **The analogy:** an independent lab is like a **mortgage broker or a travel agent**, making a lot of calls to get you the best price.
- Frontier labs are currently **subsidizing tokens** heavily - at ~$200/month you get near-infinite tokens - and Ryan thinks that is unsustainable.
- **"Yes, and":** you are not abandoning frontier models by using an independent harness. You can still run their models inside these products.
- He still uses Codex and praises the Mac app; a subsidized $200/month plan is **excellent value for a local helper agent** that opens browser tabs, creates docs, checks email.
Just don't build your company's software factory on it.

## When it applies

| Stage | What he recommends |
|---|---|
| One-person shop | A frontier-lab plan is **fine** |
| Post-PMF, real product, starting to hire | You need a software factory - use an **independent agent lab** |
| Large enough to build your own | Only then; doing it early is "stupid" |

His cost anchors: ~**$20,000/month** last month (which he calls not viable), an estimated steady state of ~**$5,000/month per engineer**, and cheap fine-tuned-model loop sessions at ~**$5 each**.
Above ~$5K/month/engineer, routing is no longer optional.

## The contradiction to hold

This is **the wiki's first explicit counter-position to its own bias.**
Most sources here are Claude Code-centric ([[designing-loops-and-workflows]], [[building-at-the-frontier]], [[every-claude-feature-ranked]], [[working-with-fable-5]]), and several are from Anthropic itself.
That is a real sampling bias in the input diet, and this source names the risk it creates.

Two caveats on the other side, in fairness:
Ryan is a **paying Devin customer** describing why his vendor choice is correct, which is its own incentive.
And [[building-at-the-frontier]] is direct evidence *for* frontier-lab depth - dynamic workflows and 15-day runs are not things an independent harness offered at the time of recording.
The claim is about **lock-in risk at scale**, not about capability today, and it should be held at that resolution.

## Synthesis

The transferable idea is that **your harness is a vendor decision, not just a tool preference**, and the switching cost is the thing to watch rather than the monthly price.
Subsidized pricing is the mechanism by which that switching cost gets built without you noticing.

For hcho this is currently a non-issue by Ryan's own staging - a one-person shop on a frontier plan is explicitly fine - but it has one concrete implication now.
The Agentic RAG starter kit is a product sold to *other* builders, and the same logic applies to it: a starter kit welded to one vendor's harness inherits that vendor's lock-in as a product liability.
The kit's existing "raw OpenAI SDK, no LLM frameworks" choice is already the same instinct applied one layer down.
See [[model-routing]] and [[model-build-vs-buy]], which cover the cost and hosting axes of the same decision.
