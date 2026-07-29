---
type: concept
tags: [planning, specs, agentic-engineering, workflow, failure-modes]
status: seed
source-count: 1
last-updated: 2026-07-28
---

# Planning Is Removing Unknowns

The reframing from [[designing-loops-and-workflows]]: planning is not a discrete phase you complete before execution, it is continuous exploration whose actual job is to eliminate your unknowns.
Tharic's words: "I'm starting to feel like the word 'planned' is maybe too broad right now... I like to say [it's about] getting rid of your unknowns."
He flags this as his personal framing rather than a formal Anthropic rule.

## The loop

1. Human request.
2. Agent does technical exploration.
3. Mockups and explainers surface the unknowns.
4. Refine the spec.
5. Hand to the agent to implement.
6. Agent keeps **implementation notes** on what it did not anticipate.
7. **Re-spec** based on those notes, if warranted.

The consequence is that specs and planning are now "very tied together."
There is no clean one-time handoff from spec to implementation, because agents read the spec too and the act of building surfaces the questions the spec should have answered.

## Three techniques

- **Interrogate the dependency before you build on it.**
Before building a transcription pipeline, have the agent explain the library and its known failure modes.
For Whisper: silence gets mis-transcribed as phrases like "thanks for watching," a single word can split into two chunks, and there is no built-in speaker recognition.
Every one of those would have been discovered mid-build, expensively, instead of up front.
- **Ask for implementation notes as it works.**
This turns the build into a source of spec corrections rather than a black box, and it is what makes mid-project re-speccing possible instead of only start-of-project speccing.
- **Prototype at the cheapest fidelity that answers the question.**
Disposable HTML mockups validate a design direction before the expensive step (rebuilding in React, which forces re-rendering video).

## Relation to plan, code, validate

This refines [[plan-code-validate]] rather than contradicting it.
That page (from [[building-products-with-agents]], 2026-07-08) holds that plan depth buys autonomy and that the human's leverage sits at the front and the end of a task.
This source (2026-07-28) agrees on the value of planning but disputes its shape: the front-loaded phase becomes a spec-explore-build-re-spec cycle, and depth is achieved by iterating on the plan against what the build discovers, not by writing more of it up front.
Both agree the plan is the control knob.
They differ on whether you turn it once or continuously.

## Synthesis

The sharpest thing here is the redefinition of what a plan is *for*.
A plan is not a description of the work, it is an inventory of what you do not yet know, and it is finished when that inventory is empty rather than when the document is long.
That reframing explains why the "interrogate the dependency" trick pays: asking an agent for a library's failure modes is a cheap, direct query against the unknown-unknown set, which is the same target [[read-what-the-agent-writes]] identifies as the real goal of getting more technical.

For hcho the mapping is almost exact.
Failure-mode enumeration before build is what hardware validation calls a test plan, and this source arrives at it independently as the highest-leverage agentic planning move.
The practical import is that the Whisper question ("explain this dependency and where it fails") is a reusable prompt worth encoding as a Mandu skill, and that asking agents for implementation notes turns every build into evidence about where the spec was wrong.
