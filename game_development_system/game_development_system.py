from games import *
from developer import Developer
from publisher import Publisher
from utils.singleton import SingletonMeta


class GameDevelopmentSystem(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__developers = []
        self.__publishers = []

    def add_developer(
            self,
            dev: Developer
    ) -> None:
        self.__developers.append(dev)
        print(f'Added developer {dev.name}. ')

    def add_publisher(
            self,
            pub: Publisher
    ) -> None:
        self.__publishers.append(pub)
        print(f'Added publisher {pub.name}. ')

    def list_developers(self) -> None:
        for dev in self.__developers:
            print(f'{dev.name}\n')

    def list_publishers(self) -> None:
        for pub in self.__publishers:
            print(f'{pub.name}\n')

    def dev_create_game(
            self,
            dev_name: str,
            title: str,
            genre: str
    ) -> Game:
        for dev in self.__developers:
            if dev_name == dev.name:
                game = dev.create_game(title, genre)
                return game
        print('Developer not found! ')

    def pub_release_game(
            self,
            pub_name: str,
            game: Game
    ) -> None:
        for pub in self.__publishers:
            if pub_name == pub.name:
                pub.release_game(game)
                return
        print('Publisher not found! ')
