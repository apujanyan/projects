from abc import ABC, abstractmethod
from utils.validators import String, CustomValidator
from teacher import Teacher


class Course(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Math(Course):
    name = String()
    # teacher = CustomValidator(Teacher)

    def __init__(
            self,
            name: str,
            teacher: Teacher
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def get_description(self) -> None:
        print(f'Math course: {self.name}. ')


class English(Course):
    name = String()
    # teacher = CustomValidator(Teacher)

    def __init__(
            self,
            name: str,
            teacher: Teacher
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def get_description(self) -> None:
        print(f'English course: {self.name}. ')
