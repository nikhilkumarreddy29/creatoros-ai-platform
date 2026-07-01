from fastapi import APIRouter
from backend.simulated_data import get_analytics_timeseries, get_genre_breakdown
from backend.simulated_data import (
    get_youtube_metrics,
    get_linkedin_metrics
)
router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)
@router.get("/youtube")
def youtube():
    return get_youtube_metrics()

@router.get("/linkedin")
def linkedin():
    return get_linkedin_metrics()
@router.get("/timeseries")
def analytics_timeseries():
    return {
        "data": get_analytics_timeseries()
    }


@router.get("/genre-breakdown")
def genre_breakdown():
    return {
        "data": get_genre_breakdown()
    }