# Walkthrough — Session 06

The analyst is still a job card. MCP does not replace `agents/`. It gives the worker **hands** — a standard way to call tools.

Open `tools/README.md` and `agents/tool-user.md`. If you deleted MCP, the agent could still *reason* about docs you pasted into context. It could not *call* `workflow_status`. That is reasoning vs capability.

This server is a teaching demo, not the production platform in `enterprise-agent-platform/`. Run the scripted client so you do not have to paste JSON-RPC by hand:

```powershell
cd sessions/session-06-mcp
py -3 scripts/mcp_client_demo.py
```

You should see initialize succeed, a tool list (`workflow_status`, `read_artifact`, `read_project_doc`, `run_next_agent`, `hitl_approve`), a doc snippet, and `hitl_approve` **refused** when the caller is the model. Same rule as Session 05, now on a tool: the model must not approve its own work.

Session 07 puts an orchestrator in front of specialists, still using artifacts, sequence, parallel join, HITL, and tools as ideas.
