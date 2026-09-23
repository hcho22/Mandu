# Beginner's Guide to Reviewing AI-Generated Code Safely

## 1. Tutorial overview

### What this tutorial teaches

This tutorial presents a risk-based workflow for reviewing code created with AI coding agents. Its central argument is that you should not review every code change with the same level of effort.

Instead, decide how closely to inspect a change based on:

- How much of the application it could affect.
- Whether it changes existing production behavior.
- Whether it is isolated behind a feature gate.
- How easily it can be tested.
- Whether it can be rolled back safely.
- How much evidence proves that it works.

The workflow uses AI throughout the development process—from planning and implementation to review and launch—but keeps humans involved in high-risk decisions, final quality improvements, and production readiness.

### What you should be able to achieve

After following this workflow, you should be able to:

- Classify code changes by risk.
- Decide how deeply each change needs to be reviewed.
- Use feature gates to isolate unfinished or risky work.
- Ask AI agents for tests, screenshots, logs, and other evidence.
- Use an independent AI agent to review AI-generated code.
- Prepare a concise, evidence-based pull request.
- Distinguish “merge ready” from “launch ready.”
- Release a feature gradually and retain the ability to disable it.

### Who this is for

This guide is intended for:

- Developers beginning to use AI coding tools.
- Teams receiving increasingly large amounts of AI-generated code.
- Engineers who want to move faster without blindly trusting generated code.
- Technical leads creating safer AI-assisted development practices.

A basic understanding of source code and Git pull requests is helpful, but the important concepts are explained below.

### Required tools and knowledge

The transcript assumes access to:

- A software project stored in version control, such as Git.
- A pull-request platform, such as GitHub.
- An AI coding agent, such as Codex or Claude Code.
- The ability to run the project's tests and automated checks.
- A way to inspect logs or run the application.
- A way to enable and disable new functionality.

Optional tools mentioned include:

- LaunchDarkly for managed feature flags.
- Codex's GitHub review integration.
- Claude Code's `/code-review` capability.
- Screenshot, video-recording, component-testing, and snapshot-testing tools.
- An automation or “goal” that periodically monitors a pull request.

### Difficulty

**Intermediate.** Beginners can follow the strategy, but implementing automated tests, feature flags, continuous integration, experiments, and canary deployments may require help from an experienced engineer.

---

## 2. Key concepts for beginners

### AI coding agent

An AI coding agent is a tool that can inspect a project, modify files, run commands, test its work, and sometimes open or review pull requests.

It is more capable than simple code completion because it can perform a sequence of development tasks. However, it can still misunderstand requirements, overlook side effects, or produce code that appears correct without actually working.

### Pull request and diff

A **pull request**, or PR, proposes a set of code changes for review before they are added to the main codebase.

A **diff** shows what was added, removed, or changed.

The tutorial recommends making the PR easy to review by including a concise explanation, a test plan, and concrete evidence that the change works.

### The codebase-as-a-tree model

The speaker suggests imagining a codebase as a tree:

- The **trunk and roots** are central systems used by many parts of the application.
- The **leaves** are isolated features or components with few dependencies.

A change to the trunk can affect the entire tree. A change to one leaf is usually more contained.

This model helps determine how much review a change deserves.

### Trunk code

Trunk code is central code with many downstream dependencies. Examples from the transcript include:

- Main application entry points such as `App.js`.
- Shared state management, such as a reducer.
- Networking infrastructure.
- Image-processing or rendering infrastructure.
- Existing behavior used throughout the application.

A defect in trunk code may affect many features or users, so it deserves deeper human review.

### Leaf code

Leaf code is isolated code that does not yet affect the main production experience.

Examples include:

- A new standalone UI component.
- A new endpoint that has not yet been integrated.
- New logic protected by a feature gate.
- A component that can be validated independently.

Leaf code can often be reviewed more quickly if there is strong evidence that it behaves correctly.

### Blast radius

The **blast radius** is the amount of damage a defective change could cause.

For example:

- Changing the color of an isolated experimental button has a small blast radius.
- Changing shared authentication or networking code has a large blast radius.

The larger the blast radius, the more carefully the code should be reviewed.

