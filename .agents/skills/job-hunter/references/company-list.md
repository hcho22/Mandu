# Company List Template

Use this structure when organizing target companies. Lets the user (and you) keep track of which buckets each company falls into and what the implicit pitch is.

## Format

```yaml
companies:
  - name: Anthropic
    bucket: ai-native
    careers_url: https://www.anthropic.com/careers
    notes: "Built on Claude — pitch as power user"
    priority: high

  - name: Convex
    bucket: ai-native
    careers_url: https://www.convex.dev/careers
    notes: "Production user — used Convex as primary backend in CreativeBridge"
    priority: high

```

## Buckets (customize for the user)

Common buckets that work well for AI engineering candidates:

- **ai-native** — Companies whose product IS an AI product (Anthropic, OpenAI, Cursor, Replicate, Vercel, etc.). Highest leverage if the user has used their product.
- **ai-applied-startup** — Small/mid AI startups applying AI to a vertical (legaltech, sales, support, etc.).
- **mid-stage-ai** — Series B–D AI companies, not yet household names but past startup stage.
- **stretch** — Companies the user wants to try even if it's a long shot.

### AI Evals strategy buckets (hardware-QA → AI pivot)

For Evals / Quality / Validation-shaped roles, the live `companies.yaml` also uses Tier A/B/C buckets, each entry carrying `tier`, `target_role`, `why_fit`, and `watch_outs`:

- **frontier-ai-labs** (Tier A) — Frontier labs with large eval orgs (Anthropic, OpenAI, Google DeepMind, xAI, Meta AI/FAIR).
- **evals-observability-tooling** (Tier B) — Vendors whose product is the eval/observability layer (Braintrust, LangChain/LangSmith, Galileo, Patronus AI, Arize AI).
- **ai-first-product** (Tier C) — Product companies where eval failures are user-visible daily (Cursor/Anysphere, Perplexity, Harvey, Sierra).

## Priority levels

- **high** — Strong product affinity + visible role fit. Apply first.
- **medium** — Good company, fit is plausible. Apply if bandwidth allows.
- **low** — Long shot or "just to track." Apply if a perfect role surfaces.

## "Cover letter writes itself" test

The original prompt that inspired the user's list mentioned: "Apply even though it's a stretch; the cover letters write themselves."

This is a useful tag. For any company where the user has been a production user of the product, mark `pitch: "I use your product daily — here's what I built with it."` That instantly makes the cover letter easier. Surface this in the rationale field of the final output.