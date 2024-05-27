from abc import ABC, abstractmethod


class Appointment(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class InPerson(Appointment):
    def __init__(
            self,
            patient,
            doctor,
            time
    ) -> None:
        self.patient = patient
        self.doctor = doctor
        self.time = time

    def get_description(self) -> None:
        print(f'In person appointment with {self.doctor.name}. ')


class Virtual(Appointment):
    def __init__(
            self,
            patient,
            doctor,
            time
    ) -> None:
        self.patient = patient
        self.doctor = doctor
        self.time = time

    def get_description(self) -> None:
        print(f'Virtual appointment with {self.doctor.name}. ')
