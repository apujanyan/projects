from costumer import Costumer
from rental import Rental
from movies import Comedy, Drama


def main() -> None:
    super_drama = Drama('Super Drama', 7.8)
    comedy_bingo = Comedy('Comedy Bingo', 8.9)

    bob = Costumer('Bob', 'bob@mail.com')
    tom = Costumer('Tom', 'tom@mail.com')

    bobs_rental = Rental(bob, super_drama, 90)
    toms_rental = Rental(tom, comedy_bingo, 60)





if __name__ == '__main__':
    main()