### Feature gate or feature flag

A feature gate is a switch that controls whether new behavior is enabled.

A simple implementation could be a Boolean value:

```js
const newFeatureEnabled = false;
```

The application checks the value before using the new feature. More advanced systems, such as LaunchDarkly, can enable a feature for selected users or a percentage of traffic.

A gate reduces risk because the feature can be disabled without removing all of its code.

### Control experience

The **control experience** is the existing production behavior that should remain unchanged for users who do not receive the new feature.

Before reviewing a change, ask:

- What currently works?
- Should this change affect it?
- How will we prove that it remains unchanged?

### Agentic validation

Agentic validation means giving an AI agent enough access and instructions to test its own work, inspect the results, and correct problems before asking a human to review it.

Evidence can include:

- Unit-test results.
- Integration-test results.
- Runtime logs.
- Screenshots.
- Screen recordings.
- Component or snapshot tests.
- Type-checking and linting results.

The key principle is that the agent should not merely claim that the code works. It should provide evidence.

### Static checking

Static checks examine code without relying on manual inspection of every line.

Examples include:

- **Type checking:** Confirms that values are used with compatible data types.
- **Linting:** Detects suspicious patterns and enforces agreed coding rules.
- **Formatting:** Applies consistent code layout.

The speaker recommends using automated checks for stylistic details instead of spending human review time debating minor preferences.

### Adversarial review

An adversarial reviewer actively searches for reasons a change might be wrong.

The transcript recommends using a new agent or sub-agent that did not create the code. The original agent may be influenced by its earlier reasoning and may defend assumptions it already made.

A separate reviewer approaches the change with fresher context and should examine the code as critically as possible.

### Atomic change

An atomic change is a small, focused change that accomplishes one clear purpose.

Smaller changes are easier to:

- Understand.
- Test.
- Review.
- Revert.
- Diagnose when something goes wrong.

### Merge ready versus launch ready

**Merge ready** means the code has enough validation to be added to the shared codebase, often while disabled behind a feature gate.

**Launch ready** means the feature has also received broader quality work, such as:

- Security review.
- Performance review.
- Full specification validation.
- Refactoring and cleanup.
- Polished user experience.
- Production rollout planning.

The speaker estimates that the initial implementation represents roughly 80% of the work. The final 20% may take as long as the first 80%.

### A/B test and canary deployment

An **A/B test** exposes different groups of users to different experiences and compares their results.

A **canary deployment** releases a change to a small portion of users or traffic first. The team watches for crashes, errors, or alerts before expanding the release.

The transcript recommends gradual rollout even when the user population is too small for statistically meaningful experimentation. In that situation, the rollout still helps detect operational failures.

---

## 3. Before you begin

### Required preparation

- [ ] Identify the feature or change being built.
- [ ] Write down what the change is supposed to accomplish.
- [ ] Identify the existing behavior that must not change.
- [ ] Locate the central systems the feature may touch.
- [ ] Determine how the project runs tests, linting, and type checks.
- [ ] Make sure the application can be run locally or in a test environment.
- [ ] Decide how the feature can be disabled or rolled back.
- [ ] Confirm that logs, errors, or monitoring data will be available during validation.
- [ ] Give the coding agent clear success criteria before it starts.

### Optional but recommended preparation

- [ ] Create a reusable AI code-review instruction or “skill.”
- [ ] Create a standard pull-request template.
- [ ] Add screenshot or screen-recording support for UI changes.
- [ ] Configure component or snapshot tests for isolated UI work.
- [ ] Use a feature-management service such as LaunchDarkly.
- [ ] Configure an AI reviewer on the GitHub repository.
- [ ] Create automation to monitor review feedback and rerun validation.
- [ ] Prepare a canary or percentage-based rollout process.

### Safety considerations

- Do not assume passing tests prove that a change is completely safe.
- Do not allow the agent that wrote the code to be the only reviewer.
- Be careful with AI-generated tests. An agent may write tests that pass without checking meaningful behavior.
- Avoid placing secrets or sensitive production data in prompts, logs, screenshots, or pull-request descriptions.
- Give infrastructure, security, networking, shared-state, and irreversible changes additional human attention.
- Confirm that feature gates fail safely. If the gating system fails, the new feature should not unintentionally become available to everyone.

