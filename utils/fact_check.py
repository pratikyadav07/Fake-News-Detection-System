import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fact_check_news(news_text):
    api_key = os.getenv("FACT_CHECK_API_KEY")
    if not api_key:
        return False

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": news_text[:100],
        "key": api_key
    }

    r = requests.get(url, params=params)
    data = r.json()

    return "claims" in data