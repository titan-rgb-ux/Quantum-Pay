import base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from fastapi.testclient import TestClient
from backend.main import app
client = TestClient(app)

def test_register_and_login():
    username = "test_auth_user"
    client.post("/users", json={"username": username, "display_name": "Test User"})
    r = client.post("/auth/register/start", json={"username": username})
    assert r.status_code == 200
    challenge = r.json()["challenge"]

    private = Ed25519PrivateKey.generate()
    public = private.public_key().public_bytes_raw()
    credential_id = base64.urlsafe_b64encode(public).decode().rstrip("=")
    public_b64 = base64.b64encode(public).decode()
    r = client.post("/auth/register/complete", json={
        "username": username, "challenge": challenge,
        "credential_id": credential_id, "public_key": public_b64
    })
    assert r.status_code == 200

    r = client.post("/auth/login/start", json={"username": username})
    challenge = r.json()["challenge"]
    sig = private.sign(challenge.encode())
    r = client.post("/auth/login/complete", json={
        "username": username, "challenge": challenge,
        "credential_id": credential_id,
        "signature": base64.b64encode(sig).decode()
    })
    assert r.status_code == 200
