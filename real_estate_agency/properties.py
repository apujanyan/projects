from abc import ABC, abstractmethod
from utils.validators import String, Number


class Property(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Residential(Property):
    address = String()
    price = Number()
    features = String()

    def __init__(
            self,
            address: str,
            price: float,
            features: str
    ) -> None:
        self.address = address
        self.price = price
        self.features = features

    def get_description(self) -> None:
        print(f'Residential property : Address {self.address}. ')


class Commercial(Property):
    address = String()
    price = Number()
    features = String()

    def __init__(
            self,
            address: str,
            price: float,
            features: str
    ) -> None:
        self.address = address
        self.price = price
        self.features = features

    def get_description(self) -> None:
        print(f'Commercial property : Address {self.address}. ')