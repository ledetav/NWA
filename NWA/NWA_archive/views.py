from django.http import HttpResponse
from django.shortcuts import render
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection

def main_page_view(request):
    blog_count = Blogs.objects.count()  # Получаем количество строк
    art_count = NWAArchiveArts.objects.count()  # Получаем количество строк
    text_count = NWAArchiveTexts.objects.count()  # Получаем количество строк
    code_count = NWAArchiveCodes.objects.count()  # Получаем количество строк
    context = {'blog_count': blog_count, 'art_count': art_count, 'text_count': text_count, 'code_count': code_count}
    return render(request, 'index.html', context)

def log_page_view(request):
    return render(request, 'log.html')

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')