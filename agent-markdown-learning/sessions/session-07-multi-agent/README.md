# Session 07 — Multi-Agent Workflow

## Objective

Combine agents, skills, rules, docs, artifacts, sequential, parallel, HITL, and MCP **ideas**. Writer is not the judge.

## What You Will Learn

Orchestrator role, least privilege, QA ‖ security then join.

## Prerequisites

Sessions 01–06.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
agents/ (orchestrator, discovery, requirements, architect,
         developer, qa, security, release)
skills/ rules/ docs/ workflow/ artifacts/
run_multi.py
```

## Step-by-Step Demo

### Step 1

Walk the architecture diagram in [architecture.md](architecture.md).

### Step 2

Show least-privilege lines in each agent file.

### Step 3

`py -3 run_multi.py` — discovery parallel, HITL pause, then remaining sequential teaching steps.

Details: [demo.md](demo.md).

## What Happens Internally

Orchestrator does not write design.json. QA does not edit code.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

Developer is not asked to certify QA.

## Common Mistakes

One agent with all permissions because it uses a “smart” model.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 08 — Complete Enterprise](../session-08-complete-enterprise/README.md)
