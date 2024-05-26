from order import Order
from utils.validators import String, Email
from order_operations import CostumerOperations


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
        self.order_history = []

    def place_order(self, menu_items) -> Order:
        order = Order(self, menu_items)
        self.order_history.append(order)
        return order

    def leave_review(self, order: Order, review: str) -> None:
        if order in self.order_history:
            order.reviews.append(review)
            return

    def view_history(self) -> None:
        for order in self.order_history:
            print(order, end='\n')
