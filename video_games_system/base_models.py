from abc import ABC, abstractmethod


class GameBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class PlayerBase(ABC):
    @abstractmethod
    def play_game(self, console, game):
        pass

    @abstractmethod
    def save_game_progress(self, console, game):
        pass

    @abstractmethod
    def complete_with_other_player(self, console, other, game):
        pass


class ConsoleBase(ABC):
    @abstractmethod
    def install_game(self, game):
        pass
