from __future__ import annotations
from utils. validators import String, Email
from operations import CostumerOperations


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
        self.cars = []

    def search_car(
            self,
            service: CarDealership,
            keyword: str
    ) -> list:
        result = []
        for car in service.cars:
            if keyword.lower() in car.model.lower():
                result.append(car)
        return result

    def purchase_car(
            self,
            service: CarDealership,
            car: Car,
            salesman: Salesman,
            amount: float
    ) -> None:
        if car not in service.cars:
            raise TypeError
        price = car.price + car.price * salesman.commission_rate / 100
        if price > amount:
            raise ValueError
        car_index = service.cars.index(car)
        self.cars.append(car)
        self.cars.pop(car_index)
        sale = f'Salesman {salesman.name} sold car {car.model}. '
        salesman.sales_history.append(sale)


from cars import Car
from dealership import CarDealership
from salesman import Salesman
