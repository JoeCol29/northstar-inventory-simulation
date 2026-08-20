# Northstar Inventory Sync: The Meridian Pivot Simulation

> **Project Goal:** Demonstrate independent learning, architectural adaptability, and problem-solving under pressure.<br/>
> **Scenario:** Northstar Retail Co. requires a real-time inventory sync service.<br/>
> **Constraint:** A non-negotiable mid-sprint pivot from **Polling** to **Webhooks**.

## 🧠 The Challenge
This project simulates a high-pressure software engineering sprint:
1.  **Days 1–2:** Learn an unfamiliar tool (**AWS Lambda + SQS**) and build a prototype solo.
2.  **Day 3:** Build a polling-based inventory sync service.
3.  **Day 4:** The client cancels polling. **Pivot to Webhooks immediately.**
4.  **Day 5:** Ship the new spec, document the delta, and reflect on adaptability.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Serverless:** AWS Lambda, Amazon SQS
- **Web Framework:** FastAPI (for Webhooks)
- **Security:** HMAC-SHA256 Signature Verification
- **Caching:** In-memory (simulated Redis)

## 📂 Project Structure
- `assignment_1_solo_recon/`: The initial Lambda/SQS prototype (Unfamiliar Tool).
- `assignment_2_mid_sprint/`: The refactored Webhook receiver (Post-Pivot).
- `assignment_3_adaptability/`: Peer review and reflection.

## 🔄 The Pivot: From Polling to Webhooks

### Before (Day 3 - Polling)
The system used a cron job to poll the warehouse API every 5 minutes.
- **Latency:** Up to 5 minutes.
- **Load:** High (constant requests).
- **Code:** `legacy_poller.py` (Deprecated).

### After (Day 5 - Webhooks)
The warehouse pushes updates instantly via HTTP POST.
- **Latency:** <1 second.
- **Load:** Low (only on change).
- **Security:** HMAC Signature Verification implemented.
- **Reliability:** Idempotency checks prevent duplicate updates.

## 📊 Scope Delta Analysis
| Feature | Old (Polling) | New (Webhook) | Action |
| :--- | :--- | :--- | :--- |
| Trigger | Cron Job | HTTP Endpoint | **Removed** |
| Security | API Key | HMAC Signature | **Added** |
| Data Freshness | 5 min | Real-time | **Improved** |

## 🚀 How to Run
1. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn boto3
