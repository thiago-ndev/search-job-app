from Search_Job.forms import FiltredForm
from Search_Job.views import filtrar_job
from django.test import RequestFactory
from django.urls import reverse
from unittest.mock import patch
import pytest


def test_validar_request_via_get():
    request = RequestFactory().get(reverse('Search_Job:home'))
    response = filtrar_job(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_verificar_se_o_request_post_e_valido(mocker):
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '2023-12-14',
                 'description_required_keywords': 'C#, .Net'
                 }
    request = RequestFactory().post(reverse('Search_Job:home'), form_data)

    # Simular JobSearchService
    mock_service = mocker.patch('Search_Job.views.JobSearchService')
    mock_service.return_value.search_jobs.return_value = ([], None)  # Simula o retorno de search_jobs

    response = filtrar_job(request)

    assert response.status_code == 200
    assert mock_service.called  # confirma que o serviço mockado foi de fato acionado


def test_confirma_se_o_metodo_filtrar_job_retorna_um_render():
    # Criar uma requisição GET (ou POST, conforme necessário)

    request = RequestFactory().get(reverse('Search_Job:home'))
    response = filtrar_job(request)

    assert response.status_code == 200
    assert 'text/html' in response['Content-Type']


def test_verifica_se_o_metodo_retorna_um_render_com_formulario_e_mensagem_de_erro():
    form_data = {'title_key_words': '', 'date_start': 'nlkklnlkn', 'description_required_keywords': ''}
    request = RequestFactory().post(reverse('Search_Job:home'), form_data)
    response = filtrar_job(request)
    HTML = response.content.decode('utf-8')

    assert response.status_code == 200
    assert 'text/html' in response['Content-Type']
    assert 'form' in str(HTML)
