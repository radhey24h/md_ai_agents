# Current architecture

Sample enterprise context for the notification-preferences feature.

- Clients: web app + mobile app
- Backend: customer-service owns customer profile data
- Notifications today are sent by notification-service using a server-side default (email on, SMS off)
- APIs are REST. Events go to an internal bus
- Agents must not invent a second source of truth for preferences

## Target for this sample

Customer-service owns notification preferences. notification-service consumes `CustomerNotificationPreferencesChanged`.
