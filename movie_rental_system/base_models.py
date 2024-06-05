from abc import ABC, abstractmethod


class MovieBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class CostumerBase(ABC):
    @abstractmethod
    def search_for_movie(self, service, title):
        pass

    @abstractmethod
    def rent_movie(self, service, movie, duration):
        pass

    @abstractmethod
    def return_movie(self, service, movie):
        pass


class RentalBase(ABC):
    @abstractmethod
    def get_description(self):
        pass
