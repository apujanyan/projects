from utils.validators import String, Integer
from utils.validators import validate_type
from movie import Movie
from showtime import Showtime


class Theater:
    location = String()
    sitting_capacity = Integer()

    def __init__(
            self,
            location: str,
            sitting_capacity: int
    ) -> None:
        self.location = location
        self.sitting_capacity = sitting_capacity
        self.movies = []
        self.showtimes = []
        self.reserved_seats = []

    def get_description(self) -> None:
        print(f'Theater: location: {self.location}, '
              f'sitting capacity: {self.sitting_capacity}. ')

    def add_movie(self, movie) -> None:
        validate_type(movie, Movie)
        self.movies.append(movie)

    def add_showtime(self, showtime) -> None:
        validate_type(showtime, Showtime)
        self.showtimes.append(showtime)


class IMaxTheater(Theater):
    def get_description(self) -> None:
        print(f'IMax theater: location: {self.location}, '
              f'sitting capacity: {self.sitting_capacity}. ')


class StandardTheater(Theater):
    def get_description(self) -> None:
        print(f'Standard theater: location: {self.location}, '
              f'sitting capacity: {self.sitting_capacity}. ')
