from __future__ import annotations
from utils.validators import String
from conversation import Conversation


class Message:
    content = String()

    def __init__(
            self,
            user,
            conversation: Conversation,
            content: str
    ) -> None:
        self.user = user
        self.conversation = conversation
        self.content = content

    def get_description(self) -> None:
        print(f'Message by {self.user.name}: {self.content}.')


class AudioMessage(Message):
    def get_description(self) -> None:
        print(f'Audio message by {self.user.name}: {self.content}.')


class VideoMessage(Message):
    def get_description(self) -> None:
        print(f'Video message by {self.user.name}: {self.content}.')
