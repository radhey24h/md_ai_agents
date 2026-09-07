# How the workflow runs (all platforms)

Cursor, Copilot, and Claude use the **same** `agents/`, `rules/`, and `skills/` folders. `AGENTS.md` is the entry file. The IDEs do not each own a copy of the org chart.

## Sequential pipeline

```text
requirements  --artifact-->  HITL  --approve-->  architecture  --artifact-->  HITL
                                                              --approve-->
implementation  --artifact-->  qa  --artifact-->  security  --artifact-->  HITL  --> DONE
```

| Stage | Agent file | Why it is separate | Model class |
|-------|------------|-------------------|-------------|
| Orchestrator | `agents/orchestrator.md` | Sequences only | `fast` |
| Requirements | `agents/requirements.md` | Must not design APIs | `high-reasoning` |
| Architect | `agents/architect.md` | Must not implement | `high-reasoning` |
| Developer | `agents/developer.md` | Must not self-certify | `coding` |
| QA | `agents/qa-reviewer.md` | Independent evidence | `high-reasoning` |
| Security | `agents/security-reviewer.md` | Independent `release_allowed` | `high-reasoning` |

See `workflow/model-policy.md`. Pick the matching model in the IDE when you invoke that agent. Catalog IDs change; classes do not.

This sample stays sequential so each stage can consume the previous artifact (or a HITL decision). QA and security *could* run in parallel after implementation; the runner keeps them in order for a clear demo.

## HITL

```text
Agent writes JSON → STOP at approval-* → human approve | reject
approve → next agent
reject  → previous agent
```

Gates: requirements (before design), design (before code), release (before done). Release is blocked if QA is `FAIL` or `release_allowed` is false.

CLI: `approve` / `reject`. MCP: `hitl_approve` / `hitl_reject` (human only).

## MCP

Same engine as `scripts/workflow_runner.py`. Config paths differ; the server does not:

- Cursor: `.cursor/mcp.json`
- Claude: `.mcp.json`
- VS Code / Copilot: `.vscode/mcp.json`

## Artifacts

```text
artifacts/runs/<feature>/
  state.json
  requirements.json | design.json | implementation.json | qa.json | security.json
  approvals/requirements.json | design.json | release.json
```
