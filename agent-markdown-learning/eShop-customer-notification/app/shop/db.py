"""SQLite: customers, email preferences, orders, email outbox. No SMS."""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parent.parent / "data" / "app.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS customers (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    display_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notification_preferences (
    customer_id TEXT PRIMARY KEY REFERENCES customers(id),
    email_enabled INTEGER NOT NULL DEFAULT 1,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL REFERENCES customers(id),
    sku TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS email_outbox (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id TEXT NOT NULL,
    order_id TEXT,
    template TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    path = db_path or DEFAULT_DB
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def seed(conn: sqlite3.Connection) -> None:
    ts = now()
    customers = [
        ("C-1001", "maya@example.com", "Maya Patel", 1),
        ("C-1002", "omar@example.com", "Omar Khan", 0),
    ]
    for cid, email, name, enabled in customers:
        conn.execute(
            "INSERT OR IGNORE INTO customers (id, email, display_name) VALUES (?, ?, ?)",
            (cid, email, name),
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO notification_preferences (customer_id, email_enabled, updated_at)
            VALUES (?, ?, ?)
            """,
            (cid, enabled, ts),
        )
    conn.execute(
        """
        INSERT OR IGNORE INTO orders (id, customer_id, sku, status, created_at)
        VALUES ('ORD-501', 'C-1001', 'MUG-BLUE', 'paid', ?)
        """,
        (ts,),
    )
    conn.execute(
        """
        INSERT OR IGNORE INTO orders (id, customer_id, sku, status, created_at)
        VALUES ('ORD-502', 'C-1002', 'MUG-RED', 'paid', ?)
        """,
        (ts,),
    )
    conn.commit()


def get_customer(conn: sqlite3.Connection, customer_id: str) -> dict | None:
    row = conn.execute(
        "SELECT id, email, display_name FROM customers WHERE id = ?", (customer_id,)
    ).fetchone()
    return dict(row) if row else None


def get_preference(conn: sqlite3.Connection, customer_id: str) -> dict | None:
    row = conn.execute(
        "SELECT customer_id, email_enabled, updated_at FROM notification_preferences WHERE customer_id = ?",
        (customer_id,),
    ).fetchone()
    if not row:
        return None
    return {
        "customer_id": row["customer_id"],
        "email_enabled": bool(row["email_enabled"]),
        "channel": "email",
        "updated_at": row["updated_at"],
    }


def set_email_enabled(conn: sqlite3.Connection, customer_id: str, enabled: bool) -> dict | None:
    if get_customer(conn, customer_id) is None:
        return None
    conn.execute(
        """
        INSERT INTO notification_preferences (customer_id, email_enabled, updated_at)
        VALUES (?, ?, ?)
        ON CONFLICT(customer_id) DO UPDATE SET
            email_enabled = excluded.email_enabled,
            updated_at = excluded.updated_at
        """,
        (customer_id, int(enabled), now()),
    )
    conn.commit()
    return get_preference(conn, customer_id)


def get_order(conn: sqlite3.Connection, order_id: str) -> dict | None:
    row = conn.execute(
        "SELECT id, customer_id, sku, status, created_at FROM orders WHERE id = ?",
        (order_id,),
    ).fetchone()
    return dict(row) if row else None


def list_orders(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute(
        "SELECT id, customer_id, sku, status, created_at FROM orders ORDER BY id"
    ).fetchall()
    return [dict(r) for r in rows]


def mark_order_shipped(conn: sqlite3.Connection, order_id: str) -> None:
    conn.execute("UPDATE orders SET status = 'shipped' WHERE id = ?", (order_id,))
    conn.commit()


def list_outbox(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute(
        """
        SELECT id, customer_id, order_id, template, status, created_at
        FROM email_outbox
        ORDER BY id
        """
    ).fetchall()
    return [dict(r) for r in rows]


def record_outbox(
    conn: sqlite3.Connection, customer_id: str, template: str, status: str, order_id: str | None
) -> int:
    cur = conn.execute(
        """
        INSERT INTO email_outbox (customer_id, order_id, template, status, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (customer_id, order_id, template, status, now()),
    )
    conn.commit()
    return int(cur.lastrowid)
