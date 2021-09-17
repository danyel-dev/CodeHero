from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home_search/', views.home_search, name='home-search'),
]