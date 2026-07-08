---
type: entity
tags: [tool, coding-agent, cloud]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Devin

A cloud-only engineering agent (Cognition) used in [[one-person-company-with-agents]] as the primary build/ship agent.

## What it does

- Spins up a real, configured production VM in the cloud per task, so there is no local development (removes port/dependency/Homebrew headaches) - a way to fight [[context-rot]] with a clean environment each time.
- "Schedules" run "playbooks" (skill-like instruction docs): e.g. a weekly full user-journey coverage run and smoke tests that record the screen and report breakages.
- Reliable in-cloud browser testing is the feature that won Carson over; supports [[everything-is-a-pr]] with a "land PR" playbook.

## Notes

Carson predicts "most serious people are going to move to cloud engineering." Playbooks map onto the wiki's [[building-skills]] concept.
