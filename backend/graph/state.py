from typing import TypedDict


class CreatorState(TypedDict):
    topic: str
    genre: str

    sentiment_status: str

    trend_status: str

    draft_status: str

    approval_required: bool

    final_result: dict