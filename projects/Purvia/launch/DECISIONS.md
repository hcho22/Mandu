# DECISIONS.md - questions I would have asked, with the answers I chose

Run started 2026-08-27. Every entry: the question, the answer, the reasoning, and the evidence.

## D1. Where does `launch/` live?

**Q:** The brief says "all local in launch/" but not where. The repo gitignores `.claude/launch/` (a prior war room, files absent on this machine) and `/gtm/`.
**A:** `projects/Purvia/launch/` at the repo root, untracked, never committed or pushed.
**Why:** The brief names `launch/` exactly; assets need relative access to repo docs for evidence paths. Nothing is staged or committed, so "publish nothing" holds without touching `.gitignore` (which would violate "don't touch the product").

## D2. The brief says `prd-retrieval-quality-pass.md` has zero stories started. The repo says Status: complete.

**Q:** Which is true?
**A:** The repo. `.claude/agent/tasks/prd-retrieval-quality-pass.md` line 3: "Status: complete. US-113 ... US-118 all landed." The nightly `docs/nightly/2026-08-27.md` confirms the fix is live: keyword paraphrase recall@5 is 0.800 (was 0.000), keyword lexical 1.000, hybrid ≥ vector in every category, non-regression hybrid 0.950 vs vector 0.875.
**Why:** "Invent nothing" and "capability proved from source" outrank a stale brief premise. The claim ledger reflects current repo evidence. Consequence: the retrieval-quality pass is **shipped**, not planned, and its stories can be cited as shipped rows.

## D3. Does "never market hybrid retrieval as an advantage" still bind now that hybrid beats vector?

**A:** Yes, as framing law. The headline stays "the harness caught the dead leg" - the 0.140 keyword recall@5 and hybrid-below-vector inversion (hybrid MRR 0.786 vs vector 0.796) are cited as *what the harness caught*, and the current numbers appear only as the measured outcome of that catch, never as a "best-in-class hybrid" pitch. <!-- CLAIMLINT-ALLOW: meta-mention of the banned phrase itself -->
**Why:** The directive's letter is explicit and its spirit (market the measurement discipline, not retrieval bragging rights) is exactly the differentiator. The recovery numbers travel with their denominator (60-question golden set, e-commerce demo corpus) per the denominators rule.

## D4. The all-1.000 permissions scale table: usable at all?

**A:** Usable only with its full caveat block: 15 multi-hop queries, 10k-chunk synthetic Wikipedia corpus, and the README's own admission that at 10k chunks the planner sidesteps HNSW so every cell is trivially 1.000. The *42 days of measured 0.000* under a green hand-copied table (2026-06-19 to 2026-07-30, README lines 41-77) leads; the recovered table follows as corroboration.

## D5. RAGAS numbers: memory of this project says `score_with_ragas()` once returned `[]` unconditionally.

**Q:** Are RAGAS weekly numbers real today?
**A:** Verified during Phase 0: still unimplemented. `evals/retrieval/ragas.py:157` returns `[]` with the comment "US-001 ships scaffold only"; the weekly page renders an all-dashes RAGAS table. RAGAS claims are banned from customer-facing assets (CLAIMS.md C22 + banned list); README.proposed.md corrects the current README's line-131 overclaim. The weekly page's retrieval and Claude-judge numbers are real and remain usable (C13).

## D6. Pricing: brief says paid tier ~$149-249 one-time. What exact number?

**A:** Deferred to Phase 1 pricing research (competitor kit pricing scan), then fixed in POSITIONING.md within the captain's stated band. The band itself is a brief constraint, not a research output.

## D7. Multi-agent orchestration is structurally simulated, not literally parallel.

**Q:** The brief demands multi-agent orchestration, but this session's environment denies both harness delegation tools (Workflow, Agent) via a fleet guard hook, and fleet crewmate dispatch requires a session lock plus machinery that is wrong for local read-only research from a background session.
**A:** The orchestration *structure* is preserved as distinct sequential passes with independent briefs - six evidence-reader passes for inventory, a positioning tournament with scored entrants, and four separately-framed red-team adversaries - each checkpointed to `launch/checkpoints/`. What is lost is wall-clock parallelism and sampling independence between "agents"; what is kept is the deliverable structure (scorecards, adversary reports, objection handling).
**Why:** The alternative (spawning tmux crewmates) risks colliding with the live primary session's lock and violates proportionality for read-only local work. Logged rather than asked, per the never-ask rule.

## D8. Trademark status appears in buyer-facing docs?

**A:** ADR-0011 admits USPTO clearance is pending and a consumer "Purvia" face-swap app exists in another class. This goes in the red-team findings and stays out of customer-facing copy (it is an internal risk, not a claim). No domain is purchased (no-spend rule); site copy references purvia.ai only as the ADR's stated intent, marked as unregistered-yet in CLAIMS.md.

## D9. Exact price within the $149-249 band?

**A:** $199 one-time for the paid tier ("Purvia Pro").
**Why:** Matches ShipFast's flagship point (fetched https://shipfa.st/), sits under SaaS Pegasus's $449 open-core paid tier (fetched https://www.saaspegasus.com/pricing/), and leaves $249 as headroom for a later post-validation raise rather than starting at the ceiling.

## D10. What does the paid tier contain, given the whole repo is already MIT?

**A:** Adoption, not withheld code: golden-set authoring workbook + review checklists, deployment hardening playbooks, 12 months prioritized issue response, widget theming presets. Nothing public moves behind a paywall; nothing unbuilt is sold as built; pricing page gated on the deliverables existing (POSITIONING.md "Pricing decision").
**Why:** Retro-paywalling MIT code would require touching the product (forbidden) and would poison the trust positioning. SaaS Pegasus proves free-core + paid-adoption coexists.

## D11. Tournament disqualification record.

Angle F (hosted multi-tenant SaaS) was generated and disqualified for violating Ground Truth (engineer-buyer kit, not SaaS). Angle D (support-deflection wedge as headline) was kept in the tournament but its loss is anchored to ADR-0011's own rejection of deflection-scoped branding.

## D12. Video: scripts only, no footage.

**Q:** Social phase calls for video from real captured footage only.
**A:** No live deployment existed in this run to record; fabricating UI footage would violate invent-nothing. Shipped instead: two complete scripts (`launch/social/video-scripts.md`) and three TikTok shot lists (`launch/social/tiktok-shotlists.md`) with exact recording requirements against a locally-run stack.
