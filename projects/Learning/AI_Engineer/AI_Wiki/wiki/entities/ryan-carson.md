---
type: entity
tags: [person, solo-founder, agent-ops, cloud-agents]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Ryan Carson

Founder/CEO of **Untangle**, an AI divorce agent for family-law firms.
His fourth company across ~25 years as a founder/CEO; his previous company **Treehouse** reached ~110 full-time employees and taught a million people to code before being acquired.

**Naming correction (2026-08-01):** this page and [[one-person-company-with-agents]] previously recorded the company as "Untangled."
[[running-teams-of-ai-agents]] consistently gives **Untangle**, and that is used here.

## Trajectory across two sources

The wiki has him at two distinct stages, and the change is the interesting part.

| | [[one-person-company-with-agents]] (2026-07-08) | [[running-teams-of-ai-agents]] (2026-08-01) |
|---|---|---|
| Stage | Pre-PMF, $2M seed raised, delaying hiring | **Post-PMF**, revenue projected to **4x this month**, first hires imminent |
| Still solo? | Yes | Yes - **still the only employee** |
| Method | Cron jobs + markdown skill files | Cloud agent fleets + playbooks with triage children |
| Throughput | Not stated | **22-25 PRs/day**, sometimes 40 |
| Spend | Not stated | ~**$20,000/month** in tokens, which he calls not viable |

## What shows up in the wiki

- [[agents-as-cron-plus-markdown]] - his original mental model, now at its fourth source and matured into cloud playbooks.
- [[cloud-agents-over-local]] - his most contested claim: "if you are working locally, I honestly think you are a caveman." Contradicts the local-worktree practice of [[josh-pigford]] and [[conductor]].
- [[manager-of-agents]] - the role reframe, and the finding that managing agents makes you **more** technical, not less.
- [[independent-agent-lab-vs-frontier-lab]] - don't build your software factory inside a frontier lab's stack.
- [[self-improving-agent-loop]] - a daily rubric-grading automation over real customer conversations that ships ~3 fixes/day.
- [[production-watchdog]] - a 9 a.m. digest of what paid customers actually did, linked back to the live UI.
- [[agent-as-employee]], [[everything-is-a-pr]], [[red-team-your-agent]], [[build-the-machine-first]] - from the first source.
- Runs engineering in the cloud on [[devin]]; names **Grace**, Untangle's paralegal agent, as a production agent with a job description.
- [[build-in-public]] - credits ~20 years on X with compounding network payoff.

## Notes

The wiki's most-followed practitioner, and useful precisely because there are two snapshots of the same operator ~3 weeks apart in ingest time.
What held: cron-plus-markdown as the primitive, everything-is-a-PR, build the machine first.
What changed: the infrastructure moved to the cloud, the bottleneck moved from building to **deciding** (10-20 high-stakes decisions before lunch), and the hard problem moved from automation to **observability**.

Read him with the caveats he supplies himself: he says this landscape changes every **3-6 months**, and he is a paying [[devin]] customer arguing for cloud harnesses.
Complements [[josh-pigford]] (build-fast, local, many products) with a build-the-system-first, cloud-first, one-product stance.
