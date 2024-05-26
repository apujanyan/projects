from menu_items import MenuItems
from typing import List


class Order:
    def __init__(
            self,
            costumer,
            menu_items: List[MenuItems] | MenuItems
    ) -> None:
        self.costumer = costumer
        self.menu_items = menu_items
        total_price = 0
        self.reviews = []
        if isinstance(menu_items, list):
            for item in menu_items:
                total_price += item.price
            self.total_price = total_price
        else:
            self.total_price = menu_items.price
