from abc import ABC, abstractmethod
from utils.validators import String


class Course(ABC):
    def get_description(self) -> None:
        pass


class UndergraduateCourse(Course):
    name = String()
    content = String()

    def __init__(
            self,
            name: str,
            instructor,
            content: str
    ) -> None:
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    def get_description(self) -> None:
        print(f'Undergraduate course {self.name}')


class GraduateCourse(Course):
    name = String()
    content = String()

    def __init__(
        self,
        name: str,
        instructor,
        content: str
    ) -> None:
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    def get_description(self) -> None:
        print(f'Graduate course {self.name}')
