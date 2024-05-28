from abc import ABC, abstractmethod
from utils.validators import String, Number


class Car(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class LuxuryCar(Car):
    model = String()
    make = String()
    rental_price = Number()

    def __init__(
            self,
            model: str,
            make: str,
            rental_price: float
    ) -> None:
        self.model = model
        self.make = make
        self.rental_price = rental_price

    def get_description(self) -> None:
        print(f'Luxury car: {self.model}. ')


class EconomyCar(Car):
    model = String()
    make = String()
    rental_price = Number()

    def __init__(
            self,
            model: str,
            make: str,
            rental_price: float
    ) -> None:
        self.model = model
        self.make = make
        self.rental_price = rental_price

    def get_description(self) -> None:
        print(f'Economy car: {self.model}. ')
