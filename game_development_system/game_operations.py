from abc import ABC, abstractmethod
from games import Game


class GameCreation(ABC):
    @abstractmethod
    def create_game(
            self,
            title: str,
            genre: str,
    ) -> Game:
        pass


class GameRelease(ABC):
    @abstractmethod
    def release_game(
            self,
            game: Game
    ) -> None:
        pass


class GameSalesManagement(ABC):
    @abstractmethod
    def manage_sales(
            self,
            game: Game
    ) -> None:
        pass
