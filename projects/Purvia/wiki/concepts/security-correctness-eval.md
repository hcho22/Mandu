---
type: concept
tags: [agentic-rag, evals, security, permissions]
date: 2026-06-15
source-count: 2
status: seeded
component: "ACL security-correctness eval"
---

# Security Correctness Eval

An eval that checks whether restricted-viewer queries return zero protected gold chunks, turning ACL correctness into a measured property rather than a narrative claim.

## From the sources

[[agentic-rag-evals]] touches this concept by drawing a boundary around the security cells:

- The RAGAS section deliberately does not score every viewer/filter combination. It scores selected hybrid pre-filter cells for answer/context quality and leaves `no_access` cells to the security table.
- The source treats `no_access` behavior as qualitatively different from faithfulness or answer relevancy. A no-access run is not a mediocre answer-quality case; it is an authorization property.
- This separation keeps [[ragas-metrics]] from diluting the ACL invariant. Security correctness should be evaluated as whether protected gold chunks are absent, not averaged into a soft generation score.
- The same gating philosophy applies: operational gates should stay fixed because a degraded pipeline must not redefine "normal." Permission correctness is one of those hard operational properties.

[[permissions-aware-rag]] supplies the concrete security result:

- The Module 11 correctness eval runs 50 questions across vector, keyword, and hybrid retrieval, three viewer setups, and pre-filter/post-filter strategies.
- The load-bearing table is the no-access security table: every vector, keyword, and hybrid cell reports 1.000 for the fraction of no-access runs returning zero gold chunks.
- Pre-filter is the important path because it enforces visibility in SQL before candidate ranking. Post-filter also passes the table, but the source notes it could still have timing or payload-shape risks.
- The eval separates security from recall. On the small 14-chunk corpus, pre-vs-post recall deltas are 0.000 because ranking competition is too small, but the security invariant still holds.

## Synthesis

The security eval should remain a hard check beside the retrieval and generation metrics. [[retrieval-eval-suite]] can say whether visible evidence is found; [[ragas-metrics]] can say whether answers use evidence well; [[permissions-aware-retrieval]] can explain where the ACL predicate runs; this page owns the separate question of whether invisible evidence ever leaks into retrieval at all.
