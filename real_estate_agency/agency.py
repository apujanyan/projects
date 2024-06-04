from utils.singleton import SingletonMeta


class Agency(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.properties = []
