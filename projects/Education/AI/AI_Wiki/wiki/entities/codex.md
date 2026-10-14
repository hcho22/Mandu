---
type: entity
tags: [tool, agent, coding-agent, openai]
status: developing
source-count: 4
last-updated: 2026-10-14
---

# Codex

[[openai]]'s agentic coding tool, and the OpenAI counterpart to [[claude-code]].
It surfaces developer-centric detail (git history, pull requests, diffs); **ChatGPT Work** is described as a different view/UX on the same engine that hides those details for non-coding tasks like slides and docs.

## What shows up in the wiki

- [[running-life-on-codex]] - the primary source. [[jason-openai-codex]] runs much of his work and life on it: pinned long-running threads with automatic [[compaction-over-context-window]], a [[heartbeat-automation]] "Chief of Staff," [[personal-voice-skill]]s, a self-improve skill, the [[skills-vs-plugins]] packaging model (with a public plugin directory), [[browser-use-vs-computer-use]], and the [[goal-plan-worklog]] "ultra goal" build workflow. Effort levels run medium for admin, extra-high/ultra for long builds ([[reasoning-effort-discipline]]).
- Recurs across earlier sources as one of the two agentic coding tools "survived in production" ([[ai-era-50-career-tips]]), and as the cheap high-throughput worker Fable "shells out" to via the Codex CLI in [[working-with-fable-5]]'s [[model-routing]].

## As a code reviewer (2026-10-14)

From [[agentic-code-review-strategies]] ([[john-meta-engineer]]), caption-derived and as of an undated talk:

- Codex's built-in review agent is one of the two default reviewers he considers good enough, alongside [[claude-code]]'s `/code-review`; in his demo it flags lint issues and suggests style changes.
- Its **GitHub integration** (captioned as the "ChatGPT Codex Connector") reviews a PR automatically when it opens, or on demand when Codex is tagged on the PR. It costs money, and he believes, hedged, that it uses a model trained specifically for review.
- He has an agent babysit the PR hourly to answer the Codex reviewer's change requests ([[adversarial-code-review]]).

## Review and goal commands (as of 2026-10-12)

From [[agentic-coding-workflow-idea-to-review]], whose compiler checked public GitHub bot messages and third-party articles rather than OpenAI's documentation:

- The GitHub integration is the `chatgpt-codex-connector` bot. Automatic reviews are enabled per repository in Codex settings; `@codex review` requests one (a focus can follow, such as "for security regressions"); `@codex address that feedback` has it update the PR. Repository review rules go in `AGENTS.md`.
- Codex CLI has a `/review` command and a `/goal` with pause, resume, and clear; the `/goal` arrived behind a feature flag (said to be v0.128) per third-party coverage only.

## Subscription claims (as of 2026-10-02)

From [[token-maxing-with-agents]] ([[theo-t3]]); unverified estimates from an undated video.

- A $200/month Codex plan is worth about $12,000 of tokens, with no split between the top model and cheaper ones.
- **Limit resets** restore the weekly limit and restart its timer; he cites 14 resets in 30 days (a count he credits to someone else) and distinguishes banked resets, usable any time, from immediate ones. He believes they tend to land on Friday evenings.
- New $200 subscriptions were temporarily paused at recording time.
- **Data controls:** Settings, Data controls, "Improve the model for everyone" off; he reads the personal plan's terms as then matching a Team account. That reading is his.
- Enabling WebSocket transport for subscription traffic reduces message latency, by his account.

## Notes

Codex is now the wiki's best-documented **non-Anthropic** agent stack, which matters against the vendor-concentration caveat the [[index]] flags (the input diet is heavily Claude Code-centric).
The patterns Jason describes are near-identical to the Anthropic-side sources - long-running threads, compaction, skills, verifiable goals, taste as the remaining skill - which is itself the finding: the practices are converging across vendors, not diverging.
Model/effort tier names in the source ("GPT-5.6," "Terra," "Luna") are transcription-flagged as uncertain; treat the patterns as durable and the exact tier names as provisional.
