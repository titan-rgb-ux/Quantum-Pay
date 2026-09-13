import hashlib

def ml_dsa_65_demo_signature(message: str) -> str:
    # Academic simulation placeholder. This is NOT ML-DSA-65.
    # Replace with an audited ML-DSA implementation for a real PQC deployment.
    return hashlib.sha3_256(("ML-DSA-65-DEMO:" + message).encode()).hexdigest()

def verify_ml_dsa_65_demo(message: str, signature: str) -> bool:
    return ml_dsa_65_demo_signature(message) == signature
