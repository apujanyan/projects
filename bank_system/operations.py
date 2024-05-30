from abc import ABC, abstractmethod


class CostumerOperations(ABC):
    @abstractmethod
    def create_account(self, balance, account_type):
        pass

    @abstractmethod
    def transfer(self, sender, receiver, amount):
        pass
