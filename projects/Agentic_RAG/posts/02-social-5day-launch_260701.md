---
purpose: 5-day X/Twitter + Reddit launch campaign for flagship post #1 (permission-aware RAG)
source: posts/01-permission-aware-rag.md
status: live - running; Day 1-2 posted 2026-07-07, Day 3 X thread posted 2026-07-08 (r/LocalLLaMA pending), Days 4-5 pending
audience: agency / freelance AI developers shipping client RAG features
cta_dependency: waitlist link (Tally) must be live before Day 4-5 CTAs go out
research_refresh: 2026-07-01 (last30days scan of "AI Chatbot" across Reddit, YouTube, and web; see "Current signal" section)
---

# 5-Day Launch Campaign: The Per-User Sharing Trap

Turns flagship post #1 into a daily X thread arc plus spaced Reddit teardowns.
The narrative climbs: problem -> fix -> the nuance nobody covers -> proof -> the pitch.

## Rules of the road

**X/Twitter**
- One thread per day, one idea per thread. Tweets written to fit the 280-char free limit; if you have Premium, merge adjacent tweets freely.
- No hashtag soup. At most one tag (#RAG) and only where natural.
- Numbering uses `1/`, `2/`. The last tweet of each day teases tomorrow to build a follow habit.
- The waitlist link goes ONLY in Day 5 (and optionally pinned as a reply on earlier days). Do not sell before you have given value.

**Reddit**
- Value-first, no link in the post body. If someone asks in comments, drop the waitlist link there. This is the difference between "useful" and "removed by mod."
- One post per subreddit, spaced out. Do NOT cross-post the same text to five subs the same day.
- Tailor the title per sub. Reddit titles are the whole game.
- Be present in the comments for the first 2 hours - that is where traction is won.
- Recommended subs: r/Rag (Day 1), r/LocalLLaMA (Day 3), optional r/SideProject (Day 5). Skip r/MachineLearning (too academic for this) and be cautious in r/LangChain (the "no framework lock-in" angle can read as a shot).

**CTA dependency:** Days 4-5 need the Tally waitlist link live. Stand that up first (see `waitlist-cta.md`). Until then, Days 1-3 run link-free with no problem.

---

## Current signal (researched 2026-07-01, last 30 days)

Fresh signal from a last-30-days scan (Reddit, YouTube, and web) to keep this campaign timely rather than evergreen.
Weave these into threads and, especially, into Reddit comment replies, where specifics win traction.

**The premise is now consensus language, not a hot take.**
The 2026 security write-ups describe the exact failure this campaign is about: vector databases flatten permission hierarchies during embedding and do not inherit source-system ACLs (Google Drive, SharePoint), so restricted documents get served to users who were never authorized to see them.
That is the same "post-filter kills recall, pre-filter is the fix" story told from the security side.
Use their framing ("vector stores don't inherit your source permissions") as a bridge into the recall-math argument.

**The leak failure mode is no longer hypothetical - name real 2026 incidents.**
EchoLeak (Microsoft 365 Copilot) was a zero-click prompt injection that silently exfiltrated enterprise data.
Slack AI leaked data through a poisoned "knowledge" item planted in a public channel.
Support-ticket archives fed into RAG have surfaced other customers' emails and pasted login tokens in answers to unrelated users.
A new attack class, Agentjacking, hit coding agents at a reported ~85% exploitation rate across 2,388 organizations.
These make the Day 4 line ("are you SURE restricted users can't see the CEO's folder?") concrete; naming one turns an abstract risk into a headline the buyer already fears.

**The buyer and the timing are real.**
Gartner projects 70% of companies will run RAG bots in customer or internal systems by 2026, and practitioners report the integration layer is 40-60% of the total build effort, which is exactly the "everything after the demo" work this kit sells.
Per-organization vector-space isolation is now the named best-practice pattern for multi-tenant and regulated clients, which is the workspace-isolation layer on the roadmap.

**Production-RAG vocabulary, to match how builders actually talk (Day 2-3).**
The recurring production failures people cite are bad chunking, limited recall, missing re-ranking, and embedding drift, plus the eval gap: final-answer quality alone is not enough, you need separate retrieval and generation metrics, realistic test sets, and ongoing monitoring.
That last point is the strongest external validation of the Day 4 eval angle - use it.

**The public mood is about trust, and permission is part of that conversation.**
Oprah's "The Dark Side of AI Chatbots" cleared 2.1M views in June, and r/artificial's "So now scraping data without permission is bad for AI training all of sudden?" pulled 747 upvotes; the consent-and-permission theme is live and emotionally charged right now.
r/Chatbots is running recurring "do people trust AI more than humans?" threads.
The wider anxiety is trust; permission-aware retrieval is a concrete, technical answer to "can I trust what this thing shows people?"

**Model-share context, if a thread needs a scene-setter.**
June 2026 share of AI-chatbot web visits: ChatGPT 54.7% (down from 76.5%), Gemini 27.4% (up 104% in six months), Claude 8.2% (up 306% in a quarter).
The market is still forming, which supports the "ship client AI defensibly now" urgency without needing to pick a model.

### Where each finding strengthens the arc

- Day 1: bridge in the security framing ("vector stores don't inherit your source permissions") before the recall math.
- Day 3-4: name a real 2026 incident (EchoLeak or Slack AI) as proof the leak is real, not a thought experiment.
- Day 4: cite the "final-answer quality alone is not enough" consensus as outside validation of separate retrieval and generation evals.
- Day 5: lead the urgency with Gartner's 70%-by-2026 and the 40-60% integration-effort stat; the kit sells that 40-60%.

---

## DAY 1 - The hook (the silent bug)

### X thread

**1/**
You sold a client "chat with your docs." It demos great.
Then they ask the obvious thing: "can sales see only the sales folder, support only the support folder?"
You add per-user filtering the way everyone does first. You just shipped a silent bug.

**2/**
The natural fix: leave retrieval alone, pull the top-k chunks, then drop the ones this viewer can't see.
Clean. Permissions live in one place.
It fails in production, and the failure is invisible.

**3/**
Here's the math. Say a viewer can see 5% of the corpus and you fetch the top 10 chunks.
Expected visible chunks in that result:
10 x 0.05 = 0.5
Half a chunk. On average that user gets back ZERO relevant context.

**4/**
Any question that needs 2 chunks to answer is now unanswerable for them.
The model does what models do with thin context: it guesses.
Your client's restricted users get worse answers than everyone else, with no error to explain why.

**5/**
"Just fetch more and filter harder" doesn't save you.
At 5% selectivity you'd need the top 100 candidates to expect 5 visible chunks back.
Post-filter the top 100 and embedding distance is no longer ranking the visible chunks. You threw the ranking away.

**6/**
This is the per-user sharing trap: post-filtering kills recall for exactly the users you added permissions for.
The fix is to filter BEFORE ranking, not after. Breaking that down tomorrow.
(Building a permission-aware RAG starter kit in public - follow along.)

**Optional timely hook (swap into 1/, or drop as a pinned reply):**
The 2026 security writeups have a name for this now: your vector database doesn't inherit your source permissions.
Embed a SharePoint or Google Drive folder and the access list doesn't come with it. Same silent bug, told from the security side.

### Reddit - r/Rag

**Title:** The per-user sharing "fix" everyone ships first silently kills RAG recall (here's the math)

**Body:**

If you have added per-user document permissions to a RAG system, there is a good chance you did it the way I first did, and there is a good chance it is quietly broken.

The natural approach: leave retrieval alone, pull the top-k most similar chunks, then drop the ones the current viewer is not allowed to see. Retrieval stays simple, permissions live in one place. It passes every demo.

The problem is recall collapse for viewers with sparse permissions. If a viewer can see 5% of the corpus and you fetch the top 10 chunks, the expected number of visible chunks you get back is:

    10 x 0.05 = 0.5

Half a chunk on average. Most of the time that viewer gets zero relevant context, sometimes one chunk. Any question that needs two chunks to answer is effectively unanswerable for them. The model fills the gap by guessing, and your restricted users get worse answers than everyone else with no error message to explain why.

"Fetch more and filter harder" does not save you. At 5% selectivity you would need the top 100 candidates to expect 5 visible chunks back, and once you post-filter the top 100, embedding distance is no longer ranking the visible chunks against each other. You have thrown away the ranking that made retrieval work in the first place.

The fix is to filter before ranking instead of after: push the permission predicate into the query so the database only ever ranks chunks the viewer can actually see. I will follow up with the SQL and the index gotcha (HNSW has a sharp edge here), but I wanted to start with the failure mode because it is so easy to ship without noticing.

Curious how others here have handled per-user ACLs in retrieval. Pre-filter in the query, a metadata filter in the vector store, row-level security, something else?

---

## DAY 2 - The fix (filter before ranking)

### X thread

**1/**
Yesterday: adding per-user permissions by post-filtering the top-k silently destroys recall for restricted users.
(10 x 5% = 0.5 visible chunks on average.)
Today: the fix. Filter BEFORE ranking, not after.

**2/**
Put the permission predicate INSIDE the query.
Let the database choose only among chunks this viewer can actually see, then rank that visible set.
In Postgres + pgvector, that's a similarity filter AND-ed with an access check.

**3/**
Shape of it:

```sql
where (1 - (c.embedding <=> query_embedding)) >= match_threshold
  and (
    c.user_id = auth.uid()            -- owner
    or exists (                        -- or explicitly granted
      select 1 from chunk_acl ca
      where ca.chunk_id = c.id and ca.principal_id = auth.uid()
    )
  )
```

**4/**
Design call #1: access is additive to ownership.
The owner always sees their chunk; grants only ever ADD viewers.
An existing single-user corpus keeps working with zero backfill the day you turn sharing on.

**5/**
Design call #2: one source of truth for grants.
Sharing a doc writes one ACL row per chunk, not a separate "intent" table you reconcile later.
Costs storage, keeps the retrieval predicate one join shallower. That predicate is your hottest query - trade storage for read latency every time.

**6/**
Now ranking operates on the visible set, which is what you wanted all along. Recall stops collapsing.
But there's a sharp edge with your vector index that most write-ups skip.
That's tomorrow, and it's the interesting one.

---

## DAY 3 - The nuance nobody covers (HNSW)

### X thread

**1/**
The part most "add permissions to RAG" posts skip:
pre-filtering is correct, but it interacts with your vector index.
Specifically HNSW, the pgvector default. Here's the sharp edge.

**2/**
HNSW is a proximity graph. The query walks it greedily toward your vector.
When a selective permission filter rejects most of the candidates the walk sees, it can burn its search budget without finding enough visible chunks.

**3/**
Worse: its stop condition looks at ALL visited candidates, not just the visible ones.
So it can halt before reaching the region that actually matters for this viewer.
Recall drops for filtered users again, for a totally different reason than Day 1.

**4/**
Here's the honest version, which is the whole point:
at small and mid corpus sizes this does not even fire.
The Postgres planner is not naive.

**5/**
When the visible set is small in absolute terms, the planner skips HNSW entirely: grabs the visible chunk IDs by index, sorts those exactly by distance, returns the top k.
EXPLAIN ANALYZE on a 10k-chunk corpus: no HNSW walk, exact nearest-neighbor, every recall cell 1.000.

**6/**
The collapse only shows up when the visible set is large in absolute terms but small relative to the corpus - a 100k+ scale question.
So I shipped a benchmark harness and a regression alarm. The day a workload crosses that line, the nightly fails loudly instead of a user finding it for me.

**7/**
Measuring the failure instead of asserting it won't happen is the whole game.
Tomorrow: the eval numbers that let me make a promise to a client.

### Reddit - r/LocalLLaMA

**Title:** Permission-filtered retrieval on pgvector has an HNSW gotcha at scale - here's when it bites and when the planner saves you

**Body:**

Sharing a pgvector detail that cost me some time and that I have not seen written up clearly.

Context: I am building permission-aware RAG, where each viewer can only retrieve chunks they are allowed to see. The correct approach is to pre-filter (put the access check inside the query so ranking only ever operates on the visible set) rather than post-filter the top-k, which collapses recall for restricted users. That part is well understood once you see the math.

The part that surprised me is the interaction with HNSW, the default pgvector index. HNSW is a proximity graph that the query walks greedily toward the query vector. When a selective permission filter rejects most of the candidates the walk encounters, two things happen: the walk can exhaust its search budget before it collects enough visible chunks, and its stop condition considers all visited candidates rather than only the visible ones, so it can halt before reaching the region that matters for this viewer. Net effect: recall silently degrades for filtered viewers at scale.

The honest part: at small and mid corpus sizes this does not fire at all. The Postgres planner is smart about it. When the visible set is small in absolute terms, it skips the HNSW walk entirely, pulls the visible chunk IDs by index, sorts them exactly by distance, and returns the top k. I confirmed with EXPLAIN ANALYZE on a 10k-chunk corpus: no HNSW walk, exact nearest-neighbor over the filtered set, recall at 1.000 across the board.

The collapse only appears when the visible set is large in absolute terms but small relative to the corpus, which is a 100k+ chunk question. So rather than pre-optimize, I shipped a benchmark harness and a nightly regression alarm: the day a real workload crosses that line, the curve shows up in the table and the nightly fails loudly, instead of a restricted user quietly getting bad answers.

Has anyone here pushed permission-filtered HNSW past the 100k-chunk mark? Curious whether you dropped to IVFFlat, leaned on partial indexes per tenant, raised ef_search, or partitioned the table.

---

## DAY 4 - Proof (evals, and the differentiator)

### X thread

**1/**
A security property you can't measure is a security property you don't have.
So the permission-aware retrieval is backed by a correctness eval: 50 questions, 3 retrieval modes, 3 viewer setups. It scores two things.

**2/**
Leakage: the fraction of restricted-viewer runs that returned ANY chunk they weren't allowed to see.
Pre-filter and post-filter both score 0 gold chunks leaked, every mode.
(Pre-filter is the load-bearing row - post-filter can still leak via timing or payload-size side channels.)

**3/**
Non-regression: full-access recall@5 holds at 0.86 (vector and hybrid) against the prior baseline.
Adding permissions did not quietly degrade retrieval for everyone else. That is the number I actually watch.

**4/**
That second number separates "works in the demo" from "I can tell my client exactly what this system does and does not do."
When they ask "are you SURE restricted users can't see the CEO's folder?" the answer is a number from a test that runs on every PR. Not a shrug.

**5/**
I spent 10 years in hardware validation before moving into AI. This is that rigor applied to production RAG.
Most tutorials stop at "embed, retrieve, generate." The hard part of a client deliverable is everything after the demo.
Tomorrow: what I'm building from all this.

**Optional timely hook (add as 6/, or a reply):**
This isn't hypothetical. In 2026 alone: EchoLeak silently exfiltrated data from Microsoft 365 Copilot, and Slack AI leaked through a poisoned knowledge item.
"0 chunks leaked, on every PR" is the answer to the headline your client already read.

---

## DAY 5 - The pitch (synthesis + CTA)

### X thread

**1/**
5 days on the per-user sharing trap in RAG. Recap for anyone who's shipping client AI:

**2/**
- Post-filter the top-k -> recall collapses for restricted users (10 x 5% = 0.5 visible chunks)
- Fix: push the permission predicate into the query, filter before ranking
- HNSW has a sharp edge past ~100k chunks; the planner covers you until then, so ship a benchmark + alarm
- Prove it: 0 chunks leaked, recall@5 holds at 0.86, on every PR

**3/**
I'm packaging all of it - the fix, the data model, the eval harness - into a permission-aware RAG + AI support starter kit.
One engine, two faces: internal "chat with your docs" and a customer-facing support deflection layer. No framework lock-in.

**4/**
It's for the agency or freelance dev who sold a client an AI feature and needs to ship it defensibly.
I'm building it in public and validating with real buyers before I build more.
If that's you, I want to talk. Waitlist + a 20-min call box: [WAITLIST LINK]

**5/** (optional, links out to the full piece)
Full write-up with the SQL, the index analysis, and the eval tables is here: https://x.com/hyungjcho/status/2074233331236167799
More deep-dives coming - next one is the leak-eval suite that caught a -0.51 recall@5 regression from a one-line change before it shipped.

**Optional timely hook (add as an urgency opener or reply):**
Gartner expects 70% of companies to be running RAG bots by 2026, and teams say integration is 40-60% of the build.
This kit is that 40-60%: the permission model, the workspace isolation, and the evals, done right the first time.

### Reddit - optional, r/SideProject (only if you want a build-in-public post)

**Title:** Building a permission-aware RAG starter kit in public - 5-part teardown of the bug that started it

**Body:**

Over the past week I wrote up a failure mode I kept hitting in client RAG work: per-user document permissions, added the obvious way (post-filter the top-k), silently destroy retrieval quality for restricted users. The math, the fix (filter before ranking in the query), the pgvector/HNSW gotcha at scale, and the evals that prove it are in the thread linked below.

I'm turning it into a starter kit for agency and freelance devs who sold a client an AI feature and need to ship it defensibly: permission-aware retrieval, workspace isolation, and answer quality, all backed by runnable evals, no framework lock-in. Background: 10 years in hardware validation before AI, so the eval rigor is the part I actually care about.

I'm validating with real buyers before building more. If you ship client AI features, I'd genuinely like to hear what would save you time. Happy to share the waitlist in a comment if useful. What would you want in something like this?

---

## Posting checklist

- [x] Waitlist (Tally) live, link ready for Day 4-5
- [x] Post #1 published somewhere linkable for the Day 5 "full write-up" link (X, 2026-07-07: https://x.com/hyungjcho/status/2074233331236167799)
- [x] Day 1: X thread + r/Rag post; reply to comments within 2 hrs (live 2026-07-07)
- [x] Day 2: X thread (live 2026-07-07)
- [x] Day 3: X thread (live 2026-07-08); r/LocalLLaMA post still pending; reply to comments within 2 hrs
- [ ] Day 4: X thread
- [ ] Day 5: X thread with CTA (+ optional r/SideProject post)
- [ ] Optional: swap in a timely hook (see "Current signal") on Day 1 / 4 / 5 to cite a named 2026 incident or stat; refresh the scan if posting slips past mid-July
- [ ] Log signups + interview-yes counts in the daily log under `## Validation`
