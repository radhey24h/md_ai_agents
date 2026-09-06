# Architecture overview

This curriculum uses **one mental model**. Sessions add pieces. They do not replace the model.

```text
AGENT     Who performs the work?
SKILL     How is this type of work performed?
RULE      What must always be true?
DOC       What facts do we know?
ARTIFACT  What does the worker hand to the next worker?
WORKFLOW  What happens next?
HITL      Where must a human decide?
MCP       What external capability can the agent call?
MODEL     What provides reasoning?
```

## Execution decision table

| Situation | Execution |
|-----------|-----------|
| Requirements → Architecture | Sequential |
| Architecture → Development | Sequential |
| API + DB + UI discovery | Parallel |
| QA + Security analysis | Parallel |
| Release after QA (and security join) | Sequential |
| Human approval | Gate |
| Independent inventory tasks | Parallel |
| Dependent tasks | Sequential |

```text
Dependency exists → Sequential
No dependency → Parallel
Risk/decision exists → HITL
External capability required → MCP
Persistent communication → Artifact
```

## Least privilege

| Role | Allowed | Not allowed |
|------|---------|-------------|
| Architect | Read, analyze, design | Change app code, deploy |
| Developer | Change application code after design HITL | Approve own work, production deploy |
| QA | Run tests, write verdict | Modify production code |
| Security | Analyze, set `release_allowed` | Approve release as a human |
| Release | Deploy after HITL | Invent business rules |
| Orchestrator | Sequence, read state | Do specialist design/code |

More capable **models** do not get more **permissions**.

## Native vs demonstration

| Concern | Native IDE (typical) | This curriculum |
|---------|----------------------|-----------------|
| Job cards / skills / rules as files | Yes, if you put them where the product looks | Yes, as teaching files in each session |
| Subagent picker | `.cursor/agents`, `.github/agents`, `.claude/agents` | Not required for learning |
| Guaranteed HITL stop | Not reliable across products | Session 5+ **scripts** stop until approve/reject |
| MCP | Product loads a configured server | Session 6 tiny teaching server |

Do not tell learners that a folder of `.md` files is a workflow engine.

## Evidence

```text
FACT:      GET /customers/{id} exists.
EVIDENCE:  Sample catalog in examples/customer-notification/sample-data/
INFERENCE: Used for customer lookup.
UNKNOWN:   Whether SMS is a supported channel.
```

If it is not proven, it is UNKNOWN. Agents must not invent business behavior.
