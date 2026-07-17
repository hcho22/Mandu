---
purpose: Ready-to-paste build sheet for the Agentic RAG waitlist form (Tally)
status: ready — build the form, then send the live URL to wire into post #1
audience: internal (hcho) — 10-minute fill-in
related: waitlist-cta.md, 01-permission-aware-rag.md, buyer-interview-script.md
---

# Agentic RAG Waitlist - Tally build sheet

Build the form in Tally block-by-block, top to bottom.
It maps 1:1 to Tally's builder.
Copy matches the positioning in `01-permission-aware-rag.md` and the 4-field spec in `waitlist-cta.md`.

## 1. Form settings (do these first, ~1 min)

| Setting | Value |
|---|---|
| Form name (internal) | `Agentic RAG starter kit - waitlist` |
| URL slug | `permission-aware-rag` -> gives you `tally.so/r/permission-aware-rag` |
| Email notifications | **ON** (Settings -> Notifications -> email yourself on every submission - this is your signal counter) |
| "Powered by Tally" | Leave on (free tier); fine for validation |

## 2. Form blocks (paste top to bottom)

**Block 1 - Title** (Tally: the big heading at the top)

```
Permission-aware RAG starter kit
```

**Block 2 - Text / description** (insert a "Text" block under the title)

```
I'm building a starter kit so you don't have to solve permission-aware retrieval and the "is it actually correct" eval problem from scratch on your next client deliverable. It's early and built in public. Join the waitlist and tell me what would save you time. Takes 30 seconds.
```

**Block 3 - Email** (insert an "Email" input block - it auto-validates format)

- Label:

```
Email
```

- Placeholder:

```
you@yourstudio.com
```

- Required: **ON**

**Block 4 - Short answer** (insert a "Short answer" block)

- Label:

```
What do you build, and for whom?
```

- Help/description text:

```
One line is plenty - e.g. "freelance, I ship RAG chatbots for B2B SaaS clients."
```

- Required: **ON**

**Block 5 - Multiple choice** (insert a "Multiple choice" block - single select)

- Label:

```
Have you shipped a client RAG/AI feature that needed per-user or per-team access?
```

- Options (one per line):

```
Yes
Not yet, but about to
No
```

- Required: **ON**

**Block 6 - Checkbox** (insert a single "Checkbox" block)

- Label:

```
Open to a 20-minute call about it? No pitch - I just want to hear how you handle this today.
```

- Checkbox text:

```
Yes, I'm open to a short call
```

- Required: **OFF** (this is opt-in; forcing it costs signups)

**Block 7 - Submit button** (edit the button label)

```
Join the waitlist
```

## 3. Confirmation screen (Tally: "Thank you page" tab)

Set to show after submit.
This copy serves both people who checked the call box and those who didn't:

```
You're on the list.

Thanks - you'll hear from me as the kit takes shape, not before. If you checked the call box, I'll reach out to find 20 minutes and hear how you handle permissions and correctness on client work today.

Meanwhile, the first deep-dive - the per-user sharing trap that silently breaks RAG retrieval - is here: [paste post #1 link once published]

- Hyung
```

## 4. Recommended add: hidden source field (2 min, high payoff)

The AR campaign runs across LinkedIn, X, and Reddit this week, and FitSnack clones this same form Tuesday.
Add **one hidden field** so you know which channel converts.
It stays invisible to the user, so it does not count against the "keep it to 4 visible fields" rule.

- In Tally: insert a **Hidden field**, name it `source`
- Then tag your links per channel:
  - `tally.so/r/permission-aware-rag?source=linkedin`
  - `tally.so/r/permission-aware-rag?source=x`
  - `tally.so/r/permission-aware-rag?source=reddit`

Every submission now records where it came from.
This directly feeds the per-platform tagged-links task the weekly plan has for Tuesday.

## 5. 10-minute checklist

1. Create form, set name + slug (Section 1)
2. Paste blocks 1-7 in order (Section 2)
3. Paste the thank-you page (Section 3)
4. Add the hidden `source` field (Section 4)
5. Turn on email notifications
6. Hit **Publish**, copy the live URL
7. Send the URL to Claude -> wire it into post #1 (Variant A CTA), ready to publish

## Notes

- **Segmentation is automatic:** anyone who answers "Yes" or "about to" on Block 5 **and** checks Block 6 is the interview shortlist, straight out of the funnel.
- **Don't add fields.** No name, company, budget, or role - every extra field costs signups, and the rest gets asked on the call.
- **Tracking:** once live, log signups + interview-yes counts under a `## Validation` section in the daily log, per `waitlist-cta.md`. Checkpoints: 10 signups (signal), 50 (quarter goal), 10 completed interviews (the gate input).
