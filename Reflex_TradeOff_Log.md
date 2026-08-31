# Reflex Trade-Off Log

This document records deliberate compromises made during the sprint. Each entry includes:
- **Decision**: What was chosen
- **Trade-Off**: What was sacrificed
- **Rationale**: Why the choice was made
- **Future Fix**: How we plan to address it

---

## 🔐 Authentication
- **Decision**: No authentication or role-based access implemented.
- **Trade-Off**: All routes are open; retailer, dispatcher, and rider roles are not enforced.
- **Rationale**: Sprint time constraints; focus was on proving workflow concept.
- **Future Fix**: Add JWT/OAuth with role-based access control (RBAC).

---

## 📜 Status Logging
- **Decision**: Delivery status is overwritten in the `deliveries` table.
- **Trade-Off**: No audit trail; cannot reconstruct past transitions.
- **Rationale**: Simplified schema for MVP; easier to demo status changes.
- **Future Fix**: Introduce `DeliveryLog` table to record every status change with timestamp + actor.

---

## 📱 Proof of Delivery
- **Decision**: Retailer confirmation is manual only.
- **Trade-Off**: No QR/scan or OTP verification; prone to human error.
- **Rationale**: Kept frontend simple; avoided dependency on mobile camera/QR libraries.
- **Future Fix**: Generate QR codes per delivery; rider scans at drop-off, retailer confirms via scan.

---

## 🗄️ Database Choice
- **Decision**: SQLite used for persistence.
- **Trade-Off**: Not production-grade; limited concurrency and scalability.
- **Rationale**: Lightweight, zero-config DB suitable for sprint demo.
- **Future Fix**: Migrate to PostgreSQL with SQLAlchemy migrations.

---

## 🖥️ Frontend UX
- **Decision**: Plain HTML/CSS templates.
- **Trade-Off**: Limited interactivity; no modern UX features.
- **Rationale**: Ensure accessibility for all team members; avoid framework learning curve.
- **Future Fix**: Rebuild frontend with React or Flutter for mobile-first experience.

---

## 🚀 Deployment
- **Decision**: Local-only run (`python app.py`).
- **Trade-Off**: No cloud deployment, CI/CD, or containerization.
- **Rationale**: Sprint scope limited to local demo.
- **Future Fix**: Add Dockerfile + GitHub Actions pipeline; deploy to Heroku/AWS.

---

## ✅ Summary
These trade-offs allowed the team to deliver a working MVP quickly. Each gap is acknowledged and mapped to a concrete future fix for production readiness.