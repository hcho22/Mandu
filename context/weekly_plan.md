# Weekly Plan: 2026-06-29 to 2026-07-05

_Created 2026-06-27. Regenerate at the start of each week; this file holds the current week only._

## Framing

FitSnack is now a real build with dedicated time (new income bet #2), but the Agentic RAG daily logs show the validation gate has been open for 3 straight days: post #1 unpublished, no waitlist, no interviews booked, while the build raced ahead.
So this week's job is to clear that gate first and prevent the new FitSnack build from cannibalizing it.
Validation is the spine of the week; FitSnack build slots in after Monday's unblock; the job search holds at 5/week.

Note: Sat 7/4 is the July 4th holiday, so the working week is Mon-Fri. Front-loaded accordingly.

## Week at a glance

| Day | Primary block | Secondary block | Job search |
|-----|--------------|-----------------|------------|
| **Mon 6/29** | AR: publish post #1 + Tally waitlist + CTA | AR: buyer-interview outreach (book 3) | 1 app |
| **Tue 6/30** | FitSnack: build ViewModels layer | AR: post engagement, confirm CI green on main | 1 app + finalize behavioral answers |
| **Wed 7/1** | AR: draft post #2 (leak-eval / CI-gate rigor) | FitSnack: engine Epic C steps 1-2 (TDD) | 1 app |
| **Thu 7/2** | FitSnack: engine Epic C steps 3-4 (TDD) | AR: run booked interviews / polish post #2 | 1 app |
| **Fri 7/3** | AR: publish post #2 | FitSnack buffer + weekly closeout | 1 app (hits 5/week) |
| **Sat 7/4** | Holiday - off (light: reply to post engagement) | - | - |
| **Sun 7/5** | Light: plan the following week, rest | - | - |

## Daily template (daily-loop skill)

Adjust clock times to your rhythm:

- **9:00** Morning brief (15 min)
- **9:15-12:00** Block 1 - primary deep work
- **1:00-2:30** Block 2 - secondary
- **2:30-3:15** Job-search slice (1 application or interview prep)
- **5:00** EOD closeout + daily log (15 min)

## Day-by-day

### Monday 6/29 - Clear the validation gate (highest leverage)

- Block 1: Publish flagship post #1 (`projects/Agentic_RAG/posts/01-permission-aware-rag.md`, already drafted). Pick channel (LinkedIn + a dev community), final proof, post. Create the Tally waitlist form and wire `waitlist-cta.md` variant A + link.
- Block 2: Buyer-interview outreach - send 5-8 personalized notes to your network using `projects/Agentic_RAG/posts/buyer-interview-script.md`; target booking 3.
- This single day kills the 3-day-old blocker that gates the income thesis.

### Tuesday 6/30 - FitSnack momentum + AR follow-through

- Block 1: FitSnack - implement the empty `ViewModels/` layer wired to the mock services. Re-establish build momentum on the new #2 bet.
- Block 2: AR - respond to post #1 engagement, chase interview replies; confirm the per-PR E7 tripwire + weekly escalation sweep run green on `main` (carried from 6/24).
- Job search: 1 app + finalize the two behavioral answers with real Omdena/Zebra metrics (carried blocker since 6/18).

### Wednesday 7/1 - Post #2 draft (and evals-as-edge, priority #4)

- Block 1: Draft flagship post #2 (leak-eval suite / CI-gate rigor) from `docs/evals.md`. Cite concrete shipped material: the -0.51 recall@5 regression catch, the E7 false-resolve gate (PRs #27-30), and the #30 mislabel-ratio guard. This is your evals edge expressed, not a separate track.
- Block 2: FitSnack - start the deterministic engine (Epic C): session shape + pillar balance, test-first.

### Thursday 7/2 - FitSnack engine + interviews

- Block 1: FitSnack engine continued (Epic C): movement-pattern focus + filter pool, test-first.
- Block 2: Run any booked buyer interviews (log findings); otherwise more outreach. Fresh-read polish on post #2, ready to ship.

### Friday 7/3 - Ship post #2 + weekly closeout

- Block 1: Publish flagship post #2, route to the waitlist CTA.
- Block 2: FitSnack buffer (engine progression-chain / adaptive overload, or catch-up). Then weekly closeout: log interview findings, update `current-priorities.md` if focus shifted, plan the following week.
- Job search: 1 app (reaches 5/week).

### Sat 7/4 / Sun 7/5

Holiday and rest.
Optional: reply to post engagement; light planning Sunday.

## Weekly targets (the deliverables)

- [ ] Post #1 published, Tally waitlist live, CTA wired
- [ ] 3 buyer interviews booked (run whatever gets scheduled)
- [ ] Post #2 drafted and published
- [ ] FitSnack: ViewModels done + deterministic engine started (Epic C, with tests)
- [ ] 5 job applications submitted
- [ ] Behavioral answers finalized with real metrics
- [ ] Weekly closeout + next-week plan

## Balance note

Weighted ~45% Agentic RAG validation / ~30% FitSnack build / ~25% job search + admin.
This deliberately keeps Agentic RAG validation ahead of FitSnack, because the daily logs flag the validation gate as the actual income blocker.
Rebalance toward the FitSnack build if the priority for the week shifts to getting the engine done.
