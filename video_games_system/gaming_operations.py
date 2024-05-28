from abc import ABC, abstractmethod


class PlayerOperations(ABC):
    @abstractmethod
    def play_game(self, console, game) -> None:
        pass

    @abstractmethod
    def save_game_progress(self, console, game) -> None:
        pass

    @abstractmethod
    def complete_with_player(self, console, game, other) -> None:
        pass
