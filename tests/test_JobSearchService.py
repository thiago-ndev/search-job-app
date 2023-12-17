from Search_Job.models import JobSearchService
from Search_Job.forms import FiltredForm
from datetime import datetime
from decouple import config
from icecream import ic
import requests
import pytest


def test_verificar_os_tipos_de_dados_do_formulario():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '2023-12-14',
                 'description_required_keywords': 'C#, .Net'
                 }
    job_search_service = JobSearchService(form_data)
    assert isinstance(job_search_service.title, list)
    assert isinstance(job_search_service.date_start, str)
    assert isinstance(job_search_service.description_required_keywords, list)


def test_verificar_se_o_header_esta_correto():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '2023-12-14',
                 'description_required_keywords': 'C#, .Net'
                 }
    service = JobSearchService(form_data)
    assert service.headers == {'user-agent': config('header')}


def test_validar_resposta_da_requisicao_da_api_via_get():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '2023-12-14',
                 'description_required_keywords': 'C#, .Net'
                 }
    for label in form_data['title_key_words'].split(','):
        label_formatted = label.replace(" ", "%20")
        url = f"https://portal.api.gupy.io/api/job?name={label_formatted}&offset=0&limit=10000"
        response = requests.get(url, headers={'user-agent': config('header')})
        assert response.status_code == 200

def test_validar_se_o_metodo_search_jobs_retorna_uma_lista_de_jobs():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': datetime(2023, 10, 10, 1, 11, 56, 130162),
                 'description_required_keywords': 'C#, .Net'
                 }
    job_search_service = JobSearchService(form_data)
    job_data_list, error = job_search_service.search_jobs()
    assert isinstance(job_data_list, list)
    assert error is None

def test_confirmar_mensagem_de_erro_quando_a_requisicao_falha():
    form_data = {'title_key_words': '',
                 'date_start': datetime(2023, 10, 10, 1, 11, 56, 130162),
                 'description_required_keywords': 'C#, .Net'
                 }
    job_search_service = JobSearchService(form_data)
    job_data_list, error = job_search_service.search_jobs()
    ic(error)
    assert error is not None

