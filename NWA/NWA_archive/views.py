from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def log(request):
    return render(request, 'log.html')