from costumer import Costumer


def main() -> None:
    bob = Costumer('Bob', 'bob@mail.com')
    jack = Costumer('Jack', 'jack@mail.com')

    account_1 = bob.create_account(1, 100.0,
                                   'checking')
    account_2 = jack.create_account(2, 300.0,
                                    'saving')

    bob.transfer_funds(account_1, account_2, 70.0)

    print(account_1.balance)
    print(account_2.balance)

    bob.view_transaction_history()
    jack.view_transaction_history()


if __name__ == '__main__':
    main()
