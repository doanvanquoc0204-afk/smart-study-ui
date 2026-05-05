export default function BottomSection() {
  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_1fr]">
      <section className="rounded-3xl border border-slate-200 bg-white p-6 shadow-card transition hover:shadow-soft">
        <div className="flex items-start justify-between gap-4">
          <div className="flex gap-4">
            <div className="grid h-12 w-12 place-items-center rounded-2xl bg-indigo-50 text-2xl">✦</div>
            <div>
              <h3 className="text-lg font-extrabold text-slate-950">Gợi ý lịch học thông minh</h3>
              <p className="mt-2 max-w-md text-sm font-medium leading-6 text-slate-500">
                AI đề xuất ưu thời gian học dựa trên môn học, deadlines và mức độ ưu tiên.
              </p>
            </div>
          </div>
          <button className="rounded-xl border border-slate-200 bg-white px-5 py-3 text-sm font-bold text-blue-600 shadow-card transition hover:-translate-y-0.5 hover:bg-blue-50">
            Xem gợi ý
          </button>
        </div>
      </section>

      <section className="rounded-3xl border border-slate-200 bg-white p-6 shadow-card transition hover:shadow-soft">
        <div className="mb-6 flex items-center gap-4">
          <div className="grid h-12 w-12 place-items-center rounded-2xl bg-emerald-50 text-2xl">☀</div>
          <h3 className="text-lg font-extrabold text-slate-950">Thống kê tuần</h3>
        </div>
        <div className="grid grid-cols-4 divide-x divide-slate-200 text-center">
          <Stat value="28" label="Tổng số tiết" />
          <Stat value="22" label="Tiết học" />
          <Stat value="6" label="Tự học" />
          <div>
            <p className="text-2xl font-extrabold text-slate-950">85%</p>
            <p className="mt-2 text-xs font-semibold text-slate-500">Hoàn thành</p>
            <div className="mx-auto mt-2 h-1.5 w-16 rounded-full bg-slate-200">
              <div className="h-full w-[85%] rounded-full bg-blue-600" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function Stat({ value, label }) {
  return (
    <div>
      <p className="text-2xl font-extrabold text-slate-950">{value}</p>
      <p className="mt-2 text-xs font-semibold text-slate-500">{label}</p>
    </div>
  );
}
