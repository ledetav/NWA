from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница")

def log(request):
    return HttpResponse("Лог")