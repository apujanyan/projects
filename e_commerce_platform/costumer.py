from typing import List
from base_models import CostumerBase, ProductBase
from order import Order
from platform import Platform
from utils.validators import String, Email


class Costumer(CostumerBase):
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

    def search_for_product(
            self,
            platform: Platform,
            product_name: str
    ) -> List[ProductBase | None]:
        result = []
        for product in platform.products:
            if product_name.lower() in product.name.lower():
                result.append(product)
        return result

    def purchase_product(
            self,
            platform: Platform,
            *products: ProductBase
    ) -> None:
        purchase = []
        for product in products:
            if product in platform.products:
                purchase.append(product)
        order = Order(self, *purchase)
        self.__order_history.append(order)

    def view_order_history(self) -> None:
        for order in self.__order_history:
            print(order.description)
