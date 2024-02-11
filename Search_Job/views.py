from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import JobSearchService
from .forms import FiltredForm
from dotenv import load_dotenv

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

# def my_custom_page_not_found_view(request, exception=None):
#     return render(request,  "404.html")
#
# def my_custom_session_expired_view(request, exception):
#     return render(request,  "403.html", {}, status=403)

