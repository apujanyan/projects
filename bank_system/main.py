from costumer import Costumer


def main() -> None:
    bob = Costumer('Bob', 'bob@mail.com')
    jack = Costumer('Jack', 'jack@mail.com')

    account_b = bob.create_account(50, 'Checking')
    account_j = jack.create_account(100, 'Saving')

    print(bob.accounts)
    print(jack.accounts)

    bob.transfer(account_b, account_j, 20)
    print(account_b.balance)
    print(account_j.balance)

    bob.view_transaction_history()
    jack.view_transaction_history()


if __name__ == '__main__':
    main()
