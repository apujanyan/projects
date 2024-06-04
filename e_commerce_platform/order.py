from base_models import OrderBase, CostumerBase, ProductBase
from utils.validators import CustomValidator, ArgsCustomValidator


class Order(OrderBase):
    costumer = CustomValidator(CostumerBase)
    products = ArgsCustomValidator(ProductBase)

    def __init__(
            self,
            costumer: CostumerBase,
            *products: ProductBase
    ) -> None:
        self.costumer = costumer
        self.products = products
        self.total_price = sum(product.price for product in products)

    @property
    def description(self) -> str:
        return (f'Order for {self.costumer.name}, total price: '
                f'{self.total_price} dollar(s).')
