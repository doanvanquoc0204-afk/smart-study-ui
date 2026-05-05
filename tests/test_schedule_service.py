from __future__ import annotations

import sys
from pathlib import Path
import unittest


def _bootstrap_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    sys.path.insert(0, str(src_dir))


_bootstrap_src_on_path()

from smartstudy.core.models import Event  # noqa: E402
from smartstudy.services.schedule_service import ScheduleService  # noqa: E402


class ScheduleServiceTests(unittest.TestCase):
    def test_add_event_appends_and_sorts(self) -> None:
        service = ScheduleService()

        service.add_event(
            Event(
                day_index=0,
                start_hour=7.0,
                end_hour=7.5,
                title="Test Event",
                room="X",
                color="#000000",
            )
        )

        events = service.list_events()
        self.assertTrue(any(e.title == "Test Event" for e in events))
        self.assertEqual(events, sorted(events, key=lambda e: (e.day_index, e.start_hour, e.end_hour, e.title)))

