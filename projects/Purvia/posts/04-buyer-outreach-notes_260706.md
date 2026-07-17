---
purpose: Personalizable outreach to book 10 buyer-discovery interviews, sourced without a warm network
status: rewritten 2026-07-08 for cold + community channels (no warm intros assumed)
method: behavior-first (The Mom Test) + a free "permission-RAG teardown" as the value-first on-ramp. The ask is "hear how you handle this today," never "would you buy."
related: buyer-interview-script.md
target: 10 completed calls is the gate input. Sources, in order of yield: waitlist call-box, community posts, campaign engagers, cold ICP outreach.
---

# Buyer-interview outreach notes (cold + community)

The premise changed: there is no warm-intro list. So interviews get sourced three ways, in this order of effort-to-yield:

1. **The waitlist call-box** - anyone who signs up and checks "open to a call" is pre-qualified. Warmest source; the running campaign feeds it. No outreach needed, just book them.
2. **Communities hcho already belongs to** - FourthBrain alumni, Omdena, and the niche subreddits. Posting a genuine research ask there is warm-ish, not cold.
3. **Cold ICP outreach** - strangers who visibly fit the buyer (GitHub RAG repos, X accounts posting about client AI, freelance directories). Lowest conversion, most scalable.

One rule holds across all of them (from `buyer-interview-script.md`): **ask to hear how they already handle this. Never pitch the kit, never ask "would you buy."** Honest calls come from curiosity, not a sales frame.

## The on-ramp that lowers every ask: the free teardown

A cold "give me 20 minutes" is a heavy first ask. Lead with value instead:

> **The offer:** "Send me how you do per-user access in your RAG setup (post-filter the top-k, metadata filter, RLS, whatever) and I'll tell you if you've got the silent recall-collapse bug - free, no strings."

This does three things a call request can't: it gives before it asks, it self-selects for the exact buyer (only people shipping this respond), and the teardown *is* the interview - you learn how they built it while delivering something useful. Convert to a live call only if the thread has momentum. Use this on-ramp in every channel below.

## The async fallback (for people who won't call)

Not everyone will take a call; many will still type. For those, offer the 5 behavior-first questions from `buyer-interview-script.md` as a DM/email reply or a short form. A typed answer is still a data point for the gate. Always offer this as the lighter alternative when someone declines a call.

---

## Channel 1 - Waitlist call-box (warmest, no outreach)

No message needed. When someone checks the call box on the Tally form, book them within 24 hours while intent is fresh:

> Thanks for signing up and saying yes to a call - that's genuinely useful. I'm talking to people shipping client RAG before I build more of this. Grab any slot here: [scheduling link]. 20 minutes, and I mostly want to hear about the last AI feature you shipped and where the time actually went - not a pitch.

Action: make sure a scheduling link (Calendly/Cal.com) exists and rides on the Tally confirmation screen next to the post #1 link.

---

## Channel 2 - Community posts (one-to-many, warm-ish)

These are posts to a room you're already in, not DMs. Value-first, research-framed, teardown offered.

### 2a - FourthBrain alumni / bootcamp community (Slack or Discord)

> Working on something and could use the group's brain. I'm building a permission-aware RAG starter kit in public - the "who-can-see-what plus is-it-actually-correct" layer for client AI features - and before I build further I want to hear how people here actually handle it.
>
> If you've shipped RAG with per-user document access: how did you do it? And free offer - send me your approach (post-filter, metadata filter, row-level security) and I'll tell you if it has the recall-collapse bug that quietly breaks retrieval for restricted users. Happy to hop on 20 min with anyone who's living this.

### 2b - Omdena community (Slack/Discord)

> Question for anyone who's taken AI/ML work to real client delivery. I'm building a permission-aware RAG kit in public and validating it before building more. The wall I keep hitting: per-user access plus proving to a client that restricted users genuinely can't see restricted docs. How do you handle the access + "prove it's correct" side on deliverables? Glad to trade a free teardown of your retrieval-permission setup for 20 minutes of how you've approached it.

### 2c - Reddit (r/RAG, r/LocalLLaMA, plus r/freelance / r/forhire for the buyer)

Follow the campaign's Reddit rules: value in the body, no link, tailor the title per sub, be in comments the first 2 hours. Drop the waitlist/teardown in a comment only if asked.

