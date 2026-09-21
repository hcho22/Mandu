# PRD: Purvia Public Launch and Buyer Validation

**Status:** Draft — execution is blocked by unresolved governance prerequisites

**Owner:** hcho

**Created:** 2026-09-02

**Scope:** Pre-launch decisions, credibility clearance, buyer validation, public release, distribution, and launch-experiment adjudication

**Source audit:** `/Users/hcho/firstmate/data/mandu-purvia-launch-plan-scout/report.md`

## 1. Introduction and Overview

Purvia's product implementation, rebrand, and canonical go-to-market package are complete. The project is no longer in a general build phase. It is in pre-public-launch buyer validation and credibility-gate clearance, with no launch date assigned and zero of ten target buyer interviews booked.

This PRD turns the existing launch package into an executable, evidence-producing launch program. It does not choose among unresolved governance options. Instead, every disputed policy is a prerequisite that must be answered explicitly before dependent work begins.

The launch will test whether a defined buyer segment will pay for a permissions-aware RAG implementation whose authorization is enforced inside the SQL retrieval predicate and whose credibility rests on shipped evaluation and security controls. The current candidate offer is an MIT-licensed free core plus a $199 one-time Purvia Pro adoption pack, but the buyer, paid-surface timing, measurement canon, public artifact boundary, model-alignment policy, runtime-judge rollout, and domain strategy all remain unresolved.

### Current baseline

- Phase 2 implementation A-F completed on 2026-07-07.
- Purvia display rebrand completed on 2026-07-17.
- Canonical launch-package phases 0-6 completed on 2026-08-27.
- Four of eight hard public-launch preconditions are green.
- Four hard preconditions remain open: trademark/name testing, founder-biography verification, repository hygiene/publication scope, and five-person external credibility review.
- The canonical 2026-08-27 package has not been published.
- A previous July campaign is historical evidence, not this launch.
- Buyer validation is at 0/10 interviews, and P-series productization must not begin before the interview findings are synthesized.

### Governing source hierarchy

When sources disagree, use this precedence until a governance decision deliberately changes it:

1. `projects/Purvia/README.md` for current operating status and the eight hard launch preconditions.
2. This PRD for launch execution state, sequencing, requirements, and story completion.
3. `projects/Purvia/launch/THESIS.md` for candidate launch hypotheses and tripwires, pending GOV-002.
4. `projects/Purvia/launch/POSITIONING.md` for candidate buyer, offer, and pricing, pending GOV-001 and GOV-003.
5. `projects/Purvia/launch/CLAIMS.md` for the maximum permissible customer-facing claims.
6. `projects/Purvia/launch/RED-TEAM.md` for unresolved launch risks, corrected by newer README status where a risk is already resolved.
7. `projects/Purvia/launch/recap.html` for candidate publishing order, corrected by newer README and this PRD.
8. Dated logs, build logs, old campaigns, weekly plans, and older portfolio summaries as historical evidence only.

The actual Purvia software repository remains authoritative for implementation state where Mandu lacks the promised raw PRD/wiki copy.

## 2. Governance Prerequisites

All governance choices remain unresolved. A prerequisite is resolved only when its decision, rationale, date, and affected documents are recorded. Recommendations in the source audit are context, not adopted policy.

| ID | Decision required | Options that remain open | Blocks | Resolution evidence |
|---|---|---|---|---|
| GOV-001 | Choose the launch ICP | Production-minded engineers and 2-5-person product teams building multi-user RAG, excluding agencies; the older agency/freelancer audience; or a newly specified segment | Interview sourcing, copy, channel selection | Recorded ICP, exclusions, qualifying criteria, and updated conflicting sources |

-   1. Production-minded engineers and small product teams
Developers or teams of 2–5 people building real, multi-user RAG products. RAG is a way for AI applications to retrieve relevant information before answering. “Production-minded” means they care about reliability, security, monitoring, and serving actual users.

| GOV-002 | Choose the measurement canon | One-week `THESIS.md` tripwires; older README 30/90-day criteria; or a documented hybrid | Analytics, launch timing, day-seven adjudication, stop/go actions | Threshold table defining windows, denominators, compound conditions, insufficient-sample handling, and actions |

- 1. One-week THESIS.md tripwires
Judge the launch after seven days using the thresholds in THESIS.md. A “tripwire” is a predefined result that triggers
an action—for example, stop investing if fewer than five qualified users activate.
  - Windows: When each measurement is evaluated, such as 7, 30, or 90 days
  - Thresholds: The numerical boundary for success or failure
  - Denominators: What population a percentage uses—for example, 10 activated users out of 50 qualified signups
  - Compound conditions: Whether several requirements must be met together
  - Insufficient-sample handling: What to do when too few people participated to reach a fair conclusion
  - Actions: Exactly what happens after each result—continue, investigate, revise, or stop

| GOV-003 | Choose paid-surface readiness | Allow a labeled $199 founding preorder before every Pro file exists; require all deliverables before any paid CTA; or remove/defer the paid surface | Final site, CTA, payment metric | Written rule and inventory of what must exist at publication |

