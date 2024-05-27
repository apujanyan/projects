from appointments import Virtual, InPerson
from patient import Patient
from doctor import Doctor
from datetime import datetime


def main() -> None:
    bob = Patient('Bob', 'bob@mail.com')
    tom = Patient('Tom', 'tom@mail.com')

    dr_smith = Doctor('Smith', 'smith@mail.com',
                      'Neurolog')

    dr_johnson = Doctor('Johnson', 'johnson@mail.com',
                        'Expert')

    bob.schedule_appointment(dr_johnson, datetime.now(), 'virtual')
    tom.schedule_appointment(dr_smith, datetime.now().now, 'in_person')

    bob.view_medical_history()
    tom.view_medical_history()

    dr_johnson.manage_schedule()


if __name__ == '__main__':
    main()
