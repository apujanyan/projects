from base_models import ProductBase
from utils.validators import String, Number


class Electronic(ProductBase):
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float
    ) -> None:
        self.name = name
        self.price = price

    @property
    def description(self) -> str:
        return f'Electronic product {self.name}.'


class Cloth(ProductBase):
    name = String()
    price = Number()

    def __init__(
            self,
            name: str,
            price: float
    ) -> None:
        self.name = name
        self.price = price

    @property
    def description(self) -> str:
        return f'Cloth product {self.name}.'
