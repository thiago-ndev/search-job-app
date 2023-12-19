from django.shortcuts import render, HttpResponse
from .models import JobData, JobSearchService
from .forms import FiltredForm
from dotenv import load_dotenv
import pandas as pd
import csv
import os

# Create your views here.
load_dotenv()


def filtrar_job(request):
    form = FiltredForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        job_search_service = JobSearchService(form.cleaned_data)
        job_data_list, error = job_search_service.search_jobs()
        if job_data_list == []:
            job_data_list = None
        if error:
            return render(request, 'home.html', {'form': form, 'messages': error})

        return render(request, 'home.html', {'form': form, 'job_data_list': job_data_list})

    return render(request, 'home.html', {'form': form})
