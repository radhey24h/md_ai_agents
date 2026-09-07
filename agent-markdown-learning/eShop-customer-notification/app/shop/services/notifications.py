"""Ship an order, then email only if the customer opted in."""
from __future__ import annotations

import sqlite3

from shop import db

SHIPPED_TEMPLATE = "order_shipped"


def ship_and_notify(conn: sqlite3.Connection, order_id: str) -> dict:
    order = db.get_order(conn, order_id)
    if order is None:
        return {"ok": False, "error": "order_not_found", "order_id": order_id}

    customer = db.get_customer(conn, order["customer_id"])
    if customer is None:
        return {"ok": False, "error": "customer_not_found", "customer_id": order["customer_id"]}

    pref = db.get_preference(conn, customer["id"])
    opted_in = pref is not None and pref["email_enabled"]

    if order["status"] != "shipped":
        db.mark_order_shipped(conn, order_id)

    if not opted_in:
        outbox_id = db.record_outbox(
            conn, customer["id"], SHIPPED_TEMPLATE, "skipped_opt_out", order_id
        )
        return {
            "ok": True,
            "order_id": order_id,
            "order_status": "shipped",
            "notification": "skipped_opt_out",
            "outbox_id": outbox_id,
        }

    outbox_id = db.record_outbox(conn, customer["id"], SHIPPED_TEMPLATE, "sent", order_id)
    return {
        "ok": True,
        "order_id": order_id,
        "order_status": "shipped",
        "notification": "sent",
        "to": customer["email"],
        "outbox_id": outbox_id,
    }
