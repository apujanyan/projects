from abc import ABC, abstractmethod
from utils.validators import String


class CourseAssignment(ABC):
    @abstractmethod
    def view_completed_students(self) -> None:
        pass


class Assignment(CourseAssignment):
    name = String()

    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name
        self.completed_students = []

    def view_completed_students(self) -> None:
        for student in self.completed_students:
            print(student.name)
