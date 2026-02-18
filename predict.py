import joblib
from .preprocess import clean_text
from .entity_extractor import extract_entities
from .fact_checker import verify_facts
from .decision_engine import final_decision

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_news(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec).max()

    ml_label = "REAL" if pred == 1 else "FAKE"

    entities = extract_entities(text)
    fact_status, fact_reasons = verify_facts(entities, text)

    result = final_decision(
        ml_label=ml_label,
        ml_confidence=prob,
        fact_status=fact_status,
        fact_reasons=fact_reasons
    )

    result["entities"] = entities
    return result

