from abc import ABC, abstractmethod


class PropertyBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class AgentBase(ABC):
    @abstractmethod
    def add_property(self, service, features):
        pass

    @abstractmethod
    def view_client_info(self, client):
        pass


class ClientBase(ABC):
    @abstractmethod
    def search_for_property(self, service, property_name):
        pass

    @abstractmethod
    def purchase_property(self, service, property):
        pass
