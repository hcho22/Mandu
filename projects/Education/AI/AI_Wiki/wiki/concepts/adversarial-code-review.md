---
type: concept
tags: [code-review, verification, agents, evals, quality]
status: developing
source-count: 6
last-updated: 2026-10-14
---

# Adversarial Code Review

Verifying AI-generated code by making a model actively hunt for its flaws, from [[building-5-ai-products-solo]] and [[working-with-fable-5]] (and, as a productized gate, [[building-robust-apps-with-ai]]).
Two complementary forms:

- **Cross-model review:** a *different* model reviews the builder's output. Josh Pigford has Claude Opus ([[anthropic]]) build and GPT-5.5 ([[openai]]) review the worktree; it "invariably finds 3-5 bugs Opus overlooked."
- **Forced self-critique (the "but-for-real" skill):** the *same* model is told it almost certainly broke something and made to re-examine its work; this finds another 3-5 bugs, separate from the cross-model pass. Much of the value is simply forcing a second look.

## Key points

- Treat the AI like a PR reviewer: a forced second set of eyes reliably surfaces issues.
- Cross-model review works because a second model does not share the first's blind spots.
- Being blunt/"mean" in the critique prompt measurably helps.
- **Productized as a skill and a merge gate** ([[working-with-fable-5]]): Theo's Codex Review skill has a sub-agent run `codex review` on a diff/branch, then verifies its claims against the code before trusting them; and his long-running "goal" is forbidden from merging until independent automated reviewers (Bugbot, Macroscope, CodeRabbit) approve. Cross-model review becomes the gate that makes [[get-out-of-the-loop]] safe.
- **Confidence-scored gate** ([[building-robust-apps-with-ai]]): Ross uses Greptile to review PRs with a summary + a 1-5 confidence score, and won't personally review or merge anything below 4/5 - a threshold that routes his scarce attention, a cousin of [[time-to-fix-as-health-signal]].

## Concrete findings over confidence (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] asks a separate reviewer to inspect the specification, diff, context, and validation evidence without inheriting the full implementation conversation.
Each important finding needs a failure scenario and supporting evidence; validate it before making a fix, then rerun the affected checks on the new revision.
The earlier claims above about reliable bug discovery, different models lacking shared blind spots, and blunt prompts measurably helping are practitioner claims, not universal guarantees established by this guide.
Changing model or context may reduce shared assumptions without eliminating shared errors.
The guide supplies no benchmark proving AI review is superior to human review.
Source count includes the previously cited [[building-robust-apps-with-ai]], omitted from the old count of two, plus this new guide.

## A reviewer on the PR, and a loop to answer it (2026-10-14)

[[agentic-code-review-strategies]] adds the hosted layer.
[[john-meta-engineer]] runs [[codex]]'s GitHub integration so a Codex reviewer comments automatically when a PR opens, or on demand when tagged; it costs money, and he believes (hedged) it uses a model trained for review.
His view that AI review is already "better than most humans" is an opinion with no measurement attached; the problem, he says, is that people use it wrong.
The new part is what happens after the review: review comments arrive, you fix them, more arrive.
He hands that back-and-forth to an hourly loop that checks the PR, fixes the requested changes, re-runs local and agentic validation, updates the PR notes, and resubmits.
That closes the loop this page describes, but only in one direction: a babysitter that applies every comment can still apply a wrong one, which is why the earlier verify-the-claim-first step still matters.
[[agentic-coding-workflow-idea-to-review]] adds the matching rule: the babysitter fixes reviewer comments but does not settle disagreements, so a comment asking for a design or scope change goes to the human instead of into an endless fix cycle.

## Synthesis

This is the code-level member of the wiki's verification family, alongside the [[skill-eval-loop]] (checklist grader), [[fresh-context-review]] (clean-context reviewer), and [[llm-as-judge]] (model grader): all say never trust a single AI pass, and all work because a fresh or different perspective does not share the original's blind spots.
For hcho this is the most directly portable idea in the source - adversarial review is validation engineering for AI-written code, and a multi-model review harness is a concrete portfolio/interview artifact.
It pairs with [[phased-implementation]] (review each small worktree) and is a natural thing to encode as a reusable skill.
