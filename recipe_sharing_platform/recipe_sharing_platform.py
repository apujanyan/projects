from recipe_sharing_operations import SharingPlatformOperations


class RecipeSharingPlatform(SharingPlatformOperations):
    def __init__(self) -> None:
        self.users = []
        self.recipes = []

    def search_recipe(self, title) -> list:
        res = []
        for recipe in self.recipes:
            if title.lower() in recipe.title.lower():
                res.append(recipe)
        return res

    def browse_recipes(self) -> None:
        print('\n')
        for recipe in self.recipes:
            print(recipe.title)
        print('\n')
