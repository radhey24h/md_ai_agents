# Business rules

These are facts. Agents must not silently change them.

1. A customer can opt in or out of email, SMS, and push independently.
2. Marketing notifications require explicit opt-in. Transactional notifications default to email on.
3. Preference changes apply only to future notifications, not in-flight sends.
4. A customer may change only their own preferences.
5. Locale is stored with preferences and must be a supported locale (`en-US`, `en-GB`, `hi-IN`).

If a requested behavior is not in this list, mark it UNKNOWN and wait for HITL.
