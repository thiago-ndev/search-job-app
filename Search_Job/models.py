from datetime import datetime
from decouple import config
import requests


# Create your models here.
class JobData:
    def __init__(self, job_id, company_id, name, description,
                 career_page_name, types, published_date, is_remote_work,
                 city, state, country, job_url, current_date):
        self.job_id = job_id
        self.company_id = company_id
        self.name = name
        self.description = description
        self.career_page_name = career_page_name
        self.type = types
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
        return self.__str__()


class JobSearchService:
    def __init__(self, form_data):
        self.title = [label.strip() for label in form_data['title_key_words'].split(',')]
        self.date_start = form_data['date_start']
        self.description_required_keywords = [word.strip() for word in
                                              form_data['description_required_keywords'].split(',')]
        self.headers = {'user-agent': config('header')}

    def search_jobs(self):
        job_data_list = []
        error = None

        # Filtra as palavras chaves do titulo
        for label in self.title:
            label_formatted = label.replace(" ", "%20")
            url = f"https://portal.api.gupy.io/api/job?name={label_formatted}&offset=0&limit=10000"
            try:
                response = self._request(url)
                job_data_list.extend(self._processar_response(response))
            except Exception as e:
                error = str(e)
                break
        return job_data_list, error

    def _request(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        return response.json()

    def _processar_response(self, response_data):
        processed_data = []
        incre = 0 # contador para debug
        for job in response_data.get('data', []):
            incre += 1
            if self._validar_job(job):
                processed_data.append(self._cadastrar_job(job))
            #print(incre)
        return processed_data

    def _validar_job(self, job):
        """Verifica se o job é válido
            Args: Converte a data de publicação para datetime e verifica se é posterior à data de início
        """
        try:
            published_date = datetime.strptime(job.get('publishedDate', ''), "%Y-%m-%dT%H:%M:%S.%fZ")
            date_start_datetime = datetime.combine(self.date_start, datetime.min.time())

            if published_date > date_start_datetime:
                description = job.get('description', '')
                # Verifique se as palavras-chave necessárias estão na descrição
                return [word in description for word in self.description_required_keywords]
            return False
        except Exception as ex:
            return ex.args

    @staticmethod
    def _cadastrar_job(job):
        return JobData(
            job.get('id', ''),
            job.get('companyId', ''),
            job.get('name', ''),
            job.get('description', ''),
            job.get('careerPageName', ''),
            job.get('type', ''),
            job.get('publishedDate', ''),
            job.get('isRemoteWork', ''),
            job.get('city', ''),
            job.get('state', ''),
            job.get('country', ''),
            job.get('jobUrl', ''),
            datetime.today().strftime('%d/%m/%Y')
        )
