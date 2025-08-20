import os
from serpapi import GoogleSearch

api_key = "844a6545ac4147d69590c0c880572f5c68c48500be5034e290b391d40a34f3a6"

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
