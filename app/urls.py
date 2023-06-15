from django.urls import path
from django import views
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]