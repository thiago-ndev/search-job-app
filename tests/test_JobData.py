import pytest
from Search_Job.models import JobData


def test_JobData():
    Job = JobData(1, 1, 'name', 'description', 'career_page_name', 'type', 'published_date', 'is_remote_work',
                  'city', 'state', 'country', 'job_url', 'current_date')
    assert Job.job_id == 1
    assert Job.company_id == 1
    assert Job.name == 'name'
    assert Job.description == 'description'


def test_JobData_str():
    Job = JobData(1, 1, 'name', 'description', 'career_page_name', 'type', 'published_date', 'is_remote_work',
                  'city', 'state', 'country', 'job_url', 'current_date')
    assert Job.__str__() == ('1, 1, name, description, career_page_name, type, published_date, is_remote_work ,city,'
                             ' state, country, job_url, current_date')

def test_JobData_repr():
    Job = JobData(1, 1, 'name', 'description', 'career_page_name', 'type', 'published_date', 'is_remote_work',
                  'city', 'state', 'country', 'job_url', 'current_date')

    assert Job.__repr__() == ('1, 1, name, description, career_page_name, type, published_date, is_remote_work ,city,'
                             ' state, country, job_url, current_date')