from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import ChatMessage
from smartstudy.services.assistant_service import AssistantService
from smartstudy.services.schedule_service import ScheduleService


class AssistantPage(ctk.CTkFrame):
    def __init__(
        self,
        master,
        *,
        assistant_service: AssistantService,
        schedule_service: ScheduleService,
        on_navigate=None,
    ):
        super().__init__(master, fg_color=COLORS["app_bg"])

        self._assistant_service = assistant_service
        self._schedule_service = schedule_service
        self._on_navigate = on_navigate

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_messages()
        self._build_composer()
        self._render_history()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header, text="AI Assistant", font=FONTS["h1"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=16, pady=(12, 2)
        )
        ctk.CTkLabel(
            header,
            text="Trợ lý học tập - hiện dùng phản hồi mẫu để sẵn sàng nối chatbot thật.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        actions = ctk.CTkFrame(header, fg_color="transparent")
        actions.grid(row=0, column=1, rowspan=2, padx=16, pady=12)

        if self._on_navigate is not None:
            ctk.CTkButton(
                actions,
                text="Về tổng quan",
                width=110,
                command=lambda: self._on_navigate("dashboard"),
            ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(actions, text="Xóa chat", width=90, command=self._clear_chat).pack(
            side="left"
        )

    def _build_messages(self) -> None:
        self._messages = ctk.CTkScrollableFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        self._messages.grid(row=1, column=0, sticky="nsew", padx=24, pady=10)
        self._messages.grid_columnconfigure(0, weight=1)

    def _build_composer(self) -> None:
        composer = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        composer.grid(row=2, column=0, sticky="ew", padx=24, pady=(10, 20))
        composer.grid_columnconfigure(0, weight=1)

        self._input = ctk.CTkEntry(composer, placeholder_text="Nhập câu hỏi về lịch học, bài tập, tài liệu...")
        self._input.grid(row=0, column=0, sticky="ew", padx=(12, 8), pady=12)
        self._input.bind("<Return>", lambda _event: self._send_message())

        ctk.CTkButton(composer, text="Gửi", width=80, command=self._send_message).grid(
            row=0, column=1, padx=(0, 12), pady=12
        )

    def _render_history(self) -> None:
        for widget in self._messages.winfo_children():
            widget.destroy()

        history = self._assistant_service.list_history()
        if not history:
            self._render_empty_state()
            return

        for row_index, message in enumerate(history):
            self._render_message(row_index, message)

    def _render_empty_state(self) -> None:
        box = ctk.CTkFrame(self._messages, fg_color="transparent")
        box.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)

        ctk.CTkLabel(
            box,
            text="Bạn có thể hỏi về lịch học, việc cần làm hoặc nhờ gợi ý kế hoạch học.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
            wraplength=520,
        ).pack(anchor="center")

    def _render_message(self, row_index: int, message: ChatMessage) -> None:
        is_user = message.role == "user"
        row = ctk.CTkFrame(self._messages, fg_color="transparent")
        row.grid(row=row_index, column=0, sticky="ew", padx=12, pady=6)
        row.grid_columnconfigure(0, weight=1)

        bubble = ctk.CTkFrame(
            row,
            fg_color=COLORS["primary"] if is_user else COLORS["surface_2"],
            corner_radius=10,
        )
        bubble.grid(row=0, column=0, sticky="e" if is_user else "w", padx=(120, 0) if is_user else (0, 120))

        ctk.CTkLabel(
            bubble,
            text=message.content,
            font=FONTS["body"].tk(),
            text_color="white" if is_user else COLORS["text"],
            justify="left",
            wraplength=620,
        ).pack(anchor="w", padx=12, pady=(10, 4))

        ctk.CTkLabel(
            bubble,
            text=message.created_at.strftime("%H:%M"),
            font=FONTS["tiny"].tk(),
            text_color=("white", "#DBEAFE") if is_user else COLORS["muted"],
        ).pack(anchor="e", padx=12, pady=(0, 8))

    def _send_message(self) -> None:
        message = self._input.get().strip()
        if not message:
            return

        self._input.delete(0, "end")
        self._assistant_service.send_message(message, context=self._chat_context())
        self._render_history()

    def _clear_chat(self) -> None:
        self._assistant_service.clear_history()
        self._render_history()

    def _chat_context(self) -> dict:
        return {"schedule_count": len(self._schedule_service.list_events())}
