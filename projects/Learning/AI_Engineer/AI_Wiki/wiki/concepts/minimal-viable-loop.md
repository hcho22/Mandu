---
type: concept
tags: [agent-operations, loops, metrics, scoping]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# The Minimal Viable Loop

**Don't hand the agent a giant goal. Start with the smallest verifiable outcome.**

From [[loops-to-run-your-business]], where the host names it the "MVL" and the guest agrees "100%."

## The rule

Do **not** start with "get 100,000 X followers."
Start by optimizing for **great posts**, with a small verifiable outcome like **10 likes**, or average impressions per post.

**Pick a leading, achievable objective metric** (impressions or views per post per week) rather than a lagging vanity number (total follower count).
Follower growth is a downstream result and is hard to move directly.

## Why the big goal fails

- A lagging metric gives the loop **no gradient**. Total followers barely moves in response to any single post, so there is nothing to learn from.
- It has **no honest stop condition**, which [[business-loops]] identifies as one of the two non-negotiable parts of a loop.
- It fails silently and expensively. The loop runs, burns tokens, and produces no signal that anything is working.
- Be realistic about what a loop can move: the guest is openly skeptical you could get an AI to 100,000 followers, while being happy to run the SEO loop on any site.

## Synthesis

This is the loop-shaped restatement of a rule the wiki already holds in other forms.
[[minimal-useful-agent]] says build the smallest useful agent; [[start-as-a-workflow]] says begin predictable and earn autonomy; [[phased-autonomy]] says grant scope in stages.
The MVL adds the specifically *metric-side* version: **scope the measurement down before you scope the work down**, because the measurement is what makes the loop a loop.

The leading-versus-lagging distinction is the transferable part and generalizes past marketing.
A bug loop on "uptime" is leading; a feature loop on "revenue" is lagging and will not converge.
An eval threshold at 90% is leading; "users are happier" is lagging.
See [[leading-metric-over-vanity-metric]] for that distinction on its own.

For hcho this is the correct scoping for any first loop - Agentic RAG waitlist signups per week rather than "get 50 signups," Rep Today ASO impressions rather than installs.
It is also a caution against the shape of the current validation goal: "book 10 buyer interviews" is a countable target but a *lagging* one, and the leading metric underneath it (conversations started per week from communities and campaign engagers) is the thing a loop could actually move.
