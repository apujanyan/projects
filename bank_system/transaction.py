from base_models import TransactionBase, AccountBase
from utils.validators import String, Number, CustomValidator


class Transaction(TransactionBase):
    account = CustomValidator(AccountBase)
    amount = Number()
    transaction_type = String()

    def __init__(
            self,
            account: AccountBase,
            amount: float,
            transaction_type: str
    ) -> None:
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def get_description(self) -> None:
        print(f'Transaction for {self.account.account_number}.')
