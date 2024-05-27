from utils.validators import Integer
from costumer import Costumer
from movies import Movie


class Rental:
    duration = Integer()

    def __init__(
            self,
            costumer: Costumer,
            movie: Movie,
            duration: int
    ):
        self.costumer = costumer
        self.movie = movie
        self.duration = duration
