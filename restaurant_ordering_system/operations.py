from abc import ABC, abstractmethod


class MenuOperations(ABC):
    @abstractmethod
    def add_dish(self, dish):
        pass

    @abstractmethod
    def remove_dish(self, dish):
        pass
