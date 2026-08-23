---
type: concept
tags: [agent-operations, marketing, ads, distribution]
status: developing
source-count: 2
last-updated: 2026-08-21
---

# The Creative Is the Targeting

**Andromeda** is Meta's newer ad-serving algorithm.
Rather than relying on interest-based targeting, its AI reads **the ad creative itself** - image, video, on-screen text, script - **and the landing page content**, then uses that combined understanding to decide which ad is shown to which person.

From [[building-marketing-agents]].

## What changes

- **Interest-based targeting is largely obsolete post-Andromeda.**
Targeting people with a "WordPress" interest is no longer how you reach them.
- Instead, **the creative must speak directly to the pain point or outcome** of the target customer, paired with a landing page that clearly explains the product.
The algorithm does the audience-matching for you.
- **Set up conversion events for both the signup action and the payment action** deeper in the funnel, so the algorithm optimizes toward real revenue rather than clicks.
- Consequence Cody draws: "Facebook has turned into the best B2B ads channel that exists right now" - sufficiently niche creative can find the small pool of people (his example: maybe ~10 people in the US) with that exact problem.

## Why this matters beyond ads

The mechanism is that **a model now reads your content and routes it**, replacing a targeting parameter you used to set by hand.
That is the same structural shift as search becoming answer-engine retrieval.

The wiki already holds the search-side version: [[aeo-answer-engine-optimization]] describes SEO becoming AEO, where a model reads your docs and decides whether to cite you.
This is the paid-media instance of the identical change - the interface you optimize against stopped being a keyword or an interest checkbox and became **a model reading your actual content.**

## Arrived at independently, without the mechanism (2026-08-21)

[[one-person-marketing-team]] never mentions Andromeda, ad serving, or targeting at all.
Asked to build a site for a target persona, the agent reported that it had deliberately **opened on the pain, not the product** - the hero line is "Your morning shouldn't require two drinks," with the can arriving second.
The whole asset set is derived from a stated Pain, Person, and Promise ([[three-ps-business-context]]) rather than from product features.

That is this page's prescription reached from craft instinct rather than from how the algorithm works, which is mildly interesting on its own.
The more useful thing it supplies is the **input format**.
This page says specificity is now the targeting mechanism but does not say how to produce specificity on demand; the Three Ps are a three-question schema that does, and it is small enough that people actually fill it in.

Read together: **write down the exact person and the exact pain, put that in the creative and on the landing page, and the algorithm does the audience-matching.**
The corollary is sharper than either page alone - vague positioning is no longer merely unpersuasive, it is *unroutable*, because there is nothing for the model to match on.

## Synthesis

The general rule is that **as models mediate distribution, content quality and specificity become the targeting mechanism.**
There is no longer a meaningful gap between "what you say" and "who sees it," which removes a lever marketers used to pull and makes message clarity load-bearing.

That is good news for a narrow technical product and bad news for vague positioning.
A pitch aimed at "AI developers" gives the algorithm nothing to route on; a pitch aimed at "agency devs who have to make RAG respect per-user document permissions" is legible to both the model and the ten people who have that problem.

For hcho this is a concrete argument that the Agentic RAG campaign's specificity is an asset rather than a reach limitation, and it pairs with [[test-breadth-over-conviction]]: be specific in each variant, and run many specific variants rather than one broad one.
The B2B claim is also worth taking seriously given the starter kit's buyer is a narrow, hard-to-reach professional audience with no warm network to route through.
