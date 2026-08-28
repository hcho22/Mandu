# RED-TEAM.md - four adversaries against the launch package

Each adversary was run as a separate pass with a hostile brief.
**Finding format:** attack -> verdict -> disposition. "FOLDED" means the fix or the surviving objection now lives in a customer-facing asset, not just here.

## Adversary 1 - the engineer, attacking every claim from the code

1. **"Hybrid ≥ vector in every category" is false.** `docs/nightly/2026-08-27.md` shows hybrid paraphrase MRR 0.767 vs vector 1.000. The claim only holds for recall@5.
   Verdict: CONFIRMED - our site, X post 3, INVENTORY N6, and CLAIMS C6 all overstated.
   Disposition: **FOLDED** - all four assets corrected to "hybrid recall@5 ≥ vector in every category", with the MRR inversion now cited *as further proof the harness keeps score on us*. C6 carries an explicit "never claim the MRR version" cap.
2. **"Re-proved on every PR" (Instagram card 2) is false.** `ship-green.yml` runs on changes to the green-determining surface and on `push: main`, not on every PR.
   Verdict: CONFIRMED.
   Disposition: **FOLDED** - card re-rendered with "every relevant PR and on main" (matches `docs/evals.md:163-164`).
3. **"A run that measures nothing can never publish a number" is an inductive claim.** The guards cover every *known* degeneracy path (authored gold, derived gold, missing snapshot, stranded publish) and are themselves CI-pinned, but "never" is a claim about unknown paths too.
   Verdict: PLAUSIBLE overreach; however the product's own docs use the same wording ("an unmeasured run can never read as a measured 0.000", `README.md:96`), so marketing does not exceed the source.
   Disposition: accepted with the source citation; no change.
4. **"No human in the loop" on the Δ-0.510 catch.** A human authored the throwaway PR; the catch and the comment were automated.
   Verdict: wording survives - every asset scopes the automation to "ran ... and posted", and the site/cards state the cause was contrived.
   Disposition: no change; the "cause contrived, catch real" caption stays mandatory on every use (C5).
5. **Escalation numbers are tiny (3/4/9 rows).**
   Verdict: TRUE and already disclosed in the same visual unit everywhere they appear.
   Disposition: standing rule - those numbers may never appear without their populations.

## Adversary 2 - the competitor's most damaging true comparison

Their opening move, as briefed, is the lexical leg:

> "Purvia shipped for months with a dead keyword leg - recall@5 0.140, 0.000 on paraphrase - that made their hybrid retrieval *worse* than doing nothing. Their security proof is 60 questions on 16 chunks. Their scale test is 15 queries at a size where perfect scores are mathematically guaranteed. Their 'RAGAS weekly' has never computed a RAGAS score. Their safety rate is 9 questions. Their trademark isn't cleared, they have zero customers, and the outage they lead with happened because they mis-seeded their *own permissions system*. Oh - and the README table they talk about? Still updated by hand."

Line-by-line verdict:

| Attack | True? | Our standing answer (and where it lives) |
|---|---|---|
| Dead lexical leg shipped for months | TRUE | We publish the catch and the measured fix ourselves; it is the lead of X post 3 and the site's "harness also caught us" block. The competitor retelling it is retelling our asset. |
| 60q/16-chunk security proof | TRUE | Disclosed beside every use (C3); FAQ answers it head-on; the discipline (cold-seed re-proof, no off switch, vacuous-pass refusal) is the claim. |
| Scale table trivially perfect | TRUE | We say "trivially-perfect" ourselves on the site's who-not-to-buy list (C26). |
| RAGAS never computed | TRUE | Banned from our copy (C22); README.proposed.md corrects the repo's own overclaim. **This attack lands hardest on the CURRENT live README** - see Residual risk R1 below. |
| 9-question safety rate | TRUE | Populations always attached (C12). |
| Trademark pending / zero customers | TRUE | Never claimed otherwise; no testimonials or traction language anywhere (BRAND.md bans them). |
| Mis-seeded own permissions system | TRUE | **FOLDED** - new site FAQ: the boundary failed *closed* (hid everything); the failure direction is the one you want, and the reporting that deserved the embarrassment got rebuilt. |
| README table still hand-copied | TRUE | **FOLDED** - new site FAQ: yes, the README says so itself and names the automated source of truth that now corroborates it. |

Overall verdict: the comparison is damaging only to a reader who has not seen our assets, because every line of it is already in our assets. That is the point of the positioning.

## Adversary 3 - the brand critic

1. **"Purvia" reads pharmaceutical.** True risk (coined -ia suffix). Mitigation folded into BRAND.md already: the wordmark never appears without the descriptor line "permissions-aware RAG" in profile and hero assets. Name is settled (ADR-0011); noted, closed.
2. **A failure-led brand can become "the 0.000 company."** Real risk if the story runs without its second act. Standing rule (BRAND.md §4): the failure never appears without the fix in the same asset; hero, cards, and thread all pair them. Verified in shipped assets.
3. **The denominator habit can read as pedantry.** Accepted trade - the buyer is an engineer; the tone is the moat. Calibration: denominators live in captions (slate, mono), headlines carry the story - already the layout grammar.
4. **The scope-bracket mark could be mistaken for a "crop" icon.** At avatar size it reads as a distinct badge (verified render); the green fill and constant pairing with the wordmark carry recognition. Accepted.
5. **Two voices risk: site says "we", ADRs say "the kit".** Ruled: customer-facing assets use "we/our" for the story and "the kit/Purvia" for the artifact - consistent across shipped assets. Closed.

## Adversary 4 - the career auditor (job-search impact for the maintainer)

1. **Asset:** the failure story + guard architecture is senior-engineer signal (eval design, CI design, honest incident writing). The repo's docs read as work samples; the launch amplifies them. Net positive.
2. **Risk: the live README's RAGAS bullet.** An interviewer who greps `ragas.py` finds a scaffold behind a "computed weekly" claim - an integrity ding in the exact repo being showcased.
   Disposition: **README.proposed.md fixes it; recommend landing that fix before the X thread runs.** (Residual risk R1.)
3. **Risk: a launched-then-abandoned "product" looks worse than a portfolio repo.** Mitigated structurally: THESIS.md carries one-week kill criteria with explicit fold-back actions ("reposition as portfolio/credibility asset"), so a no-traction outcome has a dignified, pre-planned exit.
4. **Risk: "42 days to notice" skim-read.** The story's own text preempts it (alarm fired nightly; the human-facing table was the gap) - present in every telling.
5. **Risk: preorder revenue with undelivered Pro pack looks bad if it stalls.** Mitigated: pricing page labels Pro "founding preorder - not yet shipped" and POSITIONING gates going-live on deliverables existing.

## Residual risks (open, not fixable from launch/)

- **R1 - the live README overclaims RAGAS.** The fix exists only as `README.proposed.md`; until it lands on main, adversary 2's sharpest true attack stands. Recommended order: land the README fix, then run the thread.
- **R2 - trademark clearance still pending** (ADR-0011). No branding spend beyond zero-cost local assets until cleared; customer copy stays silent on it.
- **R3 - purvia.ai unregistered.** All local assets reference the GitHub repo, not a domain; registering is a captain decision outside no-spend.
- **R4 - single-maintainer bus factor** is visible to any buyer reading the repo. Not concealable and not currently answerable; the MIT license is the honest mitigation (a buyer keeps the code regardless).
