from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass(frozen=True)
class User:
    full_name: str
    student_code: str


@dataclass(frozen=True)
class CalendarDay:
    label: str  # e.g. "Thứ 2"
    date_text: str  # e.g. "20/04"


@dataclass(frozen=True)
class Event:
    day_index: int  # 0..6 (Mon..Sun in the current UI)
    start_hour: float  # e.g. 7, 14.5
    end_hour: float
    title: str
    room: str
    color: str


@dataclass(frozen=True)
class Task:
    title: str
    code: str
    time_text: str
    urgent: bool = False


@dataclass(frozen=True)
class Notification:
    text: str
    time_text: str


@dataclass(frozen=True)
class Exam:
    title: str
    subject: str
    term: str
    status: str
    question_count: int


@dataclass(frozen=True)
class StudyDocument:
    title: str
    subject: str
    file_type: str
    updated_text: str
    size_text: str


@dataclass(frozen=True)
class StatsSummary:
    total_events: int
    total_tasks: int
    urgent_tasks: int
    completed_percent: int


@dataclass(frozen=True)
class ChatMessage:
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime

