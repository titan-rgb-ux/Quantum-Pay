from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    display_name = Column(String(150), nullable=False)
    wallet_balance = Column(Float, default=10000.0, nullable=False)
    credential_id = Column(Text, nullable=True, unique=True)
    public_key = Column(Text, nullable=True)
    credential_type = Column(String(50), default="Ed25519-demo")
    credential_revoked = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, index=True)
    challenge = Column(String(128), nullable=False, unique=True)
    purpose = Column(String(30), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False, nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String(64), unique=True, nullable=False, index=True)
    sender = Column(String(100), nullable=False)
    receiver = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    risk_level = Column(String(20), nullable=False)
    transaction_hash = Column(String(64), nullable=False)
    pqc_required = Column(Boolean, default=False, nullable=False)
    status = Column(String(30), default="SUCCESS", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditEvent(Base):
    __tablename__ = "audit_events"
    id = Column(Integer, primary_key=True)
    event_type = Column(String(100), nullable=False)
    transaction_id = Column(String(64), nullable=True)
    event_hash = Column(String(64), nullable=False)
    previous_hash = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
