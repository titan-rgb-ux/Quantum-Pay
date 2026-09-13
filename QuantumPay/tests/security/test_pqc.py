from backend.security.pqc import ml_dsa_65_demo_signature, verify_ml_dsa_65_demo

def test_demo_pqc():
    message = "high-risk transaction"
    sig = ml_dsa_65_demo_signature(message)
    assert verify_ml_dsa_65_demo(message, sig)
    assert not verify_ml_dsa_65_demo("tampered", sig)
