---
type: entity
tags: [tool, agent-orchestration, open-source, remote, parallelism]
status: seed
source-count: 2
last-updated: 2026-10-02
---

# T3 Code

Free, open-source front end for running many coding-agent threads across machines, built by [[theo-t3]].
It drives [[claude-code]] or [[codex]] on each machine, works with existing subscriptions, and is reachable from web, desktop, and mobile clients.

## What shows up in the wiki

- [[working-with-fable-5]] - used with Tailscale and git worktrees to parallelize work and drive agents across machines from a phone.
- [[token-maxing-with-agents]] - the main account of its thread model, which is the product form of [[agent-threads-as-inbox]].

## Features described (as of the 2026-10-02 ingest; undated video)

- **Thread lifecycle:** settle (distinct from archive) removes a finished thread from the sidebar; snooze hides one for later; auto-settle defaults to 3 days of inactivity; merging the PR removes the thread.
- **Background dispatch:** `Cmd+Enter` sends a prompt and runs the thread in the background; `Cmd+Shift+O` opens a new thread.
- **Worktree per thread** by default, so parallel agents do not collide.
- **Multi-machine:** an environment selector chooses which computer runs a thread, projects sharing a git origin are grouped across machines, and a load-balancing setting distributes threads across connected servers.
- **Remote connection:** `npx t3 connect` links a machine through T3 Connect (3 devices free without Tailscale at recording time); `npx t3 serve` connects directly over Tailscale without T3's servers.

## Notes

Every comparison with competing tools comes from its builder and should be read as an interested party's view.
The earlier source's "T3 Connect service is forthcoming" note on [[theo-t3]] is superseded: by this video it exists with a free three-device tier.
