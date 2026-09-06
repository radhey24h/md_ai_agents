# Business rules

Agents must treat these as facts. They must not silently add rules.

1. A customer can enable or disable email notifications.
2. A customer can opt out of notifications.
3. Notification preference belongs to the customer.
4. The system must not send a notification when the customer has opted out.
5. Unknown business behavior must not be invented by an agent.

If a request is not covered here, mark **UNKNOWN** and stop for a human (from Session 5 onward).
