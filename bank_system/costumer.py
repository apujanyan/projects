from utils.validators import String, Email
from accounts import Account, IndividualAccount, JointAccount
from transaction import Transaction
from operations import CostumerOperations


class Costumer(CostumerOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.accounts = []

    def create_account(self, balance: float, account_type: str) -> Account:
        account = IndividualAccount(account_type, balance)
        self.accounts.append(account)
        return account

    def transfer(self, sender: Account, receiver: Account,
                 amount: float) -> None:
        if sender not in self.accounts:
            raise ValueError
        if amount > sender.balance:
            raise ValueError
        sender.balance -= amount
        receiver.balance += amount
        sender_transaction = Transaction(sender,
                                         'Withdrawal',
                                         amount)
        receiver_transaction = Transaction(receiver,
                                           'Deposit',
                                           amount)
        sender.transactions.append(sender_transaction)
        receiver.transactions.append(receiver_transaction)

    def view_transaction_history(self) -> None:
        for account in self.accounts:
            for transaction in account.transactions:
                print(transaction)
