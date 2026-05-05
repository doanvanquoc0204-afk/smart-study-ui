from __future__ import annotations

from smartstudy.core.models import CalendarDay, Event
from smartstudy.data.repositories.contracts import ScheduleRepository
from smartstudy.data.repositories.schedule_repo import InMemoryScheduleRepository


def _default_seed_events() -> list[Event]:
    return [
        Event(day_index=1, start_hour=7, end_hour=9, title="Thiết kế web", room="K.A215", color="#d1fae5"),
        Event(day_index=2, start_hour=7, end_hour=9, title="Kiến trúc máy tính", room="K.A212", color="#fef3c7"),
        Event(day_index=3, start_hour=8, end_hour=10, title="Tiếng Anh 2", room="K.B102", color="#1f2937"),
        Event(day_index=5, start_hour=7, end_hour=9, title="GDTC 2", room="Sân bóng", color="#7c2d12"),
        Event(day_index=0, start_hour=13, end_hour=14.5, title="Đại số tuyến tính", room="K.A212", color="#14532d"),
        Event(day_index=1, start_hour=13, end_hour=16, title="Lập trình Python", room="K.A312", color="#1e3a8a"),
        Event(day_index=2, start_hour=13, end_hour=16, title="Tiếng Anh CN", room="K.B102", color="#78350f"),
        Event(day_index=4, start_hour=13, end_hour=16, title="Cấu trúc DL", room="K.A313", color="#581c87"),
    ]


class ScheduleService:
    def __init__(self, repository: ScheduleRepository | None = None):
        self._repo = repository or InMemoryScheduleRepository(seed_events=_default_seed_events())

    def list_calendar_days(self) -> list[CalendarDay]:
        return [
            CalendarDay("Thứ 2", "20/04"),
            CalendarDay("Thứ 3", "21/04"),
            CalendarDay("Thứ 4", "22/04"),
            CalendarDay("Thứ 5", "23/04"),
            CalendarDay("Thứ 6", "24/04"),
            CalendarDay("Thứ 7", "25/04"),
            CalendarDay("CN", "26/04"),
        ]

    def list_events(self) -> list[Event]:
        return self._repo.list_events()

    def add_event(self, event: Event) -> None:
        self._repo.add_event(event)

    def add_event_from_payload(self, payload: dict) -> tuple[bool, str]:
        title = (payload.get("title") or "").strip()
        day_text = (payload.get("day") or "").strip()
        start_text = (payload.get("start") or "").strip()
        end_text = (payload.get("end") or "").strip()

        if not title:
            return False, "Vui lòng nhập tên môn."

        try:
            day_num = int(day_text)
        except ValueError:
            return False, "Ngày phải là số từ 1 đến 7."

        if day_num < 1 or day_num > 7:
            return False, "Ngày phải nằm trong khoảng 1..7."

        try:
            start_hour = float(start_text)
            end_hour = float(end_text)
        except ValueError:
            return False, "Giờ bắt đầu/kết thúc phải là số (vd: 7, 14.5)."

        if end_hour <= start_hour:
            return False, "Giờ kết thúc phải lớn hơn giờ bắt đầu."

        if not self._is_half_hour_slot(start_hour) or not self._is_half_hour_slot(end_hour):
            return False, "Giờ học phải theo mốc 30 phút (vd: 7, 7.5, 14)."

        if not self._fits_visible_calendar_range(start_hour, end_hour):
            return False, "Giờ học phải nằm trong khung 7:00-12:00 hoặc 13:00-18:00."

        self.add_event(
            Event(
                day_index=day_num - 1,
                start_hour=start_hour,
                end_hour=end_hour,
                title=title,
                room="(Tự thêm)",
                color="#dbeafe",
            )
        )

        return True, ""

    def _is_half_hour_slot(self, hour: float) -> bool:
        return abs(hour * 2 - round(hour * 2)) < 1e-9

    def _fits_visible_calendar_range(self, start_hour: float, end_hour: float) -> bool:
        return (7 <= start_hour < end_hour <= 12) or (13 <= start_hour < end_hour <= 18)
