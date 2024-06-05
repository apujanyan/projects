from base_models import CostumerBase, MovieBase
from utils.validators import String, Email, typed
from service import RentingService
from typing import List
from rental import Rental


class Costumer(CostumerBase):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.__rental_history = []
        self.__movies = []

    @typed
    def search_for_movie(
            self,
            service: RentingService,
            title: str
    ) -> List[MovieBase | None]:
        result = []
        for movie in service.movies:
            if title.lower() in movie.title.lower():
                result.append(movie)
        return result

    @typed
    def rent_movie(
            self,
            service: RentingService,
            movie: MovieBase,
            duration: int
    ) -> None:
        if movie not in service.movies:
            print(f'Unavailable movie {movie.title}.')
            return
        rental = Rental(movie, self, duration)
        self.__rental_history.append(rental)
        print(f'Successfully rented movie {movie.title} for {duration} days.')

    @typed
    def return_movie(
            self,
            service: RentingService,
            movie: MovieBase
    ) -> None:
        if movie not in self.__movies:
            print(f'Movie {movie.title} is not in your movies list.')
            return
        movie_index = self.__movies.index(movie)
        service.movies.append(movie)
        self.__movies.pop(movie_index)
        print(f'Movie {movie.title} is successfully returned.')

    def view_rental_history(self) -> None:
        print(f'Rental history of {self.name}.')
        for rental in self.__rental_history:
            rental.get_description()
