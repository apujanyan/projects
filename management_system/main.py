from hotel import Hotel
from guest import Guest
from rooms import Deluxe
from datetime import datetime


def main() -> None:
    hotel = Hotel()

    bob = Guest('Bob', 'bob@mail.com')
    deluxe = Deluxe(12, 32323, 'Cosy')

    hotel.add_room(deluxe)
    hotel.add_guest(bob)

    hotel.book_room(bob, 12, datetime.now())
    bob.view_reservation_history()


if __name__ == '__main__':
    main()
