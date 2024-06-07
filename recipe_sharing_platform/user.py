from base_models import UserBase, RecipeBase
from platform import RecipeSharingPlatform
from utils.validators import String, Email, typed
from rating import Rating


class User(UserBase):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.saved_recipes = []
        self.shared_recipes = []

    def search_for_recipe(
            self,
            platform: RecipeSharingPlatform,
            title: str
    ) -> list:
        res = []
        for recipe in platform.recipes:
            if title.lower() in recipe.title.lower():
                res.append(recipe)
        return res

    @typed
    def save_recipe(
            self,
            platform: RecipeSharingPlatform,
            recipe: RecipeBase
    ) -> None:
        if recipe not in platform.recipes:
            print(f'Unavailable recipe {recipe.title}.')
            return
        if recipe in self.saved_recipes:
            print(f'{recipe.title} was already saved.')
            return
        self.saved_recipes.append(recipe)
        print(f'{recipe.title} is added to {self.name} '
              f'saved recipes list.')

    @typed
    def share_recipe(
            self,
            platform: RecipeSharingPlatform,
            other,
            recipe: RecipeBase
    ) -> None:
        if recipe not in platform.recipes:
            print(f'Unavailable recipe {recipe.title}.')
            return
        if recipe in self.saved_recipes:
            print(f'{recipe.title} was already saved.')
            return
        other.shared_recipes.append(recipe)
        print(f'{recipe.title} is shared to {other.name}.')

    @typed
    def rate_recipe(
            self,
            platform: RecipeSharingPlatform,
            recipe: RecipeBase,
            score: float
    ) -> None:
        if recipe not in platform.recipes:
            print(f'Unavailable recipe {recipe.title}.')
            return
        if score > 10:
            raise ValueError
        rating = Rating(self, recipe, score)
        recipe.ratings.append(rating)
        print(f'{self.name} rated {recipe.title}, score {score}.')

    @typed
    def comment_on_recipe(
            self,
            platform: RecipeSharingPlatform,
            recipe: RecipeBase,
            comment_content: str
    ) -> None:
        if recipe not in platform.recipes:
            print(f'Unavailable recipe {recipe.title}.')
            return
        comment = f'{self.name} commented on {recipe.title}: {comment_content}.'
        recipe.comments.append(comment)
