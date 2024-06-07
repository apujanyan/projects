from base_models import ConversationBase, UserBase
from utils.validators import ArgsCustomValidator


class Conversation(ConversationBase):
    users = ArgsCustomValidator(UserBase)

    def __init__(self, *users: UserBase) -> None:
        self.users = list(users)
        self.history = []

    def get_description(self) -> None:
        print('Conversation users.')
        for user in self.users:
            print(f'{user.name}.')
