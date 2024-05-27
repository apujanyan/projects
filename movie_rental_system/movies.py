from abc import ABC, abstractmethod
from utils.validators import String, Number


class Movie(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Comedy(Movie):
    title = String()
    rating = Number()

    def __init__(
            self,
            title: str,
            rating: float
    ) -> None:
        self.title = title
        self.rating = rating
        self.genre = 'comedy'

    def get_description(self) -> None:
        print(f'Comedy movie: {self.title}')


class Drama(Movie):
    title = String()
    rating = Number()

    def __init__(
            self,
            title: str,
            rating: float
    ) -> None:
        self.title = title
        self.rating = rating
        self.genre = 'drama'

    def get_description(self) -> None:
        print(f'Comedy movie: {self.title}')
