def assess_risk(amount: float, receiver: str, abnormal: bool = False) -> str:
    if abnormal or amount >= 5000:
        return "HIGH"
    if amount >= 1000:
        return "MEDIUM"
    return "LOW"

def pqc_required(risk_level: str) -> bool:
    return risk_level == "HIGH"
