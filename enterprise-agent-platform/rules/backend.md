# Backend rules

- Keep business logic out of controllers.
- Do not access another service's database.
- Use structured logging. Do not log secrets, tokens, or full notification payloads that include PII.
- Preserve existing API contracts unless a breaking change is approved in HITL.
- All new I/O should be async where the platform supports it.
