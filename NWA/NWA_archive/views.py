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
    try:
        moderator = Moderators.objects.get(pk=moderator_id) #Получаем модератора по id
        name = moderator.nw_ID.nw_name # получаем nw_name
        #Получаем один экземпляр NorthernWarmers
    except Moderators.DoesNotExist:
        name = None #Если не находим, то присваиваем значение None

    try:
        moderator = Moderators.objects.get(pk=moderator_id)
        position = moderator.moderator_position
    except Moderators.DoesNotExist:
        position = None
    
    try:
        moderator = get_object_or_404(Moderators, pk=moderator_id)
        cat_id = moderator.nw_ID.cat_id  #Получаем cat_id из NorthernWarmers, связанного с модератором.

    except Moderators.DoesNotExist:
        #Обработка, если id не верен.
        cat_id = 558107 #Или возвращаем ошибку 404. Либо выводим сообщение на HTML.
    except Exception as e:
        cat_id = 558107

    context = {
        'blog_count': blog_count,
        'art_count': art_count,
        'text_count': text_count,
        'code_count': code_count,
        'name': name,
        'position': position,
        'moderator_id': moderator_id,
        'cat_id': cat_id
    }
    return render(request, 'index.html', context)

def log_page_view(request):
    return render(request, 'log.html')

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')