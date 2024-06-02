from company import Company
from job_seeker import JobSeeker


def main() -> None:
    bob = JobSeeker('Bob', 'bob@mail.com',
                    'Python programmer')
    job_company = Company('Job company', 'contact@mail.com')

    job = job_company.add_job_posting('Python developer',
                                      'Developing python apps',
                                      1000.0)

    print("Job company's jobs.")
    for job in job_company.jobs:
        job.get_description()

    bob.apply_to_job(job_company, job)

    print("\nJob company's applications.")
    for application in job_company.applications:
        print(application)

    print()
    job_company.review_applications()


if __name__ == '__main__':
    main()
