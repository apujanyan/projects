from operations import ShoppingOperations
from products import Product
from utils.validators import typed
from typing import List


class ShoppingPlatform(ShoppingOperations):
    def __init__(self) -> None:
        self.products = []
        self.orders = []

    @typed
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def search_product(self, keyword: str) -> List[Product | None]:
        result = []
        for product in self.products:
            if keyword in product.name:
                result.append(product)
        return result

