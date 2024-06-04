from base_models import CostumerBase, AccountBase
from accounts import IndividualAccount, JointAccount
from transaction import Transaction
from utils.validators import String, Email, typed


class Costumer(CostumerBase):
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

    def create_account(
            self,
            account_number: int,
            balance: float,
            account_type: str
    ) -> AccountBase:
        if account_type in ('checking', 'saving'):
            account = IndividualAccount(account_number, account_type, balance)
            self.accounts.append(account)
            print(f'Account {account_number} created.')
            return account
        print(f'Invalid account type.')

    @typed
    def transfer_funds(
            self,
            sender: AccountBase,
            receiver: AccountBase,
            amount: float
    ) -> None:
        if sender == receiver:
            print('Invalid operation.')
            return
        if not sender in self.accounts:
            print('Invalid operation.')
            return
        if amount > sender.balance:
            print('Invalid operation.')
            return
        sender.balance -= amount
        receiver.balance += amount
        sender_transaction = Transaction(sender, amount,
                                         'Withdrawal')
        receiver_transaction = Transaction(receiver, amount,
                                           'Deposit')
        sender.transactions.append(sender_transaction)
        receiver.transactions.append(receiver_transaction)

    def view_transaction_history(self) -> None:
        print(f"Transaction history of {self.name}.")
        for account in self.accounts:
            for transaction in account.transactions:
                transaction.get_description()
