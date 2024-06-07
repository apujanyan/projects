from abc import ABC, abstractmethod


class UserBase(ABC):
    @abstractmethod
    def create_conversation(self, *users):
        pass

    @abstractmethod
    def participate_in_conversation(self, conversation):
        pass

    @abstractmethod
    def send_message(self, conversation, content, message_type='Text'):
        pass

    @abstractmethod
    def receive_message(self, conversation):
        pass

    @abstractmethod
    def remove_message(self, conversation, message):
        pass


class MessageBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class ConversationBase(ABC):
    @abstractmethod
    def get_description(self):
        pass