- 2. Require everything before accepting payment
Do not show a purchase button until all promised Pro deliverables are complete and available.
  - A written rule stating when it is acceptable to take payment
  - An inventory of everything that must exist when the offer is published, such as:
      - A clear description of what buyers receive
      - The price
      - Delivery dates
      - Completed and unfinished items
      - Refund and cancellation terms
      - A working checkout and confirmation process
      - A way to support and update purchasers

| GOV-004 | Choose the public artifact boundary | Publish all launch artifacts; publish a named subset; or keep launch assets private while linking only the product repository/site | Repository hygiene, public claims, links | Path-level include/exclude manifest |

-   3. Keep launch materials private
Publish only links to the Purvia product repository or website, without exposing the supporting launch documents.
  PUBLIC
  site/
  README.md
  launch/product-demo.md

  PRIVATE
  launch/interview-notes/
  launch/internal-strategy.md
  analytics/raw-data/

| GOV-005 | Reconcile evaluation and production answerer models | Restore eval generation to production; migrate production to eval; or justify intentional divergence | Evidence narrative and benchmark interpretation | Model-role matrix, rationale, and validation evidence |

-   1. Restore evaluation generation to the production model
Make tests generate answers with the same model and settings used in production.
  - A model-role matrix showing which model performs each job:

   Role                   Model                   Same as production?    Purpose
  ━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Production answerer    Production model                        Yes    Answers users
  ─────────────────────  ──────────────────────  ─────────────────────  ────────────────────────────────
   Evaluation answerer    Production model                        Yes    Recreates user-facing behavior
  ─────────────────────  ──────────────────────  ─────────────────────  ────────────────────────────────
   Evaluation judge       Separate judge model           Not required    Scores answer quality

  - A written explanation of why each model was selected
  - Validation evidence showing that evaluation runs reproduce production settings and behavior
  - If any difference remains, evidence measuring how that difference affects scores

| GOV-006 | Decide runtime-judge cutover readiness | Complete issue #105 and live E7 before atomic `gpt-5-mini` cutover; retain the current judge; or choose another reviewed path | Reliability claims, runtime configuration, monitoring | Current-repo verification, issue #105 disposition, E7 result, database readiness, and atomic config decision |

-   1. Finish the safety gates, then switch
Resolve issue #105, run E7 against the live system, confirm the database is ready, and only then switch atomically to gpt-5-mini.
  - Current-repository verification: Which judge the current code and configuration actually use
  - Issue #105 disposition: Completed, deliberately deferred, or otherwise resolved—with a reason
  - E7 result: Pass/fail evidence from the live evaluation
  - Database readiness: Required records, migrations, permissions, and monitoring are available
  - Atomic configuration decision: Exact settings to change together, deployment timing, verification steps, and rollback plan

| GOV-007 | Decide domain strategy | Register `purvia.ai`; choose another domain; or launch on current GitHub links | Optional branding/link changes | Recorded no-spend/spend decision and any redirect plan |
-   1. Register purvia.ai
     Use a short, branded address that clearly signals an AI product.
  To complete GOV-007, record:

  - Whether spending money is approved
  - The maximum acceptable registration and renewal cost
  - The selected official domain
  - Who owns the registrar account and renewal responsibility
  - Whether automatic renewal is enabled
  - Which old URLs should redirect to the new domain
  - Which links must be updated in the README, launch material, and product

### Governance rule

- No dependent story may be marked complete while its prerequisite remains unresolved.
- No launch date may be assigned until GOV-001 through GOV-006 are resolved and all eight hard preconditions are green.
- GOV-007 is non-blocking unless the chosen distribution plan explicitly makes a custom domain mandatory.
- Resolving a prerequisite must update or clearly supersede every conflicting active source; a decision recorded only in chat is insufficient.

## 3. Goals

- Resolve six launch-blocking governance prerequisites and one non-blocking domain decision without silently adopting a recommendation.
- Clear all eight hard public-launch preconditions with verifiable evidence.
- Complete and synthesize ten interviews with the chosen ICP before P-series productization.
- Publish only claims permitted by `CLAIMS.md`, with denominators and caveats attached.
- Freeze one measurement plan before the first public post or site publication.
- Publish the site and distribution assets only after a formal go/no-go review passes.
- Execute the chosen distribution sequence with dated evidence for every release.
- Produce a day-seven decision that applies pre-registered thresholds without retrospective reinterpretation.
- Convert the launch outcome into a concrete next state: continue, revise and retest, retain Purvia as a free credibility asset, reposition, or stop paid-tier work for the quarter.

## 4. Execution Sequence

1. **Phase 0 — Governance:** resolve GOV-001 through GOV-006; record GOV-007 without making it a default blocker.
2. **Phase 1 — Parallel clearance:** run buyer recruitment, trademark/name testing, biography verification, repository cleanup, career review, and green-gate monitoring in parallel where independent.
3. **Phase 2 — Buyer evidence:** complete and synthesize ten interviews; do not begin P-series productization before the synthesis exists.
4. **Phase 3 — Final readiness:** freeze claims, paid-surface behavior, measurement, distribution order, and a launch-date-relative schedule; verify all eight hard preconditions.
5. **Phase 4 — Publication:** publish the approved site and public artifacts, then release content in the approved sequence.
6. **Phase 5 — Measurement:** capture the evidence required by GOV-002 without changing thresholds mid-experiment.
7. **Phase 6 — Adjudication:** perform the day-seven read, apply triggered actions, and record the commercial next state.

