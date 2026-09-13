import base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from sqlalchemy.orm import Session
from ..models import User
from .challenges import create_challenge, consume_challenge

def start_login(db: Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    if not user or not user.credential_id or user.credential_revoked:
        raise ValueError("No active credential found")
    return create_challenge(db, username, "login")

def verify_login(db: Session, username: str, challenge: str, credential_id: str, signature: str):
    user = db.query(User).filter_by(username=username).first()
    if not user or user.credential_id != credential_id or user.credential_revoked:
        raise ValueError("Credential rejected")
    if not consume_challenge(db, username, challenge, "login"):
        raise ValueError("Invalid, expired, or replayed challenge")
    try:
        key = Ed25519PublicKey.from_public_bytes(base64.b64decode(user.public_key))
        key.verify(base64.b64decode(signature), challenge.encode())
    except Exception as exc:
        raise ValueError("Invalid signature") from exc
    return user
