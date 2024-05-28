from recipes import Recipe
from utils.validators import Number


class Rating:
    rating = Number()

    def __init__(
            self,
            recipe: Recipe,
            user,
            rating: float
    ) -> None:
        self.recipe = recipe
        self.user = user
        self.rating = rating
