---
type: concept
tags: [agentic-engineering, skills, writing, voice, codex]
status: developing
source-count: 2
last-updated: 2026-09-23
---

# Personal Voice Skill

A reusable skill that writes in **your** voice, built by pointing the agent at your own historical messages rather than by describing your style in a prompt.
From [[running-life-on-codex]]: [[jason-openai-codex]] built a "write me" skill that reads a past week of his Slack messages and mimics his voice, plus tweet-me, email-me, voice-transcript-to-blog, and video-to-video-essay skills.

## Key points

- **Learned from examples, not instructions.** The skill is grounded in a corpus of your real messages, so it captures voice the way you actually write, not the way you would describe it - an application of "show, don't tell" to style.
- **Refined by audience, not just built once.** Jason tunes tone to shift by audience: external users vs team members, executive vs coworker. The nuance lives in the skill, edited over time.
- **Kept current by re-reading recent output.** Because voice drifts, the maintenance move is periodic: "read the last 200 Slack messages / tweets / blog posts and tell me what's changed," then update the skill ([[self-improving-agent-loop]]).
- **A channel each.** One skill per surface (email, Slack, Twitter) rather than one global "sound like me," because the same person writes differently in each - though these can later be bundled (see [[skills-vs-plugins]]).

## Voice and endorsement are separate (2026-09-23)

[[projects/Education/Marketing/wiki/sources/build-a-digital-brain-guide|The Nicholas Cole interview guide]] complements example-based voice learning with explicit vocabulary, rhythm, formality, and evidence preferences.
Its emphasis on writing down choices qualifies the earlier “examples, not instructions” framing: examples and articulated preferences can work together.
[[projects/Education/Marketing/wiki/concepts/approved-language-repurposing|Approved language repurposing]] adds a different boundary: matching style does not establish that the author endorses a belief or experienced a story.
The marketing guide remains in its subject library; this cross-link is not a duplicate AI source summary.

## Synthesis

This is [[building-skills]] and [[elicitation-over-prompt-engineering]] applied to the narrow, high-frequency task of sounding like yourself: the durable artifact is a skill grounded in your own data, not a paragraph of style rules that a new model will over-fit to.
It connects cleanly to [[taste-as-moat]] - the skill encodes *what you would write*, but you still supply the judgment of whether a given draft is right, which is the part that does not transfer.

For hcho this is directly reusable and already partly in place: Mandu carries a `~/VOICE.md` and communication-style rules for external writing. The upgrade this source suggests is to ground that voice in a corpus of his actual posts/messages rather than a rules file, and to split it by channel (a LinkedIn voice, a cover-letter voice, an outreach voice) - useful for the job-search and build-in-public writing where sounding like himself, not like AI ([[ai-slop]]), is the whole point.
