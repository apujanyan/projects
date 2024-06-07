from abc import ABC, abstractmethod


class UserBase(ABC):
    @abstractmethod
    def search_for_recipe(self, platform, title):
        pass

    @abstractmethod
    def save_recipe(self, platform, recipe):
        pass

    @abstractmethod
    def share_recipe(self, platform, other, recipe):
        pass

    @abstractmethod
    def rate_recipe(self, platform, recipe, score):
        pass

    @abstractmethod
    def comment_on_recipe(self, platform, recipe, comment_content):
        pass


class RecipeBase(ABC):
    @abstractmethod
    def get_description(self):
        pass


class RatingBase(ABC):
    @abstractmethod
    def get_description(self):
        pass
