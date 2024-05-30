from shopping_platform import ShoppingPlatform
from costumer import Costumer
from products import ElectronicProduct, ClothProduct


def main() -> None:
    service = ShoppingPlatform()

    electronic = ElectronicProduct('Electronic', 50)
    cloth = ClothProduct('Hat', 10)

    electronic.get_description()
    cloth.get_description()

    service.add_product(electronic)
    service.add_product(cloth)

    search = service.search_product('Ha')
    print(search)

    bob = Costumer('Bob', 'bob@mail.com')
    bob.purchase_product(service, electronic)

    print(bob.products)
    bob.view_order_history()


if __name__ == '__main__':
    main()
