from base_models import StudentBase, CourseBase
from school import School
from utils.validators import String, Email, typed


class Student(StudentBase):
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

    @typed
    def enroll_in_courses(
            self,
            school: School,
            course: CourseBase
    ) -> None:
        if course not in school.courses:
            print('Unavailable course.')
            return
        self.courses.append(course)
        print('Enrolling.')

    @typed
    def view_student_progress(
            self,
            course: CourseBase
    ) -> None:
        if course in self.courses:
            print('Enrolling.')
            return
        print('Not enrolling.')
