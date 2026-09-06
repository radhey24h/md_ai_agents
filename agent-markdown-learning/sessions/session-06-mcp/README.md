# Session 06 — MCP

## Objective

Separate **job cards** from **capabilities**. MCP is how an agent calls tools. Markdown is not a tool.

## What You Will Learn

Agent vs MCP vs workflow vs tool. Why `hitl_approve` is human-only.

## Prerequisites

Sessions 03 and 05 conceptually.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
agents/  skills/  rules/  docs/  workflow/
tools/                 what each tool means
scripts/mcp_demo_server.py
```

## Step-by-Step Demo

### Step 1

Explain the four layers (concept.md).

### Step 2

Show `tools/` list. No secrets.

### Step 3

Run the tiny teaching server (initialize + tools/list). Optional: call `read_project_doc`.

Details: [demo.md](demo.md).

## What Happens Internally

JSON-RPC over stdin. This is a **teaching** MCP-shaped server, not a product plugin pack.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

`hitl_approve` description says human only. Markdown did not “become” the database.

## Common Mistakes

Calling every HTTP API “an agent.” Putting API keys in SKILL.md.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 07 — Multi-Agent](../session-07-multi-agent/README.md)
