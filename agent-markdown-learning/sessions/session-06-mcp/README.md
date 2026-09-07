# Session 06 — MCP

## Objective

Separate **job cards** from **capabilities**. MCP is how an agent calls tools. Markdown is not a tool.

## What you will learn

Agent vs MCP vs workflow vs tool. Why `hitl_approve` is human-only.

## Prerequisites

Sessions 03 and 05 conceptually.

## How it works

```text
Agent = reasoning + instructions + context + state
MCP   = standardized access to external tools/data
```

```text
Markdown tells the worker what to do.
Workflow controls when it can do it.
MCP provides capabilities/tools it can call.
```

```text
Agent
 │
 ├── workflow_status
 ├── read_artifact
 ├── read_project_doc
 ├── run_next_agent
 └── hitl_approve   ← human only
       │
       ▼
      MCP
       │
       ▼
     Tools
```

| Layer | Job |
|-------|-----|
| Markdown agent/skill/rule | Who / how / must |
| Workflow | When |
| MCP | How to invoke a tool |
| Tool | The actual capability |

This session’s server is **educational**. Wiring it into Cursor still needs a product MCP config; we do not claim the IDE auto-loads this folder.

## Folder structure

```text
agents/  skills/  rules/  docs/  workflow/
tools/                 what each tool means
scripts/mcp_demo_server.py
scripts/mcp_client_demo.py
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

JSON-RPC over stdin. This is a **teaching** MCP-shaped server, not a product plugin pack.

## Expected output

`py -3 scripts/mcp_client_demo.py` prints initialize ok; tools `workflow_status`, `read_artifact`, `read_project_doc`, `run_next_agent`, `hitl_approve`; `read_project_doc` returns the session doc; `hitl_approve` is refused for model self-approve.

This is a **scripted client**, so you do not need to paste JSON-RPC by hand.

## What to observe

`hitl_approve` is human only. Markdown did not “become” the database.

## Common mistakes

Calling every HTTP API “an agent.” Putting API keys in SKILL.md.

## Interview takeaway

1. “MCP separates agent reasoning from external capabilities by providing a standardized mechanism for accessing tools and data.”
2. “Markdown is the job card; workflow is when; MCP is what the worker can call.”
3. “I do not put secrets in agent Markdown; tools authenticate outside the prompt.”
4. “`hitl_approve` is a human recording action, not a self-score by the model.”

## Next session

[Session 07 — Multi-Agent](../session-07-multi-agent/README.md)
