from abc import ABC, abstractmethod
from utils.validators import String


class Exercise(ABC):
    name = String()
    muscle_group = String()

    def __init__(
            self,
            name: str,
            muscle_group: str
    ) -> None:
        self.name = name
        self.muscle_group = muscle_group

    @abstractmethod
    def get_description(self) -> None:
        pass


class Cardio(Exercise):
    def get_description(self) -> None:
        print(f'Cardio exercise: {self.name}')


class Strength(Exercise):
    def get_description(self) -> None:
        print(f'Strength exercise: {self.name}')
