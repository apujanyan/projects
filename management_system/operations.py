from abc import ABC, abstractmethod


class ReservationOperations(ABC):
    @abstractmethod
    def search_available_room(self):
        pass

    @abstractmethod
    def book_room(self, guest, number, date):
        pass
