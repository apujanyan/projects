from utils.validators import String, Email
from recipe_sharing_operations import UserOperations
from rating import Rating


class User(UserOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.favourite_recipes = []

    def save_recipe(self, recipe) -> None:
        if recipe in self.favourite_recipes:
            print(f'You already save {recipe.title}. ')
            return
        self.favourite_recipes.append(recipe)

    def share_recipe(self, recipe, user) -> None:
        if recipe in self.favourite_recipes:
            if recipe in user.favourite_recipes:
                print(f'{user.name} already had {recipe.title}. ')
                return
            user.favourite_recipes.append(recipe)

    def rate_recipe(self, recipe, rating) -> None:
        recipe_rating = Rating(recipe, self, rating)
        recipe.ratings.append(recipe_rating)

    def comment_recipe(self, recipe, comment) -> None:
        recipe.comments.append(comment)
