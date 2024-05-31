class Order:
    def __init__(
            self,
            costumer,
            *products,
    ) -> None:
        self.costumer = costumer
        self.products = products
        self.total_price = sum(products)
        self.reviews = []
