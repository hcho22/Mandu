# Video scripts (X/LinkedIn native video)

## Why scripts and not footage

The brief allows video only from real captured footage.
Real footage requires the full local stack (Supabase Docker + backend + frontend, seeded corpus, two user accounts) running in a recordable session; this run's environment did not include a live deployment to capture, and fabricating UI shots would violate the invent-nothing rule.
Decision logged here and in `launch/DECISIONS.md` (D12): ship the scripts + shot lists; the captain records against a locally-running stack per README "Local development" when convenient.
Everything needed to record is specified; nothing visual is faked in the meantime.

## Script A - 60s talking-head + screen ("the failure that mattered")

> [Face, 5s] For forty-two days, our benchmark measured zero point zero zero zero - and our README stayed green.
> [Screen: README table, 10s] This is a permissions-aware RAG platform. This table says a viewer with no access retrieves nothing - one point zero, every cell.
> [Screen: outage paragraph, 15s] In June, a seeding bug removed our eval users' workspace memberships. The tenant boundary hid the entire corpus from them - so the benchmark measured a real zero, for forty-two nights, while the alarm fired and this hand-copied table never updated.
> [Face, 10s] The zeros weren't the failure. The reporting was. "We measured nothing" could be published looking exactly like "we measured everything."
> [Screen: DEGENERATE RUN output + guard test, 12s] Now a run that measures nothing refuses to publish. An empty gold set is a hard error. A missing weekly snapshot is its own state: unmeasured. And CI pins the guards themselves.
> [Face, 8s] The whole story is in the README, with dates. If you're building RAG into a multi-user product - that's the question to ask any eval: what happens when it measures nothing?

## Script B - 45s pure screen capture ("grant, retrieve, badge")

> [Two browsers side by side] Same question, two users. The left one owns the document - answer, with a badge: via owner.
> The right one was never granted it. Watch the retrieval - the chunk isn't ranked and then dropped; it's never a candidate. The ACL check is inside the SQL predicate, under her JWT.
> [Share dialog] Grant her the document. Ask again. Answer - and the badge says exactly why: via direct grant.
> [Terminal: eval run] And this property isn't a demo trick - it's the thing our eval hard-fails CI on, sixty questions, three modes, three viewers, every PR.
