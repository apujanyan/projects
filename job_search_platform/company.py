from utils.validators import String, Email
from operations import CompanyOperations
from job_postings import JobPosting, FullTime, PartTime


class Company(CompanyOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str,
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.applications = []
        self.jobs = []

    def add_job_posting(
            self,
            title: str,
            description: str,
            salary: float,
            job_type: str = 'Full time'
    ) -> JobPosting:
        if job_type.lower() == 'Part time'.lower():
            job = PartTime(title, description, salary)
        else:
            job = FullTime(title, description, salary)
        self.jobs.append(job)
        return job

    def review_applications(self) -> None:
        for application in self.applications:
            print(f'Reviewing resume {application}.')
    