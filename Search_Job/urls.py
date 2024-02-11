from django.urls import path
from . import views

app_name = 'Search_Job'

handler404 = "Search_Job.views.my_custom_page_not_found_view"

handler403 = "Search_Job.views.my_custom_session_expired_view"

urlpatterns = [
    path('', views.filtrar_job, name='home'),

]
