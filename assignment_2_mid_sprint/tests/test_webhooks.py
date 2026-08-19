import pytest
import hmac
import hashlib
from unittest.mock import Mock
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.security import verify_signature
from src.idempotency import check_idempotency, mark_processed

SECRET_KEY = "northstar_secret_key_2026"

def test_webhook_signature_verification_valid():
    payload = b'{"sku": "ABC123", "quantity": 50}'
    expected_sig = hmac.new(SECRET_KEY.encode('utf-8'), payload, hashlib.sha256).hexdigest()
    mock_request = Mock()
    mock_request.headers = {"X-Signature": expected_sig}
    assert verify_signature(mock_request, payload) is True

def test_webhook_signature_verification_invalid():
    payload = b'{"sku": "ABC123", "quantity": 50}'
    mock_request = Mock()
    mock_request.headers = {"X-Signature": "invalid"}
    assert verify_signature(mock_request, payload) is False

def test_idempotency_check():
    processed_ids = {"id-1", "id-2"}
    assert check_idempotency("id-3", processed_ids) is False
    assert check_idempotency("id-1", processed_ids) is True

def test_mark_processed():
    processed_ids = set()
    mark_processed("new-id-1", processed_ids)
    assert "new-id-1" in processed_ids
