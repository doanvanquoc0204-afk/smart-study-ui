from __future__ import annotations

from typing import Protocol

from smartstudy.core.models import Event, Exam, Notification, StudyDocument, Task, User


class ScheduleRepository(Protocol):
    def list_events(self) -> list[Event]:
        ...

    def add_event(self, event: Event) -> None:
        ...


class UserRepository(Protocol):
    def get_user(self) -> User:
        ...


class TaskRepository(Protocol):
    def list_tasks_today(self) -> list[Task]:
        ...


class NotificationRepository(Protocol):
    def list_notifications(self) -> list[Notification]:
        ...


class ExamRepository(Protocol):
    def list_exams(self) -> list[Exam]:
        ...


class DocumentRepository(Protocol):
    def list_documents(self) -> list[StudyDocument]:
        ...
