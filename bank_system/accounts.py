from abc import ABC, abstractmethod
from utils.validators import String, Integer, Number
from itertools import count


class Account(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class IndividualAccount(Account):
    account_type = String()
    balance = Number()

    __number = count()

    def __init__(
            self,
            account_type: str,
            balance: float
    ) -> None:
        if account_type not in('Checking', 'Saving'):
            raise ValueError
        self.number = self.__number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def get_description(self) -> None:
        print(f'Individual account {self.number}. ')


class JointAccount(Account):
    account_type = String()
    balance = Number()

    __number = count()

    def __init__(
            self,
            number: int,
            account_type: str,
            balance: float
    ) -> None:
        if account_type not in('Checking', 'Saving'):
            raise ValueError
        self.number = self.__number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def get_description(self) -> None:
        print(f'Joint account {self.number}. ')
