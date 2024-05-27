from abc import ABC, abstractmethod


class RentalOperations(ABC):
    @abstractmethod
    def rent_movie(self, rental, title) -> None:
        pass

    @abstractmethod
    def search_movie(self, rental, title) -> list:
        pass

    @abstractmethod
    def return_movie(self, title) -> None:
        pass

    @abstractmethod
    def view_rental_history(self) -> None:
        pass