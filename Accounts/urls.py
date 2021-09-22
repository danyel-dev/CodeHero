from django.urls import path

from . import views


urlpatterns = [
    path('', views.registration, name='registration'),
    path('registration', views.registration, name='registration'),
]