> **Additional context:** Before connecting an AI reviewer to a private repository, verify what repository data it can access, how that data is retained, and whether the configuration complies with your organization's policies.

---

## 4. Step-by-step workflow

### Step 1: Define the feature and its success criteria

**Goal:** Establish what the feature must accomplish before code is generated.

**Actions:**

1. Write a short specification.
2. Describe the expected user experience.
3. List the behavior that must remain unchanged.
4. Define measurable validation criteria.
5. Identify important error cases and edge cases.

**Explanation:** An agent cannot validate its work effectively when “done” is undefined. Planning the tests and evidence in advance reduces the chance that the agent creates code first and invents weak validation afterward.

**Expected result:** A clear feature description and a checklist of conditions that must be true before the change can be accepted.

**Common mistakes:**

- Giving the agent only a vague feature request.
- Describing the happy path but not failure cases.
- Forgetting to identify existing behavior that must be protected.

**Troubleshooting:** If the agent repeatedly produces incomplete work, make each requirement independently testable and state what proof should accompany it.

### Step 2: Map the affected code by blast radius

**Goal:** Decide whether the planned changes are leaf changes, trunk changes, or a mixture.

**Actions:**

1. List the files and systems likely to change.
2. Identify which existing components depend on them.
3. Mark shared infrastructure and existing production behavior as trunk areas.
4. Mark isolated, newly added, or fully gated code as leaf areas.
5. Assign a simple risk level, such as low, medium, or high.

A basic classification might look like this:

| Change type | Typical risk | Suggested review depth |
|---|---:|---|
| Isolated, gated component | Low | Evidence review and code skim |
| New endpoint with limited integration | Medium | Tests plus focused code review |
| Shared state or existing behavior | High | Deep human and AI review |
| Networking, security, or core infrastructure | Very high | Deep review, specialist input, and gradual rollout |

**Explanation:** Review effort should follow potential impact. A small isolated component and a shared networking layer should not receive identical treatment.

**Expected result:** A risk map showing which areas need deep review.

**Common mistakes:**

- Treating every new file as low risk.
- Ignoring indirect dependencies.
- Assuming a small diff has a small blast radius.
- Looking only at the number of changed lines.

**Troubleshooting:** If the blast radius is unclear, trace where the changed function, module, state, or API is used. When uncertain, classify the change at the higher risk level.

### Step 3: Add a feature gate before integration

**Goal:** Make the new behavior reversible.

**Actions:**

1. Create a switch that controls the new feature.
2. Keep the existing production behavior as the default control path.
3. Put integration points behind the gate.
4. Test both the enabled and disabled states.
5. Document how to turn the feature off.

The transcript suggests that a Boolean flag is enough for a simple starting point. A feature-management platform can provide more advanced targeting and percentage-based rollout.

**Explanation:** A feature gate separates landing code from exposing it to users. It also creates a fast recovery path when a problem appears after deployment.

**Expected result:** The new code can exist in the codebase without changing the normal user experience until explicitly enabled.

**Common mistakes:**

- Gating the visible UI while leaving risky background behavior active.
- Testing only the enabled path.
- Scattering unrelated gate checks throughout the codebase.
- Forgetting how the gate will eventually be removed.

**Troubleshooting:** If disabling the gate does not completely restore the control experience, identify every integration point and move it behind the gate.

### Step 4: Build the feature in small, isolated changes

**Goal:** Make the implementation easier to understand, validate, review, and reverse.

**Actions:**

1. Ask the coding agent to make focused, atomic changes.
2. Build isolated components or logic before connecting them to shared systems.
3. Keep risky integration work separate from low-risk leaf work.
4. Require the agent to run relevant checks after each meaningful change.
5. Ask it to fix validation failures before continuing.

**Explanation:** Smaller changes provide clearer evidence. If a failure appears, it is easier to identify which change caused it.

**Expected result:** A sequence of focused changes instead of one large, tangled diff.

**Common mistakes:**

