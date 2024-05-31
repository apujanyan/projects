from utils.validators import String
from operations import UserOperations


class User(UserOperations):
    name = String()

    def __init__(self, name: str) -> None:
        self.name = name
        self.listening_history = []

    def search_for_song(
            self,
            service,
            song
    ):

