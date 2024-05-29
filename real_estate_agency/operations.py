from abc import ABC, abstractmethod


class ClientOperations(ABC):
    @abstractmethod
    def search_for_property(self, service, property_):
        pass

    @abstractmethod
    def purchase_property(self, service, property_, price):
        pass


class AgentOperations(ABC):
    @abstractmethod
    def add_property(self, service, property_):
        pass

    @abstractmethod
    def remove_property(self, service, property_):
        pass

    @abstractmethod
    def manage_client_info(self, service, client):
        pass
