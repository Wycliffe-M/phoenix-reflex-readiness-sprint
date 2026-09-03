# Reflex — Submission Checklist
**Who owns this:** Member 5 runs this checklist top to bottom before submitting, but every checkbox needs the actual owning member's confirmation — Member 5 shouldn't tick a box on someone else's behalf without hearing "yes, done" from them directly.

This maps 1:1 to the brief's own "Deliverables Checklist." Don't submit until every box is genuinely true, not just checked out of hope.

---

## 1. Frozen build
- [ ] `main` branch on GitHub reflects the final, working app — no uncommitted work sitting on anyone's laptop
- [ ] Repo is accessible to whoever's grading it (confirm: public repo, or instructor added as collaborator — check which your program requires)
- [ ] App runs cleanly from a fresh clone (`git clone` → `pip install -r requirements.txt` → `python app.py`) — test this on a machine/venv that hasn't already got it running, to catch anything that only works because of leftover local state
- [ ] No feature changes since the freeze point at the end of Day 1 — if something changed since then, confirm it was a bug fix responding to something broken, not new scope
- [ ] `README.md` is current and matches the actual final contract/behavior
- [ ] Live deployment URL (`https://phoenix-reflex-readiness-sprint.onrender.com`) is reachable and has been tested end-to-end (create → assign → pick up → deliver) — confirm again shortly before the panel, since free-tier data resets on idle/redeploy

**Owner confirming:** Member 4, with Members 1–3 confirming their own screens still match

---

## 2. Deck: Problem → Solution → Architecture → Trade-offs → Roadmap
- [ ] All 7 slides in `Reflex_Deck_Outline.md` have zero remaining `[bracket]` placeholders
- [ ] Each slide lands exactly one takeaway — re-check this specifically today, since Day 2 additions can quietly make a slide carry two ideas
- [ ] Slide 6 (Trade-offs) matches `Reflex_TradeOff_Log.md` in substance, not just similar wording
- [ ] Deck exported to whatever format your submission requires (PDF, PPTX, Google Slides link, etc. — confirm which before exporting)
- [ ] A non-team-member has skimmed it once and could follow the story without the live demo

**Owner confirming:** Member 5

---

## 3. One-page trade-off log
- [ ] `Reflex_TradeOff_Log.md` has at least 3 complete entries
- [ ] Each entry has all three parts: what it is / acceptable because / what we'd do with more time
- [ ] Genuinely one page if printed/exported — trim if it's run long
- [ ] Every listed owner has actually rehearsed explaining their entry out loud (per Day 2), not just written it

**Owner confirming:** Member 5, with each trade-off's individual owner confirming their entry is accurate

---

## 4. Demo script
- [ ] `Reflex_Demo_Script_and_SCE_Prep.md` Part 1 has no remaining `[bracket]` placeholders
- [ ] Script matches the app's actual current behavior — re-verify today specifically, since Day 2 fixes may have changed exact button labels, screen order, or wording
- [ ] Backup plan line names an actual person and references the actual backup video recorded on Day 2
- [ ] Total scripted time still fits inside the ~4–5 minute target

**Owner confirming:** Member 5, with Members 1–3 confirming their own beat

---

## 5. Timing log from at least two dry runs
- [ ] Timing Log #1 (Day 1) — actual recorded time, not estimated
- [ ] Timing Log #2 (Day 2) — actual recorded time, not estimated
- [ ] Both logs show what changed between them (what got faster/tighter, what was fixed)
- [ ] Logs are in whatever format your submission form expects — a simple table with date, duration, and notes is enough if no format is specified:

| Dry Run | Date | Total Time | Notes |
|---|---|---|---|
| #1 | | | |
| #2 | | | |

**Owner confirming:** Member 5

---

## 6. Submission form itself
*(Adjust this section once you can see the real form — the fields below are based on the Week 1/2 pattern and are a best guess, not confirmed.)*

- [ ] Repo link
- [ ] Deck link/file
- [ ] Trade-off log link/file
- [ ] Demo script link/file
- [ ] Timing log link/file (or pasted into the form directly)
- [ ] Team member names/roles, if the form asks
- [ ] Any reflection/narrative fields the form asks for — answer these grounded in what actually happened this sprint (real trade-offs, real critique feedback, real timing improvement), not generic statements
- [ ] Proofread once before hitting submit — check every link actually opens in a private/incognito window, so you're not relying on your own logged-in session to confirm access works

**Owner confirming:** Member 5, submits once every above section is checked off

---

## Final sign-off
Before Member 5 clicks submit, get a one-line "good to go" from all five members — a quick group chat message is enough. Don't submit on one person's confidence alone when it's a shared deliverable.

- [ ] Member 1 confirmed
- [ ] Member 2 confirmed
- [ ] Member 3 confirmed
- [ ] Member 4 confirmed
- [ ] Member 5 confirmed
- [ ] **Submitted** — [timestamp]
