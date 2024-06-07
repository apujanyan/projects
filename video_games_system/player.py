from base_models import PlayerBase, GameBase, ConsoleBase
from utils.validators import String, Email, typed


class Player(PlayerBase):
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
        self.played_games = []

    @typed
    def play_game(
            self,
            console: ConsoleBase,
            game: GameBase
    ) -> None:
        if game not in console.installed_games:
            print(f'Unavailable game to play.')
            return
        print(f'Player {self.name} is playing game {game.title}.')
        self.played_games.append(game)
        return

    @typed
    def save_game_progress(
            self,
            console: ConsoleBase,
            game: GameBase
    ) -> None:
        if game not in self.played_games or game not in console.installed_games:
            print(f'Unavailable game to save progress.')
            return
        print(f'Saved game {game.title} progress.')
        self.saved_games.append(game)

    @typed
    def complete_with_other_player(
            self,
            console: ConsoleBase,
            other,
            game: GameBase
    ) -> None:
        if not isinstance(other, type(self)):
            raise TypeError(f'Expected {other} to be a Person type.')
        if game not in console.installed_games:
            print('Unavailable game.')
            return
        print(f'Game {game.title} successfully completed with player'
              f' {other.name}.')
