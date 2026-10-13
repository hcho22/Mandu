---
type: concept
tags: [agent-operations, agentic-engineering, parallelism, attention, workflow]
status: seed
source-count: 1
last-updated: 2026-10-02
---

# Agent Threads as an Inbox

Treat agent threads as tasks to clear, like an email inbox, rather than as conversation history to revisit.
Agents are multi-threaded and humans are single-threaded, so the human is the bottleneck and the interface should show only the threads that need a decision.
From [[token-maxing-with-agents]].

## Key points

- **Threads are to-dos.** A thread that is working should not demand attention; the goal is inbox zero, ending the day with every thread either gone or running.
- **Never watch an agent work.** [[theo-t3]] calls it one of the worst uses of time: if it succeeds, merge; if it fails, read the reasoning or ask the agent why.
Check a thread only when it shows done or needs input.
- **Send in the background.** Dispatch a prompt and stay where you are rather than following the new thread.
- **Remove finished work from view.** In [[t3-code]] a thread can be settled (distinct from archived), snoozed, auto-settled after inactivity, and disappears when its PR merges; working threads are rendered semi-transparent so they draw the eye less.
- **Bundle the next visit into the prompt.** Ask for the PR, a preview environment, and PR babysitting in one message, and state the conditions under which the agent may merge, so the next time you open the thread it is a decision rather than a task.
He estimates about half his threads are archived without his reading the final message.
- **Isolate threads by default.** Each new thread starts in its own git worktree; he treats worktrees as "not perfect but good enough" and leaves collisions to the agents.
- **Morning triage.** After overnight runs (some of his ran 18 hours), go through threads one at a time and decide merge, follow up, or discard, spinning up new threads for fixes noticed along the way.

## Synthesis

The wiki now has three answers to the same bottleneck, and they differ on what the human's interface looks like.

| Answer | Interface | Source |
|---|---|---|
| [[manager-of-agents]] | Many threads, pinned priorities, a fixed check-in cadence | [[ryan-carson]] |
| [[one-orchestrator-agent]] | One agent you talk to; it manages the rest | [[kun]] |
| This page | Many threads, surfaced only when they need a decision | [[theo-t3]] |

All three accept that agent throughput now exceeds human decision throughput; they disagree on whether the human schedules the work, delegates the scheduling, or filters it.
The inbox model is the cheapest to adopt because it is a viewing discipline, but it places the most weight on the merge conditions written into each prompt, which is where [[risk-based-agent-governance]] and [[define-the-end-to-end-gate]] have to live.

It also sharpens the [[read-what-the-agent-writes]] tension.
Archiving threads unread is safe only when the stated merge conditions are a real oracle; a thread closed on a passing unit test has exited the judgment loop, not just the review loop ([[get-out-of-the-loop]]).
And it is a counterweight to [[tharic]]'s retreat from five sessions to one: the inbox discipline is an attempt to raise the number of threads a person can carry without degrading prompt quality, and nothing in the source measures whether it does.

For hcho's firstmate-driven builds the importable parts are small: dispatch and leave, bundle the PR and the check into one prompt, and write merge conditions that name the end-to-end evidence rather than a green unit suite.

## Source

- [[token-maxing-with-agents]] - Theo's practice in his own tool; experience-based, and he builds the product he describes.
