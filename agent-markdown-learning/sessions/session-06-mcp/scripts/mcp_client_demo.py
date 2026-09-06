"""Drive the teaching MCP server once. No extra packages."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SERVER = Path(__file__).resolve().parent / "mcp_demo_server.py"


def main() -> int:
    proc = subprocess.Popen(
        [sys.executable, str(SERVER)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert proc.stdin and proc.stdout

    def call(msg: dict, wait: bool = True) -> dict | None:
        proc.stdin.write(json.dumps(msg) + "\n")
        proc.stdin.flush()
        if not wait:
            return None
        return json.loads(proc.stdout.readline())

    print("initialize", call({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "learn", "version": "0"}}})["result"]["serverInfo"])
    call({"jsonrpc": "2.0", "method": "notifications/initialized"}, wait=False)
    tools = call({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    names = [t["name"] for t in tools["result"]["tools"]]
    print("tools", names)
    doc = call({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_project_doc", "arguments": {}}})
    print("doc", doc["result"]["content"][0]["text"][:80].replace("\n", " "), "...")
    denied = call({"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "hitl_approve", "arguments": {"by": "model"}}})
    print("hitl_approve", denied["result"]["content"][0]["text"])
    proc.stdin.close()
    proc.terminate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
