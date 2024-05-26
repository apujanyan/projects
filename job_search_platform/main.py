from company import Company
from jobs import FullTimeJob, PartTimeJob
from job_seeker import JobSeeker


def main() -> None:
    job_company = Company('Job Company', 'contact@example.com')

    job1 = FullTimeJob('Programming', 4444)
    job2 = PartTimeJob('Management', 3333)

    job_company.add_job(job1)
    job_company.add_job(job2)

    job_seeker1 = JobSeeker('Bob', 'Programmer',
                            'b@mail.com')
    job_seeker2 = JobSeeker('Tim', 'Project manager',
                            'a@mail.com')

    job_seeker1.apply_to_job(job_company, 'Programming')
    job_seeker2.apply_to_job(job_company, 'Management')

    for applications in job_company.applications:
        print(applications)


if __name__ == '__main__':
    main()
