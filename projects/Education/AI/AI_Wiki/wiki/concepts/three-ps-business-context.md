---
type: concept
tags: [agent-operations, marketing, context-engineering, positioning, brand]
status: seed
source-count: 1
last-updated: 2026-08-21
---

# The Three Ps: Pain, Person, Promise

**The minimum context an agent needs before it can generate anything specific about your business.**

From [[one-person-marketing-team]], where it is run as a prerequisite before any tooling is touched.

| P | The question |
|---|---|
| **Pain** | What pain is your business trying to solve? |
| **Person** | Who specifically feels that pain? |
| **Promise** | How does your product promise to solve that pain for that person? |

## The worked example

The source's fictional brand, a canned protein coffee:

- **Person** - a busy, fitness-minded professional who relies on coffee, cares about protein, and rushes through breakfast.
- **Pain** - mornings require too many separate products: coffee, a protein shake, and something portable.
- **Promise** - the coffee ritual and the protein in one grab-and-go can.

Everything downstream is derived from these three: website copy, ad angles, carousel hooks, UGC scripts.
The website that came out of it opened on *"Your morning shouldn't require two drinks"* - the Pain, stated first, with the product arriving second.

## Why it is the anti-slop mechanism

The source's claim is that this is what stops marketing assets from reading as [[ai-slop]].
Assets need purpose and intent behind them, and **the intent has to come from the Three Ps rather than from the model**, because the model has no way to invent a specific person with a specific problem and will default to a plausible average one.

That is worth stating precisely, because it explains a failure mode rather than just prescribing a template.
Generic output is not usually a prompting failure.
It is the model correctly answering an underspecified question.
"Write me an ad" has no right answer, so it returns the average of all ads.
"Write an ad for someone who owns three separate morning products and is late" has one.

## Synthesis

This is [[context-is-king]] compressed into the smallest schema that still does work, and its value is precisely that it is small.
The wiki holds several context frameworks - [[four-cs-framework]], [[goal-plan-worklog]], the [[seven-part-agent-spec]] - and all of them are heavier than most people will actually fill in.
Three questions get filled in.

It also connects to the wiki's distribution material more tightly than the source realizes.
[[creative-is-the-targeting]] says Meta's ad serving now reads your creative and your landing page and routes on *content* rather than on interest checkboxes, which makes specificity the targeting mechanism.
The Three Ps are the input format that produces that specificity.
Read together, the two pages make an unusually clean claim: **write down the exact person and their exact pain, and the algorithm will find them for you.**
Vague positioning gives the model nothing to route on.

The limit is that the Three Ps are only as true as your answers.
This source filled them in for an invented brand, so they were internally consistent and unfalsifiable.
[[test-breadth-over-conviction]] is the necessary counterweight: your stated Pain and Promise are a hypothesis, not a finding, and the market decides which framing of them lands.
The Three Ps get you specific; testing tells you whether you were specific about the right thing.

For hcho the direct application is that Purvia and Rep Today should each be able to answer these three in one sentence apiece, and the honest test is whether an agent handed only those three sentences could write copy he would actually ship.
That is a cheap and uncomfortable diagnostic for positioning clarity.
