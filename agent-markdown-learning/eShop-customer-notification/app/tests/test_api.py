import json
import sqlite3
import sys
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from shop import db  # noqa: E402
from shop.api.http import ShopServer  # noqa: E402


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        conn = sqlite3.connect(":memory:", check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.executescript(db.SCHEMA)
        db.seed(conn)
        cls.httpd = ShopServer(("127.0.0.1", 0), conn)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def url(self, path: str) -> str:
        return f"http://127.0.0.1:{self.port}{path}"

    def get(self, path: str):
        with urlopen(self.url(path)) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def put(self, path: str, payload: dict):
        req = Request(
            self.url(path),
            data=json.dumps(payload).encode("utf-8"),
            method="PUT",
            headers={"Content-Type": "application/json"},
        )
        with urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def post(self, path: str, payload: dict | None = None):
        req = Request(
            self.url(path),
            data=json.dumps(payload or {}).encode("utf-8"),
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        with urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def test_health_email_only(self) -> None:
        data = self.get("/api/health")
        self.assertEqual(data["channels"], ["email"])

    def test_preferences_have_no_sms(self) -> None:
        data = self.get("/api/customers/C-1001/preferences")
        self.assertEqual(data["channel"], "email")
        self.assertNotIn("sms", data)

    def test_put_rejects_sms_field(self) -> None:
        req = Request(
            self.url("/api/customers/C-1001/preferences"),
            data=json.dumps({"email_enabled": True, "sms_enabled": False}).encode("utf-8"),
            method="PUT",
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(HTTPError) as ctx:
            urlopen(req)
        self.assertEqual(ctx.exception.code, 400)

    def test_ship_skips_opted_out(self) -> None:
        data = self.post("/api/orders/ORD-502/ship")
        self.assertEqual(data["notification"], "skipped_opt_out")
        outbox = self.get("/api/outbox")
        self.assertTrue(any(r["status"] == "skipped_opt_out" for r in outbox))


if __name__ == "__main__":
    unittest.main()
