# Architecture — Session 07

| Agent | Responsibility | Privilege |
|-------|----------------|-----------|
| Orchestrator | Sequence only | No code |
| Requirements | Spec | Read |
| Discovery* | Inventories | Read |
| Architect | Design | Read |
| Developer | Code after HITL | Write code |
| QA | Verdict | Tests, no prod edit |
| Security | Findings | Read / scanners |
| Release | After HITL | Deploy (not in this teaching script) |

\*Discovery is the Session 04 fan-out, invoked by the orchestrator conceptually.

MCP is available as a *capability layer* (Session 06); this session’s script still uses local files so the demo runs offline.
