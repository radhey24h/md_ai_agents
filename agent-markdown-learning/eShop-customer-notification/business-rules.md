# Business rules

Agents must treat these as facts. They must not silently add rules.

1. A customer can enable or disable **email** notifications for order events.
2. A customer can opt out of those emails.
3. Preference belongs to the customer (`notification_preferences.customer_id`).
4. Shipping an order must not send email when the customer has opted out. See `app/shop/services/notifications.py`.
5. Unknown channels must not be invented. This service has **no SMS** (or push, or WhatsApp).

If a request is not covered here or in the app code, mark **UNKNOWN** and stop for a human (from Session 5 onward).
