from __future__ import annotations

import sys
from pathlib import Path
import unittest


def _bootstrap_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    sys.path.insert(0, str(src_dir))


_bootstrap_src_on_path()

from smartstudy.services.schedule_service import ScheduleService  # noqa: E402


class EventParsingTests(unittest.TestCase):
    def test_add_event_validation_rejects_empty_title(self) -> None:
        service = ScheduleService()
        ok, msg = service.add_event_from_payload({"title": "", "day": "1", "start": "7", "end": "8"})
        self.assertFalse(ok)
        self.assertIn("tên môn", msg.lower())

    def test_add_event_validation_rejects_time_outside_visible_calendar(self) -> None:
        service = ScheduleService()
        ok, msg = service.add_event_from_payload({"title": "Test", "day": "1", "start": "6.5", "end": "7"})
        self.assertFalse(ok)
        self.assertIn("7:00-12:00", msg)

    def test_add_event_validation_accepts_visible_half_hour_slot(self) -> None:
        service = ScheduleService()
        ok, msg = service.add_event_from_payload({"title": "Test", "day": "1", "start": "7", "end": "8.5"})
        self.assertTrue(ok, msg)
        self.assertTrue(any(e.title == "Test" for e in service.list_events()))

