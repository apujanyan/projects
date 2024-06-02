from abc import ABC, abstractmethod
from utils.validators import String, Number


class JobPosting(ABC):
    @abstractmethod
    def get_description(self) -> None:
        pass


class FullTime(JobPosting):
    title = String()
    description = String()
    salary = Number()

    def __init__(
            self,
            title: str,
            description: str,
            salary: float
    ) -> None:
        self.title = title
        self.description = description
        self.salary = salary

    def get_description(self) -> None:
        print(f'Full time job {self.title}.')


class PartTime(JobPosting):
    title = String()
    description = String()
    salary = Number()

    def __init__(
            self,
            title: str,
            description: str,
            salary: float
    ) -> None:
        self.title = title
        self.description = description
        self.salary = salary

    def get_description(self) -> None:
        print(f'Part time job {self.title}.')
