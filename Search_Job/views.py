from django.shortcuts import render, HttpResponse
from .models import JobData
from .forms import FiltredForm
from dotenv import load_dotenv
from datetime import datetime
from datetime import date
import pandas as pd
import requests
import csv
import os

# Create your views here.
load_dotenv()

HOME_HTML = 'home.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)'}
COLUMN_NAMES = ['id', 'companyId', 'name', 'description', 'careerPageName', 'type', 'publishedDate', 'isRemoteWork',
                'city', 'state', 'country', 'JobLink', 'searchDate']
data = []
ids = set()

def cadastrar_filtro(request):
    form = FiltredForm()
    job_data_list = []
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)'}

    try:
        if request.method == 'POST':
            form = FiltredForm(request.POST)
            if form.is_valid():
                title = [label.strip() for label in form.cleaned_data['title_key_words'].split(',')]
                date_start = form.cleaned_data['date_start']
                START_DATE_DATETIME = datetime.strptime(date_start, "%d/%m/%Y")

                description_required_keywords = [word.strip() for word in
                                                 form.cleaned_data['description_required_keywords'].split(',')]

                for label in title:

                    labelFormated = label.replace(" ", "%20")
                    url = f"https://portal.api.gupy.io/api/job?name={labelFormated}&offset=0&limit=10000"
                    try:
                        response = requests.get(url, headers=HEADERS)
                        response.raise_for_status()
                        data = response.json().get('data', [])

                        for job in data:
                            job_id = job.get('id', '')
                            published_date_str = job.get('publishedDate', '')
                            published_date = datetime.strptime(published_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                            description = job.get('description', '')

                            if published_date > START_DATE_DATETIME and all(
                                    word in description for word in description_required_keywords):
                                job_data = JobData(
                                    job_id,
                                    job.get('companyId', ''),
                                    job.get('name', ''),
                                    description,
                                    job.get('careerPageName', ''),
                                    job.get('type', ''),
                                    published_date_str,
                                    job.get('isRemoteWork', ''),
                                    job.get('city', ''),
                                    job.get('state', ''),
                                    job.get('country', ''),
                                    job.get('jobUrl', ''),
                                    datetime.today().strftime('%d/%m/%Y')
                                )
                                job_data_list.append(job_data)

                    except requests.exceptions.RequestException as e:
                        return render(request, HOME_HTML, {'messages': e.args})

        return render(request, HOME_HTML, {'form': form, 'job_data_list': job_data_list})
    except Exception as ex:
        return render(request, HOME_HTML, {'form': form, 'messages': ex})


