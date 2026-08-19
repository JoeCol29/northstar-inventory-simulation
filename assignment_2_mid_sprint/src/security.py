import hmac
import hashlib
import json
from fastapi import HTTPException, Request

SECRET_KEY = "northstar_secret_key_2026" # In production, use environment variables

def verify_signature(request: Request, payload: bytes) -> bool:
    """
    Verifies the HMAC-SHA256 signature sent by the warehouse.
    Prevents spoofed requests.
    """
    signature_header = request.headers.get("X-Signature")
    if not signature_header:
        return False

    # Calculate expected signature
    expected_sig = hmac.new(
        SECRET_KEY.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()

    # Constant-time comparison to prevent timing attacks
    return hmac.compare_digest(signature_header, expected_sig)
