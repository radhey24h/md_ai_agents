# Notification facts (session seed)

Facts come from eShop under `eShop-customer-notification/`, not from a fake catalog.

- Preference belongs to the customer (`notification_preferences.customer_id`).
- Email can be enabled or disabled (`email_enabled`).
- Shipping an order must not email opted-out customers (`shop/services/notifications.py` records `skipped_opt_out`).
- SMS is not in this service. No SMS table, `/api` route, or checkbox on settings/warehouse pages.
