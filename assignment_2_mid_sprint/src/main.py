from fastapi import FastAPI, Request, HTTPException
from src.security import verify_signature
from src.idempotency import check_idempotency, mark_processed
import json

app = FastAPI(title="Northstar Inventory Sync (Webhook Mode)")

# Simulated Redis Cache (In-memory for this demo)
inventory_cache = {}
processed_ids = set()

@app.post("/webhook/inventory")
async def receive_inventory_update(request: Request):
    """
    The new pivot endpoint. Replaces the 5-minute polling loop.
    """
    # 1. Security: Verify Signature
    payload = await request.body()
    if not verify_signature(request, payload):
        raise HTTPException(status_code=401, detail="Invalid Signature")

    data = json.loads(payload)
    update_id = data.get("id")
    sku = data.get("sku")
    qty = data.get("quantity")

    # 2. Idempotency: Check if already processed
    if check_idempotency(update_id, processed_ids):
        return {"status": "skipped", "reason": "Duplicate update ID"}

    # 3. Process: Update Cache
    inventory_cache[sku] = qty
    mark_processed(update_id, processed_ids)

    return {"status": "success", "sku": sku, "new_qty": qty}

@app.get("/inventory/{sku}")
async def get_inventory(sku: str):
    """
    The query endpoint. Returns the cached value.
    """
    qty = inventory_cache.get(sku, 0)
    return {"sku": sku, "stock": qty, "source": "cache"}

# LEGACY CODE REMOVED: 
# The function 'poll_warehouse()' from Day 3 has been deprecated and removed 
# to meet the "Non-Negotiable Pivot" requirement.
