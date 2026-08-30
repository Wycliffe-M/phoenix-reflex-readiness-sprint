"""
Reflex — Database layer (SQLite)
Member 4 owns this file.
"""

import sqlite3
from datetime import datetime, timezone
from contextlib import contextmanager

DB_PATH = "reflex.db"


@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    """Creates tables if they don't exist yet, and seeds 3 fake riders."""
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS riders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                item_description TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'PENDING',
                rider_id INTEGER,
                created_at TEXT NOT NULL,
                FOREIGN KEY (rider_id) REFERENCES riders(id)
            )
        """)
        existing = conn.execute("SELECT COUNT(*) as count FROM riders").fetchone()
        if existing["count"] == 0:
            conn.executemany(
                "INSERT INTO riders (name) VALUES (?)",
                [("Brian",), ("Kevin",), ("James",)],
            )


def _delivery_row_to_dict(row):
    return {
        "id": row["id"],
        "customerName": row["customer_name"],
        "phone": row["phone"],
        "address": row["address"],
        "itemDescription": row["item_description"],
        "status": row["status"],
        "riderId": row["rider_id"],
        "createdAt": row["created_at"],
    }


def _rider_row_to_dict(row):
    return {"id": row["id"], "name": row["name"]}


def get_all_deliveries(status=None, rider_id=None):
    query = "SELECT * FROM deliveries"
    conditions = []
    params = []
    if status:
        conditions.append("status = ?")
        params.append(status)
    if rider_id:
        conditions.append("rider_id = ?")
        params.append(rider_id)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY created_at DESC"

    with get_conn() as conn:
        rows = conn.execute(query, params).fetchall()
    return [_delivery_row_to_dict(r) for r in rows]


def get_delivery(delivery_id):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM deliveries WHERE id = ?", (delivery_id,)).fetchone()
    return _delivery_row_to_dict(row) if row else None


def create_delivery(customer_name, phone, address, item_description):
    created_at = datetime.now(timezone.utc).isoformat()
    with get_conn() as conn:
        cursor = conn.execute(
            """INSERT INTO deliveries
               (customer_name, phone, address, item_description, status, rider_id, created_at)
               VALUES (?, ?, ?, ?, 'PENDING', NULL, ?)""",
            (customer_name, phone, address, item_description, created_at),
        )
        new_id = cursor.lastrowid
    return get_delivery(new_id)


def get_all_riders():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM riders").fetchall()
    return [_rider_row_to_dict(r) for r in rows]


def get_rider(rider_id):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM riders WHERE id = ?", (rider_id,)).fetchone()
    return _rider_row_to_dict(row) if row else None


def assign_rider(delivery_id, rider_id):
    with get_conn() as conn:
        conn.execute(
            "UPDATE deliveries SET rider_id = ?, status = 'ASSIGNED' WHERE id = ?",
            (rider_id, delivery_id),
        )
    return get_delivery(delivery_id)


def update_status(delivery_id, new_status):
    with get_conn() as conn:
        conn.execute(
            "UPDATE deliveries SET status = ? WHERE id = ?",
            (new_status, delivery_id),
        )
    return get_delivery(delivery_id)
