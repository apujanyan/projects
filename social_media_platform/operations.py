from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class UserOperations(ABC):
    @abstractmethod
    def create_post(
            self,
            post_type: str,
            date: datetime,
            content: str,
    ):
        pass

    @abstractmethod
    def view_post(
            self,
            post
    ) -> None:
        pass

    @abstractmethod
    def leave_comment(
            self,
            post,
            content: str
    ):
        pass

