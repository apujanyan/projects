from base_models import ProductBase


class Platform:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: ProductBase) -> None:
        if not isinstance(product, ProductBase):
            raise TypeError
        self.products.append(product)
