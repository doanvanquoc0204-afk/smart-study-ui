from __future__ import annotations

import customtkinter as ctk

from smartstudy.core.state import CalendarState
from smartstudy.services.notification_service import NotificationService
from smartstudy.services.schedule_service import ScheduleService
from smartstudy.services.task_service import TaskService
from smartstudy.services.user_service import UserService
from smartstudy.ui.widgets.bottom_cards import BottomCards
from smartstudy.ui.widgets.calendar import Calendar
from smartstudy.ui.widgets.header import Header
from smartstudy.ui.widgets.right_panel import RightPanel
from smartstudy.ui.widgets.sidebar import Sidebar
from smartstudy.ui.widgets.topbar import TopBar


class DashboardPage(ctk.CTkFrame):
    def __init__(
        self,
        master,
        *,
        user_service: UserService,
        schedule_service: ScheduleService,
        task_service: TaskService,
        notification_service: NotificationService,
        on_navigate,
    ):
        super().__init__(master)

        self._user_service = user_service
        self._schedule_service = schedule_service
        self._task_service = task_service
        self._notification_service = notification_service

        user = self._user_service.get_user()
        self._calendar_state = CalendarState(
            days=self._schedule_service.list_calendar_days(),
            events=self._schedule_service.list_events(),
            current_day_index=1,
        )
        tasks = self._task_service.list_tasks_today()
        notifications = self._notification_service.list_notifications()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        Sidebar(self, user=user, on_navigate=on_navigate).grid(row=0, column=0, sticky="ns")

        from smartstudy.config.theme import COLORS  # local import to avoid UI import cycles

        main = ctk.CTkFrame(self, fg_color=COLORS["app_bg"])
        main.grid(row=0, column=1, sticky="nsew")

        main.grid_rowconfigure(0, weight=0)  # topbar
        main.grid_rowconfigure(1, weight=0)  # header
        main.grid_rowconfigure(2, weight=1, minsize=650)  # calendar
        main.grid_rowconfigure(3, weight=0, minsize=150)  # bottom cards

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=0)

        TopBar(main, user=user).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=22,
            pady=(22, 8),
        )

        Header(main, on_add_event=self._on_add_event).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=22,
            pady=(0, 16),
        )

        self._calendar = Calendar(
            main,
            days=self._calendar_state.days,
            events=self._calendar_state.events,
            current_day_index=self._calendar_state.current_day_index,
        )
        self._calendar.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(22, 18),
            pady=0,
        )

        RightPanel(main, tasks=tasks, notifications=notifications).grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0, 22),
            pady=0,
        )

        BottomCards(main).grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=22,
            pady=(18, 22),
        )

    def _on_add_event(self, payload: dict) -> tuple[bool, str]:
        ok, message = self._schedule_service.add_event_from_payload(payload)
        if not ok:
            return ok, message

        # Refresh state + UI
        self._calendar_state = self._calendar_state.with_events(self._schedule_service.list_events())
        self._calendar.set_data(events=self._calendar_state.events)

        return ok, message

