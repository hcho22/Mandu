---
type: concept
tags: [agentic-engineering, context-engineering, skills, prompting, elicitation]
status: seed
source-count: 1
last-updated: 2026-08-21
---

# Let the Agent Interview You for Context

**Instead of writing a context dump, install a skill whose job is to interrogate you until it understands.**

From [[one-person-marketing-team]], where the skill is called `grill me` and its stated purpose is to relentlessly interview the user about every aspect of a topic until shared understanding is reached.

## How it runs

1. Install the skill in the project.
2. Say: "Run `grill me` on my product and my marketing so you understand how I think about it."
3. The agent asks **one question at a time**, digging until it is satisfied.
4. It **saves the interview** as a context file for later sessions.

The source offers it as the fix for a specific and very common blocker: *"I do not know what context to give it."*
The transfer problem is not that the knowledge is missing, it is that it is tacit and unprompted knowledge does not get written down.

## Why one question at a time matters

A questionnaire gets skimmed and half-answered.
A conversation that follows up on your answer reaches the thing you would never have thought to volunteer, which is exactly where the non-obvious context lives.
The agent is also a better interviewer than a form because it can notice when an answer is vague and push on that specific vagueness.

The source makes a second point worth keeping: **skills are not only for generating deliverables.**
Intake and discovery are repeatable workflows too, and they deserve the same treatment as a carousel recipe.

## Synthesis

This is the practical, buildable form of [[elicitation-over-prompt-engineering]], and it inverts that page in a useful way.
[[boris-cherny]]'s formulation is about eliciting good work *from the model* - give it a task that is a little too hard, make its work verifiable.
This is elicitation pointed the other direction: **the scarce material is in the human's head, and the agent is the instrument for extracting it.**

It is also the interview form of [[ramble-then-structure]].
That page says exhaust the constraints first because structure is cheap and completeness is not.
This says you will not exhaust them unaided, so let something else drive the questioning until it stops finding gaps.
The two are the self-serve and assisted versions of the same insight, and the assisted one is strictly better when you do not already know the shape of what you know.

Note the compounding relationship with [[own-the-context-layer]] and [[building-skills]]: the interview produces a durable context file, so the extraction happens once and every later session inherits it.
That is what separates this from just having a good conversation with a chatbot.

Two cautions the source does not raise.
First, an interview transcript is a *raw* artifact and tends to be long and repetitive; it should be distilled into the context file rather than saved as the context file, or it becomes exactly the bloat [[principles-over-constraints]] warns about.
Second, the agent will confidently interview you into confirming a framing it proposed, which is a mild instance of the closure problem in [[creative-entropy]] - the questions come from inside the system.

For hcho this is directly usable and already partly in place: his own harness carries `grill-me` and `grill-with-docs` skills, and this source is outside confirmation that interview-as-intake is a recognized pattern rather than a personal habit.
The specific unexploited application is positioning.
[[three-ps-business-context]] is a three-question version of the same idea, and the honest way to fill it in for Purvia or Rep Today is to be grilled on it rather than to draft it, because a draft will reproduce the framing he already has.
