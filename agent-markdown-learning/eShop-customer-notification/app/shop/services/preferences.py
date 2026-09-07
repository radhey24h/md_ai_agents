"""Customer-owned email preference. SMS is not a field."""
from __future__ import annotations

import sqlite3

from shop import db


def get(conn: sqlite3.Connection, customer_id: str) -> dict | None:
    return db.get_preference(conn, customer_id)


def update_email(conn: sqlite3.Connection, customer_id: str, enabled: bool) -> dict | None:
    return db.set_email_enabled(conn, customer_id, enabled)
