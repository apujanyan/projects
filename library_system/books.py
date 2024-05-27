from abc import ABC, abstractmethod
from utils.validators import String, DateTime


class Book(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Fiction(Book):
    title = String()
    author = String()
    publication_date = DateTime()

    def __init__(
            self,
            title: str,
            author: str,
            publication_date
    ) -> None:
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def get_description(self) -> None:
        print(f'Fiction book {self.title} by {self.author}. ')

    def __repr__(self) -> str:
        return f'Fiction book {self.title}'


class Fantasy(Book):
    def __init__(
            self,
            title: str,
            author: str,
            publication_date
    ) -> None:
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def get_description(self) -> None:
        print(f'Fantasy book {self.title} by {self.author}. ')

    def __repr__(self) -> str:
        return f'Fantasy book {self.title}'
