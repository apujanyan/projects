from __future__ import annotations
from utils.validators import String, Email
from operations import AgentOperations


class Agent(AgentOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    def add_property(self, service: RealEstateAgency,
                     property_: Property) -> None:
        if property_ not in service.properties:
            service.properties.append(property_)
            return
        print('Property already was in service. ')

    def remove_property(self, service: RealEstateAgency,
                        property_: Property) -> None:
        if property_ in service.properties:
            property_index = service.properties.index(property_)
            service.properties.pop(property_index)
            return
        print('Property not in service. ')

    def manage_client_info(self, service: RealEstateAgency,
                           client: Client) -> None:
        if client in service.clients:
            print(f'Client {client.name}, '
                  f'contact information: {client.contact_info}')
            return
        print('Client not in service. ')


from agency import RealEstateAgency
from properties import Property
from client import Client
