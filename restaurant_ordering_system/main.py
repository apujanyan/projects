from costumer import Costumer
from dishes import Appetizer, Entree
from menu import Menu


def main() -> None:
    bob = Costumer('Bob', 'bob@mail.com')

    appetizer = Appetizer('GOOD Appetizer', 20.0)
    entree = Entree('Super Entree', 30.0)

    menu = Menu()
    menu.add_dish(appetizer)
    menu.add_dish(entree)

    bob.place_order(menu, appetizer, entree)
    bob.view_order_history()


if __name__ == '__main__':
    main()
