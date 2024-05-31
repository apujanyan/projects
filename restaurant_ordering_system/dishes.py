from abc import ABC, abstractmethod
from utils.validators import String, Number


class Dish(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Appetizer(Dish):
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float
    ) -> None:
        self.name = name
        self.price = price

    def get_description(self) -> None:
        print(f'Appetizer {self.name} costs {self.price} dollar(s).')


class Entree(Dish):
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float
    ) -> None:
        self.name = name
        self.price = price

    def get_description(self) -> None:
        print(f'Entree {self.name} costs {self.price} dollar(s).')