## 5. User Stories

### US-001: Resolve and record launch governance

**Description:** As the launch owner, I want every disputed policy resolved in one traceable register so that execution does not embed accidental product or go-to-market decisions.

**Acceptance Criteria:**

- [ ] GOV-001 through GOV-007 each have a recorded decision, rationale, date, and owner.
- [ ] Each decision names the documents and assets it governs.
- [ ] GOV-001 through GOV-006 are launch-blocking; GOV-007 is non-blocking unless explicitly promoted.
- [ ] Every conflict in the source audit is corrected or carries an explicit superseded pointer.
- [ ] No recommendation is represented as adopted without the owner's recorded approval.

**Validation Test:**

- **Setup:** Open this PRD, `README.md`, `THESIS.md`, `POSITIONING.md`, and the decision record.
- **Steps:**
  1. Review GOV-001 through GOV-007 one by one.
  2. Trace each decision to its rationale and affected source updates.
  3. Search the launch package for conflicts identified by the source audit.
  4. Attempt to schedule dependent work whose prerequisite is unresolved.
- **Expected Result:** All choices are traceable, conflicting active guidance is eliminated or superseded, and unresolved prerequisites prevent dependent work.
- **Failure Indicator:** A choice is inferred, conflicting instructions remain equally authoritative, or dependent work proceeds without a decision.

### US-002: Define the qualified buyer and interview protocol

**Description:** As the launch owner, I want a concrete ICP and repeatable interview protocol so that ten conversations test one buyer hypothesis rather than a mixture of incompatible audiences.

**Prerequisite:** GOV-001.

**Acceptance Criteria:**

- [ ] The ICP names buyer role, team profile, current RAG use case, authority/urgency signals, and explicit exclusions.
- [ ] A lead qualifies or disqualifies through observable criteria.
- [ ] The guide tests current workflow, permissions risk, evaluation practice, adoption friction, connector demand, willingness to pay, and objections.
- [ ] The guide avoids leading questions and captures problem evidence before pitching.
- [ ] A standard record exists for source, qualification, notes, verbatim evidence, requested capabilities, and commercial signal.

**Validation Test:**

- **Setup:** Prepare qualified, disqualified, and ambiguous sample leads.
- **Steps:**
  1. Apply the qualification criteria to all three.
  2. Conduct a dry-run interview.
  3. Complete the standard record.
- **Expected Result:** Clear cases receive deterministic outcomes, the ambiguous case identifies missing evidence, and the record is complete.
- **Failure Indicator:** Agency and product-team targets remain mixed, qualification is subjective only, or records are not comparable.

### US-003: Recruit and schedule the buyer-validation cohort

**Description:** As the launch owner, I want a tracked outreach cohort so that buyer validation advances from 0/10 interviews to scheduled conversations with the chosen ICP.

**Prerequisite:** GOV-001 and US-002.

**Acceptance Criteria:**

- [ ] The outreach list contains enough qualified prospects to make ten completed interviews plausible.
- [ ] Each prospect has a source, qualification evidence, outreach status, last-contact date, and next action.
- [ ] Outreach copy matches the chosen ICP and makes no unsupported claims.
- [ ] At least one outreach batch is sent.
- [ ] Interview #1 is booked, or the failed attempt is documented with response rate and revised sourcing action.
- [ ] Product work is not used as a substitute for buyer discovery.

**Validation Test:**

- **Setup:** A reviewed prospect list and approved message exist.
- **Steps:**
  1. Verify every selected prospect against the qualification rule.
  2. Send the first batch.
  3. Record delivery, replies, bookings, and next actions.
- **Expected Result:** The tracker shows an auditable funnel from qualified prospect to completed interview.
- **Failure Indicator:** Prospects do not match the ICP, outreach state cannot be reconstructed, or failed recruitment causes premature productization.

### US-004: Complete and synthesize ten buyer interviews

**Description:** As the launch owner, I want ten comparable buyer interviews synthesized into evidence so that commercialization reflects observed demand.

**Prerequisite:** GOV-001 and US-002.

**Acceptance Criteria:**

- [ ] Ten substantive interviews with qualified participants are complete.
- [ ] Every record separates observation from interpretation.
- [ ] Connector requests, permissions concerns, evaluation needs, deployment friction, willingness-to-pay evidence, and objections are coded consistently.
- [ ] The synthesis reports recurring themes, segment differences, contradictions, outliers, and confidence limits.
- [ ] The synthesis tests the buyer-fit condition selected under GOV-002.
- [ ] It recommends continue, revise, reposition, or stop without starting implementation automatically.
- [ ] P-series productization remains unstarted until review of the synthesis.

**Validation Test:**

