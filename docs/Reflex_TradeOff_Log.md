# Reflex — Trade-Off Log
**Required by the brief as its own one-page deliverable — at least 3 weak points, each with an "acceptable because…" justification. This must match what's said on the Trade-offs slide, word-for-word in substance if not in phrasing.**

Fill in the bracketed sections once Day 1's build is final. The four candidates below are already identified from earlier planning — confirm each still holds after the real build, add any new ones the mock panel or dry runs surface, and don't submit fewer than three.

---

### Trade-off 1 — Simplified authentication
**Owner:** Member 1 (with Member 3)

**What it is:** [e.g. "There's no real login — the retailer, dispatcher, and rider views are open, and 'becoming' a specific rider on the rider screen is just a dropdown, not an authenticated session."]

**Acceptable because:** [e.g. "The core problem we were asked to solve is delivery visibility, not access control. Building real role-based auth would have taken time away from the actual workflow the brief is graded on."]

**What we'd do with more time:** [e.g. "Implement proper role-based authentication so each persona only sees and can act on their own data, with a real login step per user."]

---

### Trade-off 2 — No GPS / live location tracking, no proof of delivery
**Owner:** Member 3

**What it is:** [e.g. "A rider marks a delivery 'Delivered' with a single button tap — there's no photo, signature, or location check confirming it actually happened."]

**Acceptable because:** [e.g. "The brief's core problem is status visibility, not navigation or fraud prevention. GPS integration is also explicitly called out in the brief as something we could consider but shouldn't let derail the core workflow."]

**What we'd do with more time:** [e.g. "Add GPS tracking during transit and require a photo or signature capture at the Delivered step as proof."]

---

### Trade-off 3 — Polling instead of real-time sync
**Owner:** Member 4 (with Members 1, 2, 3)

**What it is:** [e.g. "Every screen refreshes its data every 3 seconds via polling (fetch on an interval), rather than the server pushing updates the instant something changes."]

**Acceptable because:** [e.g. "Polling is far simpler to build and reason about than WebSockets, and a 3-second delay is invisible in a live demo while still meeting the 'always know where a delivery stands' requirement from the brief."]

**What we'd do with more time:** [e.g. "Move to WebSockets or Server-Sent Events so status changes appear instantly rather than within a few seconds."]

---

### Trade-off 4 — No notification when a delivery is assigned
**Owner:** Member 2

**What it is:** [e.g. "When a dispatcher assigns a delivery to a rider, the rider isn't proactively notified — they only see it once they check their own dashboard (or the next poll cycle refreshes it)."]

**Acceptable because:** [e.g. "Push notifications require infrastructure (SMS gateway, push service) that's out of scope for demonstrating the core workflow, and the brief explicitly lists notifications under 'don't overbuild it.'"]

**What we'd do with more time:** [e.g. "Add SMS or push notifications so a rider is alerted the moment they're assigned a delivery."]

---

### [Trade-off 5 — add if the mock panel or dry runs surface a new one]
**Owner:**

**What it is:**

**Acceptable because:**

**What we'd do with more time:**

---

## Cross-check before submitting
- [ ] At least 3 trade-offs listed (brief's minimum)
- [ ] Each has all three parts filled in — what it is / why accepted / what we'd change
- [ ] These exact points match what Slide 6 of the deck says
- [ ] Each owner has rehearsed explaining their trade-off out loud, not just written it down
