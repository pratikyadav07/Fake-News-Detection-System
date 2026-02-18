def final_decision(
    ml_label,
    ml_confidence,
    fact_status,
    fact_reasons
):
    """
    Hybrid decision logic:
    - Fact check overrides ML
    - ML confidence used only if facts are OK
    """

    # ❌ Hard False
    if fact_status == "FALSE":
        return {
            "label": "FAKE",
            "confidence": 0.95,
            "reason": fact_reasons
        }

    # ⚠️ Suspicious
    if fact_status == "SUSPICIOUS":
        return {
            "label": "UNCERTAIN",
            "confidence": 0.55,
            "reason": fact_reasons
        }

    # ✅ Fact OK → trust ML but cap confidence
    if ml_label == "REAL":
        confidence = max(ml_confidence, 0.80)
    else:
        confidence = min(ml_confidence, 0.60)

    return {
        "label": ml_label,
        "confidence": confidence,
        "reason": fact_reasons if fact_reasons else ["ML-based prediction"]
    }
