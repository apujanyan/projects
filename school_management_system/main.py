import courses
import teacher
import student


def main() -> None:
    bob = student.Student('Bob', 'bob@mail.com')
    jack = student.Student('Jack', 'jack@mail.com')

    mr_smith = teacher.Teacher('Smith', 'smith@mail.com',
                               'math')
    mrs_johnson = teacher.Teacher('Johnson', 'johnson@mail.com',
                                  'english')

    math = courses.Math('Math course', mr_smith)
    english = courses.English('English course', mrs_johnson)

    mr_smith.add_student(4, 5)


if __name__ == '__main__':
    main()
