---
type: concept
tags: [agent-operations, agentic-engineering, cloud, parallelism, contradiction]
status: developing
source-count: 2
last-updated: 2026-10-02
---

# Cloud Agents Over Local

[[ryan-carson]]'s central and most contested claim in [[running-teams-of-ai-agents]]: **stop running agents on your own machine.**

## Why local development breaks down

- Local means running your own database, authentication, and dev server - the whole environment on your Mac.
- To do **two** things at once you need **git worktrees** (technical and hard to reason about) or a second copy of the repo in another directory.
- Three, four, five, ten parallel efforts simply does not work.
- **The overhead isn't just mechanical, it's mental:** which worktree am I on, has this been synced, does this change collide with that one.
That overhead is what stops you shipping.

## What cloud agents do instead

- A cloud harness spins up a **VM per session** on a button click - a small server that *is* your dev environment.
- You can create effectively **infinite** numbers of them, with **zero risk of code collision**.
- Ryan typically runs **at least 5 at once, often 10**.
- His workflow reduces to: open browser, new session, new VM, work. He never thinks about environment coordination.
- A side effect he treats as essential: the browser is the client, so he does **50%+ of his work from his phone**, because agents are blocked waiting on his decisions and waiting until he's back at his Mac makes no sense.

## The contradiction to hold

This directly contradicts two sources the wiki already recorded, and the disagreement is load-bearing rather than cosmetic:

| Source | Position |
|---|---|
| [[building-5-ai-products-solo]] (Josh Pigford) | **Local** phased worktrees, one per product, as the working method |
| [[inside-conductor-workflow]] ([[conductor]]) | Automated parallel **local** worktrees - it is the entire product |
| [[running-teams-of-ai-agents]] (Ryan Carson) | "If you are working locally, I honestly think you are a caveman"; you're shipping **10x less**; the local maxis "are not doing real work" |

Notably, [[conductor]] exists *because* worktrees are painful, and Ryan's argument is that automating the pain is treating the symptom.
That is a coherent disagreement, not a misunderstanding.

**What is not in dispute:** all three want many parallel efforts with no collisions.
They disagree on whether isolation should live in your filesystem or in a VM.

**The one exception Ryan grants:** heavy new front-end work.
Spin up a **local** agent for light front-end and wireframing, then move it into the cloud as quickly as you can.

**Weighing it.** Ryan's evidence is throughput at PMF - 22-25 PRs/day, sometimes 40, one employee, revenue 4x-ing - and his stated forcing function was needing to 50x output.
That is real evidence but it is *n* of 1, from someone with a paid Devin seat, and he concedes the landscape changes every 3-6 months.
The honest position is that the cloud argument gets stronger the more parallel work you actually have, and that below some threshold the local answer is fine.
Josh Pigford runs five products locally, which is not nothing.

## A third position: an owned box at home (2026-10-02)

[[token-maxing-with-agents]] rejects both the laptop and the cloud VPS.
[[theo-t3]] runs long and overnight threads on owned always-on Linux machines (an old computer with Ubuntu is enough; at least 8 GB RAM and 4 cores), reached over Tailscale and driven from [[t3-code]].
His reasons against the cloud are cost (he compares about $275/month for a comparable Hetzner server with about $700 once for owned hardware) and provider scrutiny of sign-ins from server IP ranges; his reason against the Mac is that macOS file-system and security overhead bottlenecks parallel agents.
He still isolates threads with local worktrees on that box, calling them "good enough."
This splits the question in two: where the agent's machine lives (laptop, home server, cloud) and how threads are isolated on it (worktree or VM).
Ryan Carson's argument is mainly about the second; Theo's is mainly about the first.

## Synthesis

The useful reframe is that **worktrees are a workaround for a machine you can only have one of**, and once environments are disposable the whole coordination problem disappears rather than getting easier.

For hcho the practical read is that this is not yet his constraint.
Running one or two focused efforts, the local answer holds, and adopting a cloud harness now would buy parallelism he isn't using while adding vendor exposure - which [[independent-agent-lab-vs-frontier-lab]] argues is the decision that actually matters.
The trigger to revisit is the one Ryan names: **the moment real customers need real fixes and the parallel-effort count goes past two or three.**
Worth noting that this is also the moment [[cost-of-being-wrong]] starts to bite, and the two changes probably arrive together.
