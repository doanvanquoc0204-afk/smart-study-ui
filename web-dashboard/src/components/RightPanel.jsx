import { notifications, quickActions, tasks } from "../data/dashboardData.js";

export default function RightPanel() {
  return (
    <aside className="space-y-5 xl:w-[360px] xl:shrink-0">
      <PanelCard title="Việc cần làm hôm nay" icon="📋">
        <div className="space-y-5">
          {tasks.map((task) => (
            <label key={task.title} className="group flex cursor-pointer items-start gap-3 rounded-2xl p-2 transition hover:bg-slate-50">
              <input type="checkbox" className="mt-1 h-5 w-5 rounded border-slate-300 text-blue-600 focus:ring-blue-500" />
              <span className="min-w-0 flex-1">
                <span className="block text-sm font-bold text-slate-900 group-hover:text-blue-700">{task.title}</span>
                <span className="mt-1 block text-xs font-semibold text-slate-500">{task.code}</span>
              </span>
              <span className={`pt-1 text-xs font-semibold ${task.urgent ? "text-rose-500" : "text-slate-500"}`}>{task.deadline}</span>
            </label>
          ))}
        </div>
        <button className="mt-5 w-full rounded-xl py-2 text-sm font-bold text-blue-600 transition hover:bg-blue-50">
          Xem tất cả (6) →
        </button>
      </PanelCard>

      <PanelCard title="AI Assistant" icon="🤖">
        <p className="mb-4 text-sm font-medium text-slate-500">Hỏi đáp, tóm tắt và hỗ trợ học tập</p>
        <button className="w-full rounded-xl bg-blue-600 py-3 text-sm font-extrabold text-white shadow-lg shadow-blue-200 transition hover:-translate-y-0.5 hover:bg-blue-700">
          💬 Chat với AI
        </button>
      </PanelCard>

      <PanelCard title="Truy cập nhanh" icon="🟡">
        <div className="grid grid-cols-2 gap-3">
          {quickActions.map((action) => (
            <button
              key={action.label}
              className="flex items-center justify-center gap-2 rounded-2xl bg-slate-50 px-3 py-4 text-sm font-bold text-slate-700 transition hover:-translate-y-0.5 hover:bg-blue-50 hover:text-blue-700"
            >
              <span className={action.color}>{action.icon}</span>
              {action.label}
            </button>
          ))}
        </div>
      </PanelCard>

      <PanelCard title="Thông báo" icon="🔔">
        <div className="space-y-4">
          {notifications.map((notification) => (
            <div key={notification.text} className="flex gap-3 rounded-2xl p-2 transition hover:bg-slate-50">
              <span className={`mt-1 text-sm ${notification.color}`}>{notification.icon}</span>
              <div>
                <p className="text-sm font-semibold text-slate-800">{notification.text}</p>
                <p className="mt-1 text-xs font-medium text-slate-400">{notification.time}</p>
              </div>
            </div>
          ))}
        </div>
        <button className="mt-5 w-full rounded-xl py-2 text-sm font-bold text-blue-600 transition hover:bg-blue-50">
          Xem tất cả thông báo →
        </button>
      </PanelCard>
    </aside>
  );
}

function PanelCard({ title, icon, children }) {
  return (
    <section className="rounded-3xl border border-slate-200 bg-white p-5 shadow-card transition duration-200 hover:shadow-soft">
      <div className="mb-4 flex items-center gap-3">
        <span className="grid h-9 w-9 place-items-center rounded-2xl bg-blue-50 text-lg">{icon}</span>
        <h3 className="text-lg font-extrabold text-slate-950">{title}</h3>
      </div>
      {children}
    </section>
  );
}
