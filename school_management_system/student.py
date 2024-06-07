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

    @typed
    def enroll_in_course(
            self,
            school: School,
            course: CourseBase
    ) -> None:
        if course not in school.courses:
            print(f'Unavailable course {course.name}.')
            return
        if self in course.enrolled_students:
            print('Already enrolling.')
            return
        course.enrolled_students.append(self)
        print(f'Now {self.name} is enrolling in course {course.name}.')

    @typed
    def view_progress(
            self,
            school: School,
            course: CourseBase
    ) -> None:
        if course not in school.courses:
            print(f'Unavailable course {course.name}.')
            return
        if self not in course.enrolled_students:
            print(f'Not enrolling in course {course.name}.')
            return
        print(f'Enrolling in course {course.name}.')
