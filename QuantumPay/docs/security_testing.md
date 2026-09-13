# Security Testing

| ID | Test | Expected |
|---|---|---|
| TC01 | Normal authentication | Accepted |
| TC02 | Replay old challenge | Rejected |
| TC03 | Invalid signature | Rejected |
| TC04 | Wrong credential | Rejected |
| TC05 | Revoked credential | Rejected |
| TC06 | Alter transaction fields | SHA3 digest changes |
| TC07 | High-risk transaction | HIGH + PQC-required flag |
| TC08 | Audit chain | Previous hash links events |

The ML-DSA-65 portion in this starter repository is intentionally a demo placeholder, not a cryptographic implementation.
