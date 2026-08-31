# Reflex — Demo Script & Cross-Exam Prep

> **Who owns this document:** This file was created as a template — no one on the team needs to build it from scratch. **Member 5 is the custodian**: they open it on Day 1 and start replacing brackets in Part 1 once the app is running, and they chase down entries in Part 2 across Day 1–2 — but **Member 5 does not write other members' answers for them.** Each row in Part 2 has a named owner; that member writes their own State → Context → Evidence answer, because it needs to be something they can actually say and defend live, in their own words.

## Part 1: Demo Script Skeleton
**Who fills this in:** Member 5 drafts it on Day 1 once the app is working, using the real screen/button names. Members 1–4 should check their own beat (below) is still accurate whenever their screen changes, especially after Day 2's fixes.

**Total target time: ~4–5 minutes of live demo, inside your 10-minute slot.**
Fill in the [bracketed] parts once the build is final. Practice reading it out loud — if a line takes longer to say than the click takes to happen, trim the line, not the click.

---

### Setup (before you start talking)
- Browser open, three tabs/windows ready: Retailer view, Dispatcher view, Rider view
- Database reset to a clean state (no leftover test deliveries from earlier runs)
- Presenter for this section: **[Member ___]**

### Beat 1 — Retailer creates a delivery (~45 sec)
> "We'll follow one delivery through its full lifecycle. I'm a retailer — say, a hardware store — and I've just got an order to send out."

- Click into Retailer tab
- Fill form: Customer Name, Phone, Address, Item Description
- Submit
- Point at result: "Delivery [D00X] is now logged, status **Pending**."

### Beat 2 — Dispatcher assigns a rider (~45 sec)
> "Now switching to the dispatcher — this is the person who sees every open request and decides who takes it."

- Switch to Dispatcher tab
- Point at the open delivery in the list
- Click assign, select a rider
- Point at result: "Status is now **Assigned**, and it's tied to [Rider name]."

### Beat 3 — Rider updates status (~60 sec)
> "Now the rider's view — they only see what's assigned to them, and they can't skip steps."

- Switch to Rider tab
- Show delivery appears with status Assigned
- Click "Picked Up" → show status updates
- Click "Delivered" → show status updates
- **Optional but strong:** try clicking a disabled/invalid transition (e.g. attempt to jump straight to Delivered from Assigned) to show the guard actively works, not just that you didn't build the button

### Beat 4 — Retailer sees it close the loop (~30 sec)
> "And back to the retailer — no phone call, no WhatsApp message needed. They see it went from Pending to Delivered on their own screen."

- Switch back to Retailer tab, refresh/poll
- Point at final status: **Delivered**

### Closing line (~15 sec)
> "That's the full loop — Retailer, Dispatcher, Rider, no manual coordination outside the app. Happy to take questions."

---

**Backup plan if something breaks live:** name which member has a phone-recorded backup video of a clean run, and where the trade-off log's "known fragile points" list overlaps with anything that might break — if the panel sees it break, you want to already have that failure listed as a known trade-off, not a surprise.

---

## Part 2: State → Context → Evidence Prep
**Who fills this in:** the member named in the "Owner" column of each row — not Member 5. Member 5's job is compiling and cross-checking these once written, and following up with whoever hasn't filled in their row yet, not authoring the content itself.

For each question: **State** your answer in one plain sentence. **Context**: the one sentence of reasoning behind it. **Evidence**: one concrete detail — a number, a decision, a test you ran. Each owner writes their own row — on Day 1 as a rough draft where possible, finalized with real details on Day 2.

### Category 1 — Architecture ("why this choice over the obvious alternative?")

| Likely question | Owner | State → Context → Evidence (fill in) |
|---|---|---|
| Why Flask instead of Node/Django/etc.? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| Why SQLite instead of Postgres/MySQL? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| Why did you split retailer/dispatcher/rider into separate views instead of one shared dashboard? | Member 1/2/3 | State: [...] Context: [...] Evidence: [...] |
| Why REST instead of GraphQL or something else? | Member 4 | State: [...] Context: [...] Evidence: [...] |

### Category 2 — Trade-offs ("what did you simplify, and what's the cost?")

| Likely question | Owner | State → Context → Evidence (fill in) |
|---|---|---|
| Why no real authentication? | Member 1 | State: [...] Context: [...] Evidence: [...] |
| Why no GPS/live location tracking? | Member 3 | State: [...] Context: [...] Evidence: [...] |
| Why no QR/barcode scanning for order confirmation, given the case study mentions it? | Lastborn | State: [...] Context: [...] Evidence: [...] |
| Why polling instead of WebSockets/real-time sync, and how do you handle a rider going offline mid-update? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| Why no rider notification when assigned? | Member 2 | State: [...] Context: [...] Evidence: [...] |

### Category 3 — Edge cases ("what happens when two things happen at once, or something fails partway through?")

| Likely question | Owner | State → Context → Evidence (fill in) |
|---|---|---|
| What if a dispatcher tries to assign a delivery that's already assigned? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| What if a rider tries to skip a status (Assigned → Delivered directly)? | Member 3/4 | State: [...] Context: [...] Evidence: [...] |
| What if two dispatchers try to assign the same delivery at the same moment? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| What happens if the server restarts mid-delivery — is data lost? | Member 4 | State: [...] Context: [...] Evidence: [...] |
| What if the retailer submits a form with missing/invalid data? | Member 1 | State: [...] Context: [...] Evidence: [...] |

### Category 4 — Candor ("a question with no clean answer, to see if you bluff")

Rehearse saying this sentence out loud until it's automatic: **"I don't know, but here's how I'd find out: [...]"**

| Likely question | Owner | Honest answer + "how I'd find out" |
|---|---|---|
| How would this scale to 10,000 deliveries a day? | Member 4 | [...] |
| How would you prevent a rider from marking something Delivered fraudulently (no proof of delivery)? | Member 3 | [...] |
| What's your plan for offline riders with no signal? | Member 3/5 | [...] |
| How would you handle multiple retailers/regions at once? | Member 5 | [...] |

---

## Handoff Assignments (fill in before Day 2 mock panel)
**Who fills this in:** the whole team, together, during Day 2's handoff-rehearsal step — Member 5 facilitates and records the decisions here, but who owns which slide/question category should be agreed as a group, not assigned unilaterally by any one person.

| Slide | Owner | Fields first question in |
|---|---|---|
| Problem | | Architecture |
| Solution | | Trade-offs |
| Architecture | | Edge cases |
| Trade-offs | | Candor |
| Demo | | (rotates — whoever isn't driving the keyboard) |
| Roadmap | | (rotates) |

**Rule:** every member must field at least one live question. If your name is only on one row above, you're also on standby to jump in on a category if the assigned person freezes.
