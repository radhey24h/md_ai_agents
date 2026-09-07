FACT: C-1002 turned shipping email off. Shipping their order does not send mail.
EVIDENCE: eShop-customer-notification/app/shop/services/notifications.py (skipped_opt_out);
tests/test_notifications.py (test_opted_out_customer_is_not_emailed).
INFERENCE: Preference is stored on the customer; warehouse ship is the send path.
UNKNOWN: Any channel not in the app (there are no phone texts here).
