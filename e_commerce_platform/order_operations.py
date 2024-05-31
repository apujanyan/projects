from abc import ABC, abstractmethod


class OrderOperation(ABC):
    @abstractmethod
    def deliver_order(self, order) -> None:
        pass
