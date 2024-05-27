from books import Fantasy, Fiction
from borrower import Borrower
from librarian import Librarian
from library import Library
from datetime import datetime


def main() -> None:
    library = Library()

    fiction_book = Fiction('Super Fiction', 'Abraham Cruse', 5)
    fantasy_book = Fantasy('Fantasiest', 'Jay Cole', datetime.now())

    librarian_mike = Librarian('Mike', 'mike@mail.com')

    bob = Borrower('Bob', 'bob@mail.com')
    jay = Borrower('Jay', 'jay@mail.com')

    library.books.append(fiction_book)
    library.books.append(fantasy_book)

    search = library.search_book('Fantasiest')
    print(search)

    library.borrow_book(bob, fiction_book)
    library.borrow_book(jay, fantasy_book)

    library.return_book(bob, fantasy_book)

    library.view_borrowing_history(jay)


if __name__ == '__main__':
    main()
