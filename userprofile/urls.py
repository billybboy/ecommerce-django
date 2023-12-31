from django.urls import path
from django.contrib import messages
from django.contrib.auth import views as auth_views
from . import views


app_name = 'userprofile'

urlpatterns = [
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('mystore/', views.mystore, name='mystore'),
    path('mystore_order_detail/<int:pk>', views.mystore_order_detail, name='mystore_order_detail'),
    path('mystore/add_product/', views.add_product, name='add_product'),
    path('mystore/edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('mystore/delete_producr/<int:pk>', views.delete_product, name='delete_product')
]