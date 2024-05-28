from abc import ABC, abstractmethod


class CostumerOperations(ABC):
    @abstractmethod
    def browse_movies(self, theater) -> None:
        pass

    @abstractmethod
    def browse_showtimes(self, theater) -> None:
        pass

    @abstractmethod
    def reserve_seat(self, theater, showtime, seat_number) -> None:
        pass

    @abstractmethod
    def purchase_ticket(self, theater, showtime, amount) -> None:
        pass
