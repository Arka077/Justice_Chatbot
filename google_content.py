import os
from serpapi import GoogleSearch

api_key = os.getenv("SERPAPI_KEY")

params = {
    "engine": "google",
    "q": "latest technology trends",
    "api_key": api_key,
    "num": 10
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results.get("organic_results", []):
    print(f"Title: {result.get('title')}")
    print(f"Link: {result.get('link')}")
    print(f"Snippet: {result.get('snippet')}")
    print("--------")
