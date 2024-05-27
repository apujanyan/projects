from abc import ABC, abstractmethod


class MedicalProcedure(ABC):
    def __init__(
            self,
            doctor,
            patient
    ) -> None:
        self.doctor = doctor
        self.patient = patient

    @abstractmethod
    def get_description(self) -> None:
        pass


class Surgery(MedicalProcedure):
    def get_description(self) -> None:
        print(f'Surgery: doctor: {self.doctor.name}'
              f'patient: {self.patient.name}')


class CheckUp(MedicalProcedure):
    def get_description(self) -> None:
        print(f'Check-up: doctor: {self.doctor.name}'
              f'patient: {self.patient.name}')
