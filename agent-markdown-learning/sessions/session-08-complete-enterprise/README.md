# Session 08 — Complete Enterprise Demo

## Objective

Capstone. **Customer Notification Preferences** through the full teaching path. No new primitive — show how Sessions 01–07 fit.

## What you will learn

The whole picture: foundation → artifacts → seq/parallel → HITL → MCP (as a layer) → multi-agent → this run.

## Prerequisites

Sessions 01–07.

## How it works

```text
                FEATURE
                   │
             ORCHESTRATOR
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        API       DB       UI
          │        │        │
          └────────┼────────┘
                   ▼
                  JOIN → HITL
                   ↓
               Requirements → HITL
                   ↓
               Architecture → HITL
                   ↓
              Implementation
                   ↓
              QA + Security → JOIN → HITL → Release
```

Evidence labels (FACT / EVIDENCE / INFERENCE / UNKNOWN) stay on requirements and discovery artifacts. Least privilege as in Session 07. MCP remains the toolbox (Session 06); this script uses the filesystem so the workshop works without IDE config.

This is **not** a copy of `enterprise-agent-platform/`. It is a classroom path with the same *ideas*.

## Folder structure

```text
agents/     orchestrator, discovery (api/db/ui), consolidator,
            requirements, architect, developer, qa, security, release
skills/ rules/ docs/ workflow/
artifacts/ approvals/
run_enterprise.py
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

Same as Sessions 03–05: files + state. MCP is referenced, not re-implemented here.

## Expected output

```text
artifacts/
  api-analysis.json  db-analysis.json  ui-analysis.json  consolidated-discovery.json
  requirements.json  design.json  implementation.json  qa.json  security.json
  state.json
approvals/
  discovery.json  requirements.json  design.json  release.json
```

`status` ends at `completed` after release HITL. `unknowns` still include SMS.

## What to observe

SMS stays UNKNOWN. Release waits for join of QA and security plus HITL.

## Common mistakes

Calling this “production Cursor.” It is a demo runtime.

## Interview takeaway

1. “A production-grade multi-agent system needs more than prompts: it needs role separation, skills, rules, artifacts, workflow state, tool access, guardrails and human gates.”
2. “Markdown configures workers; a runtime enforces order and HITL; MCP exposes tools.”
3. “I parallelize independent discovery and QA/security; I serialize anything that needs an approved design.”
4. “If behavior is unproven I label UNKNOWN — I do not invent business rules.”
5. “The developer must not be the only judge of the developer’s work.”

## Next

Apply the split in a real repository. Keep knowledge in one `agents/` `skills/` `rules/` `docs/` tree; use workflow + HITL for control; use MCP for tools.
