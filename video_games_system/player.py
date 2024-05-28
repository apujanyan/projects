from utils.validators import String, Email, validate_type
from gaming_operations import PlayerOperations
from console import Console
from games import Game


class Player(PlayerOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.saved_games = []
        self.completed_games = []

    def play_game(self, console, game) -> None:
        validate_type(console, Console)
        validate_type(game, Game)

        if game in console.installed_games:
            print(f'{self.name} is playing {game.title} in '
                  f'{console.console_type}. ')
            return
        print(f'{game.title} not installed in {console.console_type}. ')

    def save_game_progress(self, console, game) -> None:
        validate_type(console, Console)
        validate_type(game, Game)

        if game in console.installed_games:
            print(f'Saved {game.title} progress. ')
            self.saved_games.append(game)
            return
        print(f'{game.title} not installed in {console.console_type}. ')

    def complete_with_player(self, console, game, other) -> None:
        validate_type(console, Console)
        validate_type(game, Game)
        validate_type(other, type(self))

        if game in console.installed_games:
            if (
                game not in self.completed_games and
                game not in other.completed_games
            ):
                self.completed_games.append(game)
                other.completed_games.append(game)
                print(f'{self.name} completed {game.title} with '
                      f'{other.name}. ')
                return
            print('Already completed. ')
            return
        print(f'{game.title} not installed in {console.console_type}. ')
