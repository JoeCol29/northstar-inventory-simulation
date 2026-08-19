import pytest
from src.main import app
from src.security import verify_signature
import json
import hmac
import hashlib

SECRET_KEY = "northstar_secret_key_2026"

def test_webhook_signature_verification():
    """Test that valid signatures pass verification"""
    payload = b'{"test": "data"}'
    signature = hmac.new(
        SECRET_KEY.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    # Simulate request with valid signature
    class MockRequest:
        def __init__(self, sig):
            self.headers = {"X-Signature": sig}
    
    request = MockRequest(signature)
    assert verify_signature(request, payload) == True

def test_webhook_rejection_invalid_signature():
    """Test that invalid signatures are rejected"""
    payload = b'{"test": "data"}'
    
    class MockRequest:
        def __init__(self):
            self.headers = {"X-Signature": "invalid"}
    
    request = MockRequest()
    assert verify_signature(request, payload) == False
