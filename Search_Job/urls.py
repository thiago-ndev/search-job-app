from django.urls import path
from . import views

app_name = 'Search_Job'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_filtro, name='cadastro')

]