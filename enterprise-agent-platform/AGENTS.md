# Project instructions (Cursor, Copilot, Claude)

Load **only** these shared folders. Do not look under `.cursor/`, `.github/`, or `.claude/` for roles or procedures.

| Need | Folder |
|------|--------|
| Who does the work | `agents/` |
| What must always be true | `rules/` |
| How to do this kind of task | `skills/` |
| What the system actually does | `docs/` |
| What runs next / HITL | `workflow/feature-development.yaml` |

## Workflow

```text
requirements → HITL → architecture → HITL → implementation → qa → security → HITL → done
```

Sample: **Implement customer notification preferences.**

Use MCP `enterprise-workflow` or `py -3 scripts/workflow_runner.py`. Never skip HITL. Never auto-approve. State is `artifacts/runs/<feature>/state.json`, not chat.

When the user names a role, open that file in `agents/` and its skill. Switch the IDE model to the agent's `model:` class (`workflow/model-policy.md`). Orchestrator (`agents/orchestrator.md`) only sequences; it does not design or code.

## Apply rules by file type

Always: `rules/global.md`, `rules/security.md`, `rules/testing.md`.

| When editing | Also follow |
|--------------|-------------|
| Backend (`*.cs`, `*.py`, services) | `rules/backend.md` |
| Frontend (`*.ts`, `*.tsx`, `*.html`) | `rules/frontend.md` |

## Standing rules

- Do not invent business behavior. Missing proof → UNKNOWN → HITL.
- Requirements, architecture, QA, security: no application-code edits.
- Developer edits code only if `approvals/design.json` is `approved`.
- Done only if QA is `PASS` or `PASS_WITH_RISKS`, `release_allowed` is true, and release HITL is approved.
- No secrets in Markdown.

## Role map

| Stage | Agent | Skill | Model class |
|-------|--------|--------|-------------|
| Coordinate | `agents/orchestrator.md` | — | `fast` |
| Requirements | `agents/requirements.md` | `skills/requirements-analysis` | `high-reasoning` |
| Design | `agents/architect.md` | `skills/architecture-design` | `high-reasoning` |
| Code | `agents/developer.md` | `skills/implementation` | `coding` |
| QA | `agents/qa-reviewer.md` | `skills/qa-review` | `high-reasoning` |
| Security | `agents/security-reviewer.md` | `skills/security-analysis` | `high-reasoning` |

## MCP

`start_feature_run`, `run_next_agent`, `workflow_status`. `hitl_approve` / `hitl_reject` only after a human decision.
