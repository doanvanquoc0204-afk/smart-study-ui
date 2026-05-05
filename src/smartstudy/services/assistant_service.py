from __future__ import annotations

from datetime import datetime

from smartstudy.core.models import ChatMessage


class AssistantService:
    """Chatbot boundary used by the UI.

    Replace `_generate_reply` with an HTTP/SDK call when the real assistant is ready.
    """

    def __init__(self):
        self._history: list[ChatMessage] = []

    def list_history(self) -> list[ChatMessage]:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()

    def send_message(self, message: str, context: dict | None = None) -> ChatMessage:
        clean_message = message.strip()
        if not clean_message:
            raise ValueError("Tin nhắn không được để trống.")

        user_message = ChatMessage(role="user", content=clean_message, created_at=datetime.now())
        self._history.append(user_message)

        reply = ChatMessage(
            role="assistant",
            content=self._generate_reply(clean_message, context or {}),
            created_at=datetime.now(),
        )
        self._history.append(reply)
        return reply

    def _generate_reply(self, message: str, context: dict) -> str:
        schedule_count = context.get("schedule_count")
        if schedule_count is None:
            return f"Mình đã nhận: {message}. Phần này đang dùng phản hồi mẫu để chờ nối chatbot thật."

        return (
            f"Mình đã nhận: {message}. Hiện có {schedule_count} lịch học trong hệ thống. "
            "Phần này đang dùng phản hồi mẫu để chờ nối chatbot thật."
        )
