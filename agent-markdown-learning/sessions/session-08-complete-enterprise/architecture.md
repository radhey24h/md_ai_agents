# Architecture — Session 08

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
                  JOIN
                   ↓
               Requirements
                   ↓
                  HITL
                   ↓
               Architecture
                   ↓
                  HITL
                   ↓
              Implementation
                   ↓
              QA + Security
                   ↓
                  JOIN
                   ↓
                  HITL
                   ↓
                Release
```

Least privilege as in Session 07. MCP remains the toolbox (Session 06); this script uses the filesystem so the workshop works without IDE config.
