from abc import ABC, abstractmethod


class TeacherBase(ABC):
    @abstractmethod
    def add_course(self, school, course):
        pass

    @abstractmethod
    def view_student_progress(self, school, student, course):
        pass


class StudentBase(ABC):
    @abstractmethod
    def enroll_in_course(self, school, course):
        pass

    @abstractmethod
    def view_progress(self, school, course):
        pass


class CourseBase(ABC):
    @abstractmethod
    def get_description(self):
        pass