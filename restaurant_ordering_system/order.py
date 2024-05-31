from __future__ import annotations
from dishes import Dish


class Order:
    def __init__(
            self,
            costumer,
            *dishes: Dish
    ) -> None:
        self.costumer = costumer
        self.dishes = dishes
        self.total_price = sum(dish.price for dish in dishes)
