# rag_qa.py

import os
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from mistral_api import call_mistral

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "your_pinecone_key")
INDEX_NAME = "rag-index"

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def search_index_for_context(query: str, top_k=5):
    embedding = EMBED_MODEL.encode(query).tolist()
    results = index.query(vector=embedding, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]

def answer_query_with_context(query: str):
    context_chunks = search_index_for_context(query)
    context = "\n\n".join(context_chunks)
    
    prompt = f"""
You are a professional legal assistant. Provide a clear, confident, and helpful answer to the user's question using only the information below.

Do not mention that the information comes from a context or document. Respond naturally, as if giving direct legal guidance.

If the information below does not contain a relevant answer, respond with:
"I’m sorry, I don’t have enough information to answer that accurately."

-------------
Information:
{context}
-------------

User Question: {query}
"""
    return call_mistral(prompt)
