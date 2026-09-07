import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from shop import db  # noqa: E402
from shop.services import notifications  # noqa: E402


class ShipNotifyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(db.SCHEMA)
        db.seed(self.conn)

    def test_maya_is_emailed_when_order_ships(self) -> None:
        result = notifications.ship_and_notify(self.conn, "ORD-501")
        self.assertEqual(result["notification"], "sent")
        self.assertEqual(result["to"], "maya@example.com")
        self.assertEqual(db.get_order(self.conn, "ORD-501")["status"], "shipped")

    def test_omar_is_not_emailed(self) -> None:
        result = notifications.ship_and_notify(self.conn, "ORD-502")
        self.assertEqual(result["notification"], "skipped_opt_out")
        self.assertNotIn("to", result)
        self.assertEqual(db.get_order(self.conn, "ORD-502")["status"], "shipped")

    def test_unknown_order(self) -> None:
        result = notifications.ship_and_notify(self.conn, "ORD-999")
        self.assertEqual(result["error"], "order_not_found")


if __name__ == "__main__":
    unittest.main()
