---
type: concept
tags: [agent-operations, evals, rubric, automation, agents]
status: developing
source-count: 2
last-updated: 2026-08-05
---

# The Self-Improving Agent Loop

An agent that **grades its own production behavior against a rubric and opens PRs to fix what it fails.**

[[ryan-carson]]'s Automation C in [[running-teams-of-ai-agents]], and the clearest worked example in the wiki of evals wired directly into a shipping loop.

## The mechanism

1. Untangle runs a production agent named **Grace**, essentially a paralegal, who chats with attorney customers, paralegal customers, and those customers' own clients.
2. A **daily automation** reads those real conversations.
3. It **grades them against a rubric you define**.
4. Anything scoring below your threshold **kicks off a child session to fix it**, which produces a PR.
5. Roughly **three of these fixes ship per day.**

**How to build your own:** pick the most important part of your app that you want to self-improve, then tell the agent how to judge whether a given interaction was good or bad.
**That rubric is the whole design.**

## Why it works

- **The value is in the paper cuts** - small UX details Ryan either didn't know about or wouldn't have bothered to prioritize.
Because the agent already found it, opened the PR, and made it ready, he just ships it.
This is work that would otherwise never clear the priority bar, which is exactly the pattern [[self-maintaining-codebase]] independently arrives at.
- **The big unlock, stated generally:** set your agents up so that **they can make themselves better**, rather than you hand-building all the systems.
- The grading input is **real production traffic**, not a synthetic test set. That is [[looking-at-your-data]] running as a scheduled job.

## The same loop, pointed at a skill library

[[running-life-on-codex]] runs a smaller version of this loop against a **personal skill library** rather than a production app.
[[jason-openai-codex]] built a **"self-improve" skill** that reviews which skills are called most often, reads the sessions where they ran, and surfaces recurring feedback patterns - and periodically audits bloat ("look at the past 400 sessions, which skills were never used, clean things up, interview me").
Worked example: a Slack-reply skill noticed he *always* asked it to reply back into Slack after finishing a Slack-requested task, and absorbed that step so it stopped needing to be asked.
The signal is the same as Ryan's rubric - **a repeated correction is a spec the skill should absorb** ([[self-updating-config]]) - just sourced from your own usage history instead of graded production traffic.

## The two guardrails

**Observability is the hard part, not the automation.**
How do you *know* it failed? Did the agent silently fail and self-fix? What happened to the PR it opened?
Ryan's advice is to work this out *with* the agent - ask it "how do I find out about it?" - and build the answer chain (post to Slack, connect the MCP, pick the channel you watch).

**You still have to use your own product.**
"There's no substitute, and we probably won't have a substitute for a while, for you using your own app."
Even the smartest models still lack the sense of *obvious* - the "why did you think that was okay?" judgment.

## Synthesis

This is the operational sibling of [[outcome-rubric-iteration]], and the difference is where the loop closes.
[[production-agent-with-cma]] attaches a rubric so an agent self-checks *within a task*.
Here the rubric runs *across production history on a schedule*, and the output is a code change rather than a retry.
The eval stopped being a gate and became a **source of work**.

That is the most important idea in this batch for hcho's positioning.
The standard pitch for evals is defensive - catch regressions, prove quality.
This inverts it: a good rubric plus real traffic plus an agent that can open PRs turns the eval system into the thing that **generates the roadmap**.
It is the same move [[data-flywheel]] describes for training data, applied to product changes.

The rubric is also the honest bottleneck.
Everything downstream is plumbing; the judgment is entirely in "how do I define good here," which is [[llm-as-judge]] and [[pass-fail-over-score-evals]] doing load-bearing work in production.
Directly applicable to Rep Today and to the Agentic RAG escalation golden set, where the question "what does a good answer look like" already has to be answered.
