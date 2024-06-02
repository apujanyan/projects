from abc import ABC, abstractmethod


class JobSeekerOperations(ABC):
    @abstractmethod
    def search_job(self, company, title):
        pass

    @abstractmethod
    def apply_to_job(self, company, job):
        pass


class CompanyOperations(ABC):
    @abstractmethod
    def add_job_posting(self, title, description, salary, job_type='Full time'):
        pass

    @abstractmethod
    def review_applications(self):
        pass
