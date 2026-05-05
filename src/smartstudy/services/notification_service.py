from __future__ import annotations

from smartstudy.core.models import Notification


class NotificationService:
    def list_notifications(self) -> list[Notification]:
        return [
            Notification("Lịch học K.A215 đã được cập nhật", "2 giờ trước"),
            Notification("Có 3 đề thi mới được thêm vào", "5 giờ trước"),
        ]
