from utils.validators import String
from medical_operations import MedicalStaffOperations
from medical_procedures import *


class MedicalStaff(MedicalStaffOperations):
    name = String()
    position = String()

    def __init__(
            self,
            name: str,
            position: str
    ) -> None:
        self.name = name
        self.position = position
        self.doctors = []

    def add_doctor(self, doctor) -> None:
        if doctor not in self.doctors:
            self.doctors.append(doctor)
            print(f'Doctor {doctor.name} successfully added. ')
            return
        print(f'Doctor {doctor.name} already in medical stuff. ')

    def remove_doctor(self, doctor) -> None:
        if doctor not in self.doctors:
            print(f'Doctor {doctor.name} not in medical staff. ')
            return
        self.doctors.pop(doctor)
        print(f'Doctor {doctor.name} successfully removed from medical stuff. ')

    def create_procedure(self, patient, proc_type):
        if proc_type == 'surgery':
            proc = Surgery(self, patient)
        elif proc_type == 'check-up':
            proc = CheckUp(self, patient)
        else:
            return
        return proc

