import { useEffect, useState } from "react";
import { api } from "../services/api";

export function useDashboard() {
    const [summary, setSummary] = useState<any>(null);

    useEffect(() => {
        api.get("/analytics/summary")
            .then((res) => setSummary(res.data));
    }, []);

    return {
        summary,
    };
}