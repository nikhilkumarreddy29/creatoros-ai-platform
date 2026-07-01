import re


EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_PATTERN = r"\b\d{10}\b"


def mask_pii(text: str):
    text = re.sub(EMAIL_PATTERN, "[EMAIL_MASKED]", text)
    text = re.sub(PHONE_PATTERN, "[PHONE_MASKED]", text)

    return text