- **Setup:** Ten completed interview records exist.
- **Steps:**
  1. Recount qualified participants and inspect required fields.
  2. Reproduce coded theme counts from source notes.
  3. Trace major claims to evidence.
  4. Verify no P-series work started early.
- **Expected Result:** Comparable records support a reproducible synthesis and explicit recommendation.
- **Failure Indicator:** Fewer than ten qualified interviews are treated as complete, counts cannot be reproduced, or implementation begins early.

### US-005: Clear trademark and cold-name testing

**Description:** As the launch owner, I want the Purvia name checked legally and behaviorally so that launch does not build recognition on an avoidable naming problem.

**Acceptance Criteria:**

- [ ] USPTO Class 9 and Class 42 searches are saved with dates and search terms.
- [ ] Materially similar names and their risk are documented.
- [ ] Ten cold participants complete the chosen SERP recognition/pronunciation test.
- [ ] The pass/fail rule is defined before responses are reviewed.
- [ ] Results cover pronunciation failures, confusion, brand collision, and search ambiguity.
- [ ] A go, revise, or rename recommendation is recorded without implying legal advice.

**Validation Test:**

- **Setup:** Saved search evidence, pre-registered protocol, and ten responses exist.
- **Steps:**
  1. Re-run the documented searches.
  2. Compare current and saved results.
  3. Recalculate the cold-test outcome.
- **Expected Result:** Another reviewer can reproduce the scope, score, and residual uncertainty.
- **Failure Indicator:** Search classes are missing, scoring was created after results, or legal certainty is overstated.

### US-006: Verify founder biography claims

**Description:** As a prospective buyer or hiring reviewer, I want founder claims to match primary records so that Purvia's credibility is not weakened by inflated language.

**Acceptance Criteria:**

- [ ] Every public claim about years, titles, employers, ownership, and outcomes is inventoried.
- [ ] Each claim maps to a resume, employment record, shipped artifact, or named primary source.
- [ ] Unverifiable quantities are removed or rounded down.
- [ ] Ambiguous employment-versus-project wording is explicit.
- [ ] Site, profile, README, and social copy agree.

**Validation Test:**

- **Setup:** Current primary records and all proposed biography copy are available.
- **Steps:**
  1. Trace each claim to a primary source.
  2. Search assets for conflicting facts.
  3. Ask an unfamiliar reviewer to explain what the biography claims.
- **Expected Result:** Every factual statement is sourced, conservative, and interpreted consistently.
- **Failure Indicator:** A claim lacks evidence, assets conflict, or readers infer stronger status than the source supports.

### US-007: Define and enforce the public repository boundary

**Description:** As the launch owner, I want an explicit publication manifest and clean repository so that public release contains only intentional, safe, current artifacts.

**Prerequisite:** GOV-004.

**Acceptance Criteria:**

- [ ] A path-level manifest lists included, excluded, and intentionally private artifacts.
- [ ] Excluded files are unreachable through public links and build output.
- [ ] Included files contain no credentials, private notes, local paths, stale instructions, or unapproved personal data.
- [ ] Historical claims that the canonical package is untracked or uncommitted are corrected or marked dated.
- [ ] Missing promised Mandu `raw/` or `wiki/` copies are restored or their README pointers are corrected.
- [ ] Required repository validation passes for publication changes.

**Validation Test:**

- **Setup:** Approved manifest and release-candidate revision exist.
- **Steps:**
  1. Compare repository/public output to the manifest.
  2. Search included files for sensitive data, absolute paths, and superseded copy.
  3. Follow every public link.
  4. Run required checks.
- **Expected Result:** Public content matches the manifest, has no leaks or stale pointers, and passes checks.
- **Failure Indicator:** An excluded artifact is public, private data leaks, a source path is broken, or validation fails.

### US-008: Complete the five-person credibility review

**Description:** As a technical buyer or hiring manager, I want Purvia reviewed by experienced practitioners so that it reads as credible engineering evidence rather than inflated marketing.

**Acceptance Criteria:**

- [ ] Five staff-engineer and/or hiring-manager-caliber reviewers independently review the same defined package.
- [ ] Every reviewer answers the same rubric, including whether it feels inflated or fluffy.
- [ ] Specific unsupported, unclear, or overly broad claims are recorded before edits.
- [ ] If three or more reviewers return an inflated/fluffy verdict, the package is revised and re-reviewed before launch.
- [ ] Every accepted change remains within `CLAIMS.md`.

**Validation Test:**

- **Setup:** Five review records and the pre-review revision exist.
- **Steps:**
  1. Verify reviewer count and role qualification.
  2. Recalculate the inflated/fluffy count.
  3. Trace edits to findings and permitted claims.
- **Expected Result:** The pass/de-hype result is reproducible and changes remain evidence-bounded.
- **Failure Indicator:** Reviews are incomparable, the 3-of-5 trigger is ignored, or claims strengthen without evidence.

### US-009: Preserve the four already-green credibility gates

**Description:** As a prospective buyer, I want receipts, claim honesty, required checks, and security reporting to remain healthy through launch.

**Acceptance Criteria:**

