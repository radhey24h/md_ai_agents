# Session 07 — Multi-Agent Workflow

## Objective

Combine agents, skills, rules, docs, artifacts, sequential, parallel, HITL, and MCP **ideas**. Writer is not the judge.

## What you will learn

Orchestrator role, least privilege, QA ‖ security then join.

## Prerequisites

Sessions 01–06.

## How it works

```text
                  USER
                    │
                    ▼
              ORCHESTRATOR
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    REQUIREMENTS           DISCOVERY (parallel API/DB/UI)
          │                   │
          └─────────┬─────────┘
                    ▼
                   JOIN → HITL → ARCHITECT → HITL → DEVELOPER
                                                    │
                                             ┌──────┴──────┐
                                             ▼             ▼
                                            QA          SECURITY
                                             └──────┬──────┘
                                                    ▼
                                              JOIN → HITL → RELEASE
```

The writer should not be the judge. QA does not modify production code. Security is independent.

| Agent | Responsibility | Privilege |
|-------|----------------|-----------|
| Orchestrator | Sequence only | No code |
| Requirements | Spec | Read |
| Discovery | Inventories (Session 04 fan-out) | Read |
| Architect | Design | Read |
| Developer | Code after HITL | Write code |
| QA | Verdict | Tests, no prod edit |
| Security | Findings | Read / scanners |
| Release | After HITL | Deploy (not in this teaching script) |

MCP is a capability layer (Session 06). This session’s script uses local files so the demo runs offline.

## Folder structure

```text
agents/ (orchestrator, discovery, requirements, architect,
         developer, qa, security, release)
skills/ rules/ docs/ workflow/ artifacts/
run_multi.py
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

Orchestrator does not write `design.json`. QA does not edit code.

## Expected output

`run_multi.py` writes `api-analysis.json`, `db-analysis.json`, `ui-analysis.json`, `requirements.json`, then **stops** (teaching HITL). After `--approve-demo`: `design.json`, `implementation.json`, `qa.json`, `security.json`, `join.json`.

Use `--approve-demo` only in class to simulate a human, and say so out loud.

## What to observe

Developer is not asked to certify QA.

## Common mistakes

One agent with all permissions because it uses a “smart” model.

## Interview takeaway

1. “An orchestrator sequences specialists; it does not replace them.”
2. “The writer should not be the judge: developer ≠ QA ≠ security.”
3. “I parallelize independent discovery and independent QA/security, then join before the next dependent stage.”
4. “Permissions follow the role, not the size of the model.”

## Next session

[Session 08 — Complete Enterprise](../session-08-complete-enterprise/README.md)
