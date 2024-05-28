from utils.validators import String, Email, validate_type
from operations import CostumerOperations
from theaters import Theater
from showtime import Showtime


class Costumer(CostumerOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    def browse_movies(self, theater) -> None:
        validate_type(theater, Theater)

        print()
        for movie in theater.movies:
            print(movie.title)
        print()

    def browse_showtimes(self, theater) -> None:
        validate_type(theater, Theater)

        print()
        for showtime in theater.showtimes:
            print(showtime.movie.title)
            print(showtime.date_time)
        print()

    def reserve_seat(self, theater, showtime, seat_number) -> None:
        validate_type(theater, Theater)
        validate_type(showtime, Showtime)
        validate_type(seat_number, int)

        if showtime in theater.showtimes:
            if (
                seat_number <= 0 or
                seat_number > theater.sitting_capacity or
                seat_number in theater.reserved_seats
            ):
                raise ValueError(f'Unavailable seat number!')

            print(f'{seat_number} seat reserved for {self.name}. ')
            theater.reserved_seats.append(seat_number)
            return
        print(f'There is no {showtime} in this theater. ')

    def purchase_ticket(self, theater, showtime, amount) -> None:
        validate_type(theater, Theater)
        validate_type(showtime, Showtime)
        validate_type(amount, int)

        print(f'{self.name} purchased for {showtime} {amount} dollar(s). ')
