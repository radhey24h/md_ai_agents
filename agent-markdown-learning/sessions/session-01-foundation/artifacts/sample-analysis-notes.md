FACT: Email can be enabled or disabled per customer. Shipping honors opt-out.
EVIDENCE: eShop-customer-notification/app/shop/db.py (email_enabled);
eShop-customer-notification/app/shop/services/notifications.py (skipped_opt_out).
INFERENCE: Preference row is source of truth; ship endpoint is the enforcement path.
UNKNOWN: SMS, push, locales — not in http.py, db.py, settings.html, or warehouse.html.
