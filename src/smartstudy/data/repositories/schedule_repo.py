from __future__ import annotations

from smartstudy.core.models import Event

class InMemoryScheduleRepository:
    """In-memory persistence for schedule events (dev/demo).

    Replace with JSON/SQLite/API repository later.
    """

    def __init__(self, seed_events: list[Event] | None = None):
        self._events: list[Event] = list(seed_events or [])

    def list_events(self) -> list[Event]:
        return list(self._events)

    def add_event(self, event: Event) -> None:
        self._events.append(event)
        self._events.sort(key=lambda e: (e.day_index, e.start_hour, e.end_hour, e.title))
