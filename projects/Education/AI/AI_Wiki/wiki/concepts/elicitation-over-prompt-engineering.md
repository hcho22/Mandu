---
type: concept
tags: [agentic-engineering, prompting, verification, skill, anthropic]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Elicitation Has Replaced Prompt Engineering

The job title went from *prompt engineer* to *context engineer*, and [[boris-cherny]] expects these waves to keep coming and going.
In [[building-at-the-frontier]] he names the durable skill underneath them, and it is narrower than either title:

1. **Give Claude a task that seems a little too hard.**
2. **Make it possible for Claude to verify its own work along the way.**

That is the whole skill.

## Verification is the gap

**"Verification is probably the single most important thing that people do not get right."**

This is the second independent Anthropic source to land on the same point.
[[verification-signal-picks-the-mechanism]] ([[designing-loops-and-workflows]]) says the shape of your verification signal decides which orchestration primitive you can use.
This source says verification is the binding constraint on the whole practice, and that the reason the Bun rewrite worked at all ([[long-horizon-agent-runs]]) was a mature test suite making correctness cheap to check.

## The full debugging loop

Give it a hard task, give it the tools to verify its work **the same way you'd verify yours**, watch where it struggles, then fix that specific thing with one of three instruments:

| Failure | Instrument |
|---|---|
| It does the wrong thing | better prompting |
| It does the right thing badly or inconsistently | a **skill** |
| It's missing context it can't reach | an **MCP** server |

## Key points

- **There is no one weird trick.** Boris on where not to learn this: "Maybe don't listen to the LinkedIn influencers. Don't read Twitter." People keep hunting for a trick that doesn't exist.
- **Experienced engineers struggle most**, because over-specifying is what previous systems demanded, and unlearning it is a journey.
- The target mental model is to **treat the model like a coworker** - that is the level of intelligence it's at now.
Note that [[designing-loops-and-workflows]] tempers exactly this metaphor as "helpful but also limiting," and [[agent-as-employee]] takes it further than either.
- The mindset that separates the best is **being empirical**: forget what you learned about past models, forget the CS theory, watch the model attempt a task, adjust from that.
The people best at **letting go of their priors** are the ones succeeding.

## Elicitation pointed the other way

[[agent-interviews-you-for-context]] (added 2026-08-21) is this idea reversed, and the reversal is worth holding.

Boris's formulation is about eliciting good work **from the model**: give it a task that is a little too hard, make its work verifiable.
The other direction is eliciting the scarce material **from the human**, with the agent as the instrument - a skill whose only job is to interview you until the tacit context is on disk.

Both are elicitation in the literal sense, and they fail together: an underspecified task produces average work, and the reason tasks are underspecified is that the specifying knowledge never left the human's head.

## Synthesis

The most useful thing here is the demotion of prompting.
Two years of collective effort went into phrasing, and the frontier's own answer is that phrasing was never the lever - **task difficulty and verifiability** were.
Prompt engineering optimized the input; elicitation optimizes the *problem selection* and the *feedback path*.

This is the clearest single argument in the wiki that hcho's validation background is a first-class AI-engineering skill rather than a differentiator he has to keep justifying.
The scarce capability is designing a check the machine can run on itself.
That is what a validation engineer does, and the frontier's creator of [[claude-code]] names it as the number-one thing practitioners get wrong.

It also sets the bar for the Purvia eval harness (`projects/Purvia/wiki/`): the question is not "do we have evals" but "can the agent run them itself, mid-task, without a human in the path."
