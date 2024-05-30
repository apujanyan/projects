from __future__ import annotations
from utils.validators import String, Email


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
        self.products = []

    def purchase_product(
            self,
            service: ShoppingPlatform,
            product: Product
    ) -> None:
        if product not in service.products:
            print(f'There is no product {product.name} in products. ')
            return
        order = Order(self, product)
        self.order_history.append(order)
        product_index = service.products.index(product)
        service.products.pop(product_index)
        self.products.append(product)

    def leave_review(self, product: Product, review: str) -> None:
        review = f'Review by {self.name}: {review}. '
        product.reviews.append(review)

    def view_order_history(self) -> None:
        for order in self.order_history:
            print(order)


from order import Order
from products import Product
from shopping_platform import ShoppingPlatform
