# Business rules

1. Customers can turn **order shipping emails** on or off.
2. **Opt-out** here means: do not send that **email**. The order may still ship.
3. Preference belongs to the customer (`customer_id`).
4. C-1002 must get `skipped_opt_out` in `app/shop/services/notifications.py`.
5. There is no other channel in this shop. If someone asks for phone texts, that is UNKNOWN — not a feature to invent.

If it is not in these rules or in the app, write UNKNOWN and (from Session 5) stop for a human.
