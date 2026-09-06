# Concept — Session 06

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
