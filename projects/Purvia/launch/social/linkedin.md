# LinkedIn — one long-form post

Audience: engineers and eng leaders who will read past the first line.
Claims used: C1, C3, C4, C7, C9, C24.

---

Our RAG benchmark read 0.000 for 42 consecutive days, and the table on our README stayed green the entire time.

I want to explain why that became the paragraph I'm most proud of shipping.

Purvia is a permissions-aware RAG platform: per-document sharing is enforced inside the SQL retrieval predicate, so vector search only ever ranks chunks the viewer is authorized to see. On 2026-06-19, a seeding defect removed our eval viewers' workspace membership rows. The tenant boundary did its job perfectly - it hid the whole corpus from them - and the scale benchmark began measuring a real, correct 0.000 in every cell.

The recall-floor alarm fired every single night. But the README's table was hand-transcribed from an earlier run, and the nightly had no path to update it. For 42 days, anyone reading the docs saw green.

The lesson wasn't "fix the seeding bug" - that took a day. The lesson was that our harness could publish "we measured nothing" wearing the same clothes as "we measured 1.000." So the real fix was structural:

- A run that produced no signal now publishes a DEGENERATE RUN notice instead of a table.
- An empty gold set raises a hard error naming the question - the scoring functions refuse to return a number.
- A scheduled run with no snapshot is a third state, UNMEASURED: a failed job and a filed issue, never a green.
- And the guards themselves are pinned by CI, because the edit that must never escape a guard is the edit that weakens it.

Since 2026-07-31 the benchmark has re-measured its all-1.000 table nightly (15 multi-hop queries against 10k chunks - a size where perfect recall is expected; the benchmark exists to catch the day that stops being true).

We wrote the whole story into the README, with dates, under the heading "the failure that mattered." If you're evaluating RAG systems - anyone's, including ours - I'd suggest one interview question: what does your eval harness do when it measures nothing?

The platform is MIT-licensed, both surfaces (knowledge assistant + white-label support widget), harness included: github.com/hcho22/Purvia
