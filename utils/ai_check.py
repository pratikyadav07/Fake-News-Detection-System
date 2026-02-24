import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

def ai_fake_check(news_text):
    api_key = os.getenv("HF_API_KEY")
    if not api_key:
        return "ai_not_available", 0.0

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "inputs": news_text,
        "parameters": {
            "candidate_labels": ["true news", "fake news"]
        }
    }

    try:
        r = requests.post(
            HF_API_URL,
            headers=headers,
            json=payload,
            timeout=20
        )

        # 🔴 HF BUSY / LIMIT
        if r.status_code in [429, 503]:
            return "ai_busy", 0.0

        if r.status_code != 200:
            return "ai_error", 0.0

        result = r.json()

        if "labels" not in result:
            return "ai_loading", 0.0

        return result["labels"][0], result["scores"][0]

    except Exception:
        return "ai_exception", 0.0