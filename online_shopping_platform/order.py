from __future__ import annotations


class Order:
    def __init__(
            self,
            costumer: Costumer,
            *products: Product
    ) -> None:
        self.costumer = costumer
        self.products = products
        self.total_price = sum(product.price for product in products)

    def __str__(self) -> str:
        return (f'Order for {self.costumer.name}: Total price: '
                f'{self.total_price} dollar(s). ')


from costumer import Costumer
from products import Product
