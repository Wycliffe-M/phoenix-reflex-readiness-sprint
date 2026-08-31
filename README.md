# Reflex

A delivery-management system for small Kenyan retailers — replaces WhatsApp/phone coordination with a shared view of who's assigned, delivery status, and proof of progress.

## Personas
- 🏪 **Retailer** — creates a delivery request, watches its status
- 🧑‍💼 **Dispatcher** — sees open requests, assigns a rider
- 🛵 **Rider** — sees assigned deliveries, moves them Assigned → Picked Up → Delivered

## Stack
Flask (backend + templating) · SQLite (database) · plain HTML/CSS/JS (frontend). No build step, no frontend framework — deliberately, so the whole team can read and explain every file.

## Setup

```
python -m venv venv
venv\Scripts\activate          (Windows PowerShell)
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser. The database file (`reflex.db`) and its 3 seed riders (Brian, Kevin, James) are created automatically on first run.

## Frozen data model

```
Delivery:
  id, customerName, phone, address, itemDescription,
  status ("PENDING" | "ASSIGNED" | "PICKED_UP" | "DELIVERED"),
  riderId, createdAt

Rider:
  id, name
```

## Frozen API contract

| Method | Route | Purpose |
|---|---|---|
| GET | `/deliveries` | list all deliveries (optional `?status=` and `?riderId=` filters) |
| GET | `/deliveries/<id>` | get one delivery |
| POST | `/deliveries` | create a delivery (starts as `PENDING`) |
| GET | `/riders` | list all riders |
| POST | `/deliveries/<id>/assign` | assign a rider — body `{ riderId }` — sets status to `ASSIGNED` |
| PATCH | `/deliveries/<id>/status` | move status forward one step — body `{ status }` — server rejects skipped/invalid transitions |

## File ownership

| File | Owner |
|---|---|
| `app.py`, `models.py` | Member 4 |
| `templates/retailer.html` | Member 1 |
| `templates/dispatcher.html` | Member 2 |
| `templates/rider.html` | Member 3 |
| `templates/home.html`, `static/style.css` | shared |
| `docs/Reflex_Deck_Outline.md` | Member 5 |
| `docs/Reflex_Demo_Script_and_SCE_Prep.md` | Member 5 |
| `docs/Reflex_TradeOff_Log.md` | Member 5 (individual entries credited to whoever raised them) |
| `docs/Reflex_Submission_Checklist.md` | Member 5 |

