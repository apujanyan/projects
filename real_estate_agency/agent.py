from base_models import AgentBase, PropertyBase,ClientBase
from agency import Agency
from utils.validators import String, Email, typed


class Agent(AgentBase):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    @typed
    def add_property(
            self,
            service: Agency,
            property: PropertyBase
    ) -> None:
        if property in service.properties:
            print('Already added.')
            return
        service.properties.append(property)
        print('Successfully added.')

    @typed
    def view_client_info(
            self,
            client: ClientBase
    ) -> None:
        print(f'Client {client.name}, contact info {client.contact_info}.')
