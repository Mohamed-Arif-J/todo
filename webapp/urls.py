from functools import update_wrapper
from os import name
from turtle import update
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('delete/<int:id>/',views.delete_task,name='delete'),
    path('update/<int:id>/',views.update_task,name='update')
]
