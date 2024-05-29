from agency import RealEstateAgency
from agent import Agent
from client import Client
from properties import Residential, Commercial


def main() -> None:
    agency = RealEstateAgency()

    bob = Client('Bob', 'bob@mail.com')
    smith = Agent('Smith', 'smith@mail.com')

    residential = Residential('Yerevan', 50000, 'Cosy')
    commercial = Commercial('Moscow', 100000, 'Luxury')

    bob.search_for_property(agency, residential)
    smith.add_property(agency, residential)
    bob.purchase_property(6, residential, 4700000)
    print(bob.properties)
    smith.add_property(agency, commercial)


if __name__ == '__main__':
    main()
