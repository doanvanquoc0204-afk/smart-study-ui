from __future__ import annotations

import sys
from pathlib import Path
import unittest


def _bootstrap_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    sys.path.insert(0, str(src_dir))


_bootstrap_src_on_path()

from smartstudy.services.assistant_service import AssistantService  # noqa: E402


class AssistantServiceTests(unittest.TestCase):
    def test_send_message_stores_user_and_assistant_messages(self) -> None:
        service = AssistantService()

        reply = service.send_message("Gợi ý lịch học hôm nay", context={"schedule_count": 3})

        history = service.list_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].role, "user")
        self.assertEqual(history[1].role, "assistant")
        self.assertEqual(reply, history[1])
        self.assertIn("3 lịch học", reply.content)

    def test_send_message_rejects_empty_input(self) -> None:
        service = AssistantService()

        with self.assertRaises(ValueError):
            service.send_message("   ")

    def test_clear_history_removes_messages(self) -> None:
        service = AssistantService()
        service.send_message("Hello")

        service.clear_history()

        self.assertEqual(service.list_history(), [])
