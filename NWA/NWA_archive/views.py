from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = { 'name: nw_name'} 
    return render(request, 'index.html', context=data)

def log(request):
    return render(request, 'log.html')