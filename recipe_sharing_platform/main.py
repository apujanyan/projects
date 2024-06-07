from user import User
from platform import RecipeSharingPlatform
from receipes import Dessert, Vegetarian


def main() -> None:
    platform = RecipeSharingPlatform()

    bob = User('Bob', 'bob@mail.com')
    jack = User('Jack', 'jack@mail.com')

    veg_recipe = Vegetarian('New Recipe', 'Apple, Orange',
                            'Just cut them, and mix together.')
    dessert_recipe = Dessert('Super Dessert', 'Bread, Milk',
                             'Do what you like.')

    platform.add_recipe(veg_recipe)
    platform.add_recipe(dessert_recipe)

    search = bob.search_for_recipe(platform, 'rec')
    for recipe in search:
        recipe.get_description()

    bob.save_recipe(platform, veg_recipe)
    jack.comment_on_recipe(platform, veg_recipe, 'Salty')

    for comment in veg_recipe.comments:
        print(comment)


if __name__ == '__main__':
    main()
