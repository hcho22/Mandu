---
type: entity
tags: [person, anthropic, claude-code, agentic-engineering]
status: seed
source-count: 1
last-updated: 2026-07-28
---

# Tharic

A member of Anthropic's ([[anthropic]]) [[claude-code]] team.
The wiki's first primary-source voice on Claude Code itself; every prior account of loops, goals, and workflows came from outside practitioners such as [[theo-t3]].

## What shows up in the wiki

- [[designing-loops-and-workflows]] - interviewed by Peter Yang on getting agents to work autonomously for longer periods.

Positions he is the source for:

- **[[verification-signal-picks-the-mechanism]]** - choose between `/loop`, `/goal`, and workflows by the shape of your verification signal, not by task size.
- **[[self-referential-bias]]** - names the concept, and prescribes three separate roles (coordinate, do, verify) with different context and different models.
- **[[planning-is-removing-unknowns]]** - "the word 'planned' is maybe too broad right now... I like to say [it's about] getting rid of your unknowns." Flagged as his personal framing, not an Anthropic rule.
- **[[principles-over-constraints]]** - the overarching theme of his interview, that smarter models need less direction, fewer constraints, and fewer examples; source for the datum that Anthropic cut the Claude Code system prompt by 80%.
- **[[read-what-the-agent-writes]]** - reading agent-generated explainers as the practice that separates good from best-in-class output.

## Positions and habits

- Runs typically **one active Claude Code session** plus multiple Claude-in-Slack sessions, down from about five parallel Claude Code sessions previously.
This is a notable walk-back from the maximal-parallelism framing in [[get-out-of-the-loop]].
- "My goal for this year is to be more productive, but work less."
Focuses on one primary project at a time while background work runs in parallel.
- Names his own biggest time-waster as being "a little bit lazy," giving a weak prompt, and having to redo the work.
- Cautious about the coworker metaphor for agents: "these metaphors can sometimes be helpful but also limiting," and Claude's memory is "better and worse sometimes... it's spiky." This tempers [[agent-as-employee]].
- Prefers to fully understand a workflow and surface its edge cases before packaging it as a skill ([[building-skills]]).
- Holds that acceptable code cleanliness is use-case dependent, and that organizing a workspace is often more for the human's peace of mind than the agent's needs (tempering [[ai-slop]]).

## Notes

Surname not given in the raw source, which is a summary of an auto-captioned podcast transcript; "Tharic" is the transcribed first name and the corrections appendix does not resolve it further.
As the wiki's first insider voice, his claims carry different evidentiary weight than practitioner accounts: treat the Anthropic-internal facts (the 80% prompt cut, HTML artifacts used for PRs and incident reports, plan availability) as reliable, and the workflow habits as one person's practice, which he repeatedly flags himself.
