from backend.simulated_data import get_video_retention


def run_retention_agent():
    retention_data = get_video_retention()

    points = retention_data["retention_points"]

    drops = []

    for i in range(1, len(points)):
        previous = points[i - 1]["retention"]
        current = points[i]["retention"]

        drop = previous - current

        if drop >= 20:
            drops.append({
                "minute": points[i]["minute"],
                "drop_percentage": drop,
                "severity": "high"
            })

    recommendations = []

    for drop in drops:
        recommendations.append(
            f"Large audience drop detected near minute {drop['minute']}. Improve hook, pacing, or storytelling before this section."
        )

    return {
        "agent": "Retention Analysis Agent",
        "video": retention_data["video_title"],
        "drop_count": len(drops),
        "drops": drops,
        "recommendations": recommendations
    }