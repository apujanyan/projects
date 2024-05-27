from utils.validators import String, Email
from rental_operations import RentalOperations


class Costumer(RentalOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.rented_movies = []
        self.rental_history = []

    def search_movie(self, rental, title) -> list:
        result = []
        for movie in rental.movies:
            if title == movie.title:
                result.append(movie)
        return result

    def rent_movie(self, rental, title):

        print("Movie doesn't exist.")

    def view_rental_history(self) -> None:
        for movie in self.rental_history:
            print(movie.title, end='\n')

    def return_movie(self, title) -> None:
        for movie in self.rented_movies:
            if title == movie.title:
                self.rented_movies.pop(movie)
                return
        print('Movie not in your rented movies list!')
