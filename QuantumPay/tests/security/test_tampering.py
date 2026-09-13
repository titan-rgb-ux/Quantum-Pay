from backend.security.hashing import sha3_256_hex

def test_tampering_changes_hash():
    a = sha3_256_hex("receiver=bob&amount=100")
    b = sha3_256_hex("receiver=mallory&amount=100")
    assert a != b