- [ ] Permissions-scale receipts continue publishing for the agreed observation window.
- [ ] Failed or missing receipts are corrected or publicly annotated within the agreed same-week window.
- [ ] Uncomputed RAGAS metrics remain explicitly unmeasured and absent from promotional claims.
- [ ] Branch protection and required E6/E7/AU4 checks remain enabled and pass on the release revision.
- [ ] `SECURITY.md` and private vulnerability reporting remain reachable.
- [ ] A launch-time snapshot records all four gates.

**Validation Test:**

- **Setup:** Release candidate and agreed recent receipt window exist.
- **Steps:**
  1. Inspect each expected receipt and its publication history.
  2. Search copy for prohibited RAGAS claims.
  3. Verify required checks.
  4. Follow the vulnerability-reporting path as an unauthenticated visitor.
- **Expected Result:** Receipts are current, claims honest, checks passing, and private reporting available.
- **Failure Indicator:** Publication silently stops, unmeasured metrics appear, checks are missing/red, or security reporting is unavailable.

### US-010: Reconcile model and judge evidence

**Description:** As a technical buyer, I want production and evaluation model choices documented and validated so that published evidence does not imply an untrue runtime.

**Prerequisites:** GOV-005 and GOV-006.

**Acceptance Criteria:**

- [ ] A matrix names the production answerer, eval answer generator, metadata model, offline judge, and both runtime judges.
- [ ] Intentional divergence includes rationale, expected effect, and limits on cross-environment claims.
- [ ] Issue #105's disposition is verified before any judge cutover.
- [ ] Database/corpus access exists before live E7 is represented as runnable.
- [ ] Live E7 records latency, false-resolve rate, and escalation impact for the chosen judge path.
- [ ] Any accepted judge configuration is applied atomically.
- [ ] Launch claims reflect the actual model matrix.

**Validation Test:**

- **Setup:** Release candidate, environment configuration, model matrix, and E7 fixtures/credentials exist.
- **Steps:**
  1. Resolve each model role from code and configuration.
  2. Compare it to GOV-005/GOV-006.
  3. Run the approved E7 path.
  4. Verify atomic deployment and rollback behavior.
- **Expected Result:** Model roles match approved policy, validation evidence exists, and meaningful divergence is disclosed.
- **Failure Indicator:** Roles rely on stale docs, issue #105 remains exposed, E7 cannot run, or configuration is partial.

### US-011: Freeze claims and paid-surface behavior

**Description:** As a prospective buyer, I want every claim and paid CTA to match evidence and approved offer policy so that I am not asked to buy incomplete or overstated value.

**Prerequisites:** GOV-001, GOV-003, GOV-005, and GOV-006.

**Acceptance Criteria:**

- [ ] Every customer-facing claim maps to a current `CLAIMS.md` row.
- [ ] Denominators, caveats, dates, and scale limits appear wherever required.
- [ ] Uncomputed RAGAS and unmeasured 100k+ recall are not implied.
- [ ] Buyer language matches GOV-001 across site, repository, and social assets.
- [ ] The $199 CTA exactly implements GOV-003.
- [ ] Every Pro deliverable required by GOV-003 exists at the promised time.
- [ ] `projects/Purvia/launch/bin/claimlint.sh` passes.

**Validation Test:**

- **Setup:** Final site, repository copy, social assets, claims ledger, and GOV-003 exist.
- **Steps:**
  1. Run `claimlint.sh`.
  2. Trace quantitative/comparative claims to evidence.
  3. Exercise the paid CTA and inspect promised deliverables.
  4. Search for rejected ICP wording and prohibited metrics.
- **Expected Result:** Claims are source-bounded and the paid experience matches adopted policy.
- **Failure Indicator:** Claimlint fails, a claim exceeds evidence, unavailable material is promised, or ICP language conflicts.

### US-012: Conduct the final launch-readiness review

**Description:** As the launch owner, I want one evidence-backed go/no-go review so that publication occurs only when governance, credibility, buyer validation, measurement, and assets are ready together.

**Prerequisites:** US-001 through US-011.

**Acceptance Criteria:**

- [ ] GOV-001 through GOV-006 are resolved and GOV-007 is recorded.
- [ ] All eight hard preconditions are green with evidence.
- [ ] Ten buyer interviews and synthesis are complete.
- [ ] Claims and paid-surface validation pass.
- [ ] Measurement rules have no unresolved denominator or undersampling ambiguity.
- [ ] Publication manifest and distribution schedule are approved.
- [ ] A launch date is assigned only after all blocking items pass.
- [ ] The review records go, conditional no-go, or stop/reposition.

**Validation Test:**

- **Setup:** Assemble the complete readiness packet.
- **Steps:**
  1. Review every prerequisite and gate against evidence.
  2. Attempt to mark go while withholding one required artifact.
  3. Verify scheduling is relative to a post-readiness launch date.
- **Expected Result:** Go requires complete evidence; missing evidence produces a named no-go.
- **Failure Indicator:** A red gate is waived implicitly, evidence is missing, or a date precedes readiness.

### US-013: Publish the approved site and public artifacts

**Description:** As a qualified prospect, I want a clear, trustworthy launch surface so that I can understand the problem, inspect evidence, evaluate the free core, and take the approved commercial action.

