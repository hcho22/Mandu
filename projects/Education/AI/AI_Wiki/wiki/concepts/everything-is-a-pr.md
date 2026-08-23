---
type: concept
tags: [agent-ops, sdlc, code, workflow]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Everything Is a PR

The SDLC discipline from [[one-person-company-with-agents]]: to get a "code factory" where agents write, review, and ship close to 100% of the code, run a full software-development lifecycle "designed for a very large team" even when you are solo, and make every change a pull request.

## Key points

- Reproducible processes that do not depend on you; the human reads PRs and markdown, rarely code.
- A "land PR" playbook tells the agent exactly how to review, resolve, and merge without you (used 10-20x/day).
- Features flow: voice brain-dump to a clarifying-question PRD skill to "build it" to a browser feedback loop to land-PR.

## Synthesis

This is the team-scale version of [[phased-implementation]] (each phase = one PR) and the deployment surface for [[adversarial-code-review]] (the PR is what gets reviewed).
It makes the code factory auditable and safe: the PR is the unit of verification, exactly where hcho's validation discipline plugs in.
