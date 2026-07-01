from pathlib import Path


KNOWLEDGE_PATH = Path("data/creator_knowledge_base.txt")


def load_knowledge_base():
    if not KNOWLEDGE_PATH.exists():
        return ""

    return KNOWLEDGE_PATH.read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = 500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def simple_keyword_search(query: str, top_k: int = 3):
    text = load_knowledge_base()
    chunks = chunk_text(text)

    query_words = query.lower().split()

    scored_chunks = []

    for chunk in chunks:
        score = 0
        chunk_lower = chunk.lower()

        for word in query_words:
            if word in chunk_lower:
                score += 1

        scored_chunks.append(
            {
                "chunk": chunk,
                "score": score
            }
        )

    scored_chunks.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return [
        item for item in scored_chunks[:top_k]
        if item["score"] > 0
    ]


def rag_answer(query: str):
    results = simple_keyword_search(query)

    if not results:
        return {
            "query": query,
            "answer": "No relevant knowledge found.",
            "sources": []
        }

    context = "\n\n".join(
        item["chunk"] for item in results
    )

    answer = (
        "Based on the CreatorOS knowledge base:\n\n"
        f"{context}\n\n"
        "Use the above source material to create safe, practical, and brand-aligned content."
    )

    return {
        "query": query,
        "answer": answer,
        "sources": results
    }