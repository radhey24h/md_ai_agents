# Concept — Session 07

```text
                  USER
                    │
                    ▼
              ORCHESTRATOR
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    REQUIREMENTS           DISCOVERY (parallel API/DB/UI in Session 04 style)
          │                   │
          └─────────┬─────────┘
                    ▼
                   JOIN
                    │
                   HITL
                    │
                    ▼
                ARCHITECT
                    │
                   HITL
                    │
                    ▼
                DEVELOPER
                    │
             ┌──────┴──────┐
             ▼             ▼
            QA          SECURITY
             │             │
             └──────┬──────┘
                    ▼
                   JOIN
                    │
                   HITL
                    │
                    ▼
                 RELEASE
```

The writer should not be the judge. QA does not modify production code. Security is independent.
