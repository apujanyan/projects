from utils.validators import String, Email, validate_type
from operations import TeacherOperations
from courses import Course
from student import Student


class Teacher(TeacherOperations):
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

    def add_student(self, course: Course, student: Student) -> None:
        validate_type(course, Course)
        validate_type(student, Student)

        if student not in course.enrolled_students:
            course.enrolled_students.append(student)
            print(f'{student.name} added to {course.name}. ')
            return
        print(f'{student.name} already was in {course.name}. ')

    def remove_student(self, course: Course, student: Student) -> None:
        validate_type(course, Course)
        validate_type(student, Student)

        if student in course.enrolled_students:
            student_index = course.enrolled_students.index(student)
            course.enrolled_students.pop(student_index)
            print(f'{student.name} removed from {course.name}. ')
            return
        print(f'{student.name} was not in {course.name}. ')

    def view_student_progress(self, course: Course, student: Student) -> None:
        validate_type(course, Course)
        validate_type(student, Student)

        if student in course.enrolled_students:
            print(f'{self.name} not enrolling in {course.name}. ')
            return
        print(f'{self.name} enrolling in {course.name}. ')
