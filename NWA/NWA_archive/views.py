from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #data = { 'здесь будут переменные'} как передавать переменные: "<название переменное>": <переменная>
    return render(request, 'index.html')

def log(request):
    return render(request, 'log.html')