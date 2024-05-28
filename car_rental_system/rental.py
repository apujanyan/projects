from utils.validators import Integer


class Rental:
    rental_duration = Integer()

    def __init__(
            self,
            car,
            costumer,
            rental_duration: float
    ) -> None:
        self.car = car
        self.costumer = costumer
        self.rental_duration = rental_duration
        