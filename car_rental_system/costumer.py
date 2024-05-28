from utils.validators import String, Email
from rental_operations import CostumerOperations
from rental import Rental
from cars import Car


class Costumer(CostumerOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []
        self.cars_renting = []

    def rent_car(self, service, car, rental_duration: int) -> None:
        if not isinstance(car, Car):
            raise TypeError(f'Expected {car} to be a Car type!')
        if car in service.available_cars:
            rental = Rental(car, self, rental_duration)
            car_index = service.available_cars.index(car)
            service.available_cars.pop(car_index)
            self.rental_history.append(rental)
            self.cars_renting.append(car)

    def return_car(self, car, service) -> None:
        if not isinstance(car, Car):
            raise TypeError(f'Expected {car} to be a Car type!')
        if car in self.cars_renting:
            car_index = self.cars_renting.index(car)
            self.cars_renting.pop(car_index)
            service.available_cars.append(car)

    def view_rental_history(self) -> None:
        print()
        for rental in self.rental_history:
            print(rental)
        print()
