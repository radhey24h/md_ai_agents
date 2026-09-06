# Architecture — Session 01

Single worker. No pipeline.

```text
MODEL  →  AGENT (Customer Analyst)
              ├── SKILL  customer-analysis
              ├── RULE   do not invent
              └── DOC    notification facts
                        ↓
                   analysis notes
```

Permissions: read docs and examples only. No “next agent.” No tools.
