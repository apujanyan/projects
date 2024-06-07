from base_models import RecipeBase
from utils.validators import typed


class RecipeSharingPlatform:
    def __init__(self) -> None:
        self.recipes = []

    @typed
    def add_recipe(self, recipe: RecipeBase) -> None:
        if recipe in self.recipes:
            print(f'{recipe.title} was already in platform.')
            return
        self.recipes.append(recipe)
        print(f'{recipe.title} successfully added in platform.')
