# eShop — the shop the course talks about

Two customers. Warehouse clicks **Ship**.

- **C-1001** (ORD-501) wants shipping email → mug + email.
- **C-1002** (ORD-502) does **not** want shipping email → mug, **no email**.

C-1002’s “don’t email me” is **email opt-out**. That is the whole product.

This shop does **not** send phone texts (SMS). Nobody needs to build that.

## Prove it

```powershell
cd eShop-customer-notification/app
py -3 -m unittest discover -s tests -v
py -3 -m shop
```

| Page | What to do |
|------|------------|
| http://127.0.0.1:8080/settings | C-1001’s **email** checkbox |
| http://127.0.0.1:8080/warehouse | Ship **ORD-502** (C-1002) |
| http://127.0.0.1:8080/api/outbox | C-1002’s row: `"status": "skipped_opt_out"` |

## Where the logic lives (sessions read these)

| Layer | Path |
|-------|------|
| HTTP | `app/shop/api/http.py` |
| Database | `app/shop/db.py` |
| Ship + email | `app/shop/services/notifications.py` |
| Customer UI | `app/shop/web/settings.html` |
| Warehouse UI | `app/shop/web/warehouse.html` |

## API

| Method | Path | Meaning |
|--------|------|---------|
| GET | `/settings` | C-1001’s email toggle |
| GET | `/warehouse` | Staff ships orders |
| GET | `/api/health` | `channels: ["email"]` only |
| GET/PUT | `/api/customers/{id}/preferences` | `{ "email_enabled": true\|false }` |
| GET | `/api/outbox` | `sent` or `skipped_opt_out` |
| POST | `/api/orders/{id}/ship` | Ship; maybe email |
