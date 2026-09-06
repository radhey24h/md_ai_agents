"""Tiny MCP-shaped teaching server (stdio JSON-RPC). Independent of any other repo."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "facts.md"

TOOLS = [
    {"name": "workflow_status", "description": "Return dummy teaching status.", "inputSchema": {"type": "object"}},
    {
        "name": "read_project_doc",
        "description": "Read session docs/facts.md",
        "inputSchema": {"type": "object"},
    },
    {
        "name": "read_artifact",
        "description": "Teaching stub — no run folder required.",
        "inputSchema": {"type": "object"},
    },
    {
        "name": "run_next_agent",
        "description": "Teaching stub — would stop at HITL in a real runner.",
        "inputSchema": {"type": "object"},
    },
    {
        "name": "hitl_approve",
        "description": "HUMAN ONLY. Do not use to self-approve.",
        "inputSchema": {"type": "object", "properties": {"by": {"type": "string"}}, "required": ["by"]},
    },
]


def handle(msg: dict) -> dict | None:
    method = msg.get("method")
    mid = msg.get("id")
    if method in (None, "notifications/initialized"):
        return None
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": mid,
            "result": {
                "protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "learning-mcp-demo", "version": "1.0.0"},
            },
        }
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        name = (msg.get("params") or {}).get("name")
        if name == "read_project_doc":
            text = DOC.read_text(encoding="utf-8")
        elif name == "hitl_approve":
            text = "REFUSED in demo client unless by starts with human:. Use a real person."
        elif name == "workflow_status":
            text = json.dumps({"current": "teaching", "hitl": False})
        else:
            text = f"stub:{name}"
        return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": text}]}}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": str(method)}}


def main() -> int:
    while True:
        line = sys.stdin.readline()
        if line == "":
            return 0
        line = line.strip()
        if not line:
            continue
        resp = handle(json.loads(line))
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    raise SystemExit(main())
