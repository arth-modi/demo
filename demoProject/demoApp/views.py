from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demoApp(request):
    return HttpResponse("Hello World")

def home(request):
    return render(request,'Index.html')

def about(request):
    return render(request, 'aboutus.html')
