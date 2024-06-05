from service import RentingService
from cotumer import Costumer
from movies import Comedy, Horror


def main() -> None:
    renting_service = RentingService()

    bob = Costumer('Bob', 'bob@mail.com')

    comedy = Comedy('New Comedy', 6)
    horror = Horror('Horrible Horror', 7.8)
    another_comedy = Comedy('New Comedy 2', 6.9)

    renting_service.add_movie(comedy)
    renting_service.add_movie(horror)

    search = bob.search_for_movie(renting_service, 'horror')
    for movie in search:
        movie.get_description()

    bob.rent_movie(renting_service, horror, 90)
    bob.rent_movie(renting_service, another_comedy, 60)

    bob.return_movie(renting_service, comedy)
    bob.return_movie(renting_service, horror)

    bob.view_rental_history()


if __name__ == '__main__':
    main()
