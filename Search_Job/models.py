from django.db import models


# Create your models here.
class JobData:
    def __init__(self, job_id, company_id, name, description,
                 career_page_name, type, published_date, is_remote_work,
                 city, state, country, job_url, current_date):
        self.job_id = job_id
        self.company_id = company_id
        self.name = name
        self.description = description
        self.career_page_name = career_page_name
        self.type = type
        self.published_date = published_date
        self.is_remote_work = is_remote_work
        self.city = city
        self.state = state
        self.country = country
        self.job_url = job_url
        self.current_date = current_date

    def __str__(self):
        return (f'{self.job_id}, {self.company_id}, {self.name}, {self.description}, {self.career_page_name},'
                f' {self.type}, {self.published_date}, {self.is_remote_work} ,{self.city}, {self.state}, {self.country},'
                f' {self.job_url}, {self.current_date}')

    def __repr__(self):
        return (f'{self.job_id}, {self.company_id}, {self.name}, {self.description}, {self.career_page_name},'
                f' {self.type}, {self.published_date}, {self.is_remote_work} ,{self.city}, {self.state}, {self.country},'
                f' {self.job_url}, {self.current_date}')