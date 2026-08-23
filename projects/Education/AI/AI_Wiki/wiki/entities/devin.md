---
type: entity
tags: [tool, coding-agent, cloud]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Devin

A cloud-only engineering agent (Cognition) used in [[one-person-company-with-agents]] as the primary build/ship agent.

## What it does

- Spins up a real, configured production VM in the cloud per task, so there is no local development (removes port/dependency/Homebrew headaches) - a way to fight [[context-rot]] with a clean environment each time.
- "Schedules" run "playbooks" (skill-like instruction docs): e.g. a weekly full user-journey coverage run and smoke tests that record the screen and report breakages.
- Reliable in-cloud browser testing is the feature that won Carson over; supports [[everything-is-a-pr]] with a "land PR" playbook.

## Second source (2026-08-01)

[[running-teams-of-ai-agents]] adds history, economics, and an important disclaimer.

- **The history matters:** Devin launched ~2-2.5 years ago pitched as an AI software engineer and **did not work well** then - "no matter how good the harness was, the models weren't good enough." By 2026 the models are good enough and a well-built cloud harness on top is genuinely good. Described as "one of the best software factories in the industry - expensive, but good."
- **[[ryan-carson]] is explicit that the lessons are not Devin-specific.** They just happen to work well there. That disclaimer should travel with everything on this page.
- **Playbooks, in practice:** an end-to-end signup test running Mon/Wed/Fri at ~**$60 in tokens per run** (browser testing is expensive) that records a video, annotates it, watches its own video, and fixes bugs it sees, triggering a child triage session on failure.
- **Why he picked it:** Cognition has been running browser-capable cloud agents for two years, and reliable browser driving is the differentiator.
- **Cost/routing:** cheap reinforcement loops run on **SWE-1.7**, a Cognition-fine-tuned coding model, at ~$5/session, against ~$20,000/month total spend. (Model name unverified in the raw source.)
- **Strategic placement:** Devin is [[ryan-carson]]'s example of an **independent agent lab** rather than a frontier lab, which is the whole basis of [[independent-agent-lab-vs-frontier-lab]]. Note the incentive: he is a paying customer making the case for his own vendor category.

## Notes

Carson predicts "most serious people are going to move to cloud engineering," and by the second source has made that his whole engineering motion - see [[cloud-agents-over-local]], which the wiki records as **contested** against the local-worktree practice of [[josh-pigford]] and [[conductor]].
Playbooks map onto the wiki's [[building-skills]] concept; Carson distinguishes them from skills as "more a list of things to do and how to do them correctly."
