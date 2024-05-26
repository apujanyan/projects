from abc import ABC, abstractmethod
from utils.validators import String


class Game(ABC):
    title = String()
    genre = String()

    def __init__(
            self,
            title: str,
            genre: str,
            release_date = None
    ) -> None:
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @abstractmethod
    def get_description(self) -> None:
        pass


class ActionGame(Game):
    def get_description(self) -> None:
        print(f'Action game {self.title}. ')


class StrategyGame(Game):
    def get_description(self) -> None:
        print(f'Strategy game {self.title}. ')
