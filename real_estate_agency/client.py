from base_models import ClientBase, PropertyBase
from agency import Agency
from typing import List
from utils.validators import String, Email, typed


class Client(ClientBase):
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

    @typed
    def search_for_property(
            self,
            service: Agency,
            features: str
    ) -> List[PropertyBase]:
        result = []
        for property in service.properties:
            if features.lower() in property.features.lower():
                result.append(property)
        return result

    def purchase_property(
            self,
            service: Agency,
            property: PropertyBase
    ) -> None:
        if property not in service.properties:
            print('Unavailable property.')
            return
        property_index = service.properties.index(property)
        self.properties.append(property)
        service.properties.pop(property_index)
        print('Successfully purchased.')
