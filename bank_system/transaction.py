from __future__ import annotations
from utils.validators import Number, String


class Transaction:
    transaction_type = String()
    amount = Number()

    def __init__(
            self,
            account: Account,
            transaction_type: str,
            amount: float
    ) -> None:
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount


from accounts import Account
