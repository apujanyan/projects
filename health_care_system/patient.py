from utils.validators import String, Email
from healthcare_operations import PatientOperations
from appointments import *


class Patient(PatientOperations):
    name = String()
    contact_info = Email()

    def __init__(
        self,
        name: str,
        contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.medical_history = []

    def schedule_appointment(self, doctor, time, app_type):
        if app_type == 'virtual':
            appointment = Virtual(self, doctor, time)
        elif app_type == 'in_person':
            appointment = InPerson(self, doctor, time)
        else:
            return
        self.medical_history.append(appointment)
        doctor.schedules.append(appointment)
        return appointment

    def view_medical_history(self) -> None:
        for appointment in self.medical_history:
            appointment.get_description()
