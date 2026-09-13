from backend.security.risk import assess_risk, pqc_required

def test_risk_levels():
    assert assess_risk(100, "bob") == "LOW"
    assert assess_risk(1000, "bob") == "MEDIUM"
    assert assess_risk(5000, "bob") == "HIGH"
    assert pqc_required("HIGH") is True
    assert pqc_required("LOW") is False
