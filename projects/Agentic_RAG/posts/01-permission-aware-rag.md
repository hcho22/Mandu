---
post: 1 of 2 (flagship)
title: The per-user sharing trap that silently breaks RAG retrieval
source: docs/permissions-aware-rag.md
status: ready to publish — CTA wired to live waitlist (https://tally.so/r/vGbO0A). Pick channel: LinkedIn / dev.to / Substack / repo README
audience: agency and freelance AI developers shipping client RAG features
target_length: ~1100 words
---

# The per-user sharing trap that silently breaks RAG retrieval

You sold a client "chat with your docs." It demos well. Then they ask the
obvious next thing: "Can sales see only the sales folder, and support only
the support folder?" Per-user document sharing. You add it the way almost
everyone adds it first, and you ship.

That version is broken. It will pass your demo and fail in production, and
the failure is invisible until a user with restricted access quietly stops
getting good answers. Here is the trap, why it happens, and the fix, with
the eval numbers that prove the fix holds.

## The trap: post-filtering kills recall

The natural way to add sharing is to leave retrieval alone and filter the
results: pull the top-k most similar chunks, then drop the ones this viewer
is not allowed to see. Retrieval stays simple, permissions live in one
place. Clean.

The problem is recall collapse on viewers with sparse permissions. The math
is unforgiving. If a viewer can see 5% of the corpus and you fetch the top
10 chunks, the expected number of *visible* chunks in that result set is:

    E[visible | top-k] = k x selectivity = 10 x 0.05 = 0.5

Half a chunk, on average. Most of the time that viewer gets back zero
relevant chunks. Sometimes one. Any question that needs two chunks to
answer is effectively unanswerable. The model then does what models do with
thin context: it guesses, and your client's restricted users get worse
answers than everyone else with no error message to explain why.

"Fetch more and filter harder" does not save you. At 5% selectivity you
would need the top 100 candidates to expect five visible chunks back, and
once you post-filter the top 100, embedding distance is no longer ranking
the *visible* chunks against each other. You have thrown away the ranking
that made retrieval work.

## The fix: push the permission check into the query

The correct move is to filter *before* ranking, not after. Put the
permission predicate inside the SQL query so the database is choosing among
chunks this viewer can actually see from the start. The ranking then
operates on the visible set, which is what you wanted all along.

In a Postgres + pgvector setup the retrieval function goes from a similarity
filter to a similarity filter AND-ed with an access check:

```sql
where c.embedding is not null
  and (1 - (c.embedding <=> query_embedding)) >= match_threshold
  and (
    c.user_id = auth.uid()                      -- owner
    or exists (                                  -- or explicitly granted
      select 1 from chunk_acl ca
      where ca.chunk_id = c.id
        and ( (ca.principal_type = 'user'  and ca.principal_id = auth.uid())
           or (ca.principal_type = 'group' and ca.principal_id in (
                 select principal_id from principal_membership
                 where member_user_id = auth.uid())) )
    )
  )
```

Two design choices that matter in practice:

- **Access lists are additive to ownership.** A chunk's owner always sees
  it; grants only ever add viewers. An existing single-user corpus keeps
  working with zero backfill the day you turn sharing on.
- **One source of truth for grants.** Sharing a document writes one access
  row per chunk rather than a separate "intent" table that you reconcile
  later. Grants cost more storage, but the retrieval predicate stays one
  join shallower, and the retrieval predicate is the hottest query in the
  system. Trade storage for read latency, every time.

## The part most write-ups skip: it interacts with your vector index

Pre-filtering is correct, but it has a sharp edge with HNSW, the default
pgvector index. HNSW is a proximity graph the query walks greedily toward
your vector. When a selective permission filter rejects most candidates the
walk sees, the walk can burn its search budget without finding enough
visible chunks, and its stop condition looks at *all* visited candidates,
not just the visible ones, so it can halt before reaching the region that
actually matters.

The honest version of this story, which is the whole point: at small and
mid corpus sizes this does not even fire. The Postgres planner is not naive.
When the visible set is small in absolute terms, the planner skips HNSW
entirely, grabs the visible chunk IDs by index, sorts those exactly by
distance, and returns the top k. I confirmed this with `EXPLAIN ANALYZE` on
a 10,000-chunk corpus: no HNSW walk, exact nearest-neighbor over the
filtered set, every recall cell at 1.000. The collapse only appears when the
visible set is large in absolute terms but small relative to the corpus,
which is a 100k+ scale question. I shipped the benchmark harness and a
regression alarm so the day a workload crosses that line, the curve shows up
in the table and the nightly fails loudly, instead of a user finding it for
me.

## Proving it, not asserting it

A security property you cannot measure is a security property you do not
have. The correctness eval runs 50 questions across three retrieval modes
and three viewer setups, scoring two things:

- **Leakage:** the fraction of restricted-viewer runs that returned any
  chunk they were not allowed to see. Pre-filter and post-filter both score
  **0 gold chunks leaked**, every mode. The pre-filter row is the
  load-bearing one, because post-filter can still leak through side channels
  like timing or payload size.
- **Non-regression:** full-access recall@5 holds at **0.86** (vector and
  hybrid) against the prior baseline, so adding permissions did not quietly
  degrade retrieval for everyone else.

That second number is the one that separates "it works in the demo" from "I
can tell my client exactly what this system does and does not do." When the
client asks "are you sure restricted users can't see the CEO's folder," the
answer is a number from a test that runs on every pull request, not a
shrug.

## Why this is the differentiator

Most RAG tutorials stop at "embed, retrieve, generate." The hard part of a
production client deliverable is everything after the demo: access
correctness, the index interaction, and the evals that let you make a
defensible promise. I spent ten years in hardware validation before moving
into AI, and that is the rigor I am building into this.

This write-up is the first deep-dive from a permission-aware RAG + AI
support starter kit I am building in public: one engine, two faces (internal
"chat with your docs" and a customer-facing support deflection layer),
proven by runnable evals, with no framework lock-in. It is for the agency
and freelance developer who sold a client an AI feature and needs to ship it
defensibly.

If that is you, I want to talk to you before I build more of it.

I am building this as a starter kit so you do not have to solve the
permission-and-eval problem from scratch on your next client deliverable.
It is early and I am building it in public. If you ship client AI features,
join the waitlist and tell me what would actually save you time:
**https://tally.so/r/vGbO0A**

<!-- CTA = Variant A (waitlist-cta.md). At publish time, append the per-channel
     source tag to the link so signups are attributed:
       LinkedIn:  https://tally.so/r/vGbO0A?source=linkedin
       dev.to:    https://tally.so/r/vGbO0A?source=devto
       Reddit:    https://tally.so/r/vGbO0A?source=reddit
     Keep the bare link in this canonical source. -->

---

Next post in the series: the leak-eval suite, how the CI gate caught a
-0.51 recall@5 regression from a one-line chunk-size change before it
shipped.
