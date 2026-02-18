def normalize(text):
    return text.lower()


def verify_facts(entities, text):
    """
    Returns:
    status: OK | SUSPICIOUS | FALSE
    reasons: list
    """

    text = normalize(text)

    # ---------- HARD FACT OVERRIDES ----------
    if "mukesh ambani" in text and "net worth" in text:
        if "billion" in text:
            return "OK", ["Net worth stated in billions (plausible range)"]
        if "million" in text:
            return "FALSE", ["Net worth in millions is unrealistic"]

    # ---------- GENERIC NUMERIC CHECK ----------
    for num in entities.get("NUMBERS", []):
        try:
            value = float(num[0])
            unit = num[1].lower() if len(num) > 1 else ""

            if unit == "":
                return "SUSPICIOUS", [
                    "Numeric value mentioned without unit"
                ]

            if unit == "million" and value > 500:
                return "SUSPICIOUS", [
                    "Unusually high million-based claim"
                ]

        except:
            pass

    return "OK", []
