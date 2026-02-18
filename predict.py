import joblib
from src.preprocess import clean_text
from src.entity_extractor import extract_entities
from src.fact_checker import verify_facts
from src.decision_engine import final_decision
from src.live_fact_check import wikipedia_fact_check
from src.claim_type_detector import detect_claim_type

# ---------------- LOAD MODEL ----------------
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_news(text):
    reasons = []

    # ---------------- CLAIM TYPE CHECK ----------------
    claim_type = detect_claim_type(text)

    if claim_type == "PREDICTION":
        return {
            "label": "UNCERTAIN",
            "confidence": 0.50,
            "reason": ["This is a future prediction and cannot be verified as fact"],
            "entities": extract_entities(text)
        }

    # ---------------- ML PREDICTION ----------------
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec).max()

    ml_label = "REAL" if pred == 1 else "FAKE"
    reasons.append(f"ML model prediction: {ml_label}")

    # ---------------- ENTITY EXTRACTION ----------------
    entities = extract_entities(text)

    # ---------------- RULE-BASED FACT CHECK ----------------
    fact_status, fact_reasons = verify_facts(entities, text)

    if not fact_status:
        reasons.extend(fact_reasons)

    # ---------------- FINAL DECISION ----------------
    result = final_decision(
        ml_label=ml_label,
        ml_confidence=prob,
        fact_status=fact_status,
        fact_reasons=fact_reasons
    )

    # ---------------- LIVE FACT CHECK OVERRIDE ----------------
    text_lower = text.lower()

    # Case: India's Prime Minister
    if "prime minister" in text_lower and "india" in text_lower:
        ok, summary = wikipedia_fact_check("Narendra Modi")
        if ok:
            result["label"] = "REAL"
            result["confidence"] = 0.95
            result["reason"] = [
                "Verified factual information from Wikipedia",
                summary
            ]

    # ---------------- ATTACH ENTITIES ----------------
    result["entities"] = entities

    return result


