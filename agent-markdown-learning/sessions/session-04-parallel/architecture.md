# Architecture — Session 04

```text
          FEATURE
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
   API      DB       UI     (no dependencies)
    │        │        │
    └────────┼────────┘
             ▼
           JOIN (all)
             ▼
       consolidator
```

Synchronization: `join: all` in `workflow/parallel.yaml`.
