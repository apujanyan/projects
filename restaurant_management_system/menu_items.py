from abc import ABC, abstractmethod
from utils.validators import String, Number


class MenuItems(ABC):
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float,
            ingredients: list
    ) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @abstractmethod
    def get_description(self) -> None:
        pass


class Appetizer(MenuItems):
    def get_description(self) -> None:
        print(f'Appetizer: {self.ingredients}')


class Entree(MenuItems):
    def get_description(self) -> None:
        print(f'Entree: {self.ingredients}')
        