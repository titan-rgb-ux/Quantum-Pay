from backend.security.hashing import sha3_256_hex

def test_sha3():
    digest = sha3_256_hex("QuantumPay")
    assert len(digest) == 64
    assert digest == sha3_256_hex("QuantumPay")
