# Expected output — Session 02

`artifacts/analysis.json` (already filled as a teaching sample):

```json
{
  "feature": "customer-notification",
  "status": "PASS",
  "requirements": [
    "Customer can enable or disable email notifications",
    "Opted-out customers must not be emailed"
  ],
  "assumptions": [],
  "unknowns": ["SMS support", "push support", "locales"],
  "evidence": [
    "examples/customer-notification/business-rules.md",
    "FACT: preference belongs to the customer"
  ]
}
```
