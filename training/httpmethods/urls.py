from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.getpost, name='getpost')
]
