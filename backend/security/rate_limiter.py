import time
from fastapi import HTTPException
from backend.memory.redis_client import redis_client


def check_rate_limit(
    key: str,
    limit: int = 30,
    window_seconds: int = 60
):
    current_window = int(time.time() // window_seconds)
    redis_key = f"rate_limit:{key}:{current_window}"

    count = redis_client.incr(redis_key)
    redis_client.expire(redis_key, window_seconds)

    if count > limit:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    return {
        "allowed": True,
        "count": count,
        "limit": limit,
        "window_seconds": window_seconds
    }