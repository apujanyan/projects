from appointment import Appointment
from doctor import Doctor
from patient import Patient
from medical_staff import MedicalStaff


def main() -> None:
    bob = Patient('Bob', 18)
    tom = Patient('Tom', 23)

    dr_smith = Doctor('Smith', 'smith@mail.com')
    dr_johnson = Doctor('Johnson', 'johnson@mail.com')

    medical_staff = MedicalStaff('Staff', 'Main staff')
    medical_staff.add_doctor(dr_smith)

    appointment = dr_smith.create_appointment(bob, 'Appointment for Bob')
    dr_smith.manage_patient_info(bob)

    medical_staff.remove_doctor(dr_johnson)


if __name__ == '__main__':
    main()
