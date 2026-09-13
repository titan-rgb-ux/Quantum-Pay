from fastapi.testclient import TestClient
from backend.main import app
client = TestClient(app)

def test_transaction_requires_registered_credential():
    r = client.post("/transactions/create", json={
        "sender": "does-not-exist", "receiver": "bob", "amount": 10,
        "challenge": "x", "signature": "x", "credential_id": "x"
    })
    assert r.status_code == 400
