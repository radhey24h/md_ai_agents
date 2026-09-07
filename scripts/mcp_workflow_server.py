"""Stdio MCP server for the feature-development HITL workflow.

No third-party packages. Exposes workflow tools so Cursor, Copilot, and
Claude Code can start a run, execute the next agent, and approve/reject gates.

  Cursor:   .cursor/mcp.json
  Claude:   .mcp.json
  VS Code:  .vscode/mcp.json
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import workflow_runner as wf  # noqa: E402

SERVER_NAME = "enterprise-workflow"
SERVER_VERSION = "1.0.0"
PROTOCOL_VERSION = "2024-11-05"
DOCS = ROOT / "docs"


def _ok(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}]}


def _err(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}], "isError": True}


def _capture(fn, *args, **kwargs) -> str:
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            fn(*args, **kwargs)
        return buf.getvalue().strip() or "OK"
    except SystemExit as exc:
        msg = buf.getvalue().strip() or str(exc) or "Command failed"
        raise RuntimeError(msg) from exc


def _feature(arguments: dict) -> str:
    feature = arguments.get("feature")
    if feature:
        return feature
    return wf.current_feature(None)


TOOLS = [
    {
        "name": "start_feature_run",
        "description": (
            "Start a new feature-development workflow run. "
            "Creates artifacts/runs/<feature>/state.json. Does not auto-approve HITL."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "feature": {
                    "type": "string",
                    "description": "Feature id, for example customer-notification",
                }
            },
            "required": ["feature"],
        },
    },
    {
        "name": "workflow_status",
        "description": (
            "Show the current workflow stage, HITL gates, and whether a human "
            "must approve before the next agent can run."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "feature": {"type": "string", "description": "Optional feature id"}
            },
        },
    },
    {
        "name": "run_next_agent",
        "description": (
            "Execute the next agent stage and write its JSON artifact. "
            "Stops automatically at HITL gates. Never use this to approve a gate."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "feature": {"type": "string", "description": "Optional feature id"}
            },
        },
    },
    {
        "name": "hitl_approve",
        "description": (
            "Human-in-the-loop APPROVE for the current gate. "
            "Only call this when a human has explicitly approved."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "by": {"type": "string", "description": "Approver name"},
                "comment": {"type": "string"},
                "feature": {"type": "string"},
            },
            "required": ["by"],
        },
    },
    {
        "name": "hitl_reject",
        "description": (
            "Human-in-the-loop REJECT for the current gate. "
            "Sends the workflow back to the previous agent. "
            "Only call this when a human has explicitly rejected."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "by": {"type": "string", "description": "Reviewer name"},
                "comment": {"type": "string"},
                "feature": {"type": "string"},
            },
            "required": ["by"],
        },
    },
    {
        "name": "list_artifacts",
        "description": "List JSON artifacts and approval files for a feature run.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "feature": {"type": "string"}
            },
        },
    },
    {
        "name": "read_artifact",
        "description": "Read one artifact JSON file from the active feature run.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": (
                        "File name such as state.json, requirements.json, "
                        "or approvals/design.json"
                    ),
                },
                "feature": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    {
        "name": "read_project_doc",
        "description": "Read a domain doc from docs/ (architecture, business rules, APIs).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Doc file name, for example business-rules.md",
                }
            },
            "required": ["name"],
        },
    },
]


def list_resources() -> list[dict]:
    resources = []
    if DOCS.exists():
        for path in sorted(DOCS.glob("*.md")):
            resources.append(
                {
                    "uri": f"docs://{path.stem}",
                    "name": path.name,
                    "mimeType": "text/markdown",
                    "description": f"Project domain doc: {path.name}",
                }
            )
    workflow = ROOT / "workflow" / "feature-development.yaml"
    if workflow.exists():
        resources.append(
            {
                "uri": "workflow://feature-development",
                "name": "feature-development.yaml",
                "mimeType": "text/yaml",
                "description": "HITL feature-development workflow definition",
            }
        )
    return resources


def read_resource(uri: str) -> dict:
    if uri.startswith("docs://"):
        stem = uri.removeprefix("docs://")
        path = DOCS / f"{stem}.md"
        if not path.exists() or path.parent.resolve() != DOCS.resolve():
            raise RuntimeError(f"Unknown doc resource: {uri}")
        return {
            "contents": [
                {"uri": uri, "mimeType": "text/markdown", "text": path.read_text(encoding="utf-8")}
            ]
        }
    if uri == "workflow://feature-development":
        path = ROOT / "workflow" / "feature-development.yaml"
        return {
            "contents": [
                {"uri": uri, "mimeType": "text/yaml", "text": path.read_text(encoding="utf-8")}
            ]
        }
    raise RuntimeError(f"Unknown resource: {uri}")


def call_tool(name: str, arguments: dict | None) -> dict:
    arguments = arguments or {}
    try:
        if name == "start_feature_run":
            return _ok(_capture(wf.cmd_start, arguments["feature"]))
        if name == "workflow_status":
            return _ok(_capture(wf.cmd_status, _feature(arguments)))
        if name == "run_next_agent":
            return _ok(_capture(wf.cmd_run, _feature(arguments)))
        if name == "hitl_approve":
            return _ok(
                _capture(
                    wf.cmd_decide,
                    _feature(arguments),
                    "approved",
                    arguments["by"],
                    arguments.get("comment") or "",
                )
            )
        if name == "hitl_reject":
            return _ok(
                _capture(
                    wf.cmd_decide,
                    _feature(arguments),
                    "rejected",
                    arguments["by"],
                    arguments.get("comment") or "",
                )
            )
        if name == "list_artifacts":
            feature = _feature(arguments)
            folder = wf.run_dir(feature)
            if not folder.exists():
                return _err(f"No run folder for '{feature}'.")
            files = [str(p.relative_to(folder)).replace("\\", "/") for p in sorted(folder.rglob("*.json"))]
            return _ok(json.dumps({"feature": feature, "files": files}, indent=2))
        if name == "read_artifact":
            feature = _feature(arguments)
            relative = Path(arguments["name"])
            if relative.is_absolute() or ".." in relative.parts:
                return _err("Artifact name must be a relative path under the run folder.")
            path = (wf.run_dir(feature) / relative).resolve()
            if not str(path).startswith(str(wf.run_dir(feature).resolve())):
                return _err("Artifact path is outside the run folder.")
            if not path.exists():
                return _err(f"Missing artifact: {relative}")
            return _ok(path.read_text(encoding="utf-8"))
        if name == "read_project_doc":
            relative = Path(arguments["name"])
            path = (DOCS / relative.name).resolve()
            if path.parent != DOCS.resolve() or not path.exists():
                return _err(f"Unknown doc: {relative.name}")
            return _ok(path.read_text(encoding="utf-8"))
        return _err(f"Unknown tool: {name}")
    except Exception as exc:  # noqa: BLE001 — surface tool errors to the MCP client
        return _err(str(exc))


def handle(message: dict) -> dict | None:
    method = message.get("method")
    msg_id = message.get("id")
    params = message.get("params") or {}

    if method in (None, "notifications/initialized", "notifications/cancelled"):
        return None

    if method == "initialize":
        version = params.get("protocolVersion") or PROTOCOL_VERSION
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": version,
                "capabilities": {"tools": {}, "resources": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": (
                    "HITL workflow for this repo. Agents must not auto-approve gates. "
                    "Use start_feature_run, run_next_agent, then wait for a human "
                    "before hitl_approve / hitl_reject."
                ),
            },
        }

    if method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}

    if method == "tools/call":
        result = call_tool(params.get("name"), params.get("arguments"))
        return {"jsonrpc": "2.0", "id": msg_id, "result": result}

    if method == "resources/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"resources": list_resources()}}

    if method == "resources/read":
        try:
            result = read_resource(params.get("uri", ""))
            return {"jsonrpc": "2.0", "id": msg_id, "result": result}
        except Exception as exc:  # noqa: BLE001
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32000, "message": str(exc)},
            }

    if msg_id is None:
        return None

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


def main() -> int:
    stdin = sys.stdin
    while True:
        line = stdin.readline()
        if line == "":
            return 0
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        response = handle(message)
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    raise SystemExit(main())
