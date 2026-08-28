# Instagram captions (one per rendered card)

Post order: card1 -> card3 -> card2 -> card4, two days apart.
Cards are rendered PNGs in this directory; the HTML sources sit beside them for edits.

**card1-failure.png**
For 42 days our RAG benchmark measured 0.000 while the README's table stayed green. The alarm fired every night. The failure wasn't the zeros - the security boundary was doing its job so well it blinded our own eval. The failure was that "measured nothing" could be published as a number. That's fixed, structurally, and the whole story is in the README with dates. Link in bio.
`#rag #llm #evals #buildinpublic #postgres`

**card3-regression.png**
We broke our own retrieval on purpose - one line, chunk size 500 to 100 - to prove the harness would catch it. Four minutes later CI posted the red table on the PR: recall@5 down 0.510. Nobody was watching; nobody needed to be. 50 questions, 3 modes; the cause was contrived, the catch was not.
`#rag #cicd #evals #retrieval`

**card2-security.png**
Every cell 1.000: the fraction of no-access runs that returned zero restricted chunks - 60 questions, 3 modes, 3 viewer setups, on a 16-chunk demo corpus. A correctness proof at small scale, not a scale result; the same table is re-proved from a cold seed on every PR, and the gate has no off switch.
`#postgres #pgvector #security #rag`

**card4-notbuy.png**
Reasons not to use Purvia, in our own words: no role tiers, flat groups, unmeasured recall at 100k+, no Slack/Drive connectors, not hosted. Every limit is documented in the repo. If none of those stop you, the core is MIT.
`#opensource #rag #engineering`
