# X — launch content

Per the brief, the outage story runs first.
Every number's denominator is in the same post as the number.
Claims used: C3, C4, C5, C6, C7, C9, C24, C26, C27 (`launch/CLAIMS.md`).

## Thread 1 — the failure that mattered (run first)

**1/**
For 42 days, our RAG benchmark measured 0.000.

The table in our README stayed green the whole time.

The alarm fired every night.

This is the most useful failure we've ever shipped. Thread:

**2/**
The benchmark: permissions-aware retrieval at scale.
10,000 chunks, three viewers who can see 50% / 10% / 1% of the corpus, recall@5 across an HNSW ef_search sweep.

The point is to catch the day the query planner starts trading recall for speed under selective ACL filters.

**3/**
On 2026-06-19 a seeding defect landed: the eval's viewer accounts lost their workspace membership rows.

Our tenant-isolation clause did exactly its job — it hid the entire corpus from them.

Every cell of the benchmark: a real, measured 0.000. For 42 straight nights.

**4/**
So why did the README stay green?

The table there was hand-transcribed from an earlier run. The nightly runner died before rewriting its summary, then republished the stale checked-in table verbatim — for 18 days before the zeros even started.

Nothing automated refreshed the number people actually read.

**5/**
Here's the part that matters: the failure wasn't the zeros.

The zeros were correct! The security boundary held so hard it blinded our own eval.

The failure was that "we measured nothing" could be published wearing the same clothes as "we measured 1.000."

**6/**
The fix, shipped 2026-07-31:

- a run with no signal publishes a DEGENERATE RUN notice, never a table
- an empty gold set raises a hard error naming the question — the metrics refuse to return 0.0
- a weekly with no snapshot is a third state: UNMEASURED. Failed job + filed issue. Never green.

**7/**
And because the edit that must never escape a guard is the edit that weakens it:

the guards themselves are pinned by an offline CI job that runs on every PR touching them.

**8/**
Since the fix, the benchmark re-measures all-1.000 nightly (15 multi-hop queries, 10k chunks — and yes, 1.000 is *expected* there: the planner sidesteps HNSW at that size. The table exists to catch the day that changes).

The whole story is in the README, dates and all. We left it there on purpose.

**9/**
If you're putting RAG in a multi-user product, the question isn't "is your table green."

It's "what does your harness do when it measures nothing."

Purvia is a permissions-aware RAG platform, MIT-licensed, with this harness in the box:
https://github.com/hcho22/Purvia

## Post 2 — the staged regression (run 2-3 days later)

We once broke our own retrieval on purpose.

A one-line change (chunk size 500 → 100) on a throwaway PR.

CI ran the 50-question eval on PR-head and main, and posted the red table in 4 minutes: recall@5 −0.510, MRR −0.578, no human involved.

The cause was contrived. The catch was not.

github.com/hcho22/Purvia — docs/evals.md §4 has the actual PR comment.

## Post 3 — the harness caught us too (run ~1 week in)

Our own hybrid retrieval was losing to its plain vector leg.

Keyword recall@5: 0.140. On paraphrase questions: 0.000. Strict AND matching zeroed any query with one word missing from the chunk.

The nightly made it undeniable, so we fixed it (OR-fallback + per-query fusion weights) and the same harness measured the fix: paraphrase 0.800, exact-token 1.000, hybrid recall@5 ≥ vector in every category (60-question set, demo corpus — and it still shows hybrid trailing vector on paraphrase MRR, 0.767 vs 1.000, because the harness keeps score on us either way).

We're not selling you hybrid retrieval. We're selling the harness that refused to let us believe in ours.

## Post 4 — who should not buy (run ~10 days in)

Reasons NOT to use Purvia:

- you need owner/editor/viewer tiers (every grant is read access)
- you need nested groups (flat in v0)
- you need proven recall at 100k+ visible chunks (instrumented, unmeasured)
- you want to search your Slack/Drive (buy Onyx — no connectors here)
- you want a hosted service (it's a codebase)

Still here? github.com/hcho22/Purvia

## Reply-guy kit (prepared answers)

- "60 questions is tiny" → Yes, and the README says so above the table. The denominator is small; the discipline isn't: cold-seed re-proof on every PR, gates with no off switch, vacuous passes refused.
- "It failed 42 days, why trust you" → The predicate never leaked; the reporting failed and the alarm fired nightly. Now "measured nothing" is unpublishable. What does your eval do when it measures nothing?
- "Just use Onyx" → Different job: Onyx = internal search over SaaS tools, permission inheritance in the Enterprise Edition. Purvia = the predicate inside the product you're building, MIT.
