# Instruction: Tally confirmation-screen plumbing (Channel 1 unblock)

Task: stand up a scheduling link and place it, plus the post #1 X link, on the Tally waitlist confirmation screen.
Time budget: ~15 minutes of manual UI work.
Outcome: anyone who signs up and checks the call box can self-book a 20-minute call with zero back-and-forth, and every signup lands on the proof piece.
This permanently unblocks Channel 1 (waitlist call-box), the warmest interview source in `04-buyer-outreach-notes_260706.md`.

## Inputs

- Waitlist form: https://tally.so/r/vGbO0A (Tally dashboard, "Thank you page" tab).
- Post #1 X link: https://x.com/hyungjcho/status/2074233331236167799
- Existing confirmation-copy draft: section 3 of `03-waitlist-tally-build-sheet_260706.md` (this instruction supersedes that copy).

## Step 1 - Create the scheduling link (~8 min)

Use Cal.com (free tier, no card needed); Calendly's free single event type also works if you already have an account.

1. Sign up / log in at https://cal.com with hcho22@gmail.com.
2. Confirm timezone is set to Pacific Time.
3. Create one event type:
   - Title: `RAG permissions chat (20 min)`
   - Duration: 20 minutes.
   - Description: `Not a pitch. I want to hear how you handle per-user access and correctness in client RAG work today.`
   - Location: Google Meet (or Cal Video if Meet is not connected).
4. Set availability: pick 2-3 weekday windows you will actually honor (e.g. 10:00-12:00 and 14:00-16:00 PST), add a 15-min buffer between events, and limit to 2 bookings per day so a good day cannot wipe out a work block.
5. Turn on email confirmations and a 1-hour reminder (both are defaults on Cal.com).
6. Copy the public booking URL (looks like `cal.com/<username>/rag-permissions-chat-20-min`).

Naming rule: keep the event title curiosity-framed, never "demo" or "intro to the kit".
The Mom Test discipline from `buyer-interview-script.md` starts at the booking page.

## Step 2 - Update the Tally confirmation screen (~5 min)

1. Open the form at tally.so, go to the **Thank you page** tab (confirm "show after submit" is on).
2. Replace the confirmation copy with the version below, substituting your real booking URL for `[SCHEDULING LINK]`:

```
You're on the list.

Thanks - you'll hear from me as the kit takes shape, not before.

If you checked the call box: skip the back-and-forth and grab any 20-minute slot here: [SCHEDULING LINK]. I mostly want to hear how you handle permissions and correctness on client work today - not a pitch.

Meanwhile, the first deep-dive - the per-user sharing trap that silently breaks RAG retrieval - is here: https://x.com/hyungjcho/status/2074233331236167799

- Hyung
```

3. Make both URLs actual hyperlinks (select text, add link), not bare pasted text.
4. Publish / save the form.

## Step 3 - Verify end-to-end (~2 min)

1. Open https://tally.so/r/vGbO0A in a private browser window (as a real signup would).
2. Submit a test entry with a throwaway-looking email (e.g. hcho22+test@gmail.com) and the call box checked.
3. On the confirmation screen, click both links: the booking page must load with real slots, and the X post must open.
4. Book a test slot, confirm the confirmation email arrives, then cancel the booking.
5. Delete the test submission from Tally responses so the signup count stays honest (counter stays 0 until a real signup).

## Step 4 - Record it

1. In today's daily log (`projects/Agentic_RAG/log/2026-07-09.md`), note under `## Done`: scheduling link live, confirmation screen updated, E2E verified.
2. Paste the booking URL into the log's `## Validation` block so outreach drafts can reference it (the Channel 1 booking message in `04-buyer-outreach-notes_260706.md` needs it).

## Done means

- A stranger can go from Tally submit to a booked 20-minute slot without hcho sending a single message.
- Every signup, call box or not, exits onto post #1.
