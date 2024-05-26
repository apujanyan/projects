from games import Game
from utils.validators import String, Email
from game_operations import GameRelease, GameSalesManagement
from datetime import datetime


class Publisher(GameRelease, GameSalesManagement):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.published_games = []

    def release_game(
            self,
            game: Game
    ) -> None:
        game.release_date = datetime.now().date()
        self.published_games.append(game)

    def manage_sales(
            self,
            game: Game
    ) -> None:
        print(f'Managing sales for game {game.title}. ')
