from django.urls import path

from .views import UploadJob
from .views import JobList


urlpatterns = [
    path('upload',
         UploadJob.as_view()),
    path('jobs',
         JobList.as_view()),
]
