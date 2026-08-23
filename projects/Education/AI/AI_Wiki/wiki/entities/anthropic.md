---
type: entity
tags: [org, model-provider, agents]
status: developing
source-count: 6
last-updated: 2026-07-28
---

# Anthropic

AI safety and research company; maker of the Claude models and of widely-cited guidance on building agents.

## What shows up in the wiki

- **Agent guidance:** cited in [[agents-are-the-new-saas]] for the principle to [[start-as-a-workflow]] and earn autonomy rather than defaulting to full agent autonomy.
- Claude (and tools like Claude Design) recur as the default models/tools in the AI-builder sources hcho is ingesting.
- **[[claude-code]]** (now its own entity page): cited across [[ai-era-50-career-tips]] as one of only two agentic coding tools "survived in production" (with Codex) and the tool to master for [[agentic-engineering]]; built by [[boris-cherny]] on the [[build-for-the-model-of-the-future]] principle. Opus 4.5 is named as the model generation that made Claude Code "click." In [[ai-operating-system-tutorial]] it is the substrate of a personal [[ai-operating-system]].
- **Claude Managed Agents (CMA):** production agent infrastructure ([[managed-agent-primitives]], [[outcome-rubric-iteration]], [[credential-vaults]], [[agent-observability]]); see [[production-agent-with-cma]]. Positioned to "skate the exponential" ([[build-for-the-model-of-the-future]]).
- **Fable 5 and the reasoning-effort ladder:** in [[working-with-fable-5]], Theo ([[theo-t3]]) treats Fable as a step-change in autonomous-run length, not a faster Opus; he flags [[reasoning-effort-discipline]] (keep effort at "high"; x-high/max/Ultra Code over-reason) as a read of the whole Claude 5 family. Workflows and the long-running "goal" primitive in [[claude-code]] are what let Fable ship a month of work in one run.

- **The first insider account** ([[designing-loops-and-workflows]], from [[tharic]] on the [[claude-code]] team): the guiding theme is that as models have gotten smarter they need less direction, fewer constraints, and fewer examples, and **Anthropic cut the Claude Code system prompt by 80%** on that basis ([[principles-over-constraints]]). The same source names [[self-referential-bias]] as a design constraint on agent architecture, gives the `/loop` vs `/goal` vs workflow selection rule ([[verification-signal-picks-the-mechanism]]), and describes internal practice: HTML artifacts for plans, PRs, status reports, and incident reports, and Claude in Slack as the async work surface.

## Notes

Anthropic's published agent-building guidance ("building effective agents": prefer workflows, add agentic autonomy only when needed) is likely to recur across the agent-engineering sources in `raw/`.
The 80% prompt cut is the wiki's clearest evidence that Anthropic practices [[build-for-the-model-of-the-future]] on its own tooling: the correct response to better models was to delete instructions, not to add them.
Relevant to hcho's positioning: Anthropic states no PhD is required for its target AI-engineer roles, which supports the hardware-QA-to-AI-builder pivot.
