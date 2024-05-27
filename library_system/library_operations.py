from abc import ABC, abstractmethod
from typing import List
from books import Book
from borrower import Borrower


class LibraryOperations(ABC):
    @abstractmethod
    def search_book(self, title: str) -> List[Book | None]:
        pass

    @abstractmethod
    def borrow_book(self, borrower: Borrower, book: Book) -> None:
        pass

    @abstractmethod
    def view_borrowing_history(self, borrower: Borrower) -> None:
        pass

    @abstractmethod
    def return_book(self, borrower: Borrower, book: Book) -> None:
        pass
