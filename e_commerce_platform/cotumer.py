from utils.validators import String, Email
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
        self.order_history = []

    def leave_review(self, platform, order, review: str) -> None:
        if order in platform.orders:
            if review not in order.reviews:
                order.reviews.append(review)

    def create_order(self, *products, platform):
        order = Order(self, products)
        platform.orders.append(order)

    def search_order(self, platform, order_name):
        result = []
        for order in platform.orders:
            if order_name.lower() == order.name:
                result.append(order)
        return result

    def purchase_order(self, order, price):
        if order.costumer != self:
            print(f'This is not your order. ')
        if price == order.price:
            print('Successfully purchased. ')
        else:
            print(f'You must purchase {order.price} dollar(s). ')

    def view_order_history(self):
        return