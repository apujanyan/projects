from abc import ABC, abstractmethod


class CostumerBase(ABC):
    @abstractmethod
    def search_for_product(self, platform, product_name):
        pass

    @abstractmethod
    def purchase_product(self, platform, *products):
        pass


class OrderBase(ABC):
    @property
    @abstractmethod
    def description(self):
        pass


class ProductBase(ABC):
    @property
    @abstractmethod
    def description(self):
        pass
