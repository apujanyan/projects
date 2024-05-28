from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def save_recipe(self, recipe) -> None:
        pass

    @abstractmethod
    def share_recipe(self, recipe, user) -> None:
        pass

    @abstractmethod
    def rate_recipe(self, recipe, rating) -> None:
        pass

    @abstractmethod
    def comment_recipe(self, recipe, comment) -> None:
        pass


class SharingPlatformOperations(ABC):
    @abstractmethod
    def search_recipe(self, title) -> list:
        pass

    @abstractmethod
    def browse_recipes(self) -> None:
        pass
