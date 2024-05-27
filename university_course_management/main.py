from assignments import Assignment
from courses import UndergraduateCourse, GraduateCourse
from professor import Professor
from student import Student


def main() -> None:
    bob = Student('Bob', 'bob@mail.com')
    tom = Student('Tom', 'tom@mail.com')

    mr_smith = Professor('Smith', 'smith@mail.com')
    mr_johnson = Professor('Johnson', 'johnson@mail.com')

    math = mr_smith.create_course('Math', 'Math course',
                                  'graduate')
    english = mr_johnson.create_course('English', 'English course',
                                       'undergraduate')

    bob.enroll_in_course(math)
    tom.enroll_in_course(english)

    bob.view_progress(english)
    bob.view_progress(math)

    english_task = mr_johnson.create_assignment('Math new task')
    math_task = mr_smith.create_assignment('English task')

    bob.complete_assignment(math_task)
    tom.complete_assignment(english_task)

    english_task.view_completed_students()
    math_task.view_completed_students()


if __name__ == '__main__':
    main()
