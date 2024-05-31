from abc import ABC, abstractmethod


class TeacherOperations(ABC):
    @abstractmethod
    def add_student(self, course, student) -> None:
        pass

    @abstractmethod
    def remove_student(self, course, student) -> None:
        pass

    @abstractmethod
    def view_student_progress(self, course, student) -> None:
        pass


class StudentOperations(ABC):
    @abstractmethod
    def enroll_in_course(self, course) -> None:
        pass

    @abstractmethod
    def view_progress(self, course) -> None:
        pass