**Prerequisite:** US-012 outcome is go.

**Acceptance Criteria:**

- [ ] Only paths approved under GOV-004 are published.
- [ ] Content matches the final ICP, offer, claims ledger, and paid-surface policy.
- [ ] Navigation, repository, security, evidence, signup, and paid-action links work.
- [ ] The site renders at supported desktop/mobile widths without overflow or inaccessible controls.
- [ ] Signup/payment behavior is tested end to end according to GOV-003.
- [ ] Evidence capture required by GOV-002 is active before traffic is sent.
- [ ] Typecheck/lint and project-required validation pass for changed assets.
- [ ] Verify in browser using dev-browser skill.

**Validation Test:**

- **Setup:** Production candidate, clean browser profiles, supported viewports, and test conversion identities.
- **Steps:**
  1. Open every public page on desktop and mobile.
  2. Follow all primary and secondary links.
  3. Complete signup and the approved paid action.
  4. Verify required measurement evidence.
  5. Compare published content to the GOV-004 manifest.
- **Expected Result:** Approved assets are reachable, coherent, responsive, measurable, and functional.
- **Failure Indicator:** A link/conversion fails, an excluded file is exposed, governance conflicts, or layout breaks.

### US-014: Execute the launch distribution sequence

**Description:** As the launch owner, I want content released in a controlled sequence so that channel results can be interpreted against one pre-registered experiment.

**Prerequisite:** US-013 and GOV-002.

**Acceptance Criteria:**

- [ ] The relative schedule is frozen before the first post.
- [ ] X thread 1 launches first unless the recorded plan explicitly changes order.
- [ ] Later X posts, LinkedIn, Instagram, and any HN cross-post follow approved timing.
- [ ] Every asset uses approved claims, links, ICP language, and tracking conventions.
- [ ] URL, timestamp, channel, asset revision, and anomalies are logged.
- [ ] Thresholds and creative do not change mid-window except under a pre-registered safety rule.
- [ ] Every deviation records its trigger and effect on experiment validity.

**Validation Test:**

- **Setup:** Approved calendar, final assets, and evidence plan exist.
- **Steps:**
  1. Publish the first asset and record evidence.
  2. Verify later assets cannot be released early without a deviation record.
  3. Compare live assets to approved revisions.
- **Expected Result:** Releases follow the frozen sequence and each result is attributable.
- **Failure Indicator:** Posts are unlogged, order changes silently, claims drift, or changes make results uninterpretable.

### US-015: Produce authentic video and TikTok assets

**Description:** As a technical prospect, I want demonstrations captured from a real Purvia stack so that video evidence reflects actual behavior rather than a simulated interface.

**Prerequisite:** US-012 outcome is go and a working local stack exists.

**Acceptance Criteria:**

- [ ] Video uses a real local Purvia stack and non-sensitive test data.
- [ ] Demonstrated behavior matches the release revision.
- [ ] Scripts contain only claims permitted by `CLAIMS.md`.
- [ ] No credentials, customer data, private paths, or unrelated desktop content appear.
- [ ] TikTok publication waits for real footage; scripts alone are not treated as ready.
- [ ] Captions and links match the approved ICP and offer.
- [ ] Verify in browser using dev-browser skill where video is embedded or previewed.

**Validation Test:**

- **Setup:** Running release revision, scrubbed corpus, checklist, and final scripts.
- **Steps:**
  1. Reproduce each demonstrated action.
  2. Review the recording frame by frame for sensitive material and claim mismatches.
  3. Open the encoded asset in each intended channel preview.
- **Expected Result:** Footage is authentic, reproducible, safe, legible, and claim-aligned.
- **Failure Indicator:** The demo cannot be reproduced, sensitive data appears, or overlays overstate behavior.

### US-016: Adjudicate the launch experiment

**Description:** As the launch owner, I want the launch assessed against pre-registered evidence so that the commercial decision is not rewritten after results are known.

**Prerequisite:** GOV-002 and completion of its measurement window.

**Acceptance Criteria:**

- [ ] Adjudication uses only the recorded thresholds, windows, denominators, compound-condition semantics, and insufficient-sample rule.
- [ ] Raw evidence is linked for every metric.
- [ ] Attention, intent, buyer-fit, and payment outcomes are calculated where applicable.
- [ ] Missing/undersampled metrics are handled as pre-registered, never counted as implicit passes.
- [ ] Every triggered action is applied, including any quarter-level stop rule.
- [ ] The result selects continue, revise/retest, free credibility asset, reposition, or stop paid-tier work.
- [ ] Thresholds are not retrospectively edited.

**Validation Test:**

- **Setup:** Frozen GOV-002 record, raw evidence, and completed measurement window.
- **Steps:**
  1. Recompute every metric.
  2. Apply compound-condition and insufficient-sample rules.
  3. Count triggered tripwires.
  4. Compare the next state to the prescribed actions.
- **Expected Result:** An independent reviewer reaches the same outcome.
- **Failure Indicator:** A denominator is missing, thresholds changed, undersampling is treated as success without authorization, or an action is ignored.

