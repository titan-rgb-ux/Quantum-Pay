from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .config import settings
from .database import Base, engine, get_db
from .models import User, Transaction
from .schemas import (
    UserRegister, ChallengeRequest, ChallengeResponse, RegisterComplete,
    LoginComplete, TransactionCreate, TransactionResponse
)
from .auth.registration import start_registration, complete_registration
from .auth.authentication import start_login, verify_login
from .auth.challenges import create_challenge
from .transactions.transaction import create_transaction

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"project": "QuantumPay", "status": "running", "mode": "academic prototype"}

@app.post("/users", status_code=201)
def create_user(payload: UserRegister, db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=payload.username).first():
        raise HTTPException(409, "Username already exists")
    user = User(username=payload.username, display_name=payload.display_name)
    db.add(user); db.commit(); db.refresh(user)
    return {"id": user.id, "username": user.username, "display_name": user.display_name, "wallet_balance": user.wallet_balance}

@app.post("/auth/register/start", response_model=ChallengeResponse)
def registration_start(payload: ChallengeRequest, db: Session = Depends(get_db)):
    try:
        item = start_registration(db, payload.username)
        return {"challenge": item.challenge, "expires_at": item.expires_at}
    except ValueError as e:
        raise HTTPException(400, str(e))

@app.post("/auth/register/complete")
def registration_complete(payload: RegisterComplete, db: Session = Depends(get_db)):
    try:
        user = complete_registration(db, **payload.model_dump())
        return {"message": "Credential registered", "username": user.username, "credential_id": user.credential_id}
    except ValueError as e:
        raise HTTPException(400, str(e))

@app.post("/auth/login/start", response_model=ChallengeResponse)
def login_start(payload: ChallengeRequest, db: Session = Depends(get_db)):
    try:
        item = start_login(db, payload.username)
        return {"challenge": item.challenge, "expires_at": item.expires_at}
    except ValueError as e:
        raise HTTPException(401, str(e))

@app.post("/auth/login/complete")
def login_complete(payload: LoginComplete, db: Session = Depends(get_db)):
    try:
        user = verify_login(db, **payload.model_dump())
        return {"message": "Authentication successful", "username": user.username, "wallet_balance": user.wallet_balance}
    except ValueError as e:
        raise HTTPException(401, str(e))

@app.post("/transactions/create", response_model=TransactionResponse)
def transaction_create(payload: TransactionCreate, db: Session = Depends(get_db)):
    try:
        tx = create_transaction(db, **payload.model_dump())
        return tx
    except ValueError as e:
        raise HTTPException(400, str(e))

@app.get("/transactions/history/{username}")
def transaction_history(username: str, db: Session = Depends(get_db)):
    return db.query(Transaction).filter_by(sender=username).order_by(Transaction.id.desc()).all()

@app.post("/auth/revoke/{username}")
def revoke_credential(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise HTTPException(404, "User not found")
    user.credential_revoked = True
    db.commit()
    return {"message": "Credential revoked"}

@app.post("/auth/issue-demo-key/{username}")
def issue_demo_key(username: str, db: Session = Depends(get_db)):
    # Development helper: generates a real Ed25519 key pair server-side.
    # Production must use a device/passkey authenticator and never export its private key.
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    import base64
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise HTTPException(404, "User not found")
    private = Ed25519PrivateKey.generate()
    public = private.public_key().public_bytes_raw()
    user.credential_id = base64.urlsafe_b64encode(private.public_key().public_bytes_raw()).decode().rstrip("=")
    user.public_key = base64.b64encode(public).decode()
    user.credential_revoked = False
    db.commit()
    return {
        "username": username,
        "credential_id": user.credential_id,
        "public_key": user.public_key,
        "private_key": base64.b64encode(private.private_bytes_raw()).decode(),
        "warning": "DEVELOPMENT DEMO ONLY. Do not expose private keys in production."
    }
