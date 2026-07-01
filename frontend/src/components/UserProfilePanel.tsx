import { User, ShieldCheck, Radio, Settings } from "lucide-react";

export default function UserProfilePanel() {
  return (
    <section className="mt-6 rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-xl">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-500 text-2xl font-extrabold text-slate-950">
            N
          </div>

          <div>
            <h3 className="text-2xl font-bold text-white">
              Nikhil Creator Workspace
            </h3>
            <p className="mt-1 text-sm font-medium text-slate-300">
              CreatorOS AI Platform · Admin / Creator
            </p>
          </div>
        </div>

        <button className="rounded-xl border border-slate-600 bg-slate-800 px-4 py-2 font-bold text-slate-100 hover:border-cyan-400 hover:bg-slate-700">
          <Settings size={18} className="inline-block mr-2" />
          Settings
        </button>
      </div>

      <div className="mt-6 grid grid-cols-1 gap-4 md:grid-cols-4">
        <ProfileStat
          icon={<User />}
          label="Role"
          value="Creator Admin"
        />

        <ProfileStat
          icon={<Radio />}
          label="Platforms"
          value="YouTube + LinkedIn"
        />

        <ProfileStat
          icon={<ShieldCheck />}
          label="Approval Mode"
          value="Human Review ON"
        />

        <ProfileStat
          icon={<ShieldCheck />}
          label="System Status"
          value="Healthy"
        />
      </div>
    </section>
  );
}

function ProfileStat({ icon, label, value }: any) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-800 p-4 hover:border-cyan-400">
      <div className="flex items-center gap-2 text-cyan-300">
        {icon}
        <p className="text-sm font-bold">{label}</p>
      </div>

      <p className="mt-3 text-lg font-extrabold text-white">
        {value}
      </p>
    </div>
  );
}