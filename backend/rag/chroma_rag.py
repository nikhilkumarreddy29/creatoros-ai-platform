from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer


KNOWLEDGE_PATH = Path("data/creator_knowledge_base.txt")
CHROMA_PATH = "data/chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name="creatoros_knowledge"
)


def load_knowledge_base():
    return KNOWLEDGE_PATH.read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = 500):
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


def ingest_knowledge_base():
    text = load_knowledge_base()
    chunks = chunk_text(text)

    ids = []
    embeddings = []
    documents = []

    for index, chunk in enumerate(chunks):
        ids.append(f"chunk_{index}")
        documents.append(chunk)
        embeddings.append(
            model.encode(chunk).tolist()
        )

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    return {
        "message": "Knowledge base ingested into ChromaDB",
        "chunks_count": len(chunks)
    }


def vector_search(query: str, top_k: int = 3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "query": query,
        "results": results
    }