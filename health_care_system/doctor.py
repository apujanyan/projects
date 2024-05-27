from utils.validators import String, Email
from healthcare_operations import DoctorOperations


class Doctor(DoctorOperations):
    name = String()
    contact_info = Email()
    speciality = String()

    def __init__(
            self,
            name: str,
            contact_info: str,
            speciality: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.speciality = speciality
        self.schedules = []

    def manage_schedule(self):
        print(f"Managing {self.name}'s schedules. ")

    def view_medical_history(self, patient) -> None:
        for appointment in patient.medical_history:
            appointment.get_description()
