from django.urls import path
from . import views

urlpatterns = [
    path('taskmanager/start_scraping', views.start_scraping, name='start_scraping'),
    path('taskmanager/scraping_status/<str:job_id>', views.scraping_status, name='scraping_status'),
]
