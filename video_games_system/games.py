from utils.validators import String, DateTime
from datetime import datetime


class Game:
    title = String()
    genre = String()
    release_date = DateTime()

    def __init__(
            self,
            title: str,
            genre: str,
            release_date: datetime
    ) -> None:
        self.title = title
        self.genre = genre
        self.release_date = release_date

    def get_description(self) -> None:
        print(f'Game: {self.title}. ')


class SportGame(Game):
    def get_description(self) -> None:
        print(f'Sport game: {self.title}. ')


class AdventureGame(Game):
    def get_description(self) -> None:
        print(f'Adventure game: {self.title}. ')
