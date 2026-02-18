def detect_claim_type(text):
    """
    Detect whether a claim is:
    - FACTUAL (present/past verifiable)
    - PREDICTION (future claim)
    """

    text = text.lower()

    future_keywords = [
        "will",
        "shall",
        "going to",
        "by 2030",
        "by 2027",
        "in future",
        "expected to",
        "soon",
        "next year",
        "next decade"
    ]

    for word in future_keywords:
        if word in text:
            return "PREDICTION"

    return "FACTUAL"
