from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import Notification, Task


class RightPanel(ctk.CTkFrame):
    def __init__(
        self,
        master,
        *,
        tasks: list[Task],
        notifications: list[Notification],
    ):
        super().__init__(master, fg_color="transparent", width=304)

        self.grid_propagate(False)
        self._tasks = tasks
        self._notifications = notifications

        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.pack(fill="both", expand=True)

        self.task_section()
        self.ai_section()
        self.quick_section()
        self.notify_section()

    def set_data(
        self,
        *,
        tasks: list[Task] | None = None,
        notifications: list[Notification] | None = None,
    ) -> None:
        if tasks is not None:
            self._tasks = tasks
        if notifications is not None:
            self._notifications = notifications

        for widget in self.scroll.winfo_children():
            widget.destroy()

        self.task_section()
        self.ai_section()
        self.quick_section()
        self.notify_section()

    def card(self, title: str) -> ctk.CTkFrame:
        frame = ctk.CTkFrame(self.scroll, fg_color=COLORS["surface"], corner_radius=12)
        frame.pack(fill="x", padx=0, pady=(0, 16))
        frame.configure(border_width=1, border_color=COLORS["border"])

        ctk.CTkLabel(frame, text=title, font=FONTS["h2"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=16, pady=(16, 8)
        )
        return frame

    def task_section(self) -> None:
        frame = self.card("Việc cần làm hôm nay")

        for task in self._tasks:
            self.task_item(frame, task)

        ctk.CTkLabel(
            frame,
            text="Xem tất cả (6) →",
            text_color=COLORS["primary"],
            font=FONTS["small"].tk(),
        ).pack(anchor="e", padx=14, pady=(2, 12))

    def task_item(self, parent: ctk.CTkFrame, task: Task) -> None:
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=14, pady=9)

        checked = {"value": False}

        def toggle() -> None:
            checked["value"] = not checked["value"]

            if checked["value"]:
                title_label.configure(text_color=COLORS["muted"], font=(FONTS["body"].family, 11, "overstrike"))
            else:
                title_label.configure(text_color=COLORS["text"], font=FONTS["body_bold"].tk())

        checkbox = ctk.CTkCheckBox(row, text="", width=24, checkbox_width=24, checkbox_height=24, command=toggle)
        checkbox.pack(side="left", padx=(0, 8))

        content = ctk.CTkFrame(row, fg_color="transparent")
        content.pack(side="left", fill="x", expand=True)

        title_label = ctk.CTkLabel(
            content,
            text=task.title,
            font=FONTS["body_bold"].tk(),
            text_color=COLORS["text"],
            anchor="w",
            wraplength=176,
        )
        title_label.pack(anchor="w")

        ctk.CTkLabel(
            content,
            text=task.code,
            font=FONTS["small"].tk(),
            text_color=COLORS["muted"],
        ).pack(anchor="w")

        ctk.CTkLabel(
            row,
            text="23:59" if task.urgent else task.time_text,
            font=FONTS["small"].tk(),
            text_color=COLORS["danger"] if task.urgent else COLORS["muted"],
        ).pack(side="right")

    def ai_section(self) -> None:
        frame = self.card("AI Assistant")

        ctk.CTkLabel(
            frame,
            text="Hỏi đáp, tóm tắt và hỗ trợ học tập",
            text_color=COLORS["muted"],
            font=FONTS["small"].tk(),
        ).pack(anchor="w", padx=14, pady=(0, 8))

        ctk.CTkButton(
            frame,
            text="Chat với AI",
            fg_color=COLORS["primary"],
            height=38,
            corner_radius=12,
            hover_color=COLORS["primary_hover"],
        ).pack(fill="x", padx=14, pady=(0, 14))

    def quick_section(self) -> None:
        frame = self.card("Truy cập nhanh")

        grid = ctk.CTkFrame(frame, fg_color="transparent")
        grid.pack(fill="x", padx=10, pady=(0, 12))

        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)

        items = ["Đề thi", "Tài liệu", "Thống kê", "Ghi chú"]

        for index, item in enumerate(items):
            btn = ctk.CTkButton(
                grid,
                text=item,
                fg_color=COLORS["surface_2"],
                text_color=COLORS["text"],
                hover_color=COLORS["primary_soft"],
                height=36,
                corner_radius=12,
                font=FONTS["small"].tk(),
            )
            btn.grid(row=index // 2, column=index % 2, padx=4, pady=4, sticky="ew")

    def notify_section(self) -> None:
        frame = self.card("Thông báo")

        for notification in self._notifications:
            self.notify_item(frame, notification)

        ctk.CTkLabel(
            frame,
            text="Xem tất cả thông báo →",
            text_color=COLORS["primary"],
            font=FONTS["small"].tk(),
        ).pack(anchor="e", padx=14, pady=(2, 12))

    def notify_item(self, parent: ctk.CTkFrame, notification: Notification) -> None:
        row = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=10)
        row.pack(fill="x", padx=12, pady=5)

        ctk.CTkLabel(
            row,
            text=notification.text,
            font=FONTS["small"].tk(),
            text_color=COLORS["text"],
            wraplength=260,
            justify="left",
        ).pack(anchor="w", padx=10, pady=(8, 2))

        ctk.CTkLabel(
            row,
            text=notification.time_text,
            text_color=COLORS["muted"],
            font=FONTS["small"].tk(),
        ).pack(anchor="w", padx=10, pady=(0, 8))
