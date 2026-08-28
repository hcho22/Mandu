# THESIS.md - the falsifiable bet and its kill criteria

## The claim

Engineers adding RAG to a multi-user product will pay **$199 one-time** for a permissions-aware RAG codebase whose security property is enforced in the SQL predicate and **proved by a shipped eval harness**, because their current alternatives are:
(a) a DIY RLS pattern guide with no proof harness (Supabase docs, fetched),
(b) an internal-search product that paywalls permission-aware retrieval (Onyx EE, fetched), or
(c) a general framework whose abstractions they already distrust (framework-complaint corpus, `checkpoints/phase1-research.md`).

The lead asset is the failure story: 42 days of measured 0.000 under a green table, alarm firing, publicly documented with the fix (`README.md:41-77`).
The bet is that first-person measured failure converts engineer trust better than any all-green table.

## What would prove it false (kill criteria, each actionable within one week)

Run the X thread (failure story first, per the brief) plus the site, then measure 7 days:

1. **Attention floor.** The failure-story thread fails to reach 20k impressions or 50 meaningful engineer replies/reposts combined across X + HN (if cross-posted).
   Kill action: the story-led angle is wrong; re-run the tournament with angle A (predicate-first) as lead, spending nothing new.
2. **Intent floor.** Fewer than 30 email signups (waitlist/preorder) from the first 500 unique site visitors (6% conversion).
   Kill action: keep the free core public, kill the paid tier, and reposition Purvia as a portfolio/credibility asset rather than a product this quarter.
3. **Wrong-buyer signal.** Among the first 10 substantive inbound conversations, 5 or more ask primarily for SaaS connectors (Slack/Drive/Confluence) rather than in-product retrieval.
   Kill action: the market is pulling toward internal search, where Onyx wins; do not chase - either narrow to the support-widget wedge as the commercial face (revisiting ADR-0011's scoping *for marketing*, not naming) or shelve commercialization.
4. **Preorder floor.** Zero paid preorders in week one despite >= 30 signups.
   Kill action: price is not the issue at $199 vs $449 comps; the paid boundary (adoption pack) is unwanted - fold Pro into a "pay what you want" support tier and test once more for a week, then stop.

Any one tripwire firing forces its kill action; two or more firing kills the paid-tier plan entirely this quarter.
These thresholds are set from the verified comp market (ShipFast/Pegasus operate profitably at these price points with engineer audiences) and from the size of the reachable audience being zero-spend organic only.

## What this thesis is not

- Not a venture pitch: no TAM, no growth story, no hosted roadmap. The instrument is a one-time-priced kit and the decision horizon is one week of organic signal.
- Not a security guarantee: the product's own docs cap the claim ("weaker proof ... not proven", `docs/golden-set-authoring.md:211-229`); the thesis sells the discipline, not a certification.
