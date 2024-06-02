from utils.validators import String, Email
from operations import PublisherOperations
from games import Game, ActionGame, StrategyGame
from datetime import datetime
from player import Player


class Publisher(PublisherOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.games = []

    def release_game(self, game: Game, release_date: datetime) -> None:
        if not game.released:
            game.release_date = release_date
            self.games.append(game)

    def sell_game(self, game: Game, player: Player) -> None:
        if game in self.games:
            player.games.append(game)
