GENRES = ["Tech", "Movies", "Sports", "Food", "Friends"]


def classify_genre(text: str):
    text_lower = text.lower()

    if any(word in text_lower for word in ["ai", "python", "langgraph", "coding", "tech", "software"]):
        genre = "Tech"
    elif any(word in text_lower for word in ["movie", "cinema", "trailer", "marvel", "film"]):
        genre = "Movies"
    elif any(word in text_lower for word in ["cricket", "football", "match", "ipl", "sports"]):
        genre = "Sports"
    elif any(word in text_lower for word in ["food", "recipe", "cafe", "biryani", "street food"]):
        genre = "Food"
    elif any(word in text_lower for word in ["friends", "college", "casual", "fun", "reunion"]):
        genre = "Friends"
    else:
        genre = "Tech"

    return {
        "agent": "Genre Classification Agent",
        "input": text,
        "genre": genre,
        "available_genres": GENRES
    }