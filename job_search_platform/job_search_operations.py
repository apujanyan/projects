from abc import ABC, abstractmethod


class JobSeekerOperations(ABC):
    @abstractmethod
    def search_job(self, company, title: str) -> list:
        pass

    @abstractmethod
    def apply_to_job(self, company, title: str) -> None:
        pass


class CompanyOperations(ABC):
    @abstractmethod
    def add_job(self, job) -> None:
        pass

    @abstractmethod
    def remove_job(self, title: str) -> None:
        pass
