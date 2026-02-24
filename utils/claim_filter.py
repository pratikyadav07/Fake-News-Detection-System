def has_fake_claim_pattern(text):
    red_flags = [
        "10 lakh",
        "free money",
        "without registration",
        "every citizen",
        "all citizens",
        "cash transfer",
        "money to everyone",
        "no documents required"
    ]

    text = text.lower()
    return any(flag in text for flag in red_flags)