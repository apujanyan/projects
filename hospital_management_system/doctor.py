from utils.validators import String, Email
from medical_operations import DoctorOperations
from appointment import Appointment


class Doctor(DoctorOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.appointments = []

    def create_appointment(self, patient, name: str):
        appointment = Appointment(name)
        patient.medical_history.append(appointment)
        self.appointments.append(appointment)
        return appointment

    def manage_patient_info(self, patient):
        print(f'Patient name: {patient.name}, age: {patient.age}. ')
        print(f'Patient medical history: {patient.medical_history}')