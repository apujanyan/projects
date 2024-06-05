from base_models import RentalBase, CostumerBase, MovieBase
from utils.validators import CustomValidator, Integer


class Rental(RentalBase):
    movie = CustomValidator(MovieBase)
    costumer = CustomValidator(CostumerBase)
    duration = Integer()

    def __init__(
            self,
            movie: MovieBase,
            costumer: CostumerBase,
            duration: int
    ) -> None:
        self.movie = movie
        self.costumer = costumer
        self.duration = duration

    def get_description(self) -> None:
        print(f'Costumer {self.costumer.name} rented movie {self.movie.title} '
              f'for {self.duration} days.')

    def __repr__(self) -> str:
        return (f'Costumer {self.costumer.name} rented movie {self.movie.title}'
                f' for {self.duration} days.')
