"""HTTP API + pages. JSON under /api. Customer settings and warehouse UI are separate."""
from __future__ import annotations

import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from shop import db
from shop.services import notifications
from shop.services import preferences

WEB_DIR = Path(__file__).resolve().parent.parent / "web"

CUSTOMER_RE = re.compile(r"^/api/customers/([^/]+)$")
PREFS_RE = re.compile(r"^/api/customers/([^/]+)/preferences$")
ORDER_RE = re.compile(r"^/api/orders/([^/]+)$")
SHIP_RE = re.compile(r"^/api/orders/([^/]+)/ship$")


def json_body(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length") or 0)
    if length == 0:
        return {}
    return json.loads(handler.rfile.read(length).decode("utf-8"))


class ShopHandler(BaseHTTPRequestHandler):
    server_version = "eShop/1.0"

    def log_message(self, fmt: str, *args) -> None:
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))

    def _json(self, code: int, payload: dict | list | None = None) -> None:
        body = b"" if payload is None else json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _file(self, name: str) -> None:
        path = WEB_DIR / name
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, PUT, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path in ("/", "/settings"):
            self._file("settings.html")
            return
        if path == "/warehouse":
            self._file("warehouse.html")
            return
        if path == "/api/health":
            self._json(200, {"status": "ok", "service": "eshop-notifications", "channels": ["email"]})
            return
        if path == "/api/orders":
            self._json(200, db.list_orders(self.server.conn))
            return
        if path == "/api/outbox":
            self._json(200, db.list_outbox(self.server.conn))
            return
        m = CUSTOMER_RE.match(path)
        if m:
            row = db.get_customer(self.server.conn, m.group(1))
            return self._json(200, row) if row else self._json(404, {"error": "customer_not_found"})
        m = PREFS_RE.match(path)
        if m:
            row = preferences.get(self.server.conn, m.group(1))
            return self._json(200, row) if row else self._json(404, {"error": "customer_not_found"})
        m = ORDER_RE.match(path)
        if m:
            row = db.get_order(self.server.conn, m.group(1))
            return self._json(200, row) if row else self._json(404, {"error": "order_not_found"})
        self._json(404, {"error": "not_found"})

    def do_PUT(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        m = PREFS_RE.match(path)
        if not m:
            self._json(404, {"error": "not_found"})
            return
        try:
            body = json_body(self)
        except json.JSONDecodeError:
            self._json(400, {"error": "invalid_json"})
            return
        if "email_enabled" not in body or not isinstance(body["email_enabled"], bool):
            self._json(400, {"error": "email_enabled_must_be_boolean"})
            return
        extra = set(body) - {"email_enabled"}
        if extra:
            self._json(400, {"error": "unknown_fields", "fields": sorted(extra)})
            return
        row = preferences.update_email(self.server.conn, m.group(1), body["email_enabled"])
        if row is None:
            self._json(404, {"error": "customer_not_found"})
            return
        self._json(200, row)

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        m = SHIP_RE.match(path)
        if not m:
            self._json(404, {"error": "not_found"})
            return
        result = notifications.ship_and_notify(self.server.conn, m.group(1))
        if result.get("error") in ("order_not_found", "customer_not_found"):
            self._json(404, result)
            return
        self._json(200, result)


class ShopServer(ThreadingHTTPServer):
    def __init__(self, addr: tuple[str, int], conn) -> None:
        super().__init__(addr, ShopHandler)
        self.conn = conn


def serve(host: str = "127.0.0.1", port: int = 8080) -> None:
    conn = db.connect()
    db.seed(conn)
    httpd = ShopServer((host, port), conn)
    print(f"eShop notifications on http://{host}:{port}")
    print("  Customer UI  GET /settings")
    print("  Warehouse UI GET /warehouse")
    print("  GET  /api/customers/C-1001/preferences")
    print("  PUT  /api/customers/C-1001/preferences")
    print("  GET  /api/outbox")
    print("  POST /api/orders/ORD-502/ship   (Omar is opted out)")
    httpd.serve_forever()
