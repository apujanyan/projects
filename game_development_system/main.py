from developer import Developer
from game_development_system import GameDevelopmentSystem
from publisher import Publisher


def main() -> None:
    system = GameDevelopmentSystem()

    dev1 = Developer('John', 'john@mail.com')
    pub1 = Publisher('Art Games', 'contact@mail.com')

    dev2 = Developer('Bob', 'bob@mail.com')
    pub2 = Publisher('New Games', 'contact@gmail.com')

    system.add_developer(dev1)
    system.add_developer(dev2)

    system.add_publisher(pub1)
    system.add_publisher(pub2)

    system.list_developers()
    system.list_publishers()

    game1 = system.dev_create_game('John', 'AC', 'action')
    game2 = system.dev_create_game('Bob', 'ST', 'strategy')

    system.pub_release_game('New Games', game1)
    system.pub_release_game('Art Games', game2)

    print(pub1.published_games)
    print(pub2.published_games)


if __name__ == '__main__':
    main()
