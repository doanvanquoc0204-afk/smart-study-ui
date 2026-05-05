from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.settings import AppSettings
from smartstudy.services.assistant_service import AssistantService
from smartstudy.services.document_service import DocumentService
from smartstudy.services.exam_service import ExamService
from smartstudy.services.notification_service import NotificationService
from smartstudy.services.schedule_service import ScheduleService
from smartstudy.services.stats_service import StatsService
from smartstudy.services.task_service import TaskService
from smartstudy.services.user_service import UserService
from smartstudy.ui.pages.assistant import AssistantPage
from smartstudy.ui.pages.dashboard import DashboardPage
from smartstudy.ui.pages.documents import DocumentsPage
from smartstudy.ui.pages.exams import ExamsPage
from smartstudy.ui.pages.schedule import SchedulePage
from smartstudy.ui.pages.settings import SettingsPage
from smartstudy.ui.pages.stats import StatsPage
from smartstudy.ui.router import Route, Router


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self._settings = AppSettings()
        self.geometry(self._settings.window_geometry)
        self.title(self._settings.window_title)

        self.configure(fg_color=self._settings.root_fg_color)

        self._user_service = UserService()
        self._schedule_service = ScheduleService()
        self._task_service = TaskService()
        self._notification_service = NotificationService()
        self._assistant_service = AssistantService()
        self._exam_service = ExamService()
        self._document_service = DocumentService()
        self._stats_service = StatsService(
            schedule_service=self._schedule_service,
            task_service=self._task_service,
        )

        self._root_frame = ctk.CTkFrame(self, fg_color="transparent")
        self._root_frame.pack(fill="both", expand=True)

        self._router = Router(
            self._root_frame,
            routes=[
                Route(
                    "dashboard",
                    lambda parent: DashboardPage(
                        parent,
                        user_service=self._user_service,
                        schedule_service=self._schedule_service,
                        task_service=self._task_service,
                        notification_service=self._notification_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "schedule",
                    lambda parent: SchedulePage(
                        parent,
                        schedule_service=self._schedule_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "exams",
                    lambda parent: ExamsPage(
                        parent,
                        exam_service=self._exam_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "documents",
                    lambda parent: DocumentsPage(
                        parent,
                        document_service=self._document_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "assistant",
                    lambda parent: AssistantPage(
                        parent,
                        assistant_service=self._assistant_service,
                        schedule_service=self._schedule_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "stats",
                    lambda parent: StatsPage(
                        parent,
                        stats_service=self._stats_service,
                        on_navigate=self.navigate,
                    ),
                ),
                Route(
                    "settings",
                    lambda parent: SettingsPage(
                        parent,
                        settings=self._settings,
                        user_service=self._user_service,
                        on_navigate=self.navigate,
                    ),
                ),
            ],
        )

        self._router.show("dashboard")

    def navigate(self, page_key: str) -> None:
        self._router.show(page_key)

