from django.urls import path
from . import views

app_name = 'Search_Job'

urlpatterns = [
    path('', views.cadastrar_filtro, name='home'),

]