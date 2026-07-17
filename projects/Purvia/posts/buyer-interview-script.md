---
purpose: 10 buyer-discovery interviews to gate further Agentic RAG feature-building
status: draft — ready to run
method: behavior-first (The Mom Test). Ask about what they have actually done, not what they would hypothetically buy.
target: 10 completed calls, 20 min each
---

# Buyer interview script — permission-aware RAG starter kit

## The one rule

Ask about their past and present behavior, never about your idea or the
future. "Would you buy a starter kit?" gets you a polite yes that means
nothing. "Walk me through the last client AI feature you shipped" gets you
the truth. If they have not lived the problem, no amount of product talk
will make them a buyer; find that out in the first five minutes.

## Goal of the call

Confirm or kill three assumptions:

1. **The buyer exists.** Agency/freelance devs ship client RAG features on a
   deadline and own the outcome.
2. **The pain is real and expensive.** Permissions + "is it actually correct"
   cost them real time, rework, or client trust.
3. **The wedge is right.** The thing they would pay to skip is the
   permission-and-eval problem, not something else (auth, infra, UI, parsing).

If 1 or 2 fail across most calls, the gate says stop building and rethink the
buyer. That is a successful interview, not a failed one.

## Script (20 minutes)

**Warm-up (2 min)**
- "Tell me what you build and who your clients are."
- "What is the last AI feature you shipped for a client?"

**The problem, lived (8 min) — the core of the call**
- "Walk me through that build. Where did the time actually go?"
- "Did any of it involve who-can-see-what, per-user or per-team access?"
  - If yes: "What did you do for it? How long did that take? What broke?"
  - If no: "Has a client ever asked for that, or do you expect them to?"
- "How did you convince the client it was correct, that restricted users
  really could not see restricted docs? What did you show them?"
- "When something retrieval-related went wrong after delivery, how did you
  find out, and how did you debug it?"

**Cost and current workaround (5 min)**
- "If you had to put a number on it, how much of a typical client AI project
  is this permissions-plus-is-it-correct work?"
- "What do you reach for today, copy a past project, a framework, build from
  scratch? What do you wish existed?"
- "Have you ever turned down or de-scoped a client ask because getting the
  access/correctness part right was too much work?"

**Wedge test (3 min) — last, never first**
- "I am building a starter kit that ships permission-aware retrieval plus the
  eval harness that proves access is correct. If that existed on your last
  project, where would it have helped, or not?"
- "What would have to be true for you to actually drop it into client work?"
- "Who else doing this kind of work should I talk to?" (referral chain)

## What to record after each call

Log to `projects/Agentic_RAG/log/<date>.md` under `## Validation`:
- Buyer profile (agency / freelance / in-house; what they ship)
- Did they live the permission pain? (yes / no / partial)
- Their current workaround + rough time cost
- Strongest quote, verbatim
- Wedge reaction (would skip it / would not / wrong wedge)
- Referrals given

## Where to find 10 of them

You do not need names today; you need sources. Ranked by warmth:

1. **Your own network first** — anyone from FourthBrain, Omdena, past
   freelance/agency contacts who ships client AI. Warmest, start here.
2. **X / Twitter** — devs posting about shipping client RAG, "chat with your
   docs" builds, indie AI consultancies. Reply, then DM.
3. **Indie Hackers / r/LocalLLaMA / r/MachineLearning** build threads —
   people describing client RAG work.
4. **Upwork / Contra / agency directories** — search "RAG" / "AI chatbot"
   freelancers; they are the buyer by definition.
5. **The waitlist itself** — anyone who checked the "open to a call" box is
   pre-qualified. This becomes your primary source once the form is live.

Target: book 3 calls from network this week, then let the waitlist + outreach
fill the rest. Ten completed calls is the gate input for further building.
