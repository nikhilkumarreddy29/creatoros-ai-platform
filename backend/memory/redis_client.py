import redis
from backend.config import settings


redis_client = redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)


def set_cache(key: str, value: str, expiry_seconds: int = 300):
    redis_client.setex(key, expiry_seconds, value)


def get_cache(key: str):
    return redis_client.get(key)


def delete_cache(key: str):
    redis_client.delete(key)