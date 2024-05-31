from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def create_conversation(self, *users):
        pass

    @abstractmethod
    def participate_in_conversation(self, conversation):
        pass

    @abstractmethod
    def send_message(self, conversation, content, message_type):
        pass

    @abstractmethod
    def add_user(self, conversation, user):
        pass
