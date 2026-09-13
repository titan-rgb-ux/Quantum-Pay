from datetime import datetime
from pydantic import BaseModel, Field

class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    display_name: str = Field(min_length=1, max_length=150)

class ChallengeRequest(BaseModel):
    username: str = Field(min_length=3, max_length=100)

class ChallengeResponse(BaseModel):
    challenge: str
    expires_at: datetime

class RegisterComplete(BaseModel):
    username: str
    challenge: str
    credential_id: str
    public_key: str

class LoginComplete(BaseModel):
    username: str
    challenge: str
    credential_id: str
    signature: str

class TransactionCreate(BaseModel):
    sender: str
    receiver: str
    amount: float = Field(gt=0)
    challenge: str
    signature: str
    credential_id: str

class TransactionResponse(BaseModel):
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    risk_level: str
    transaction_hash: str
    pqc_required: bool
    status: str
    created_at: datetime
