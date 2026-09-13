# QuantumPay Architecture

## Runtime
Flutter mobile client -> FastAPI backend -> Authentication / Transactions / Risk / Database.

## Security flow
1. User account is created.
2. Registration issues a fresh challenge.
3. A credential public key is registered.
4. Login issues a fresh challenge.
5. The client signs the challenge with the credential private key.
6. Server verifies the signature.
7. Transactions are bound to sender, receiver, amount, transaction ID, session, challenge and timestamp.
8. SHA3-256 protects the transaction digest.
9. HIGH-risk transactions are marked for the ML-DSA-65 stage.

## Important prototype note
The included `/auth/issue-demo-key/{username}` endpoint is only a development bridge so the repository can be run without a real Android passkey integration. It returns a private Ed25519 key and MUST NOT be used in production.

The included `security/pqc.py` is also a simulation placeholder. It does not implement ML-DSA-65. A real deployment must integrate a vetted ML-DSA-65 implementation.
