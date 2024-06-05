from base_models import MovieBase
from utils.validators import String, Number


class Comedy(MovieBase):
    title = String()
    rating = Number()

    def __init__(
            self,
            title: str,
            rating: float
    ) -> None:
        self.title = title
        self.genre = 'Comedy'
        self.rating = rating

    def get_description(self) -> None:
        print(f'Comedy movie {self.title}.')


class Horror(MovieBase):
    title = String()
    rating = Number()

    def __init__(
            self,
            title: str,
            rating: float
    ) -> None:
        self.title = title
        self.genre = 'Horror'
        self.rating = rating

    def get_description(self) -> None:
        print(f'Horror movie {self.title}.')
