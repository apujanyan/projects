from costumer import Costumer
from menu_items import Appetizer, Entree


def main() -> None:
    milk_banana = Appetizer('milk_banana', 50,
                            ['milk', 'banana'])
    kiwi_meat = Appetizer('kiwi_meat', 100,
                          ['kiwi', 'meat'])
    carrot_apple = Entree('carrot_apple', 55,
                          ['carrot', 'apple'])

    bob = Costumer('Bob', 'bob@mail.com')
    tom = Costumer('Tom', 'tom@mail.com')

    order1 = bob.place_order(milk_banana)
    order2 = tom.place_order(kiwi_meat)
    order3 = bob.place_order(carrot_apple)

    bob.leave_review(order1, 'Salty')
    print(order1.reviews)
    tom.leave_review(order2, 'Good!')
    print(order2.reviews)
    bob.leave_review(order3, 'Not good!')

    bob.view_history()
    tom.view_history()


if __name__ == '__main__':
    main()
