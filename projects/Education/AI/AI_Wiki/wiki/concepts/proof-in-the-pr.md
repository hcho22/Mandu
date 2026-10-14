---
type: concept
tags: [code-review, validation, evidence, agents, pull-requests]
status: developing
source-count: 4
last-updated: 2026-10-14
---

# Proof in the PR

Make the agent attach evidence that its change works to the pull request itself, so the reviewer reads the evidence first and the code second.
From [[agentic-code-review-strategies]]: [[john-meta-engineer]] calls agentic validation "the core concept that lets you read less code," and the more proof a PR carries up front, the less of its code he reads.

## The evidence package

| Kind | What it shows | How the reviewer uses it |
|---|---|---|
| Unit tests | Logic coverage | Skim test names and asserts to judge coverage at a glance |
| Runtime logs | What actually executed | Visibility into behavior the diff does not show |
| Screenshots or video | The UI change as a user sees it | Confirms the visible result without running the app |
| Confidence levels | The agent's own uncertainty per part (code, gating, tests) | Points the reviewer at the low-confidence parts first |

## Key points

- **Build the requirement into skills** so every PR includes the package without being asked.
- **Guard the tests themselves.** Agents can write useless tests; he keeps a separate skill about not writing them, so the tests stay meaningful as proof.
- **Standardize the PR.** A template makes every PR look alike and always carry the important parts; without one, agents write "a giant paragraph, like a story."
- **Keep it short.** His biggest pet peeve is a PR whose summary and test plan are longer than the code change.
- His example: a screenshot of a "save card" feature showing the button and the saved state made him "a lot more believing" of the code.

## Proof versus confidence (2026-09-23 and 2026-10-14)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]], most likely derived from the same talk, adds the caveats that make the package trustworthy: evidence must match the current revision, a screenshot shows appearance but not persistence or side effects, and "a confidence score is not proof."
That last point and John's confidence levels are compatible once their jobs are separated.
A confidence level is a **routing signal** that tells the reviewer where to look; the tests, logs, and recordings are the **evidence**.
The failure mode is letting a high self-reported confidence stand in for the evidence, which [[self-referential-bias]] predicts will be optimistic.
[[adversarial-code-review]] records a related practice: Ross gates his own review on a reviewer bot's 1-5 confidence score, which is the same routing use from an independent reviewer rather than the author.

## As a gate (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] makes the package an exit gate before review: the end-to-end scenario passed with evidence attached, the tests would fail if the feature broke, the PR names its gate and how to switch it off, confidence levels are stated with low-confidence parts flagged, the docs are updated, and the PR description is shorter than the diff.
Its "prove it" prompt ends with the sentence that carries the idea: "Do not claim success from unit tests or a passing build alone."
Its PR template puts **Risk** (trunk or leaf, tier, gate, rollback) and **Evidence** ahead of a three-bullet **Reviewer focus**.

## Synthesis

This is the PR-level form of [[agent-testing-instructions]] and [[define-the-end-to-end-gate]]: the agent tests the way a human would, then hands over the record.
It changes what review is.
The reviewer stops reconstructing behavior from the diff and starts auditing a claim with its evidence attached, which is the posture of a validation sign-off rather than a code read.

The package has a precondition the sources state only implicitly: each item must be able to fail.
A test that passes whether or not the feature works, or a recording of the happy path only, is decoration.
For hcho this is the most familiar idea in the review material, because it is a test report: the claim, the procedure, the observed result, and the residual risk, attached to the change it covers.

## Source

- [[agentic-code-review-strategies]] - John's four kinds of proof, skill-encoded evidence, the useless-tests skill, and the PR template.
- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - probable derivation of the same talk; current-revision evidence and the confidence-is-not-proof caveat.
- [[agentic-coding-workflow-idea-to-review]] - the package as a pre-review gate, and a PR template; compiler-authored.
- [[building-products-with-agents]] - the No Mistakes reviewer presents screenshot and video evidence with its findings ([[fresh-context-review]]).
