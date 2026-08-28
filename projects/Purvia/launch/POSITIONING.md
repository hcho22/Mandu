# POSITIONING.md - tournament, winner, and objection handling

## The tournament

Six positioning angles were generated and scored independently against five criteria, 1-5 each.
Criteria: **Truth** (fully covered by CLAIMS.md rows), **Moat** (does the sentence die when you swap the product name out?), **Buyer fit** (engineer paying one-time for a kit), **Evidence** (numbers/files available to back it), **Risk** (inverse of red-team surface).
Disqualifications per Ground Truth are recorded below the table.

| # | Angle (headline it implies) | Truth | Moat | Buyer fit | Evidence | Risk | Total |
|---|---|---|---|---|---|---|---|
| A | The permissions predicate: "sharing lives in the SQL predicate, not a post-filter" | 5 | 4 | 4 | 4 | 3 | 20 |
| B | The receipts: "RAG with a harness that catches its own failures - including 42 days of ours" | 5 | 5 | 4 | 5 | 4 | 23 |
| C | The anti-framework: "no LangChain, code you can read" | 4 | 2 | 4 | 3 | 3 | 16 |
| D | The support-deflection wedge: "a bot that knows when to shut up" | 4 | 4 | 3 | 3 | 2 | 16 |
| E | The Onyx alternative: "the permissions they paywall, MIT" | 4 | 3 | 3 | 4 | 2 | 16 |
| F | Hosted multi-tenant AI knowledge base SaaS | - | - | - | - | - | DQ |

**Disqualified:** F converges on hosted SaaS, which Ground Truth forbids (buyer is an engineer buying a kit, not a tenant renting a service).
**Winner: B carried by A.** The permissions predicate (A) is *what* Purvia is; the measurement discipline (B) is *why an engineer can believe it*.
A alone is a trust-me security claim the product's own docs forbid ("must not be cited as proven", `docs/golden-set-authoring.md:217`); B is the only angle whose lead asset - the 42-day failure story - no competitor can copy, because it is a first-person confession with dates and a fix.

## Positioning statement

> Purvia is a permissions-aware RAG platform for engineers building multi-user products: per-document sharing is enforced inside the SQL retrieval predicate, and an eval harness proves the property on your corpus - the same harness that caught our own benchmark silently reading 0.000 for 42 days, and says so in the README.
> MIT core, one-time paid tier, no framework in the stack.

Every clause maps to ledger rows: predicate C1, harness C3/C9, failure story C4, MIT C24, paid tier C25, no-framework `README.md:10`.

## Why each loser lost = the objection bank

| Objection a buyer will raise | Source angle | Answer (ledger-backed) |
|---|---|---|
| "Isn't this just another RAG boilerplate?" | C lost because "no framework, readable code" survives a name swap - every indie kit says it | The boilerplate parts are table stakes; the parts you cannot rebuild in a weekend are the predicate (C1), the derived-for-free leak matrix (C10), and the CI that refuses to publish an unmeasured number (C7). |
| "Is this a support bot?" | D lost because ADR-0011 already rejected scoping the product to the deflection wedge (`docs/adr/0011-product-name.md:35-41`) | The widget is one of two surfaces; the platform property (permissions in the predicate) is what both surfaces stand on (C19). |
| "Why not Onyx? It has 40+ connectors." | E lost because defining Purvia as anti-Onyx invites a connector-count comparison Purvia loses | Different job. Onyx deploys internal search over your SaaS tools and mirrors their ACLs - and its permission-aware retrieval is Enterprise Edition only (fetched: docs.onyx.app). Purvia is the retrieval predicate inside the product *you* are building, MIT (C1, C24). If you want internal search over Slack and Drive, buy Onyx. |
| "Supabase's docs show me RLS-for-RAG for free." | (DIY variant of E) | Yes - and we build on exactly that foundation. The guide stops at schema patterns; it ships no eval proving the property, no tenant boundary above sharing, no share UI, no escalation pipeline (fetched: supabase.com guide; C3, C9, C10). The predicate is a pattern; the proof is the product. |
| "Your security table is only 60 questions on 16 chunks." | (red-team preview of A-alone) | Correct, and the README says so above the table (C3). The honest claim is the discipline, not the denominator: the same harness hard-fails CI on any leak, refuses vacuous passes, and its guards are themselves CI-enforced (C7, C8). |
| "It failed for 42 days - why would I trust it?" | (the B risk, inverted) | The retrieval predicate never leaked; the *benchmark reporting* failed, the alarm fired every night, and the fix made "measured nothing" unpublishable (C4). Ask your current stack what its eval does when it measures nothing. |

## Pricing decision

- **Free core:** the entire current MIT repo - both surfaces, evals, docs (C24). This is not a crippled core; SaaS Pegasus proves free-core + paid-tier coexist (fetched pricing).
- **Paid tier: $199 one-time, "Purvia Pro"** - inside the captain's $149-249 band, matching ShipFast's flagship price point (fetched), under Pegasus's $449.
- **Boundary (planned, C25):** the paid tier sells adoption, not withheld code: a guided "your corpus, proven" onboarding pack (golden-set authoring workbook + review checklists built from `docs/golden-set-authoring.md`), deployment hardening playbooks, 12 months of prioritized issue response, and Pro theming presets for the widget.
  Nothing currently public moves behind the paywall; nothing unbuilt is sold as built.
- **Launch gate:** the pricing page may go live only when every Pro deliverable exists as a file; until then the tier is shown as "founding preorder" with an explicit not-yet-shipped label. (Publish-nothing holds for this run either way.)

## Who should not buy (goes on the site verbatim, C27)

- You need owner/editor/viewer role tiers - every Purvia grant is read access (`docs/permissions-aware-rag.md:519`).
- You need nested groups - v0 ships flat groups (`docs/permissions-aware-rag.md:521`).
- You need proven recall at 100k+ visible chunks per query - the scale curve there is instrumented but unmeasured (C26).
- You want internal search across Slack/Drive/Confluence - buy Onyx or Glean; Purvia has no connectors.
- You want a hosted service - Purvia is a codebase you run.
