from utils.validators import String, Email, validate_type
from menu import Menu
from dishes import Dish
from order import Order


class Costumer:
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.__order_history = []

    def view_menu(self, menu: Menu) -> None:
        for dish in menu.dishes:
            print(dish.name)

    def place_order(self, menu, *dishes: Dish) -> None:
        for dish in dishes:
            validate_type(dish, Dish)
            if dish not in menu.dishes:
                print('Unavailable dishes.')
                return
        order = Order(self, *dishes)
        self.__order_history.append(order)

    def view_order_history(self) -> None:
        for order in self.__order_history:
            print(order)
