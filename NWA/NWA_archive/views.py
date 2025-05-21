from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection

def main_page_view(request):
    blog_count = Blogs.objects.count()  # Получаем количество строк
    art_count = NWAArchiveArts.objects.count()  # Получаем количество строк
    text_count = NWAArchiveTexts.objects.count()  # Получаем количество строк
    code_count = NWAArchiveCodes.objects.count()  # Получаем количество строк
    moderator_id = request.GET.get('moderator_id')  # Получаем id модератора из GET-параметра
    
    if moderator_id:
        # Используем get_object_or_404 для получения модератора или 404 ошибки
        moderator = get_object_or_404(Moderators, pk=moderator_id)
        name = moderator.nw_ID.nw_name
        position = moderator.moderator_position
    else:
        moderator_id = 1
        moderator = Moderators.objects.first()
        name = moderator.nw_ID.nw_name
        position = moderator.moderator_position

    context = {
        'blog_count': blog_count,
        'art_count': art_count,
        'text_count': text_count,
        'code_count': code_count,
        'name': name,
        'position': position,
        'moderator_id': moderator_id
    }
    return render(request, 'index.html', context)

def log_page_view(request):
    return render(request, 'log.html')

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')