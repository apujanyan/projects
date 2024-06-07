from base_models import ConsoleBase, GameBase
from utils.validators import String, typed


class Console(ConsoleBase):
    console_type = String()

    def __init__(
            self,
            console_type: str
    ) -> None:
        self.console_type = console_type
        self.installed_games = []

    @typed
    def install_game(self, game: GameBase) -> None:
        if game in self.installed_games:
            print(f'Game {game.title} already installed.')
            return
        print(f'Game {game.title} is installed.')
        self.installed_games.append(game)


