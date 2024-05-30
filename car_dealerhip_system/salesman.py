from __future__ import annotations
from utils.validators import String, Number
from operations import SalesmanOperations


class Salesman(SalesmanOperations):
    name = String()
    commission_rate = Number()

    def __init__(
            self,
            name: str,
            commission_rate: float
    ) -> None:
        self.name = name
        if commission_rate > 100:
            raise ValueError
        self.commission_rate = commission_rate
        self.sales_history = []

    def view_sales_history(self) -> None:
        for sale in self.sales_history:
            print(sale)

    def add_car(
            self,
            service: CarDealership,
            car: Car
    ) -> None:
        service.cars.append(car)


from dealership import CarDealership
from cars import Car
