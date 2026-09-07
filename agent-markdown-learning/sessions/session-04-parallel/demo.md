# Session 04 — do this

Same shop. Three inventories, no waiting:

| Look at | File | You are listing |
|---------|------|-----------------|
| API | `../../eShop-customer-notification/app/shop/api/http.py` | Routes (ship, preferences, outbox) |
| DB | `../../eShop-customer-notification/app/shop/db.py` | Tables (`email_enabled` on preferences) |
| UI | `settings.html` + `warehouse.html` | Email checkbox; ship buttons |

1. Open those files. None needs the others’ JSON first.

2. From this folder:

   ```powershell
   py -3 run_parallel.py
   py -3 run_parallel.py illegal
   ```

   First command: four JSON files. Second: error — developer depends on architecture.

**Check:** Join file exists. Illegal pairing failed.
