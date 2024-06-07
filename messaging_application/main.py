from user import User
from conversation import Conversation


def main() -> None:
    bob = User('Bob', 'bob@mail.com')
    jack = User('Jack', 'jack@mail.com')

    conv_bob = bob.create_conversation(jack)

    message_bob = bob.send_message(conv_bob, 'This is my message.')
    jack.receive_message(conv_bob)

    for message in conv_bob.history:
        print(message.content)

    bob.remove_message(conv_bob, message_bob)

    for message in conv_bob.history:
        print(message.content)


if __name__ == '__main__':
    main()
