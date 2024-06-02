from abc import ABC, abstractmethod


class DeveloperOperations(ABC):
    @abstractmethod
    def create_game(self, title, genre):
        pass

    @abstractmethod
    def add_game(self, game):
        pass


class PublisherOperations(ABC):
    @abstractmethod
    def release_game(self, game, release_date):
        pass

    @abstractmethod
    def sell_game(self, game, player):
        pass
