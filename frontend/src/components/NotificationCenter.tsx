import { Bell, Trash2 } from "lucide-react";

interface Props {
  notifications: any[];
  clearNotifications: () => void;
}

export default function NotificationCenter({
  notifications,
  clearNotifications,
}: Props) {
  return (
    <section className="mt-6 rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-xl">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2 text-cyan-300">
          <Bell size={22} />
          <h3 className="text-xl font-bold text-white">Notification Center</h3>
          <span className="rounded-full bg-cyan-500 px-3 py-1 text-xs font-bold text-slate-950">
            {notifications.length}
          </span>
        </div>

        <button
          onClick={clearNotifications}
          className="flex items-center gap-2 rounded-lg bg-red-500 px-3 py-2 text-sm font-bold text-white hover:bg-red-400"
        >
          <Trash2 size={16} />
          Clear
        </button>
      </div>

      <div className="mt-4 space-y-3">
        {notifications.length === 0 ? (
          <p className="text-slate-400">No notifications yet.</p>
        ) : (
          notifications.map((item, index) => (
            <div
              key={index}
              className="rounded-xl border border-slate-700 bg-slate-800 p-4"
            >
              <p className="font-bold text-cyan-300">
                {item.title || item.type || "CreatorOS Alert"}
              </p>

              <p className="mt-1 text-sm text-slate-200">
                {item.message || item?.data?.message || JSON.stringify(item)}
              </p>

              <p className="mt-2 text-xs text-slate-400">
                {item.created_at || item.timestamp || item?.data?.created_at || "live"}
              </p>
            </div>
          ))
        )}
      </div>
    </section>
  );
}