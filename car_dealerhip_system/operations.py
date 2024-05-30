from abc import ABC, abstractmethod


class CostumerOperations(ABC):
    @abstractmethod
    def search_car(self, service, keyword):
        pass

    @abstractmethod
    def purchase_car(self, service, car, salesman, amount):
        pass


class SalesmanOperations(ABC):
    @abstractmethod
    def add_car(self, service, car):
        pass
