from base_models import MessageBase, UserBase, ConversationBase
from utils.validators import String, CustomValidator


class AudioMessage(MessageBase):
    content = String()
    user = CustomValidator(UserBase)
    conversation = CustomValidator(ConversationBase)

    def __init__(
            self,
            content: str,
            user: UserBase,
            conversation: ConversationBase
    ) -> None:
        self.content = content
        self.user = user
        self.conversation = conversation

    def get_description(self) -> None:
        print(f'Audio message {self.content}, from {self.user.name}.')


class TextMessage(MessageBase):
    content = String()
    user = CustomValidator(UserBase)
    conversation = CustomValidator(ConversationBase)

    def __init__(
            self,
            content: str,
            user: UserBase,
            conversation: ConversationBase
    ) -> None:
        self.content = content
        self.user = user
        self.conversation = conversation

    def get_description(self) -> None:
        print(f'Text message {self.content}, from {self.user.name}.')