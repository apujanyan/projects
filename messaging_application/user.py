from __future__ import annotations
from utils.validators import String, Email, validate_type
from operations import UserOperations
from messages import Message, AudioMessage, VideoMessage
from conversation import Conversation


class User(UserOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    def create_conversation(self, *users) -> Conversation:
        conversation = Conversation()
        for user in users:
            validate_type(user, type(self))
        for user in users:
            conversation.users.append(user)
        return conversation

    def participate_in_conversation(self, conversation: Conversation) -> None:
        if self not in conversation.users:
            conversation.users.append(self)
            return
        print(f'{self.name} already in conversation.')

    def send_message(
            self,
            conversation: Conversation,
            content: str,
            message_type='Text'
    ) -> Message | None:
        if self not in conversation.users:
            print(f'{self.name} not in conversation.')
            return
        if message_type == 'Text':
            message = Message(self, conversation, content)
            conversation.history.append(message)
        elif message_type == 'Audio':
            message = AudioMessage(self, conversation, content)
            conversation.history.append(message)
        elif message_type == 'Video':
            message = VideoMessage(self, conversation, content)
            conversation.history.append(message)
        else:
            print('Invalid message type.')

    def add_user(self, conversation: Conversation, user) -> None:
        validate_type(user, type(self))
        if user not in conversation.users:
            conversation.users.append(user)
            return
        print(f'{user.name} already in conversation.')
