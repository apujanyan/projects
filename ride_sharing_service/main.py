from passenger import Passenger
from vehicles import Truck, Motorcycle
from driver import Driver


def main() -> None:
    bob = Passenger('Bob', 'bob@mail.com')

    truck = Truck('Truck')
    motorcycle = Motorcycle('Motorcycle')

    jack = Driver('Jack', 'jack@mail.com', truck)

    truck.get_description()
    motorcycle.get_description()

    ride = bob.request_ride(jack, 'Yerevan', 50)
    # print(jack.requested_rides)

    jack.accept_ride(ride)
    print(jack.rides)
    print(jack.completed_rides)
    jack.complete_ride(ride)
    print(jack.rides)
    print(jack.completed_rides)

    jack.rate_passenger(bob, 5.0)
    bob.rate_driver(jack, 6.0)

    print(jack.ratings)
    print(bob.ratings)


if __name__ == '__main__':
    main()
