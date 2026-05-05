from __future__ import annotations

from smartstudy.core.models import StatsSummary
from smartstudy.services.schedule_service import ScheduleService
from smartstudy.services.task_service import TaskService


class StatsService:
    def __init__(self, *, schedule_service: ScheduleService, task_service: TaskService):
        self._schedule_service = schedule_service
        self._task_service = task_service

    def get_summary(self) -> StatsSummary:
        tasks = self._task_service.list_tasks_today()
        urgent_tasks = [task for task in tasks if task.urgent]
        return StatsSummary(
            total_events=len(self._schedule_service.list_events()),
            total_tasks=len(tasks),
            urgent_tasks=len(urgent_tasks),
            completed_percent=68,
        )

    def weekly_focus(self) -> list[tuple[str, int]]:
        return [
            ("Lập trình Python", 82),
            ("Cấu trúc DL", 74),
            ("Tiếng Anh 2", 61),
            ("Kiến trúc máy tính", 55),
        ]
