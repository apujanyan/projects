from utils.validators import String, Email
from job_search_operations import JobSeekerOperations
from company import Company


class JobSeeker(JobSeekerOperations):
    name = String()
    resume = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            resume: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    def search_job(self, company: Company, title: str) -> list:
        jobs = []

        for job in company.jobs:
            if job.title == title:
                jobs.append(job)

        return jobs

    def apply_to_job(self, company: Company, title: str) -> None:
        for job in company.jobs:
            if job.title == title:
                application = f'{self.name} applied to {job.title}. '
                company.applications.append(application)
                return
        print('Job not existing. ')
