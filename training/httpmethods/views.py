from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here.

@require_http_methods(['GET', 'POST'])
def getpost(request):
    # if request == 'GET':
    return HttpResponse("Get request recieved")
    
    pass