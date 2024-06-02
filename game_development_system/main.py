from developer import Developer
from publisher import Publisher
from player import Player
from datetime import datetime


def main() -> None:
    bob = Player('Bob', 'bob@mail.com')

    jack = Developer('Jack', 'jack@mail.com')
    iron_games = Publisher('Iron Games', 'iron@contact.com')

    super_action = jack.create_game('Super Action', 'Action')
    good_strategy = jack.create_game('Good Strategy', 'Strategy')

    jack.add_game(super_action)
    jack.add_game(good_strategy)

    print("Jack's games.")
    for game in jack.games:
        print(game)

    iron_games.release_game(super_action, datetime.now())
    iron_games.release_game(good_strategy, datetime.now())

    print("\nIron games' games.")
    for game in iron_games.games:
        print(game)

    iron_games.sell_game(super_action, bob)

    print("\nBob's games.")
    for game in bob.games:
        print(game)


if __name__ == '__main__':
    main()
