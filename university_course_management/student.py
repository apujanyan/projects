from utils.validators import String, Email


class Student:
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info

    def enroll_in_course(self, course) -> None:
        if self not in course.students:
            course.students.append(self)
            print(f'Student {self.name} is now enrolling in {course.name}. ')
            return
        print(f'{self.name} is already in {course.name}. ')

    def view_progress(self, course) -> None:
        if self in course.students:
            print(f'{self.name} enrolling in {course.name}. ')
            return
        print(f'{self.name} not enrolling in {course.name}. ')

    def complete_assignment(self, assignment) -> None:
        if self in assignment.completed_students:
            print(f'{self.name} already completed {assignment.name}. ')
            return
        print(f'{assignment.name} is completed, by {self.name}!')
        assignment.completed_students.append(self)
