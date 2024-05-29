from __future__ import annotations
from utils.validators import String, Email, typed
from operations import ClientOperations


class Client(ClientOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.properties = []

    def search_for_property(self, service: RealEstateAgency,
                            property_: Property) -> Property | None:
        if property_ in service.properties:
            return property_
        else:
            print('Cannot find property. ')

    def purchase_property(self, service: RealEstateAgency,
                          property_: Property, price: float) -> None:
        if (
                property_ in service.properties and
                property_ not in self.properties and
                price >= property_.price
        ):
            self.properties.append(property_)
            return


from agency import RealEstateAgency
from properties import Property
