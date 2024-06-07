from base_models import TeacherBase, CourseBase, StudentBase
from utils.validators import String, Email, typed
from school import School


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
            print(f'Course {course.name} is already existing.')
            return
        print(f'Course {course.name} is added to list.')
        school.courses.append(course)

    @typed
    def view_student_progress(
            self,
            school: School,
            student: StudentBase,
            course: CourseBase
    ) -> None:
        if course not in school.courses:
            print(f'Unavailable course {course.name}.')
            return
        if student not in course.enrolled_students:
            print(f'Student {student.name} not enrolling in course '
                  f'{course.name}.')
            return
        print(f'Student {student.name} enrolling in course '
              f'{course.name}.')
