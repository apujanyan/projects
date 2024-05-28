from abc import ABC, abstractmethod


class CostumerOperations(ABC):
    @abstractmethod
    def rent_car(self, service, car, rental_duration) -> None:
        pass

    @abstractmethod
    def view_rental_history(self) -> None:
        pass

    @abstractmethod
    def return_car(self, car, service) -> None:
        pass


class RentalSystemOperations(ABC):
    @abstractmethod
    def search_car(self, model) -> list:
        pass

    @abstractmethod
    def add_car(self, car) -> None:
        pass

    @abstractmethod
    def add_costumer(self, costumer) -> None:
        pass