> **Title (r/RAG):** How are you handling per-user document access in RAG - and did you check what it does to recall?
>
> **Body:** I keep seeing per-user permissions added the "obvious" way (pull top-k, then drop the chunks this viewer can't see) and it silently tanks recall for restricted users - at 5% visibility, top-10 returns ~0.5 visible chunks on average. Curious what this sub actually reaches for: pre-filter in the query, metadata filter in the vector store, RLS, something else? I've been building a permission-aware setup in public and measuring the failure with evals; happy to share the math or look at anyone's approach and flag the bug. What's worked for you?

The r/freelance / r/forhire angle is the truest buyer - frame it around client delivery ("clients keep asking 'can sales only see sales docs' - how are you shipping that defensibly?").

### 2d - Indie Hackers / build-in-public (X, IH forum)

> Building in public: a permission-aware RAG + AI-support starter kit for devs who sold a client an AI feature and need to ship it defensibly. Before I build more I'm doing teardowns - send me how you handle per-user access in your RAG and I'll tell you free whether it has the silent recall-collapse bug. Also looking for 20-min chats with anyone shipping client AI. Who's in this world?

---

## Channel 3 - Cold ICP outreach (one-to-one, scalable)

Find people who visibly fit the buyer, then send a short, specific, teardown-first note. Personalize line 1 with something true about their actual work - that line is the whole difference between a reply and a delete.

### 3a - GitHub (someone with a RAG / retrieval repo)

> Hi [name] - came across [their repo] while researching how people build retrieval permissions. I'm building a permission-aware RAG kit in public and doing free teardowns: if you've added (or plan to add) per-user document access, I can tell you whether it has the recall-collapse failure mode that hits restricted viewers. No pitch - I'm learning from people who actually build this. Worth a look, or a quick 20-min call if you'd rather talk it through?

### 3b - X / Twitter (someone posting about client AI or RAG) - reply first, then DM

Public reply first; DM only after they engage.

> **Reply:** Curious how you handled per-user access there - post-filter the top-k, or push the permission check into the query? That one choice quietly makes or breaks recall for restricted viewers.
>
> **DM (after they engage):** Appreciated the exchange. I'm building a permission-aware RAG kit in public and doing free teardowns of people's access setups (flagging the recall bug if it's there). Would you want one - or 20 min to walk through how you handle access + correctness on client work? Just learning from people who ship this for real.

### 3c - Upwork / Contra / freelance directory (the paying buyer, cold)

> Hi [name] - not a job inquiry. I saw you ship AI/LLM features for clients, which makes you exactly who I'm trying to learn from. I'm building a permission-aware RAG starter kit in public - the access-control and "prove it's correct" layer for client AI - and before building more I'm talking to devs who do this for real. Would you trade 20 minutes (how you handle per-user access + correctness on client work) for a free teardown of your retrieval-permission setup? No sale, just research.

### 3d - LinkedIn (freelance/agency AI dev)

> Hi [name] - I build production RAG and I'm researching how freelance/agency devs ship client AI features defensibly (the per-user access + correctness part). Not recruiting or selling - I'm building a permission-aware RAG kit in public and learning from people who live this. Could I ask you 20 minutes about your last client AI build, or send you a free teardown of your retrieval-permission setup? Either helps me a lot.

---

## If you do have any loose contact (keep, but don't count on it)

If a specific person does come to mind in FourthBrain, Omdena, or past client work, the warm one-to-one still beats everything - use the tighter note:

> Hey [name] - [one true, specific line]. Quick ask, and you're the right person: you've actually shipped client AI. I'm building a permission-aware RAG starter kit in public and, before I build more, hearing how people who ship this handle the access + correctness parts. 20 minutes this week or next? Not a pitch - I want to hear about your last client AI feature and where the time went. If it's not your world, a pointer to someone would help.

---

## How to send

- **Personalize line 1 every time.** Non-negotiable for cold and community both. Generic = deleted.
- **Send individually; never blast.** Even community posts get one tailored version per room, not a copy-paste across five.
- **Sequence by yield:** work the waitlist call-box first, then post in the 2-3 communities you belong to, then convert campaign engagers, then cold ICP. Only grind cold DMs if the funnel is thin.
- **The math is a pipeline:** cold outreach runs ~5-15% response, ~a third of those convert to a call, so 10 calls can mean reaching 150-400 fitting people. That is exactly why the teardown on-ramp (higher reply rate, self-selecting) and the warmer sources come first.
- **Log every reply** under `## Validation` in the daily log - even a "no / not my world" is a data point for the gate. Track which channel each came from.
- **Two open dependencies before this runs at full speed:** a scheduling link on the Tally confirmation screen (Channel 1), and the post #1 X link dropped into that same screen so signups land on the proof piece.
