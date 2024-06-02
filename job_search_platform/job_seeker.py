from utils.validators import String, Email
from operations import JobSeekerOperations
from job_postings import JobPosting


class JobSeeker(JobSeekerOperations):
    name = String()
    contact_info = Email()
    resume = String()

    def __init__(
            self,
            name: str,
            contact_info: str,
            resume: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    def search_job(self, company, title: str) -> list:
        result = []
        for job in company.jobs:
            if title.lower() in job.title.lower():
                result.append(job)
        return result

    def apply_to_job(self, company, job: JobPosting) -> None:
        if job in company.jobs:
            company.applications.append(self.resume)
