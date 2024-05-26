from abc import ABC, abstractmethod
from utils.validators import String, Number


class Job(ABC):
    title = String()
    salary = Number()

    def __init__(
            self,
            title: str,
            salary: float
    ) -> None:
        self.title = title
        self.salary = salary

    @abstractmethod
    def get_description(self) -> None:
        pass


class FullTimeJob(Job):
    def get_description(self) -> None:
        print(f'Full time job: {self.title}. ')


class PartTimeJob(Job):
    def get_description(self) -> None:
        print(f'Part time job: {self.title}')
