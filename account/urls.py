from django.urls import path

from .views import Register
from .views import UserLogin


urlpatterns = [
    path('register',
         Register.as_view()),
    path('login',
         UserLogin.as_view()),
]
