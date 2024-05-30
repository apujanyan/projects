from utils.validators import String


class Vehicle:
    name = String()

    def __init__(self, name: str) -> None:
        self.name = name

    def get_description(self) -> None:
        print(f'Vehicle {self.name}. ')


class Truck(Vehicle):
    def get_description(self) -> None:
        print(f'Truck {self.name}. ')


class Motorcycle(Vehicle):
    def get_description(self) -> None:
        print(f'Motorcycle {self.name}. ')
