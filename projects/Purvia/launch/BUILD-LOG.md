# BUILD-LOG.md - run journal and resume checkpoint

Run of 2026-08-27, session goal: full marketing package under `launch/`.
Status: **COMPLETE** - all six phases delivered and graded; residual risks live in `RED-TEAM.md` ("Residual risks").

## Phase status

| Phase | Status | Outputs |
|---|---|---|
| 0 Inventory | DONE | `INVENTORY.md`, `CLAIMS.md` (30 rows + banned list), `DECISIONS.md`, `bin/claimlint.sh` |
| 1 Positioning | DONE | `POSITIONING.md` (tournament scorecard + objection bank), `THESIS.md` (kill criteria), `checkpoints/phase1-research.md` (fetched URLs) |
| 2 Brand | DONE | `BRAND.md` |
| 3 Site | DONE | `site/index.html`; screenshots in `checkpoints/` (desktop + mobile, fold + full) |
| 4 Social | DONE | `social/x-thread.md`, `linkedin.md`, `instagram/` (4 rendered PNGs + captions), `tiktok-shotlists.md`, `video-scripts.md`, `profile/` (avatar + banner) |
| 5 Red team | DONE | `RED-TEAM.md`; fixes folded into site/thread/cards/ledger |
| 6 Package | DONE | `recap.html` (all relative links verified against the filesystem; repo URL fetched and confirmed public/MIT) |

Also delivered: `../README.proposed.md` (the one permitted product artifact - fixes the RAGAS overclaim at current `README.md:131`, adds "Who should not use this").

## Verification record

- `bin/claimlint.sh launch/` - clean (marketing-speak, overclaim, placeholder scans; `CLAIMLINT-ALLOW` marks deliberate meta-mentions).
- `README.proposed.md` lint: one `wk_pk_xxx` hit inherited verbatim from the shipped README's embed example - an intentional sample key, not a launch placeholder.
- Site: 390px viewport verified programmatically (scrollWidth = innerWidth = 390; wide tables/code scroll inside their own containers); visual passes at 500px (mobile layout - headless Chrome's minimum window) and 1440px; a real nav-overflow bug was found in screenshots and fixed.
- Git: `projects/Purvia` shows only untracked `launch/` and `README.proposed.md`; no tracked file modified, nothing staged, nothing committed or pushed.
- Red-team corrections applied: hybrid MRR-vs-recall@5 precision (site, X post 3, INVENTORY N6, CLAIMS C6), "every relevant PR" on card 2 (re-rendered), two FAQ additions (fail-closed direction; hand-copied table).

## Brief-vs-repo corrections (trust the source)

- `prd-retrieval-quality-pass.md` is Status: complete (not zero-started) - its stories are shipped claims (D2).
- RAGAS scores have never been computed (`evals/retrieval/ragas.py:157` scaffold) - banned from customer copy (D5, C22); the current live README overclaims them (residual risk R1, fix = land `README.proposed.md`).

## Resume notes

- Evidence base: `INVENTORY.md` N1-N10 and "Claim caps"; all external citations in `checkpoints/phase1-research.md`.
- Orchestration: harness delegation tools were hook-blocked; multi-agent structure ran as independent sequential passes (D7).
- Rendering: Instagram cards / profile assets re-render via headless Chrome from their HTML sources (commands identical to the ones in git-less history; any `--window-size` matching the asset dimensions works).