### US-017: Close the launch loop

**Description:** As a future contributor, I want the outcome reflected in authoritative records so that later work does not resurrect stale plans or repeat resolved debates.

**Prerequisite:** US-016.

**Acceptance Criteria:**

- [ ] `projects/Purvia/README.md` records the launch outcome and current phase.
- [ ] This PRD's criteria are checked only after their Validation Tests pass.
- [ ] Superseded metric, ICP, model, and preorder guidance is corrected or marked historical.
- [ ] The commercial next state has a dated rationale and linked evidence.
- [ ] Follow-up implementation is separately scoped rather than silently added here.
- [ ] Any stop/quarter-level kill decision prevents conflicting productization work.

**Validation Test:**

- **Setup:** Final adjudication and authoritative sources are available.
- **Steps:**
  1. Search for every superseded policy and stale status from the source audit.
  2. Trace current phase and next state from README to evidence.
  3. Verify checked criteria have passing validation evidence.
- **Expected Result:** A new reader can identify current state, decisions, evidence, and next work without historical chat.
- **Failure Indicator:** Stale guidance appears current, checkboxes lack evidence, or new scope is hidden in cleanup.

## 6. Functional Requirements

- **FR-1:** Maintain GOV-001 through GOV-007 as explicit prerequisites with recorded status and evidence.
- **FR-2:** Do not assign a launch date until GOV-001 through GOV-006 are resolved and all eight hard preconditions are green.
- **FR-3:** Keep GOV-007 non-blocking unless a recorded decision makes a domain part of the launch path.
- **FR-4:** Every downstream story must name and honor its governance prerequisites.
- **FR-5:** Buyer qualification and interviews must use one schema tied to the chosen ICP.
- **FR-6:** Ten qualified interviews and a reproducible synthesis must exist before P-series productization.
- **FR-7:** Re-verify the four already-green credibility gates at release time.
- **FR-8:** Trademark/name testing must include documented Class 9/42 searches and a pre-scored ten-person cold test.
- **FR-9:** Biography claims must map to primary evidence and round down or be removed when uncertain.
- **FR-10:** Public repository content must match the GOV-004 path manifest.
- **FR-11:** Five qualified reviewers must use a consistent rubric; a 3-of-5 inflated/fluffy result blocks launch until revision and re-review.
- **FR-12:** Every public claim must map to `CLAIMS.md`; missing denominators or caveats block publication.
- **FR-13:** Uncomputed RAGAS metrics and unmeasured 100k+ recall must not appear as achieved results.
- **FR-14:** Production/eval model roles and judge configuration must match GOV-005/GOV-006 and the actual release environment.
- **FR-15:** A paid CTA must exactly implement GOV-003 and cannot imply unavailable deliverables.
- **FR-16:** Measurement evidence required by GOV-002 must be operational before public traffic.
- **FR-17:** Distribution must follow a frozen relative schedule with URL, channel, timestamp, and asset revision recorded.
- **FR-18:** Video demonstrations must use a real running stack and scrubbed data.
- **FR-19:** Adjudication must use pre-registered thresholds and undersampling rules without retrospective edits.
- **FR-20:** Every triggered stop, revise, reposition, or continue action must be recorded and applied.
- **FR-21:** A story may be checked complete only after its Validation Test passes.

## 7. Non-Goals

- Implementing P-series features before buyer-interview synthesis.
- Choosing an ICP, measurement framework, preorder policy, publication boundary, model policy, judge rollout, or domain by implication.
- Rebuilding the complete 2026-08-27 package without a specific validation finding.
- Treating the July campaign as the current launch.
- Claiming RAGAS scores the pipeline has not computed.
- Treating the perfect 10k scale result as proof of unmeasured larger-scale behavior.
- Building Slack, Drive, or Confluence connectors before buyer evidence authorizes them.
- Solving single-maintainer bus factor; MIT licensing remains the current mitigation.
- Providing legal advice through trademark research.
- Adding a launch date before readiness passes.
- Expanding into unrelated job-search, portfolio, or Rep Today work.

## 8. Design Considerations

- Lead with the measured 42-day failure and controls built afterward, not a generic all-green benchmark.
- Clearly distinguish the free MIT core from the paid/preorder offer selected under GOV-003.
- Put denominators, dates, scale, and caveats near quantitative claims.
- Make the core differentiator legible: authorization inside the retrieval predicate plus a shipped evaluation harness.
- Support desktop and mobile with no horizontal overflow and keyboard-accessible actions.
- Keep the security disclosure and private vulnerability-reporting route easy to find.
- Preserve existing GitHub links through redirects if GOV-007 selects a custom domain.
- Keep social/video ICP, offer, evidence, and caveats aligned with the site.

## 9. Technical Considerations

