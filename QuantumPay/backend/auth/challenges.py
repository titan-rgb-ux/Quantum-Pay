import base64, secrets
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..config import settings
from ..models import Challenge

def create_challenge(db: Session, username: str, purpose: str) -> Challenge:
    raw = secrets.token_bytes(32)
    value = base64.urlsafe_b64encode(raw).decode().rstrip("=")
    item = Challenge(
        username=username,
        challenge=value,
        purpose=purpose,
        expires_at=datetime.utcnow() + timedelta(seconds=settings.CHALLENGE_TTL_SECONDS),
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def consume_challenge(db: Session, username: str, value: str, purpose: str) -> bool:
    item = db.query(Challenge).filter_by(username=username, challenge=value, purpose=purpose).first()
    if not item or item.used or item.expires_at < datetime.utcnow():
        return False
    item.used = True
    db.commit()
    return True
