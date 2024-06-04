from student import Student
from teacher import Teacher
from school import School
from courses import Math, English


def main() -> None:
    school = School()

    bob = Student('Bob', 'bob@mail.com')
    jack = Student('Jack', 'jack@mail.com')

    mr_jackson = Teacher('Jackson', 'jackson@mail.com',
                         'Math')
    mrs_roberts = Teacher('Roberts', 'roberts@mail.com',
                          'English')

    english = English('English', mrs_roberts)
    math = Math('Math', mr_jackson)

    mr_jackson.add_course(school, math)
    mrs_roberts.add_course(school, english)

    for subject in school.courses:
        subject.get_description()

    bob.enroll_in_courses(school, math)
    jack.enroll_in_courses(school, english)

    mrs_roberts.view_student_progress(jack, math)
    mrs_roberts.view_student_progress(jack, english)


if __name__ == '__main__':
    main()
