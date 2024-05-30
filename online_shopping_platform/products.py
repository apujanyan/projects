from utils.validators import String, Number


class Product:
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float
    ) -> None:
        self.name = name
        self.price = price
        self.reviews = []

    def get_description(self) -> None:
        print(f'Product {self.name}, price {self.price} dollar(s). ')


class ElectronicProduct(Product):
    def get_description(self) -> None:
        print(f'Electronic product {self.name}, price {self.price} dollar(s). ')


class ClothProduct(Product):
    def get_description(self) -> None:
        print(f'Cloth product {self.name}, price {self.price} dollar(s). ')
