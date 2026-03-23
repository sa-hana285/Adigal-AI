import json
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
import os

#multilingual embedding (IMPORTANT)
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.Client()

collection = client.create_collection(
    name="silappatikaram",
    embedding_function=embedding_function
)
with open("silappatikaram_full.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Loaded:", len(data))

documents = []
metadatas = []
ids = []

for i, item in enumerate(data):
    text = f"""
    Title: {item['title']}
    Verse: {item['verse']}
    Explanation: {item['urai']}
    """

    documents.append(text)

    metadatas.append({
        "title": item["title"],
        "source": item["source"]
    })

    ids.append(str(i))

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("Stored in ChromaDB ✅")

query = "Why did Kannagi get angry?"

results = collection.query(
    query_texts=[query],
    n_results=2
)

retrieved_docs = results["documents"][0]

#Build trimmed context (IMPORTANT)
context = ""

for doc in retrieved_docs:
    if "Explanation:" in doc:
        explanation_part = doc.split("Explanation:")[1]
        context += explanation_part[:800] + "\n\n"
    else:
        context += doc[:500] + "\n\n"   # fallback


client_llm = client_llm = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Prompt
prompt = f"""
You are an expert in Tamil literature.

The following context is from the classical Tamil text Silappatikaram.

Instructions:
- Carefully understand the Tamil content.
- Explain the meaning in clear and simple English.
- Do NOT translate word-by-word.
- Focus on the story, events, and meaning.
- If multiple contexts are given, combine them meaningfully.

Context:
{context}

Question:
{query}

Final Answer (in simple English):
"""

# LLM call
response = client_llm.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You explain Tamil literature clearly in English."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

answer = response.choices[0].message.content

print("\nFINAL ANSWER:\n")
print(answer)