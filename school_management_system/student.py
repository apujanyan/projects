from utils.validators import String, Email, validate_type
from operations import StudentOperations
from courses import Course


class Student(StudentOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    def enroll_in_course(self, course: Course) -> None:
        validate_type(course, Course)
        if self not in course.enrolled_students:
            course.enrolled_students.append(self)
            return
        print(f'{self.name} already in {course.name}. ')

    def view_progress(self, course) -> None:
        if self not in course.enrolled_students:
            print(f'{self.name} not enrolling in {course.name}. ')
            return
        print(f'{self.name} enrolling in {course.name}. ')
