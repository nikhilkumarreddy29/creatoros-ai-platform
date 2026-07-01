TOXIC_WORDS = [
    "idiot",
    "stupid",
    "hate you",
    "shut up",
    "useless",
    "trash",
    "nonsense",
]


def detect_toxicity(text: str):
    lowered = text.lower()

    detected = [
        word for word in TOXIC_WORDS
        if word in lowered
    ]

    is_toxic = len(detected) > 0

    return {
        "is_toxic": is_toxic,
        "detected_terms": detected,
        "status": "blocked" if is_toxic else "passed"
    }