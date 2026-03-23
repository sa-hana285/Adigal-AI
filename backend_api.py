import json
import os
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

# Globals
embedding_function = None
client = None
collection = None

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "silappatikaram_full.json")

# Populate DB
def populate_db():
    try:
        if collection.count() == 0:
            print("📦 Populating ChromaDB...")

            with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

            documents, metadatas, ids = [], [], []

            for i, item in enumerate(data):
                text = f"Title: {item['title']}\nVerse: {item['verse']}\nExplanation: {item['urai']}"
                documents.append(text)
                metadatas.append({"title": item["title"], "source": item["source"]})
                ids.append(str(i))

            collection.add(documents=documents, metadatas=metadatas, ids=ids)

            print("✅ ChromaDB Populated")

    except Exception as e:
        print(f"⚠️ DB population error: {e}")

# ✅ LIGHTWEIGHT STARTUP (NO HEAVY WORK)
@app.on_event("startup")
async def startup_event():
    global embedding_function, client, collection

    print("🚀 Starting server...")

    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    client = chromadb.Client()

    collection = client.get_or_create_collection(
        name="silappatikaram",
        embedding_function=embedding_function
    )

    print("✅ Server ready (DB will load on first request)")

# Health check
@app.get("/")
def root():
    return {"message": "API is running"}

# Chat endpoint
@app.post("/api/chat")
async def chat(request: QueryRequest):
    global collection

    try:
        # 🔥 LAZY LOAD DB (ONLY FIRST TIME)
        if collection.count() == 0:
            print("⚡ First request → loading DB...")
            populate_db()

        results = collection.query(query_texts=[request.query], n_results=2)
        retrieved_docs = results["documents"][0]

        context = ""
        for doc in retrieved_docs:
            if "Explanation:" in doc:
                context += doc.split("Explanation:")[1][:800] + "\n\n"
            else:
                context += doc[:500] + "\n\n"

        client_llm = Groq(api_key=os.getenv("GROQ_API_KEY"))

        prompt = f"""
You are an exclusive expert on the Tamil epic Silappatikaram.

Carefully understand the Tamil context and explain the meaning in simple English.
Do NOT translate word-by-word. Focus on story events.

⚠️ CRITICAL RULE:
If the question is UNRELATED to Silappatikaram, you MUST politely refuse.

Context:
{context}

Question:
{request.query}

Final Answer:
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