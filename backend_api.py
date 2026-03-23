import json
import os
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

# 1. Initialize ChromaDB (Matches rag_chroma.py)
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="silappatikaram",
    embedding_function=embedding_function
)

# 2. Pre-populate database if empty
def populate_db():
    try:
        if collection.count() == 0:
            print("Populating ChromaDB...")
            with open("silappatikaram_full.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            documents, metadatas, ids = [], [], []
            for i, item in enumerate(data):
                text = f"Title: {item['title']}\nVerse: {item['verse']}\nExplanation: {item['urai']}"
                documents.append(text)
                metadatas.append({"title": item["title"], "source": item["source"]})
                ids.append(str(i))
                
            collection.add(documents=documents, metadatas=metadatas, ids=ids)
            print("ChromaDB Populated ✅")
    except Exception as e:
        print(f"Db population warning: {e}")

populate_db()

@app.post("/api/chat")
async def chat(request: QueryRequest):
    try:
        # ChromaDB Query
        results = collection.query(query_texts=[request.query], n_results=2)
        retrieved_docs = results["documents"][0]

        context = ""
        for doc in retrieved_docs:
            if "Explanation:" in doc:
                context += doc.split("Explanation:")[1][:800] + "\n\n"
            else:
                context += doc[:500] + "\n\n"

        # LLM Groq Call
        client_llm = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        prompt = f"""
You are an exclusive expert on the Tamil epic Silappatikaram.

Carefully understand the Tamil context and explain the meaning in simple English.
Do NOT translate word-by-word. Focus on story events.

⚠️ CRITICAL RULE:
If the question is UNRELATED to Silappatikaram (e.g., general knowledge, math, science, recipe instructions, arithmetic, or other books), you MUST politely refuse to answer. 
You are solely dedicated to answering questions about Silappatikaram. Do NOT answer off-topic queries under any circumstances.

Context:
{context}


Question:
{request.query}

Final Answer (in simple English):
"""

        response = client_llm.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You explain Tamil literature clearly in English."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return {"answer": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=5000)
