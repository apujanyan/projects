from utils.singleton import SingletonMeta
from typing import List
from library_operations import LibraryOperations
from library_system.books import Book
from library_system.borrower import Borrower


class Library(LibraryOperations):
    def __init__(self) -> None:
        self.books = []
        self.borrowers = []
        self.librarians = []

    def search_book(self, title: str) -> List[Book | None]:
        result = []
        for book in self.books:
            if book.title == title:
                result.append(book)
        return result

    def borrow_book(self, borrower: Borrower, book: Book) -> None:
        if book in self.books:
            if book not in borrower.borrowed_books:
                borrower.borrowed_books.append(book)
                borrower.borrowing_history.append(book)
                self.books.pop(self.books.index(book))
            else:
                print(f'{borrower.name} already borrowing {book.title}. ')

    def view_borrowing_history(self, borrower: Borrower) -> None:
        print(f'{borrower.name}\'s borrowing history. ')
        for book in borrower.borrowing_history:
            print(book)

    def return_book(self, borrower: Borrower, book: Book) -> None:
        if book in borrower.borrowed_books:
            borrower.borrowed_books.pop(book)
            self.books.append(book)
            print(f'{book.title} returned. ')
        else:
            print(f'{borrower.name} does not borrowed {book.title}. ')
