import { classes, days, legends, timeSlots } from "../data/dashboardData.js";

const slotHeight = 64;
const dayIndex = Object.fromEntries(days.map((day, index) => [day.key, index]));

function timeToMinutes(time) {
  const [hours, minutes] = time.split(":").map(Number);
  return hours * 60 + minutes;
}

function classPosition(event) {
  const morningStart = timeToMinutes("07:00");
  const afternoonStart = timeToMinutes("13:00");
  const start = timeToMinutes(event.start);
  const end = timeToMinutes(event.end);
  const baseOffset = start < afternoonStart ? 0 : 5 * slotHeight;
  const sectionStart = start < afternoonStart ? morningStart : afternoonStart;
  const top = baseOffset + ((start - sectionStart) / 60) * slotHeight;
  const height = Math.max(72, ((end - start) / 60) * slotHeight - 10);
  return { top, height };
}

export default function Timetable() {
  return (
    <section className="overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-card">
      <div className="grid grid-cols-[86px_repeat(7,minmax(120px,1fr))] border-b border-slate-200 bg-white">
        <div />
        {days.map((day) => (
          <div
            key={day.key}
            className={`border-l border-slate-200 px-4 py-5 text-center ${day.current ? "bg-blue-50/90" : ""}`}
          >
            <p className={`text-base font-extrabold ${day.current ? "text-blue-700" : "text-slate-800"}`}>{day.label}</p>
            <p className="mt-1 text-sm font-medium text-slate-500">{day.date}</p>
          </div>
        ))}
      </div>

      <div className="relative grid grid-cols-[86px_1fr]">
        <div className="border-r border-slate-200">
          <SectionLabel icon="☀" label="Sáng" />
          {timeSlots.slice(0, 5).map((time) => (
            <TimeLabel key={time} time={time} />
          ))}
          <SectionLabel icon="☾" label="Chiều" />
          {timeSlots.slice(5).map((time) => (
            <TimeLabel key={time} time={time} />
          ))}
        </div>

        <div className="relative min-w-[840px]">
          <div className="grid grid-cols-7">
            {days.map((day) => (
              <div key={day.key} className={`relative border-r border-slate-200 last:border-r-0 ${day.current ? "bg-blue-50/55" : ""}`}>
                <GridRows />
              </div>
            ))}
          </div>

          <div className="pointer-events-none absolute inset-0 grid grid-cols-7">
            {classes.map((event) => {
              const { top, height } = classPosition(event);
              return (
                <div
                  key={event.id}
                  className="relative"
                  style={{ gridColumnStart: dayIndex[event.day] + 1 }}
                >
                  <article
                    className={`pointer-events-auto absolute left-2 right-2 rounded-xl border p-3 text-xs shadow-lg transition duration-200 hover:-translate-y-1 hover:shadow-xl ${event.color}`}
                    style={{ top, height }}
                  >
                    <h3 className="line-clamp-2 font-extrabold leading-snug">{event.subject}</h3>
                    <p className="mt-2 font-semibold opacity-90">{event.room}</p>
                    <p className="mt-2 font-bold">{event.start} - {event.end}</p>
                    <div className="mt-3 flex items-center gap-2">
                      <span className={`h-2 w-2 rounded-full ${event.dot}`} />
                      <span className="font-semibold opacity-90">{event.place}</span>
                    </div>
                  </article>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-7 border-t border-slate-200 px-7 py-5">
        {legends.map((legend) => (
          <div key={legend.label} className="flex items-center gap-2 text-sm font-medium text-slate-500">
            <span className={`h-3 w-3 rounded-full ${legend.color}`} />
            {legend.label}
          </div>
        ))}
      </div>
    </section>
  );
}

function SectionLabel({ icon, label }) {
  return (
    <div className="flex h-11 items-center gap-2 px-5 text-sm font-extrabold text-slate-800">
      <span>{icon}</span>
      {label}
    </div>
  );
}

function TimeLabel({ time }) {
  return <div className="h-16 px-6 pt-3 text-sm font-semibold text-slate-600">{time}</div>;
}

function GridRows() {
  return (
    <div>
      {Array.from({ length: 10 }).map((_, index) => (
        <div key={index} className={`h-16 border-b border-slate-200/70 ${index === 4 ? "border-b-slate-300" : ""}`} />
      ))}
    </div>
  );
}
