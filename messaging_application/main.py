from user import User


def main() -> None:
    bob = User('Bob', 'bob@mail.com')
    jack = User('Jack', 'jack@mail.com')
    tom = User('Tom', 'tom@mail.com')

    conversation_of_bob = bob.create_conversation(jack)
    bob.add_user(conversation_of_bob, tom)

    jack.send_message(conversation_of_bob, 'This is message by Jack.',
                      'Audio')

    conversation_of_bob.history[0].get_description()
    tom.participate_in_conversation(conversation_of_bob)


if __name__ == '__main__':
    main()
