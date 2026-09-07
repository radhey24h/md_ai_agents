# eShop — customer notification preferences

Workshop evidence for every session: a small **online shop**. When an order ships, the shop may email the customer. Email is opt-in. **SMS is not in this product.**

## Use case

Maya (C-1001) ordered a blue mug (`ORD-501`) and wants shipping emails.  
Omar (C-1002) ordered a red mug (`ORD-502`) and opted out. Warehouse can still ship; **no email goes out**.

Someone will ask “add SMS opt-out.” Search the repo. There is no SMS route, column, or checkbox. That is UNKNOWN.

## Layout (maps to sessions)

| Layer | Path | Session |
|-------|------|---------|
| HTTP API | `app/shop/api/http.py` | 04, 07, 08 API inventory |
| Database | `app/shop/db.py` | 04, 07, 08 DB inventory |
| Domain services | `app/shop/services/notifications.py` | 01–02 evidence, 03 implementation target |
| Outbox API | `GET /api/outbox` | 03 / 07 / 08 QA |
| Customer UI | `app/shop/web/settings.html` | 04 UI inventory |
| Warehouse UI | `app/shop/web/warehouse.html` | 04 UI (ops), 08 demo |

## API

| Method | Path | Meaning |
|--------|------|---------|
| GET | `/settings` | Customer email toggle (Maya) |
| GET | `/warehouse` | Staff ships orders |
| GET | `/api/health` | `channels: ["email"]` only |
| GET | `/api/customers/{id}` | Customer |
| GET/PUT | `/api/customers/{id}/preferences` | `{ "email_enabled": true\|false }` — extra fields rejected |
| GET | `/api/orders` | Order list |
| GET | `/api/outbox` | Email send log (`sent` / `skipped_opt_out`) — QA evidence |
| POST | `/api/orders/{id}/ship` | Mark shipped; email or `skipped_opt_out` |

## Run

From `app/` (no pip):

```powershell
cd eShop-customer-notification/app
py -3 -m unittest discover -s tests -v
py -3 -m shop
```

http://127.0.0.1:8080/settings — Maya’s email checkbox  
http://127.0.0.1:8080/warehouse — ship ORD-502 and watch skip
