import secrets
from datetime import datetime
from sqlalchemy.orm import Session
from ..models import User, Transaction
from ..security.hashing import canonical_transaction, sha3_256_hex
from ..security.risk import assess_risk, pqc_required
from ..transactions.audit import add_audit_event

def create_transaction(db: Session, sender: str, receiver: str, amount: float, challenge: str, credential_id: str, signature: str):
    user = db.query(User).filter_by(username=sender).first()
    if not user or user.credential_id != credential_id or user.credential_revoked:
        raise ValueError("Sender credential rejected")
    if user.wallet_balance < amount:
        raise ValueError("Insufficient balance")
    tx_id = secrets.token_hex(16)
    timestamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    risk = assess_risk(amount, receiver)
    pqc = pqc_required(risk)
    canonical = canonical_transaction(sender, receiver, amount, tx_id, "wallet-session", challenge, timestamp)
    tx_hash = sha3_256_hex(canonical)

    tx = Transaction(transaction_id=tx_id, sender=sender, receiver=receiver, amount=amount,
                    risk_level=risk, transaction_hash=tx_hash, pqc_required=pqc, status="SUCCESS")
    user.wallet_balance -= amount
    db.add(tx)
    db.commit()
    db.refresh(tx)
    add_audit_event(db, "TRANSACTION_CREATED", tx_id)
    return tx