- Asking the agent to build the entire feature in one step.
- Mixing refactoring with new functionality.
- Allowing unrelated formatting changes to inflate the diff.
- Integrating into trunk code before isolated behavior is proven.

**Troubleshooting:** If the diff becomes difficult to review, pause integration and divide the work by responsibility, such as UI, business logic, tests, and shared-system integration.

### Step 5: Require evidence during implementation

**Goal:** Prove that the feature works without depending entirely on manual code reading.

**Actions:** Request evidence appropriate to the change:

- Unit tests for isolated logic.
- Integration tests for interactions between systems.
- Component or snapshot tests for isolated UI components.
- Runtime logs for behavior visible only while the application runs.
- Screenshots for static UI changes.
- Videos for interactive workflows or animations.
- Type-checking and linting results.
- A confidence assessment that identifies uncertain or weakly tested areas.

For a UI change, the agent should show the relevant interface and the result of the interaction. For example, if it adds a “Save” button, the evidence should show the button and demonstrate that saving succeeds.

**Explanation:** Evidence allows the reviewer to inspect outcomes rather than trusting an unsupported statement from the agent.

**Expected result:** Each important requirement is associated with a test result, log, screenshot, video, or other observable proof.

**Common mistakes:**

- Accepting “tests passed” without seeing which tests ran.
- Using screenshots to prove underlying behavior.
- Allowing the agent to write tests that merely reproduce its implementation.
- Treating a confidence score as proof.
- Collecting evidence only after implementation is complete.

**Troubleshooting:** If the evidence does not demonstrate the requirement directly, rewrite the success criterion and ask for proof that would fail if the feature were broken.

### Step 6: Prepare a concise, standardized pull request

**Goal:** Give reviewers the information needed to evaluate the change quickly.

**Actions:** Use a consistent template such as:

```markdown
## Summary
- What changed
- Why it changed

## Risk and blast radius
- Systems affected
- Existing behavior that must remain unchanged
- Feature gate and rollback method

## Validation
- Tests executed
- Runtime evidence
- Screenshots or videos
- Static checks

## Known limitations
- Untested cases
- Follow-up work
- Areas of lower confidence
```

Keep the description proportional to the change. Link or attach evidence rather than writing a long narrative.

**Explanation:** A standard format prevents important safety information from being buried in an AI-generated wall of text.

**Expected result:** A PR whose purpose, risk, validation, and rollback method can be understood quickly.

**Common mistakes:**

- Producing a summary longer than the code change.
- Listing checks without their results.
- Omitting the feature gate or rollback procedure.
- Hiding uncertainty behind confident language.

**Troubleshooting:** If reviewers cannot understand the PR quickly, shorten the narrative and organize the information around change, risk, proof, and recovery.

### Step 7: Run an independent, adversarial AI review

**Goal:** Find problems that the implementation agent may have overlooked or rationalized.

**Actions:**

1. Start a new agent or sub-agent that does not share the implementation conversation.
2. Give it the specification, diff, project context, and validation evidence.
3. Ask it to look for:
   - Incorrect behavior.
   - Missing requirements.
   - Regressions.
   - Security problems.
   - Performance problems.
   - Unsafe assumptions.
   - Weak or meaningless tests.
   - Missing error handling.
   - Gaps in the rollback plan.
4. Ask the reviewer to prioritize findings by severity.
5. Require evidence or a concrete failure scenario for each important finding.

The transcript mentions built-in review capabilities in Codex and Claude Code, including Claude Code's `/code-review`.

**Explanation:** An independent agent is less likely to inherit the original agent's assumptions and is better positioned to challenge the implementation.

**Expected result:** A prioritized review report containing actionable findings rather than general opinions.

**Common mistakes:**

- Asking the original implementation agent to be the only reviewer.
- Starting a “new” review while still providing the entire implementation conversation.
- Accepting speculative findings without checking them.
- Asking the reviewer to focus on style instead of correctness and safety.

**Troubleshooting:** If the review produces vague advice, require each finding to identify the affected code, the failure scenario, its impact, and a suggested validation method.

### Step 8: Perform a risk-based human review

**Goal:** Apply human attention where judgment and system knowledge matter most.

**Actions for low-risk leaf code:**

