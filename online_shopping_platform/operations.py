from abc import ABC, abstractmethod


class ShoppingOperations(ABC):
    @abstractmethod
    def search_product(self, target):
        pass

    @abstractmethod
    def add_product(self, product):
        pass
