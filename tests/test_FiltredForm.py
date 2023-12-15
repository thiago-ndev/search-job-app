import pytest
from Search_Job.forms import FiltredForm

def test_campos_obrigatorios_preenchidos_corretamente():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '01/01/2023',
                 'description_required_keywords': 'C#, .Net'
                 }
    form = FiltredForm(data=form_data)
    assert form.is_valid(), form.errors


def test_campo_title_key_words_vazio_invalido():
    form_data = {'date_start': '01/01/2023',
                 'description_required_keywords': 'C#, .Net'
                 }
    form = FiltredForm(data=form_data)
    assert not form.is_valid()

def test_campo_description_required_keywords_vazio_invalido():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'date_start': '01/01/2023'
                 }
    form = FiltredForm(data=form_data)
    assert not form.is_valid()

def test_campo_date_start_vazio_invalido():
    form_data = {'title_key_words': 'backend, Back-end, Desenvolvedor',
                 'description_required_keywords': 'C#, .Net'
                 }
    form = FiltredForm(data=form_data)
    assert not form.is_valid()
