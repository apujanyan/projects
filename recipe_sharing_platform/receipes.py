from base_models import RecipeBase
from utils.validators import String


class Vegetarian(RecipeBase):
    title = String()
    ingredients = String()
    instructions = String()

    def __init__(
            self,
            title: str,
            ingredients: str,
            instructions: str
    ) -> None:
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.ratings = []
        self.comments = []

    def get_description(self) -> None:
        print(f'Vegetarian recipe, ingredients {self.ingredients}.')


class Dessert(RecipeBase):
    title = String()
    ingredients = String()
    instructions = String()

    def __init__(
            self,
            title: str,
            ingredients: str,
            instructions: str
    ) -> None:
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.ratings = []
        self.comments = []

    def get_description(self) -> None:
        print(f'Dessert recipe, ingredients {self.ingredients}.')
