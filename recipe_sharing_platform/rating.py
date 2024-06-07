from base_models import RatingBase, UserBase, RecipeBase
from utils.validators import CustomValidator, Number


class Rating(RatingBase):
    user = CustomValidator(UserBase)
    recipe = CustomValidator(RecipeBase)
    score = Number()

    def __init__(
            self,
            user: UserBase,
            recipe: RecipeBase,
            score: float
    ) -> None:
        self.user = user
        self.recipe = recipe
        self.score = score

    def get_description(self) -> None:
        print(f'Rating from {self.user.name} for {self.recipe.title}, '
              f'score {self.score}.')
