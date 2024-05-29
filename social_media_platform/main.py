from user import User
from datetime import datetime


def main() -> None:
    bob = User('Bob', 'bob@mail.com', 'I am Bob')
    jack = User('Jack', 'jack@mail.com', 'Jackk')

    post_by_bob = bob.create_post('Audio', datetime.now(),
                                  'Post by Bob')
    post_by_jack = jack.create_post('Text', datetime.now(),
                                    'Post by Jack')

    comment1 = bob.leave_comment(post_by_jack, 'This is my comment. ')
    comment2 = jack.leave_comment(post_by_jack, 'This is my comment. ')


if __name__ == '__main__':
    main()
