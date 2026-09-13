import hashlib
from sqlalchemy.orm import Session
from ..models import AuditEvent

def add_audit_event(db: Session, event_type: str, transaction_id: str | None = None):
    previous = db.query(AuditEvent).order_by(AuditEvent.id.desc()).first()
    previous_hash = previous.event_hash if previous else "GENESIS"
    raw = f"{previous_hash}|{event_type}|{transaction_id or ''}"
    event_hash = hashlib.sha3_256(raw.encode()).hexdigest()
    item = AuditEvent(event_type=event_type, transaction_id=transaction_id,
                      event_hash=event_hash, previous_hash=previous_hash)
    db.add(item)
    db.commit()
    return item
