
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logInPage', views.logInPage, name='logInPage'),
    path('LoggingIn', views.LoggingIn, name='LoggingIn'),
]
