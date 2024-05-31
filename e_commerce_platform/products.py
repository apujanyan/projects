from abc import ABC, abstractmethod
from utils.validators import String, Number


class Product(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Clothing(Product):
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
        print(f'Clothing product {self.name}, price is {self.price}'
              f' dollar(s). ')


class Electronic(Product):
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
        print(f'Electronic product {self.name}, price is {self.price}'
              f' dollar(s). ')
