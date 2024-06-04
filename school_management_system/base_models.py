from abc import ABC, abstractmethod


class TeacherBase(ABC):
    @abstractmethod
    def add_course(self, school, course):
        pass

    @abstractmethod
    def view_student_progress(self, student, course):
        pass


class StudentBase(ABC):
    @abstractmethod
    def enroll_in_courses(self, school, course):
        pass

    @abstractmethod
    def view_student_progress(self, course):
        pass


class CourseBase(ABC):
    @abstractmethod
    def get_description(self):
        pass
