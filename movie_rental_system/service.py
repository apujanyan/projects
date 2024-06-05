from base_models import MovieBase
from utils.validators import typed
from utils import SingletonMeta


class RentingService(metaclass=SingletonMeta):
    def __init__(self):
        self.movies = []

    @typed
    def add_movie(self, movie: MovieBase) -> None:
        self.movies.append(movie)
