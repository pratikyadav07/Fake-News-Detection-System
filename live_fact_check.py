import requests

def wikipedia_fact_check(query):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return True, data.get("extract", "")
        else:
            return False, "No reliable source found"

    except:
        return False, "Live verification failed"
