def check_idempotency(update_id: str, processed_ids: set) -> bool:
    """
    Check if an update ID has already been processed.
    Returns True if duplicate (should skip), False if new.
    """
    return update_id in processed_ids

def mark_processed(update_id: str, processed_ids: set, ttl: int = 3600):
    """
    Mark an update ID as processed.
    In production, this would be Redis with TTL.
    For this demo, we use an in-memory set.
    """
    processed_ids.add(update_id)
    # Note: In production, implement TTL cleanup
    # For demo purposes, we're keeping it simple
