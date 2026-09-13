from sqlalchemy.orm import Session
from ..models import User
from .challenges import create_challenge

def start_registration(db: Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise ValueError("User must be created before registration")
    return create_challenge(db, username, "registration")

def complete_registration(db: Session, username: str, challenge: str, credential_id: str, public_key: str):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise ValueError("User not found")
    if user.credential_id:
        raise ValueError("Credential already registered")
    from .challenges import consume_challenge
    if not consume_challenge(db, username, challenge, "registration"):
        raise ValueError("Invalid or expired registration challenge")
    user.credential_id = credential_id
    user.public_key = public_key
    user.credential_type = "Ed25519-demo"
    db.commit()
    db.refresh(user)
    return user
