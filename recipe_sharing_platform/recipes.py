from utils.validators import String


class Recipe:
    instructions = String()
    ingredients = String()
    title = String()

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
        print(f'Recipe: {self.title}. ')


class Vegetarian(Recipe):
    def get_description(self) -> None:
        print(f'Vegetarian recipe: {self.title}. ')


class Dessert(Recipe):
    def get_description(self) -> None:
        print(f'Dessert recipe: {self.title}. ')
