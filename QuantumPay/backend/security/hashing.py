import hashlib
import json

def canonical_transaction(sender: str, receiver: str, amount: float, transaction_id: str, session: str, challenge: str, timestamp: str) -> str:
    data = {
        "sender": sender,
        "receiver": receiver,
        "amount": round(amount, 2),
        "transaction_id": transaction_id,
        "session": session,
        "challenge": challenge,
        "timestamp": timestamp,
    }
    return json.dumps(data, separators=(",", ":"), sort_keys=True)

def sha3_256_hex(data: str) -> str:
    return hashlib.sha3_256(data.encode()).hexdigest()
