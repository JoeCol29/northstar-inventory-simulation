# Scope Delta Analysis: Polling vs. Webhooks

| Feature | Original Spec (Day 3) | New Spec (Day 5) | Change Type | Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Trigger** | Cron Job (Every 5 min) | HTTP Webhook (Event-Driven) | **Removed** | Eliminated latency (5 min → <1s). |
| **Security** | API Key in Header | HMAC-SHA256 Signature | **Added** | Prevents spoofed requests; added complexity. |
| **Data State** | Overwrite on Poll | Idempotent Update | **Modified** | Added `processed_ids` set to handle retries. |
| **Error Handling** | Retry on Cron Fail | Dead Letter Queue (DLQ) | **Added** | Failed webhooks must be queued for later. |
| **Code Base** | `poller.py` active | `poller.py` deprecated | **Removed** | 100% of polling logic removed. |

## Trade-off Documentation
- **Benefit:** Real-time inventory accuracy.
- **Cost:** Increased complexity in signature verification and idempotency logic.
- **Risk:** If the warehouse sends a malformed webhook, the system must fail gracefully (400 Bad Request) without crashing.
