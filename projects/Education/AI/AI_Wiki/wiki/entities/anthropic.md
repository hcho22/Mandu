---
type: entity
tags: [org, model-provider, agents]
status: developing
source-count: 7
last-updated: 2026-10-02
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

## Pricing and subscription claims (as of 2026-10-02)

From [[token-maxing-with-agents]], an undated video by [[theo-t3]]; claims are his unless marked as checked.

- **API pricing, checked:** Fable 5.1 at $10/$50 per million input/output tokens matches the claude-api reference cached 2026-09-25, which also lists Opus 5.5 at $4/$20 and the Project Glasswing model Claude Mythos 5.1 at $10/$50.
- **Not documented in that reference:** his figure of $25/$125 quoted for continued Claude Mythos Preview use; his "roughly 70% cheaper" comparison is 60% on his own numbers.
- **Subscription value, his estimate:** a $200/month plan worth about $8,000 of tokens, about half of it Fable under a separate limit; on the 20x plan he says a full five-hour window equals 40% of the seven-day Fable limit.
- **Rumor, unverified:** about 95% API margins and compute rented from SpaceX.
- **Access rules as he states them:** Claude subscriptions only inside [[claude-code]]; sign-ins from known server IP ranges, VPNs, and many simultaneous machines draw scrutiny. The general rule he draws is in [[subscription-vs-api-tokens]].

## Notes

Anthropic's published agent-building guidance ("building effective agents": prefer workflows, add agentic autonomy only when needed) is likely to recur across the agent-engineering sources in `raw/`.
The 80% prompt cut is the wiki's clearest evidence that Anthropic practices [[build-for-the-model-of-the-future]] on its own tooling: the correct response to better models was to delete instructions, not to add them.
Relevant to hcho's positioning: Anthropic states no PhD is required for its target AI-engineer roles, which supports the hardware-QA-to-AI-builder pivot.
