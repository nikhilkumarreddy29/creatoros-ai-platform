import { Activity, Play, Share2, TrendingUp } from "lucide-react";

interface Props {
    summary: any;
    growthIdeas: number;
}

export default function DashboardCards({
    summary,
    growthIdeas,
}: Props) {

    return (

        <div className="mt-8 grid grid-cols-1 gap-6 md:grid-cols-4">

            <Card
                title="YouTube Views"
                value={summary?.youtube?.views_today ?? "-"}
                icon={<Play />}
            />

            <Card
                title="LinkedIn Impressions"
                value={summary?.linkedin?.post_impressions_today ?? "-"}
                icon={<Share2 />}
            />

            <Card
                title="Total Reach"
                value={summary?.total_reach_today ?? "-"}
                icon={<Activity />}
            />

            <Card
                title="Growth Ideas"
                value={growthIdeas}
                icon={<TrendingUp />}
            />

        </div>

    );
}

function Card({ title, value, icon }: any) {

    return (

        <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6">

            <div className="flex justify-between">

                <p>{title}</p>

                {icon}

            </div>

            <p className="mt-5 text-4xl font-bold">

                {value}

            </p>

        </div>

    );

}