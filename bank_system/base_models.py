from abc import ABC, abstractmethod


class CostumerBase(ABC):
    @abstractmethod
    def create_account(self, account_number, balance, account_type):
        pass

    @abstractmethod
    def transfer_funds(self, sender, receiver, amount):
        pass


class AccountBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class TransactionBase(ABC):
    @abstractmethod
    def get_description(self):
        pass
