from rating import Rating
from user import User
from recipes import *
from recipe_sharing_platform import RecipeSharingPlatform


def main() -> None:
    platform = RecipeSharingPlatform()

    bob = User('Bob', 'bob@mail.com')
    tom = User('Tom', 'tom@mail.com')

    platform.users.append(bob)
    platform.users.append(tom)

    cake = Dessert('Cake', 'Sugar and milk', '...')
    vegi = Vegetarian('Vegi', 'Flowers', '...')

    platform.recipes.append(cake)
    platform.recipes.append(vegi)

    search = platform.search_recipe('ve')

    bob.save_recipe(vegi)
    tom.save_recipe(cake)

    bob.share_recipe(vegi, tom)


if __name__ == '__main__':
    main()
