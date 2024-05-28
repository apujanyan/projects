from cars import *
from costumer import Costumer
from rental import Rental
from rental_system import RentalSystem


def main() -> None:
    service = RentalSystem()

    phantom = LuxuryCar('Phantom', 'Rolls Royce', 1000)
    camry = EconomyCar('Camry', 'Toyota', 200)

    service.add_car(phantom)
    service.add_car(camry)

    bob = Costumer('Bob', 'bob@mail.com')

    my_search = service.search_car('ph')
    print(my_search)

    print(service.available_cars)
    bob.rent_car(service, phantom, 90)
    print(service.available_cars)

    bob.view_rental_history()


if __name__ == '__main__':
    main()
