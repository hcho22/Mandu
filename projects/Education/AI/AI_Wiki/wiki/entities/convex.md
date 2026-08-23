---
type: entity
tags: [tool, backend, database, infrastructure, everything-as-code]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Convex

An everything-as-code backend platform that "marries" the server and database into one managed box (an abstraction above AWS).
A canonical example of [[everything-as-code-abstractions]].

## What shows up in the wiki

- [[building-robust-apps-with-ai]] - Pluto's "control plane": source of truth, real-time, and orchestrator.
  - **Primitives:** queries (read), mutations (write), actions (call external services); everything is code, including the schema, so an agent can build features end-to-end.
  - **Components** (copy the link, hand to the agent): Workflow for [[durable-agent-processes]] (retries + delays), Workpool for queues/parallelism, R2 (Cloudflare) for storage, Autumn for credit billing.

## Notes

Positioned against the Supabase pattern of querying the DB from the client (see [[client-never-touches-the-database]]).
Ross's default backend; expect other [[system-design]] sources to extend or contrast it.
