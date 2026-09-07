# Session 01 — do this

**Shop reminder:** C-1001 gets a shipping email. C-1002 turned email off → mug ships, no mail. That is opt-out. (Phone texts are not in this shop.)

1. Open `agents/customer-analyst.md`. That is **who**. A file on disk does nothing until you (or an IDE) read it.

2. Open `skills/customer-analysis/SKILL.md` (how) and `rules/no-invent.md` (never invent a channel that is not in the code).

3. Prove the shop in code:
   - Search `skipped_opt_out` in `../../eShop-customer-notification/app/shop/services/notifications.py`
   - Open `../../eShop-customer-notification/app/shop/web/settings.html` — the checkbox is **email**

   Optional:

   ```powershell
   cd ../../eShop-customer-notification/app
   py -3 -m unittest discover -s tests -v
   ```

   The opted-out ship test must pass.

4. Write a few lines like [sample-analysis-notes.md](artifacts/sample-analysis-notes.md).

**Check:** You can say: “Who / how / must / facts are four files. C-1002 is not emailed. That is proven in `notifications.py`.”
