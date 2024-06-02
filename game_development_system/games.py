from abc import ABC, abstractmethod
from utils.validators import String, DateTime
from datetime import datetime


class Game(ABC):
    title = String()
    release_date = DateTime()

    def __init__(
            self,
            title: str,
            release_date: datetime = datetime.now()
    ) -> None:
        self.title = title
        self.release_date = release_date
        self.released = False

    @abstractmethod
    def get_description(self) -> None:
        print(f'Game {self.title}.')

    def __repr__(self) -> str:
        return f'Game {self.title}'


class ActionGame(Game):
    def __init__(
            self,
            title: str,
            release_date: datetime = datetime.now()
    ) -> None:
        super().__init__(title, release_date)
        self.genre = 'Action'

    def get_description(self) -> None:
        print(f'Action game {self.title}.')


class StrategyGame(Game):
    def __init__(
            self,
            title: str,
            release_date: datetime = datetime.now()
    ) -> None:
        super().__init__(title, release_date)
        self.genre = 'Strategy'

    def get_description(self) -> None:
        print(f'Strategy game {self.title}.')
