from __future__ import annotations
from dishes import Dish
from utils.validators import validate_type
from operations import MenuOperations


class Menu(MenuOperations):
    def __init__(self) -> None:
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        validate_type(dish, Dish)
        if dish not in self.dishes:
            self.dishes.append(dish)
            return
        print(f'{dish.name} was in menu.')

    def remove_dish(self, dish: Dish) -> None:
        validate_type(dish, Dish)
        if dish in self.dishes:
            dish_index = self.dishes.index(dish)
            self.dishes.pop(dish_index)
            return
        print(f'{dish.name} was not in menu.')
