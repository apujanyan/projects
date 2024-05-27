from abc import ABC, abstractmethod


class PatientOperations(ABC):
    @abstractmethod
    def schedule_appointment(self, doctor, time, app_type):
        pass

    @abstractmethod
    def view_medical_history(self) -> None:
        pass


class DoctorOperations(ABC):
    @abstractmethod
    def manage_schedule(self):
        pass

    @abstractmethod
    def view_medical_history(self, patient) -> None:
        pass