1. Review the evidence.
2. Skim the code for obvious mistakes.
3. Check that the code is genuinely isolated or gated.
4. Confirm the tests represent meaningful behavior.

**Actions for high-risk trunk code:**

1. Read the changed logic carefully.
2. Trace downstream dependencies.
3. Inspect state changes and side effects.
4. Review failure behavior and recovery paths.
5. Confirm that the control experience remains intact.
6. Examine security, privacy, performance, and data-integrity implications.
7. Verify that rollback is practical.

Use automated linting, formatting, and type checking for minor stylistic issues.

**Explanation:** Human review remains important, but it should focus on architecture, product behavior, tradeoffs, and dangerous changes—not formatting preferences that automation can enforce.

**Expected result:** Review depth matches the possible consequences of failure.

**Common mistakes:**

- Skimming central infrastructure because tests passed.
- Deeply reviewing harmless style details while missing system-level risk.
- Equating feature gating with complete safety.
- Reviewing code without understanding the surrounding codebase.

**Troubleshooting:** If you cannot explain the change's effect on the broader system, pause approval and inspect its callers, dependencies, data flow, and failure modes.

### Step 9: Resolve findings and rerun validation

**Goal:** Ensure that review fixes do not introduce new problems.

**Actions:**

1. Prioritize high-severity findings.
2. Confirm that each finding is valid.
3. Make focused corrections.
4. Rerun the original validation suite.
5. Add a regression test when a genuine defect is found.
6. Update the PR evidence and notes.
7. Request another independent review if the correction materially changes the design.

The transcript also describes using a recurring automation or “goal” to check the PR periodically, address reviewer feedback, rerun validations, and update the PR.

**Explanation:** A fix can invalidate earlier screenshots, logs, or test results. Evidence must represent the current revision.

**Expected result:** All meaningful findings are resolved or explicitly documented, and the latest code has fresh validation evidence.

**Common mistakes:**

- Fixing comments without rerunning tests.
- Blindly accepting every AI review suggestion.
- Creating an endless loop in which AI reviewers repeatedly make conflicting stylistic requests.
- Allowing automation to merge changes without human oversight.

**Troubleshooting:** If automated reviewers repeatedly disagree, return to the specification and risk model. Require findings to demonstrate real behavioral, safety, or maintainability impact.

### Step 10: Complete the final launch-readiness pass

**Goal:** Turn a merge-ready implementation into a production-ready feature.

**Actions:**

1. Audit the feature against the original specification.
2. Review the implementation at a system level.
3. Examine security and privacy risks.
4. Check performance and resource usage.
5. Search for edge cases and potential bugs.
6. Refactor unnecessary duplication or confusing structure.
7. Polish visual details, interactions, and animations.
8. Remove temporary debugging code.
9. Confirm monitoring and rollback procedures.
10. Run the complete relevant validation suite.

**Explanation:** The transcript calls the initial implementation “broad strokes.” The final quality pass is where human taste, product judgment, and architectural understanding become especially important.

**Expected result:** A clean, coherent feature that satisfies its specification and is safe to expose to users.

**Common mistakes:**

- Treating “the PR can merge” as “the feature can launch.”
- Skipping cleanup because the generated code appears functional.
- Performing a large refactor without revalidation.
- Focusing only on visible behavior while ignoring security or performance.

**Troubleshooting:** If the final audit reveals extensive structural problems, keep the feature gated and address the architecture before expanding its rollout.

### Step 11: Release gradually

**Goal:** Limit the number of users affected by undiscovered problems.

**Actions:**

1. Deploy the code while keeping the feature disabled by default.
2. Enable it for internal users or a small test group.
3. Watch logs, crashes, alerts, performance, and user behavior.
4. Increase exposure gradually.
5. Compare the new experience with the control experience where practical.
6. Disable the gate immediately if serious problems appear.

**Explanation:** Gradual rollout turns production exposure into another validation layer. Even if the audience is too small for a statistically rigorous A/B test, a canary release can expose crashes and integration problems.

**Expected result:** The feature reaches users in controlled stages with no unacceptable regression.

**Common mistakes:**

