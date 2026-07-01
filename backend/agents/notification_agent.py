from datetime import datetime
from uuid import uuid4

NOTIFICATIONS = []


def create_notification(
    title: str,
    message: str,
    priority: str = "medium",
    category: str = "general"
):
    notification = {
        "notification_id": str(uuid4()),
        "title": title,
        "message": message,
        "priority": priority,
        "category": category,
        "read": False,
        "created_at": datetime.utcnow().isoformat()
    }

    NOTIFICATIONS.append(notification)

    return notification


def get_notifications():
    return {
        "count": len(NOTIFICATIONS),
        "notifications": NOTIFICATIONS
    }