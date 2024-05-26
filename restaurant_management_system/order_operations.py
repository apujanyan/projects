from abc import ABC, abstractmethod
from order import Order


class CostumerOperations(ABC):
    @abstractmethod
    def place_order(self, menu_name) -> Order:
        pass

    @abstractmethod
    def view_history(self) -> None:
        pass

    @abstractmethod
    def leave_review(self, order: Order, review: str) -> None:
        pass
