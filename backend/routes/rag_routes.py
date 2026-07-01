from fastapi import APIRouter
from backend.rag.simple_rag import rag_answer, simple_keyword_search
from backend.rag.chroma_rag import ingest_knowledge_base, vector_search




router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.get("/search")
def search_rag(query: str):
    return {
        "query": query,
        "results": simple_keyword_search(query)
    }


@router.get("/answer")
def answer_rag(query: str):
    return rag_answer(query)

@router.post("/ingest")
def ingest_rag():
    return ingest_knowledge_base()


@router.get("/vector-search")
def rag_vector_search(query: str):
    return vector_search(query)