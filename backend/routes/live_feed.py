import asyncio
from datetime import datetime
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.agents.notification_agent import NOTIFICATIONS

router = APIRouter(tags=["Real-Time Live Feed"])


@router.websocket("/stream/live-feed")
async def live_feed(websocket: WebSocket):
    await websocket.accept()

    last_notification_count = 0

    try:
        while True:
            event = {
                "type": "live_metric_update",
                "message": "CreatorOS live feed update",
                "youtube_views_delta": 25,
                "linkedin_impressions_delta": 40,
                "timestamp": datetime.utcnow().isoformat()
            }

            await websocket.send_json(event)

            if len(NOTIFICATIONS) > last_notification_count:
                new_notifications = NOTIFICATIONS[last_notification_count:]

                for notification in new_notifications:
                    await websocket.send_json({
                        "type": "notification",
                        "data": notification
                    })

                last_notification_count = len(NOTIFICATIONS)

            await asyncio.sleep(3)

    except WebSocketDisconnect:
        print("Client disconnected from live feed")