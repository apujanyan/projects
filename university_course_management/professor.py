from utils.validators import String, Email
from courses import *
from assignments import *


class Professor:
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.courses = []

    def create_course(
            self,
            name: str,
            content: str,
            course_type: str
    ) -> Course | None:
        if course_type == 'undergraduate':
            course = UndergraduateCourse(name, self, content)
        elif course_type == 'graduate':
            course = GraduateCourse(name, self, content)
        else:
            return
        self.courses.append(course)
        return course

    def manage_course(self, course) -> None:
        if course in self.courses:
            print(f'Managing {course.name}...')
            return
        print(f'There is no course with name {course.name}')

    def create_assignment(self, name: str) -> Assignment:
        assignment = Assignment(name)
        return assignment

