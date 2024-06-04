from base_models import CourseBase, TeacherBase
from utils.validators import String, CustomValidator


class Math(CourseBase):
    name = String()
    teacher = CustomValidator(TeacherBase)

    def __init__(
            self,
            name: str,
            teacher: TeacherBase
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def get_description(self) -> None:
        print(f'Math course, teacher {self.teacher.name}.')


class English(CourseBase):
    name = String()
    teacher = CustomValidator(TeacherBase)

    def __init__(
            self,
            name: str,
            teacher: TeacherBase
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []

    def get_description(self) -> None:
        print(f'English course, teacher {self.teacher.name}.')
