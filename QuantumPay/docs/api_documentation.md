# QuantumPay API

Run the backend and open `/docs`.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Health/status |
| POST | `/users` | Create prototype wallet user |
| POST | `/auth/register/start` | Generate registration challenge |
| POST | `/auth/register/complete` | Register credential |
| POST | `/auth/login/start` | Generate login challenge |
| POST | `/auth/login/complete` | Verify signed challenge |
| POST | `/transactions/create` | Create authenticated transaction |
| GET | `/transactions/history/{username}` | Sender transaction history |
| POST | `/auth/revoke/{username}` | Revoke credential |
| POST | `/auth/issue-demo-key/{username}` | Development-only key helper |

For the Android emulator, a Flutter app normally reaches a host-machine backend using `10.0.2.2` instead of `localhost`.
