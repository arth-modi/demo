from django.urls import path
from demoApp import views

urlpatterns = [
    path('', views.demoApp, name='demoApp'),
    path('home/', views.home),
    path('aboutus/', views.about),
]
