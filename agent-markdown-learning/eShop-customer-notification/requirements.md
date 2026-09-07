# Requirements (seed)

Keep **customer notification preferences** for eShop **email** when an order ships.

Proven in [app/](app/README.md):

- Customer can GET/PUT email preference (`/api/customers/{id}/preferences`).
- Warehouse can POST `/api/orders/{id}/ship`.
- QA can GET `/api/outbox` (`sent` vs `skipped_opt_out`).
- Opted-out customers get `notification: skipped_opt_out` (order still ships).
- Preference is keyed by `customer_id`.

UNKNOWN until proven in code, tests, or HITL:

- SMS / WhatsApp / push
- Locales
