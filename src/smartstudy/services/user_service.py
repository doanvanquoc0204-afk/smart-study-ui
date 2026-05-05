from __future__ import annotations

from smartstudy.core.models import User


class UserService:
    def get_user(self) -> User:
        return User(full_name="Nguyễn Văn A", student_code="K.AI212")