- Releasing to everyone immediately.
- Increasing traffic without checking results from the previous stage.
- Running an A/B test without enough users and drawing strong conclusions from weak data.
- Discovering that the gate cannot be changed quickly during an incident.

**Troubleshooting:** If errors increase, stop or reverse the rollout, preserve the evidence, identify the affected path, fix the issue, rerun validation, and restart with a small audience.

---

## 5. Complete workflow at a glance

- [ ] Define the feature, control behavior, and success criteria.
- [ ] Identify trunk code, leaf code, dependencies, and blast radius.
- [ ] Choose a review depth based on risk.
- [ ] Put the feature and its integration points behind a gate.
- [ ] Build the feature through small, focused changes.
- [ ] Require tests, logs, screenshots, videos, and static-check results.
- [ ] Prepare a concise pull request using a standard template.
- [ ] Run an independent adversarial AI review.
- [ ] Perform a human review focused on high-risk areas.
- [ ] Resolve valid findings and rerun all affected validation.
- [ ] Complete the final security, performance, quality, and specification audit.
- [ ] Deploy with the feature disabled by default.
- [ ] Release to a small group and monitor the results.
- [ ] Expand the rollout gradually.
- [ ] Disable or roll back the feature if serious problems appear.

---

## 6. How to verify the final result

A successful implementation should satisfy all of the following:

- The feature meets its written specification.
- The existing control experience remains unchanged when the gate is off.
- Enabling the gate activates only the intended behavior.
- Disabling the gate safely restores the control experience.
- Relevant unit, integration, component, or snapshot tests pass.
- Type checking and linting pass.
- Runtime logs do not show unexplained errors.
- UI evidence matches the intended experience.
- An independent reviewer has examined the change.
- High-risk trunk changes have received deep human review.
- Known limitations and areas of uncertainty are documented.
- Production monitoring is ready before rollout.
- The feature can be stopped or rolled back quickly.

Warning signs include:

- Evidence from an older revision rather than the latest code.
- Tests that only check whether components render without validating behavior.
- A disabled gate that still allows side effects.
- Unexpected changes in existing features.
- New crashes, errors, latency, or resource consumption.
- Review findings that remain unresolved without an explicit reason.
- No clear person or procedure for stopping the rollout.

If the result is incorrect, check the following first:

1. Is the feature gate controlling every integration point?
2. Were the correct and latest tests executed?
3. Does the failure occur only when the feature is enabled?
4. Did a review fix invalidate earlier evidence?
5. Does the change touch shared state or infrastructure unexpectedly?
6. Can the feature be disabled while the problem is investigated?

---

## 7. Troubleshooting guide

| Problem or symptom | Likely cause | How to fix it |
|---|---|---|
| The PR is too large to understand | The feature was built as one broad change | Divide it into isolated components, logic, tests, and integration changes |
| Tests pass, but the feature does not work | The tests do not validate real behavior | Add runtime, integration, or end-to-end evidence tied to the requirement |
| The AI reviewer reports only minor style issues | The review instructions are too general | Ask for correctness, regression, security, performance, and rollback analysis |
| The AI reviewer overlooks an obvious assumption | It shares too much context with the implementation agent | Use a separate agent with the specification, diff, and evidence only |
| Disabling the feature does not restore normal behavior | Some integration or side effect exists outside the gate | Trace every entry point and move all new behavior behind the gate |
| A small change causes unrelated failures | The edited code is actually trunk code with downstream dependencies | Reclassify it as high risk and trace its callers, state, and side effects |
| Screenshots look correct, but behavior is broken | A screenshot proves appearance, not interaction | Add video, runtime logs, or an automated interaction test |
| AI-generated tests provide little confidence | The tests repeat the implementation or assert trivial facts | Review test names, inputs, outputs, edge cases, and assertions manually |
| Review becomes an endless back-and-forth | Reviewers are making conflicting or low-value suggestions | Use the specification and risk criteria to decide which findings matter |
| The feature is merged but still feels unfinished | Merge readiness was mistaken for launch readiness | Perform the final security, performance, refactoring, and UX audit |
| A production issue affects too many users | The feature was launched too broadly | Disable the gate and resume with a small canary group after fixing it |
| An A/B test produces unclear results | The audience is too small for meaningful statistical power | Use the rollout primarily for safety monitoring rather than strong product conclusions |

---

## 8. Key takeaways

- Continue reading code, but vary the depth according to risk.
- Think of central, widely shared code as the trunk and isolated code as leaves.
- Review effort should follow blast radius, not line count.
- Design for safety and rollback before implementation begins.
- Keep new behavior behind feature gates whenever practical.
- Require evidence from coding agents instead of accepting claims that the code works.
- Use tests, logs, screenshots, and videos for different kinds of proof.
- Treat AI-generated tests as reviewable code, not automatic truth.
- Use a separate agent for adversarial review.
- Spend human attention on architecture, behavior, security, performance, and irreversible decisions.
- Leave stylistic consistency to automated linting and formatting rules.
- Keep pull-request summaries concise and evidence-based.
- Treat merge readiness and launch readiness as separate milestones.
- Expect the final refinement phase to require substantial human judgment.
- Release gradually and preserve the ability to turn bad changes off.

---

## 9. Gaps or unclear information

### No exact video title was provided

The transcript identifies the topic as AI-assisted or agentic code review, but it does not include the official video title.

**Why it matters:** The title may clarify whether this is intended as a conceptual discussion or a hands-on tool tutorial.

**What to confirm:** Add the original title if this guide will accompany or reference the video.

### No complete feature-gate implementation is demonstrated

The speaker describes Boolean flags and mentions LaunchDarkly, but does not provide a full implementation.

**Why it matters:** Correct gating may require server-side evaluation, user targeting, audit logs, safe defaults, and cleanup procedures.

**What to confirm:** Consult the selected feature-management system's documentation and the project's architectural conventions.

### The review “skill” is not included

The speaker recommends creating a strong review skill and a skill that prevents useless tests, but does not provide the actual instructions.

**Why it matters:** Review quality depends heavily on the criteria given to the agent.

**What to confirm:** Define project-specific review requirements covering correctness, regressions, security, performance, meaningful tests, and rollback safety.

### The pull-request template is not shown in full

The speaker refers to a personal template but does not provide its exact contents.

**Why it matters:** Teams need an agreed structure for risk, validation evidence, and known limitations.

**What to confirm:** Adapt the example template in this guide to the project's review process.

### Tool setup details are missing

The transcript mentions Codex, Claude Code, GitHub review integration, LaunchDarkly, and recurring goals without showing how to install or configure them.

**Why it matters:** Availability, commands, permissions, pricing, and behavior may differ by tool and version.

**What to confirm:** Check the current official documentation for each selected tool.

### The recurring PR-monitoring workflow is only conceptual

The speaker suggests checking a PR every hour, addressing feedback, rerunning validation, and updating the PR.

**Why it matters:** Fully automated changes to an active PR can create incorrect fixes or repetitive review loops.

**What to confirm:** Decide what the automation may change independently and which actions require human approval.

### No quantitative review thresholds are provided

The transcript describes a gradient but does not define an exact scoring model.

**Why it matters:** Different reviewers may classify the same change differently.

**What to confirm:** Create team-specific rules for low-, medium-, high-, and critical-risk changes.

### Statistical experimentation is not explained

The speaker acknowledges that small products may lack enough users for a valid A/B test but does not explain sample size or experiment design.

**Why it matters:** Weak experiments can encourage incorrect conclusions.

**What to confirm:** Seek appropriate experimentation guidance before making product decisions from small samples. Use limited rollout for safety monitoring when statistical power is insufficient.

### The “80% versus 20%” estimate is an opinion

The statement that the final 20% takes as long as the initial 80% is presented as the speaker's experience, not a measured universal rule.

**Why it matters:** Actual effort varies by project, feature, team, and risk.

**What to confirm:** Treat the ratio as a reminder to budget for refinement—not as a scheduling formula.

### The claim that AI may review better than most humans is unverified

The speaker presents this as a personal opinion and does not cite a benchmark.

**Why it matters:** AI review quality varies by model, repository context, language, tooling, and task.

**What to confirm:** Measure review performance within your own project and retain human oversight for consequential changes.
