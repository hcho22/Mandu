# Phase gates and exit criteria

Each phase closes only when its mechanical gates pass (`scripts/journal.py pass <gate>`, which runs the checks named here) and its completeness critic (`workflows/critic.js`) says PASS against the criteria below.
Pass the critic each phase's list, item by item, as its `criteria`.
A critic's report must be newer than the latest pass of each of the phase's work gates, first pass or re-pass.
Re-passing a work gate re-runs its checks and records the time it passed again, so a fix re-gated after the critic ran makes that phase's critic gate fail until the critic runs again.
The `package` gate re-checks the critics of phases 1 to 4 that way, and `journal.py complete` re-checks all five.

A gate a later phase sends back is reopened (`journal.py reopen <gate> --reason "<why>"`): it keeps its record, counts as not passed, and passes again in order, with the same checks, before any later gate; reopening a work gate reopens its phase's critic too.
A name-only rerun reopens the tournament and every later passed gate, and refuses every gate after the tournament until the Founder hands over a shortlisted name App Store Connect accepted; after the hand-over swaps it through the package, the reopened gates pass again in order.
After the swap (the journal's `rename.stage` is `swapped`), add this criterion to every phase's list: the phase fails while any of its deliverables or renders, or the naming decision, still presents the earlier name as the brand; a record of what was found, judged, or decided under the earlier name (the records `scripts/rename.py` lists, the naming decision aside) may still name it, as the earlier name.
The `brand` gate also refuses a fresh-agent gate report and a naming decision older than the hand-over (`rename.accepted_at`), and the `launch-set` and `video` gates refuse any Launch Set image and the walkthrough video older than it.
See "Name-only rerun" in `SKILL.md`.

## Read the product

Gate `product-facts`: `01-research/product-facts-brief.md` exists and cites the repository with at least five `repo:` paths; `decisions-log.md` and `sources.md` exist.

## Phase 1: market the brand

Gates: `research` (at least three competitor teardowns, `pain-points.md`, and the source check passes), `tournament` (four pitches, three judges, three published rubrics, a scorecard with margins), `brand` (positioning, naming verdict with clearance UNVERIFIED, brand guidelines, a passed fresh-agent gate with its asset, the channel plan, the thesis), `claims-1` (the claim audit passes, ledger included), `critic-1`.

Exit criteria:

1. The product-facts brief states every non-negotiable product fact with its `repo:` source, the Product's real state (users, revenue, listing, price, name), and the Founder's held decisions.
2. Research ran in parallel lanes by source and angle, including the Product's named competitors, competitors the records do not name, store reviews, Reddit or other communities through last30days, category economics, channels, creators, and name collisions; every gap a lane reported is closed or stated.
3. Each competitor is reverse engineered: positioning in its own words, pages, pricing, store listing, and recurring complaints, each with a fetched URL.
4. The pain corpus ranks pains by independent sources, quotes people word for word with URLs, and labels confidence.
5. The tournament had at least four blind pitches, one arguing against the brief's riskiest lead at full strength, and at least three judges with published, differing rubrics; the scorecard shows every pitch, the losers' reasons, and the margins, and the naming verdict follows the judges, not incumbency.
6. Positioning states the verdict first, the ICP in their own words, the messaging hierarchy, and a competitive map showing the quadrant no competitor owns.
7. Every naming document and the recap say trademark and App Store name clearance are UNVERIFIED and are the Founder's next action.
8. The brand guidelines are complete (logo concept as SVG, hex palette, type scale, voice, do and don't), and a fresh agent given only them made an on-brand asset; every failed round and what it fixed is in the report.
9. The channel plan ranks channels for $0 and no audience and again for $500 a month, each with reasoning, cost assumption, 90-day signal, and kill criterion, gives a plain verdict on spending, and answers paid versus organic first signal with fetched sources.
10. The price is sourced against competitors and labeled `[PROPOSAL]` where the Founder holds it.
11. The thesis has what must be true, what to expect in 90 days, explicit kill criteria, and the observation that should make someone walk away.
12. Every load-bearing claim is in the ledger with a skeptic verdict, refuted claims are gone, and weakened ones are reworded.

## Phase 2: landing page

Gates: `site` (two variants, screenshots at 390x844 and 1440x900, no horizontal overflow, an inspection note per screenshot, the event list), `critic-2`.

1. The page runs locally with a one-line command in the README and is static.
2. Its copy names the pain state and the outcome literally, in the ICP's words.
3. It is credible with zero social proof and holds none: no counts, ratings, quotes, or logos.
4. Every factual claim links out to a fetched source.
5. Two hero variants match the top two positioning angles.
6. The Waitlist form asks the Product's Fit question and has no live backend.
7. Structured data holds no ratings or reviews; the AI-search and conversion reviews are written and acted on.
8. Both variants were captured at both widths, every capture was viewed, and the layout holds at both.
9. The event and metric list defines the events from install to paying, with no tracking installed and no warehouse.

## Phase 3: social

Gates: `test-kit` (the layout check over the Test Kit and brand rules), `launch-set` (the manifest, the sizes, the brand lint), `video` (ffprobe facts, five viewed frames, the strip, the audio stated), `critic-3`.

1. The Test Kit has at least 15 distinct Angles spanning the top pains, each tracing to a pain's URL, with at least one deliberately contrarian Angle and one that argues against the category's consensus the Product opposes.
2. Every A/B pair changes only the Hook.
3. Platforms are TikTok and YouTube Shorts, with the reasoning against the ICP.
4. The 14-day cadence has a mid-point review and explicit kill and double-down rules, and every success signal is measurable at zero followers.
5. The read-the-results guide says what a win looks like at zero followers, what is noise, and which result should change the product rather than the copy, and states where the sample is too small to conclude anything.
6. Week-1 drafts are ready to post, with on-screen text and shot lists, and no fabricated engagement.
7. The Launch Set covers Instagram, X, and TikTok: profile image, banner where the platform has one, bio, and first-week posts, each at the size the platform's fetched help page gives.
8. The walkthrough video shows real screens only, its script matches its frames, and its gate report describes each frame as viewed.
9. Every simulator the run started is shut down.
10. A creator shortlist was vetted with the influencer-marketing checklist.

## Phase 4: break it

Gates: `red-team` (four persona reports, a dossier with material changes before and after, surviving objections, the pre-publication checklist), `critic-4`.

1. Every persona read every deliverable a stranger would see, social drafts included.
2. Every MUST-FIX finding is fixed, and every declined SHOULD-FIX says why.
3. At least one material change is recorded with its before and after.
4. Surviving objections ship visibly, strongest first, each with the package's best answer.
5. Claims the fixes touched were re-verified, and screenshots and video were re-gated where their content changed.
6. The copy-editing sweep ran across every copy file.
7. The pre-publication checklist lists every act the Founder must do or confirm before anything goes public.

## Phase 5: package

Gates: `package` (every check: sources, claims, layout with the Handoff entry written, brand lint, site, Launch Set, video, recap; the README, self-grade, launch checklist, and Handoff README; no simulator left), `critic-5`.

1. Extras were chosen by "which make this company feel most real, different, and creative to a stranger", and the dropped ones are named with reasons.
2. At least one deliverable nobody would ask for exists and is finished work.
3. The recap explains the business in under five minutes, states the naming verdict with clearance UNVERIFIED, puts the thesis beside the strongest surviving objection, logs the orchestration topology, maps every deliverable, and ends with the package's Handoff line, or, beside a live package, says why there is none yet.
4. Nothing is a placeholder pretending to be finished; a stub is labeled a stub in the recap.
5. The self-grade is honest, including what failed and why it was kept.
6. The run audit shows no question asked and nothing published.

## Self-grade

`self-grade.md` answers each line, with what was not fixed and why:

- No spend, no publication, nothing live, no account touched.
- Every factual claim has a URL fetched in this run; `sources.md` is complete; no dead links.
- Zero fabricated stats, users, quotes, testimonials, engagement, or social proof, in mockups and social drafts too.
- Every guess is labeled with its reasoning.
- No claim the category forbids, and every line passes the derived voice rules.
- Naming carries the clearance-UNVERIFIED caveat everywhere.
- Nothing contradicts the product facts.
- The contrarian pitch was argued at full strength and scored, not strawmanned.
- The site was verified at both widths, with screenshots in the package, and names the pain state.
- The video has its ffprobe report and frame strip, and its script passes the voice rules.
- The brand guidelines passed the fresh-agent test, and the test asset ships.
- The Test Kit has 15 or more distinct Angles, hook-only pairs, pre-registered signals, and honest sample-size limits, and parses as gr0wthlab reads it.
- The channel plan commits to a ranking and answers paid versus organic with citations.
- The red team ran, something changed because of it, and surviving objections are visible.
- The recap links everything and every link resolves.
- Every simulator the run started is shut down.
