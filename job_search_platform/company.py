from utils.validators import String, Email
from job_search_operations import CompanyOperations


class Company(CompanyOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.jobs = []
        self.applications = []

    def add_job(self, job) -> None:
        self.jobs.append(job)

    def remove_job(self, title: str) -> None:
        for job in self.jobs:
            if job.title == title:
                self.jobs.pop(job)

    def review_applications(self) -> None:
        for application in self.applications:
            print(f'Reviewing application \'{application}\' ')
