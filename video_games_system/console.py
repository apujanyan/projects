from utils.validators import String, validate_type
from games import Game


class Console:
    console_type = String()

    def __init__(self, console_type: str) -> None:
        self.console_type = console_type
        self.installed_games = []

    def install_game(self, game) -> None:
        validate_type(game, Game)
        self.installed_games.append(game)
