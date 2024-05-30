from abc import ABC, abstractmethod
from utils.validators import String, Number


class Car(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class ElectricCar(Car):
    model = String()
    make = String()
    price = Number()

    def __init__(
            self,
            model: str,
            make: str,
            price: float
    ) -> None:
        self.model = model
        self.make = make
        self.price = price

    def get_description(self) -> None:
        print(f'Electric car {self.model}.')


class PetrolCar(Car):
    model = String()
    make = String()
    price = Number()

    def __init__(
            self,
            model: str,
            make: str,
            price: float
    ) -> None:
        self.model = model
        self.make = make
        self.price = price

    def get_description(self) -> None:
        print(f'Petrol car {self.model}.')
