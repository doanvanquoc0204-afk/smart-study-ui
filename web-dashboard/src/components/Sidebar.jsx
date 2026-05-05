const menuItems = [
  ["Tổng quan", "🏠", true],
  ["Lịch học", "🗓", false],
  ["Đề thi", "📄", false],
  ["Tài liệu", "📁", false],
  ["AI Assistant", "🤖", false],
  ["Thống kê", "📊", false],
  ["Cài đặt", "⚙", false]
];

export default function Sidebar() {
  return (
    <aside className="fixed inset-y-0 left-0 z-20 hidden w-[270px] border-r border-slate-200/80 bg-white/95 px-4 py-7 shadow-soft backdrop-blur lg:flex lg:flex-col">
      <div className="mb-10 flex items-center gap-3 px-2">
        <div className="grid h-12 w-12 place-items-center rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 text-2xl text-white shadow-lg shadow-blue-200">
          🎓
        </div>
        <div>
          <h1 className="text-xl font-extrabold tracking-tight text-slate-950">SmartStudy AI</h1>
          <p className="text-xs font-medium text-slate-500">Học thông minh, hiệu quả hơn</p>
        </div>
      </div>

      <nav className="space-y-2">
        {menuItems.map(([label, icon, active]) => (
          <button
            key={label}
            className={`group flex h-12 w-full items-center gap-4 rounded-2xl px-4 text-left text-sm font-semibold transition-all duration-200 ${
              active
                ? "bg-blue-600 text-white shadow-lg shadow-blue-200"
                : "text-slate-700 hover:-translate-y-0.5 hover:bg-slate-100 hover:text-blue-700"
            }`}
          >
            <span className="text-lg">{icon}</span>
            <span>{label}</span>
          </button>
        ))}
      </nav>

      <div className="mt-auto rounded-3xl border border-slate-200 bg-slate-50 p-3 shadow-card">
        <div className="flex items-center gap-3">
          <div className="grid h-11 w-11 place-items-center rounded-full bg-slate-300 text-xl">👤</div>
          <div className="min-w-0">
            <p className="truncate text-sm font-bold text-slate-900">Nguyễn Văn A</p>
            <p className="text-xs font-medium text-slate-500">K.AI212</p>
          </div>
          <span className="ml-auto text-xs text-slate-500">⌄</span>
        </div>
      </div>
    </aside>
  );
}
