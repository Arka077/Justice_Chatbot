# rag_indexer.py

import os
from serpapi import GoogleSearch
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
load_dotenv()

# === Embedding Model ===
EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
EMBED_DIM = 384
INDEX_NAME = "rag-index"
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# === Pinecone Setup ===
pc = Pinecone(api_key=PINECONE_API_KEY)
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=EMBED_DIM,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(INDEX_NAME)

# === Fetch legal content from Google ===
def fetch_legal_web_results(query: str, num_results=10):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results,
        "hl": "en",
        "gl": "in"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    content = []
    for i, res in enumerate(results.get("organic_results", [])):
        text = f"{res.get('title', '')}. {res.get('snippet', '')}"
        metadata = {"source": res.get("link"), "rank": i+1}
        content.append((f"query-{query.replace(' ', '_')}-result-{i}", text, metadata))
    
    return content

# === Main entry for live indexing ===
def index_query_from_google(query: str):
    entries = fetch_legal_web_results(query)
    if not entries:
        print(f"❌ No results found for: {query}")
        return

    ids = [entry[0] for entry in entries]
    texts = [entry[1] for entry in entries]
    metas = [entry[2] for entry in entries]

    embeddings = EMBED_MODEL.encode(texts, show_progress_bar=False)
    vectors = [(ids[i], embeddings[i].tolist(), {**metas[i], "text": texts[i]}) for i in range(len(texts))]
    index.upsert(vectors)
    print(f"✅ Indexed {len(texts)} chunks for query: '{query}'")
