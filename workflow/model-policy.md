# Model routing

Pick the model by **task**, not by prestige. Catalog names change; these classes do not.

| Class | Use for | In the IDE, choose |
|-------|---------|-------------------|
| `fast` | Orchestration, status, cheap classification | Fast / inexpensive model |
| `high-reasoning` | Requirements, architecture, QA, security | Strongest reasoning model |
| `coding` | Implementation and test generation | Strongest coding model |

Agent files set `model:` in frontmatter. Workflow stages repeat the same class so the runner stamps it on artifacts.

Do not run architecture or security on `fast`. Do not spend a reasoning model on `workflow_status`.
