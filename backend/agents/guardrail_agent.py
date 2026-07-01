SUSPICIOUS_WORDS = [
    "password",
    "api key",
    "secret",
    "token",
    "hack",
    "malware",
    "phishing",
    "click this link immediately",
    "guaranteed money",
]


def run_guardrail_check(text: str):
    lowered = text.lower()

    detected = [
        word for word in SUSPICIOUS_WORDS
        if word in lowered
    ]

    if detected:
        status = "blocked"
        safe_to_publish = False
        reason = "Draft contains unsafe or suspicious content."
    else:
        status = "passed"
        safe_to_publish = True
        reason = "No major safety issue detected."

    return {
        "agent": "Brand Voice Guardrail Agent",
        "status": status,
        "safe_to_publish": safe_to_publish,
        "detected_terms": detected,
        "reason": reason
    }