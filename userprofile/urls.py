from django.urls import path
from . import views


app_name = 'userprofile'

urlpatterns = [
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail')
]