from backend.security.pii_detector import mask_pii
from backend.security.toxicity_detector import detect_toxicity


def run_toxicity_agent(text: str):
    masked_text = mask_pii(text)
    result = detect_toxicity(masked_text)

    return {
        "agent": "Toxicity Detection Agent",
        "text": masked_text,
        **result
    }