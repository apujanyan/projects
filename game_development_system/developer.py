from utils.validators import String, Email
from operations import DeveloperOperations
from games import Game, ActionGame, StrategyGame


class Developer(DeveloperOperations):
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

    def create_game(self, title: str, genre: str) -> Game:
        if genre == 'Action':
            game = ActionGame(title)
        elif genre == 'Strategy':
            game = StrategyGame(title)
        else:
            game = Game(title)
        return game

    def add_game(self, game: Game) -> None:
        if game not in self.games:
            self.games.append(game)
