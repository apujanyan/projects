from __future__ import annotations
from abc import ABC, abstractmethod
from utils.validators import String, DateTime
from datetime import datetime


class Post(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class TextPost(Post):
    date = DateTime()
    content = String()

    def __init__(
            self,
            user: User,
            content: str,
            date: datetime
    ) -> None:
        self.user = user
        self.content = content
        self.date = date

    def get_description(self) -> None:
        print(f'Text post by {self.user.name}: {self.content}. ')


class AudioPost(Post):
    date = DateTime()
    content = String()

    def __init__(
            self,
            user: User,
            content: str,
            date: datetime
    ) -> None:
        self.user = user
        self.content = content
        self.date = date

    def get_description(self) -> None:
        print(f'Audio post by {self.user.name}: {self.content}. ')


from user import User
