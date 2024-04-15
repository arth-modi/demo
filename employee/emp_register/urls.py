from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.employee_list), 
    path('', views.employee_form), 
]