from __future__ import annotations

from dataclasses import dataclass

from smartstudy.core.models import CalendarDay, Event


@dataclass
class CalendarState:
    days: list[CalendarDay]
    events: list[Event]
    current_day_index: int = 1

    def with_events(self, events: list[Event]) -> "CalendarState":
        return CalendarState(days=self.days, events=events, current_day_index=self.current_day_index)

