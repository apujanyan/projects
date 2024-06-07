from student import Student
from school import School
from teacher import Teacher
from courses import Math, English


def main() -> None:
    school = School()

    bob = Student('Bob', 'bob@mail.com')
    jack = Student('Jack', 'jack@mail.com')

    mr_jackson = Teacher('Jackson', 'jackson@mail.com',
                         'Math')
    mr_smith = Teacher('Smith', 'smith@mail.com',
                       'English')

    math = Math('Math course for beginners', mr_jackson)
    english = English('Basic English course', mr_smith)

    mr_jackson.add_course(school, math)
    mr_smith.add_course(school, english)

    mr_jackson.view_student_progress(school, bob, math)
    bob.enroll_in_course(school, math)

    bob.view_progress(school, english)
    jack.view_progress(school, math)


if __name__ == '__main__':
    main()
