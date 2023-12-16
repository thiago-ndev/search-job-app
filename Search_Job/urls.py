from django.urls import path
from . import views

app_name = 'Search_Job'

urlpatterns = [
    path('', views.filtrar_job, name='home'),

]