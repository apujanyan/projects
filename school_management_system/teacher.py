from base_models import TeacherBase, CourseBase, StudentBase
from school import School
from utils.validators import String, Email, typed


class Teacher(TeacherBase):
    name = String()
    contact_info = Email()
    subject_taught = String()

    def __init__(
            self,
            name: str,
            contact_info: str,
            subject_taught: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.subject_taught = subject_taught

    @typed
    def add_course(
            self,
            school: School,
            course: CourseBase
    ) -> None:
        if course in school.courses:
            print('Already added.')
            return
        school.courses.append(course)
        print('Successfully added.')

    @typed
    def view_student_progress(
            self,
            student: StudentBase,
            course: CourseBase
    ) -> None:
        if course in student.courses:
            print('Enrolling.')
            return
        print('Not enrolling.')
