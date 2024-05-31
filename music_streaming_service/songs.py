from abc import ABC, abstractmethod
from utils.validators import String, Number


class Song(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Rock(Song):
    title = String()
    artist = String()
    length = Number()

    def __init__(
            self,
            title: str,
            artist: str,
            length: float
    ) -> None:
        self.title = title
        self.artist = artist
        self.length = length

    def get_description(self) -> None:
        print(f'Rock music by {self.artist}. ')


class Pop(Song):
    title = String()
    artist = String()
    length = Number()

    def __init__(
            self,
            title: str,
            artist: str,
            length: float
    ) -> None:
        self.title = title
        self.artist = artist
        self.length = length

    def get_description(self) -> None:
        print(f'Pop music by {self.artist}. ')
