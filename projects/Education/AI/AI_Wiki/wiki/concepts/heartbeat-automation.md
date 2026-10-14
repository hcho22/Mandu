---
type: concept
tags: [agent-operations, automation, scheduled-tasks, chief-of-staff, codex]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Heartbeat Automation

A scheduled agent that runs on a fixed cadence, reads across all your communication surfaces, and hands back one consolidated "what needs your attention" briefing.
From [[running-life-on-codex]], where [[jason-openai-codex]] runs a daily "Chief of Staff" automation on [[codex]] scheduled tasks at 9am, 1pm, and 5pm that reads all Slack, Twitter DMs (via computer use), unanswered email, and his Linear board, updates Linear directly when needed, and surfaces one prioritized view.

## How it is built

- **Start with a one-line heartbeat prompt:** "check my email, Slack, and Linear every [interval] - 9am, 1pm, 5pm - and tell me what to prioritize."
- **Layer incrementally through feedback,** not a big upfront spec: "make sure everything has a link," "start using Linear," until it pre-drafts replies (a link to a ready draft) instead of just flagging that a message arrived.
- **It is not free.** Jason is explicit that this was built up over time through iteration and specific corrections; the polished version is the endpoint of that loop, not the starting prompt.
- **Auto-send is scoped, not uniform.** Reserve autonomous sending for well-defined, low-risk workflows ("make a PR, once tests are green, DM the reviewer the PR link"); stay "surgical" - draft-not-send - on broad inbox and Slack triage ([[phased-autonomy]], [[cost-of-being-wrong]]).

## Relationship to the wiki's existing patterns

This is the OpenAI-side instance of a pattern the wiki already holds from the Anthropic/solo-founder sources:

- [[agents-as-cron-plus-markdown]] - a scheduled trigger plus a good instruction file is the whole primitive; the heartbeat is that, pointed at your inboxes.
- [[production-watchdog]] - the same "compress many events into one digest a human will actually read" move, pointed at your own attention rather than at customer activity.
- [[business-loops]] and [[self-maintaining-codebase]] - recurring scheduled agents that do the individually-low-value, collectively-large work.
- [[open-claw]] - already filed as "an open-source agent platform run as a personal chief-of-staff"; this is the same job on a different stack.

## The same cadence from a builder (2026-10-14)

[[stop-prompting-design-loops-and-goals]] lists three recurring loops [[john-meta-engineer]] runs: babysitting PRs, checking in on work every hour or two, and pulling messages from the threads he follows every three hours into a summary.
The last one is this page's pattern with a narrower intake, and the first two point the same cadence at agent work rather than at inboxes.
He frames all three as automating his own manual attention, which is the heartbeat's purpose stated in one line.

## Synthesis

The contribution over the existing pages is the **on-ramp**: a single heartbeat prompt that a non-engineer can run today, then grow by correction, which is a gentler entry than "build 20-30 daily routines." It is the personal-productivity twin of the production automations in [[agent-operations]], and it shares their real constraint - observability and trust calibration (what it may send vs must only draft) are the hard parts, not the scheduling.

For hcho the honest note is that this overlaps his own [[ai-operating-system]] instinct but points outward at live inboxes rather than inward at a knowledge base; the durable lesson is the build method (start with a heartbeat, grow by feedback, scope auto-send by blast radius), not the specific Slack/Linear wiring.
