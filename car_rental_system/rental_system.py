from rental_operations import RentalSystemOperations
from cars import Car
from costumer import Costumer


class RentalSystem(RentalSystemOperations):
    def __init__(self) -> None:
        self.cars = []
        self.costumers = []
        self.available_cars = []

    def add_car(self, car) -> None:
        if not isinstance(car, Car):
            raise TypeError(f'Expected {car} to be a Car type!')
        self.cars.append(car)
        self.available_cars.append(car)

    def add_costumer(self, costumer) -> None:
        if not isinstance(costumer, Costumer):
            raise TypeError(f'Expected {costumer} to be a Costumer type!')

    def search_car(self, model) -> list:
        res = []
        for car in self.cars:
            if model.lower() in car.model.lower():
                res.append(car)
        return res
