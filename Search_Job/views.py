from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from .models import JobSearchService
from .forms import FiltredForm
from dotenv import load_dotenv
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
load_dotenv()


def filtrar_job(request):
    form = FiltredForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        job_search_service = JobSearchService(form.cleaned_data)
        job_data_list, error = job_search_service.search_jobs()
        if not job_data_list:
            job_data_list = None
        if error:
            return render(request, 'home.html', {'form': form, 'messages': error})

        return render(request, 'home.html', {'form': form, 'job_data_list': job_data_list})

    return render(request, 'home.html', {'form': form})

def my_custom_page_not_found_view(request, exception=None):
     return render(request,  "404.html")
#
def my_custom_session_expired_view(request, exception):
     return render(request,  "403.html", {}, status=403)


@csrf_exempt
def export_to_excel(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))

        df = pd.DataFrame(data)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=tabela_vagas.xlsx'
        print(response)
        print(df)

        # Salvando DataFrame no response
        df.to_excel(response, index=False)

        return response