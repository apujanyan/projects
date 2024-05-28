from costumer import Costumer
from movie import Movie
from showtime import Showtime
from theaters import IMaxTheater, StandardTheater
from utils.validators import validate_type
from datetime import datetime


def main() -> None:
    bob = Costumer('Bob', 'bob@mail.com')
    tom = Costumer('Tom', 'tom@mail.com')

    adventure = Movie('New Adventure', 'adventure', 90)
    horror = Movie('Super Horror', 'horror', 120)

    imax = IMaxTheater('Yerevan', 120)
    standard = StandardTheater('Moscow', 150)

    horror_showtime = Showtime(horror, imax, datetime.now())
    adventure_showtime = Showtime(adventure, standard, datetime.now())


if __name__ == '__main__':
    main()
