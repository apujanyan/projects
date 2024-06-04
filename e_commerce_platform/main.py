from costumer import Costumer
from platform import Platform
from products import Electronic, Cloth


def main() -> None:
    platform = Platform()

    bob = Costumer('Bob', 'bob@mail.com')

    e_product = Electronic('RGB', 10.0)
    c_product = Cloth('Hat', 5.0)

    platform.add_product(e_product)
    platform.add_product(c_product)

    print(e_product.description)
    print(c_product.description)
    print()

    bob.purchase_product(platform, e_product, c_product)
    bob.view_order_history()


if __name__ == '__main__':
    main()
