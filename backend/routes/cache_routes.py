from fastapi import APIRouter
from backend.memory.redis_client import set_cache, get_cache, delete_cache

router = APIRouter(prefix="/cache", tags=["Redis Cache"])


@router.post("/set")
def set_cache_value(key: str, value: str):
    set_cache(key, value)

    return {
        "message": "Cache value stored",
        "key": key,
        "value": value
    }


@router.get("/get")
def get_cache_value(key: str):
    value = get_cache(key)

    return {
        "key": key,
        "value": value
    }


@router.delete("/delete")
def delete_cache_value(key: str):
    delete_cache(key)

    return {
        "message": "Cache value deleted",
        "key": key
    }