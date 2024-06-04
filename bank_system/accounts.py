from base_models import AccountBase
from utils.validators import Integer, String, Number


class JointAccount(AccountBase):
    account_number = Integer()
    account_type = String()
    balance = Number()

    def __init__(
            self,
            account_number: int,
            account_type: str,
            balance: float
    ) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def get_description(self) -> None:
        print(f'Print account {self.account_number}.')


class IndividualAccount(AccountBase):
    account_number = Integer()
    account_type = String()
    balance = Number()

    def __init__(
            self,
            account_number: int,
            account_type: str,
            balance: float
    ) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def get_description(self) -> None:
        print(f'Print account {self.account_number}.')
