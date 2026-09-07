# API contracts

Existing (do not break without HITL):

```text
GET  /customers/{id}
GET  /notifications/send  (internal)
```

Target for customer notification preferences:

```text
GET  /customers/{id}/notification-preferences
PUT  /customers/{id}/notification-preferences
```

PUT body (conceptual):

```json
{
  "email": { "marketing": false, "transactional": true },
  "sms": { "marketing": false, "transactional": false },
  "push": { "marketing": false, "transactional": true },
  "locale": "en-US"
}
```

Breaking changes need design HITL approval.
