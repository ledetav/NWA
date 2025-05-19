from django.http import HttpResponse
from django.shortcuts import render

def main_page_view(request):
    #data = { 'здесь будут переменные'} как передавать переменные: "<название переменное>": <переменная>
    return render(request, 'index.html')

def log_page_view(request):
    return render(request, 'log.html')

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')