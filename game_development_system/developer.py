from datetime import datetime
from games import Game, ActionGame, StrategyGame
from utils.validators import String, Email
from game_operations import GameCreation


class Developer(GameCreation):
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

    def create_game(
            self,
            title: str,
            genre: str,
    ) -> Game:
        if genre.lower() == 'action':
            game = ActionGame(title, genre)
        elif genre.lower() == 'strategy':
            game = StrategyGame(title, genre)
        else:
            game = Game(title, genre)
        return game
