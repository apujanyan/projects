from base_models import UserBase, MessageBase, ConversationBase
from utils.validators import String, Email
from conversation import Conversation
from messages import AudioMessage, TextMessage


class User(UserBase):
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
        conversation = Conversation(*users, self)
        print(f'{self.name} successfully created conversation.')
        return conversation

    def participate_in_conversation(
            self,
            conversation: ConversationBase
    ) -> None:
        if self in conversation.users:
            print(f'{self.name} already in conversation.')
            return
        conversation.users.append(self)
        print(f'{self.name} successfully added to conversation.')

    def send_message(
            self,
            conversation: ConversationBase,
            content: str,
            message_type='Text'
    ) -> MessageBase:
        if self not in conversation.users:
            print(f'{self.name} not in conversation.')
            return
        if message_type == 'Audio':
            message = AudioMessage(content, self, conversation)
            conversation.history.append(message)
            return message
        message = TextMessage(content, self, conversation)
        conversation.history.append(message)
        return message

    def receive_message(self, conversation: ConversationBase) -> None:
        if self not in conversation.users:
            print(f'{self.name} not in conversation.')
            return
        for message in conversation.history:
            if message.user != self:
                print(f'{self.name} receiving message {message.content} '
                      f'from {message.user.name}.')
                return
        print('No new messages.')

    def remove_message(
            self,
            conversation: ConversationBase,
            message: MessageBase
    ) -> None:
        if self not in conversation.users:
            print(f'{self.name} not in conversation.')
            return
        if message.user != self:
            print('Unavailable operation.')
            return
        if message not in conversation.history:
            print('Unavailable operation.')
            return
        message_index = conversation.history.index(message)
        conversation.history.pop(message_index)
        print('Message was removed from conversation.')
