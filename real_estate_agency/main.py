from client import Client
from properties import Residential, Commercial
from agency import Agency
from agent import Agent


def main() -> None:
    agency = Agency()

    bob = Client('Bob', 'bob@mail.com')
    jack = Agent('Jack', 'jack@mail.com')

    residential = Residential('Yerevan', 120000.0,
                              'Big, comfortable')
    commercial = Commercial('Moscow', 300000.0,
                            'Comfortable, Huge')

    jack.add_property(agency, residential)
    jack.add_property(agency, commercial)

    search = bob.search_for_property(agency, 'Comfort')

    print()
    for prop in search:
        prop.get_description()

    print()
    for prop in agency.properties:
        prop.get_description()

    print()
    bob.purchase_property(agency, residential)

    jack.view_client_info(bob)


if __name__ == '__main__':
    main()
