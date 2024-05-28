from console import Console
from player import Player
from games import *
from datetime import datetime


def main() -> None:
    adventure_game = AdventureGame('Super Adventure', 'adventure',
                                   datetime.now())
    sport_game = SportGame('FIFA 2025', 'sport',
                           datetime.now())

    bob = Player('Bob', 'bob@mail.com')
    jay = Player('Jay', 'jay@mail.com')

    xbox = Console('XBox')
    xbox.install_game(sport_game)
    bob.play_game(xbox, sport_game)
    bob.complete_with_player(xbox, sport_game, jay)


if __name__ == '__main__':
    main()
