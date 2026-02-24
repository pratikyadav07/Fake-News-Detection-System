import os
import requests
from dotenv import load_dotenv

load_dotenv()

def extract_keywords(text):
    stop_words = {
        "the","is","was","were","to","from","according","of","and",
        "a","an","in","on","for","with","by","officials"
    }

    words = [
        w.lower().strip(".,")
        for w in text.split()
        if w.lower() not in stop_words and len(w) > 3
    ]

    return " ".join(words[:6])  # top keywords only


def check_live_news(news_text):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return False

    keywords = extract_keywords(news_text)

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": keywords,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3
    }

    r = requests.get(url, params=params)
    data = r.json()

    return data.get("totalResults", 0) > 0