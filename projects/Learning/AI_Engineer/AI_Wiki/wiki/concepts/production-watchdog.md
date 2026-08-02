---
type: concept
tags: [agent-operations, observability, automation, agents]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# The Production Watchdog

A daily agent that reads everything your real customers actually did and hands you a summary with links back into the live product.

[[ryan-carson]]'s Automation B in [[running-teams-of-ai-agents]].

## The mechanism

- Runs **daily at 9:00 a.m.**
- Walks **every event in the database for paid customers**.
- Summarizes them into a **JSON file** and surfaces that file in the admin panel.
- Each morning he opens it and reads what customers actually did.

**The framing:** it's a chief of staff showing up and saying "here's the important stuff that happened for our customers yesterday - what went well, and a couple of bugs we saw."

**The motivation:** with lots of real law firms and real clients on the product, there is no way to track activity mentally by reading logs.

## The detail that makes it work

**Link out to the real UI.**
Pick your most important customers and make sure each line reads *"the customer did X - here's a link to view it,"* pointing at a production instance where you can see exactly what they did.

Ryan calls the linked version "a game changer," and his reason is the interesting part:
**humans are extraordinarily good at spotting "that's weird" at a glance.**
Several times this has led him to click in and discover the UX an agent built wasn't what he assumed.

## Synthesis

The design insight generalizes well beyond this one automation: **the agent's job is not to judge, it is to compress and route.**
It reads a volume of events no human would read, and hands back the one thing humans are better at than models - pattern-breaking recognition on a glance.

That is a cleaner division of labor than most agent designs manage, and it is the mirror image of [[self-improving-agent-loop]], which sits right next to it in the same stack.
There the agent judges against a rubric and acts; here it deliberately does **not** judge, because the failure mode being caught is precisely the one a rubric would miss - the agent built something that works but is obviously wrong to a person.

It also supplies the concrete answer to a gap in [[get-out-of-the-loop]].
Getting out of the loop on *code review* is well covered in the wiki; getting out of the loop on *what your product is doing in production* is not, and the honest constraint from the same source is that you still have to use your own app.
The watchdog is what makes that periodic rather than constant.

Applicable to Rep Today the moment there are real users: a daily digest of what actual people did, linked to the screens they did it on, is a cheaper and better signal than any analytics dashboard at that stage.
