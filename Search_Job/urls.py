from django.urls import path
from . import views

app_name = 'Search_Job'

urlpatterns = [
    path('', views.filtrar_job, name='home'),

]
handler404 = "Search_Job.views.my_custom_page_not_found_view"