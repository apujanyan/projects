from abc import ABC, abstractmethod


class DoctorOperations(ABC):
    @abstractmethod
    def manage_patient_info(self, patient):
        pass

    @abstractmethod
    def create_appointment(self, patient, name: str):
        pass


class MedicalStaffOperations(ABC):
    @abstractmethod
    def add_doctor(self, doctor) -> None:
        pass

    @abstractmethod
    def remove_doctor(self, doctor) -> None:
        pass

    @abstractmethod
    def create_procedure(self, patient, proc_type):
        pass
