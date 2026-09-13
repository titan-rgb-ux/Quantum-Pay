# QuantumPay — Hybrid Quantum Passkey Authentication

Academic mini-project prototype implementing the core backend workflow described in the project write-up.

## Included
- FastAPI backend
- SQLite database
- Fresh challenge generation and one-time challenge consumption
- Ed25519 challenge-signature verification
- Transaction risk classification
- SHA3-256 transaction binding
- Audit hash chain
- ML-DSA-65 *simulation flag* for high-risk transactions
- Flutter starter application
- Automated backend/security tests

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
python -m uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

### Demo credential flow
1. POST `/users`
2. POST `/auth/register/start`
3. Generate or use an Ed25519 key pair.
4. POST `/auth/register/complete`.
5. POST `/auth/login/start`.
6. Sign the returned challenge with the private key.
7. POST `/auth/login/complete`.

For a quick development-only bridge, `/auth/issue-demo-key/{username}` returns an Ed25519 private key. Do not use this pattern in production.

## Flutter
Create the Flutter project from the supplied mobile starter files or copy this repository into your Flutter workspace. The starter client targets the FastAPI API.

## Security warning
This is an academic prototype. It is not a real payment system. It does not contain banking integrations, real money transfer, production WebAuthn attestation, or a real ML-DSA-65 implementation.