- The launch site is a self-contained static artifact at `projects/Purvia/launch/site/index.html`; avoid an unnecessary application stack.
- `projects/Purvia/launch/bin/claimlint.sh` is the minimum automated claims check.
- Branch protection and E6/E7/AU4 required checks are part of the public credibility story.
- Live E7 depends on reachable database/corpus infrastructure; judge cutover cannot rely on a validation path that remains unavailable.
- A partial judge configuration is unsafe. If GOV-006 chooses `gpt-5-mini`, model, temperature omission, and reasoning effort must move together after issue #105 and E7.
- Model divergence changes what benchmarks prove; public material must show the actual launch-time matrix.
- GOV-002 determines analytics requirements. Use the smallest privacy-conscious mechanism that proves required denominators and conversions.
- Scan publication content for credentials, private notes, absolute local paths, personal data, and excluded artifacts.
- Video requires a real local stack and test data; a script/static mock is not implementation evidence.
- Mandu lacks promised raw Phase 2 PRD/wiki copies; use the actual Purvia repository for implementation disputes until repaired.

## 10. Risks and Mitigations

| Risk | Consequence | Required mitigation |
|---|---|---|
| Conflicting ICP sources | Interviews/copy test different markets | Resolve GOV-001 and update active sources before outreach |
| One-week vs. 30/90-day criteria | Results can be reinterpreted | Resolve GOV-002 and freeze thresholds/undersampling before publication |
| Preorder promises incomplete value | Trust, refund, and reputation risk | Resolve GOV-003 and validate deliverables/CTA |
| Private or stale artifacts publish | Security/privacy leak or confused narrative | Resolve GOV-004 and validate the path manifest |
| Eval/production model divergence | Benchmarks overstate runtime behavior | Resolve GOV-005 and publish the model matrix |
| Unsafe judge cutover | Errors may permanently latch conversations | Resolve GOV-006, issue #105, database access, and E7 |
| Receipt publication regresses | Evidence silently becomes stale | Monitor and correct/annotate failures promptly |
| Small evaluation denominators | Readers infer stronger reliability | Keep denominators and limits adjacent to claims |
| Single-maintainer bus factor | Support and maintenance concern | Disclose honestly; retain MIT mitigation |
| Weak buyer recruitment | Launch proceeds without market evidence | Treat it as a sourcing problem, not permission to skip interviews |
| Schedule outruns readiness | Traffic reaches inconsistent assets | Assign dates only after the go decision |

## 11. Success Metrics

### Pre-launch completion

- 7/7 governance prerequisites recorded, with GOV-001 through GOV-006 cleared.
- 8/8 hard public-launch preconditions green with evidence.
- 10/10 qualified buyer interviews completed and synthesized.
- 5/5 external credibility reviews completed; any 3-of-5 de-hype trigger resolved.
- Zero customer-facing claims outside `CLAIMS.md`.
- Zero exposed artifacts outside the GOV-004 manifest.
- Zero broken primary links or failed approved conversion paths.
- Required repository checks and `claimlint.sh` pass on the release candidate.

### Launch experiment

Binding metrics are **TBD pending GOV-002**. These source values are candidates, not adopted requirements:

- Candidate attention pass: at least 20,000 impressions **and** 50 meaningful engineer replies/reposts across X plus HN if cross-posted.
- Candidate intent pass: at least 30 email signups from the first 500 unique visitors (6%).
- Candidate buyer-fit tripwire: at least 5 of the first 10 substantive inbound conversations primarily request Slack/Drive/Confluence connectors.
- Candidate payment tripwire: zero paid preorders in week one despite at least 30 signups.
- Candidate portfolio stop rule: two or more tripwires stop paid-tier work for the quarter.

GOV-002 must define insufficient-sample handling, compound attention semantics, and how older 30/90-day measures relate to the launch-window decision.

### Process integrity

- 100% of published assets record URL, timestamp, channel, and revision.
- 100% of adjudicated metrics link to reproducible raw evidence.
- Zero threshold changes after first publication unless the experiment is invalidated and restarted.
- 100% of completed stories have passing Validation Tests.

## 12. Open Questions

All remain unresolved prerequisites:

1. **GOV-001 — ICP:** Which buyer segment governs outreach, qualification, copy, and channels?
2. **GOV-002 — Measurement:** Which windows and thresholds govern, how do compound conditions work, and what happens when denominators are not reached?
3. **GOV-003 — Paid surface:** May a labeled founding preorder publish before all Pro deliverables exist?
4. **GOV-004 — Publication boundary:** Which exact launch artifacts become public?
5. **GOV-005 — Model alignment:** Must eval match production, must production migrate, or is disclosed divergence acceptable?
6. **GOV-006 — Runtime judge:** What evidence/infrastructure is required before cutover, and is `gpt-5-mini` still intended?
7. **GOV-007 — Domain:** Use `purvia.ai`, another domain, or no custom domain?

## 13. Definition of Done

This PRD is complete when:

- Every blocking governance prerequisite is resolved and reflected in authoritative sources.
- All eight hard launch preconditions pass with evidence.
- Ten qualified interviews are synthesized before productization.
- The site, publication boundary, claims, paid surface, model narrative, and measurement plan pass validation.
- The approved publication and distribution sequence is executed.
- The launch is adjudicated against frozen rules.
- The commercial next state is recorded and stale planning material is corrected or marked historical.
- Acceptance criteria are checked only after their corresponding Validation Tests pass.
