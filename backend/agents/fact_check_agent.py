RISKY_CLAIM_WORDS = [
    "guaranteed",
    "100%",
    "always",
    "never",
    "best in the world",
    "number one",
    "proven cure",
    "officially confirmed",
]


def run_fact_check(text: str):
    lowered = text.lower()

    risky_claims = [
        word for word in RISKY_CLAIM_WORDS
        if word in lowered
    ]

    if risky_claims:
        status = "needs_review"
        fact_safe = False
        reason = "Draft contains strong factual/marketing claims that need human verification."
    else:
        status = "passed"
        fact_safe = True
        reason = "No risky factual claims detected."

    return {
        "agent": "Fact Checking Agent",
        "status": status,
        "fact_safe": fact_safe,
        "risky_claims": risky_claims,
        "reason": reason
    }