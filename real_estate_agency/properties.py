from base_models import PropertyBase
from utils.validators import String, Number


class Residential(PropertyBase):
    address = String()
    price = Number()
    features = String()

    def __init__(
            self,
            address: str,
            price: float,
            features: str
    ) -> None:
        self.address = address
        self.price = price
        self.features = features

    def get_description(self) -> None:
        print(f'Residential property in {self.address}.')


class Commercial(PropertyBase):
    address = String()
    price = Number()
    features = String()

    def __init__(
            self,
            address: str,
            price: float,
            features: str
    ) -> None:
        self.address = address
        self.price = price
        self.features = features

    def get_description(self) -> None:
        print(f'Commercial property in {self.address}.')
