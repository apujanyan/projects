from player import Player
from console import Console
from games import Adventure, Sports
from datetime import datetime


def main() -> None:
    bob = Player('Bob', 'bob@mail.com')
    jack = Player('Jack', 'jack@mail.com')

    new_adventure = Adventure('New Adventure', datetime.now())
    fifa = Sports('FIFA 2025', datetime.now())

    playstation = Console('Playstation')

    playstation.install_game(fifa)
    playstation.install_game(fifa)
    playstation.install_game(new_adventure)

    bob.play_game(playstation, fifa)
    bob.save_game_progress(playstation, new_adventure)
    bob.save_game_progress(playstation, fifa)

    bob.complete_with_other_player(playstation, jack, new_adventure)

    for game in bob.saved_games:
        game.get_description()


if __name__ == '__main__':
    main()
