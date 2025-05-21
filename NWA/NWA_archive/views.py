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
    # Получаем все блоги
    blogs = Blogs.objects.all()

    # Получаем все арты
    arts = NWAArchiveArts.objects.all()

    # Получаем все тексты
    texts = NWAArchiveTexts.objects.all()

    # Получаем все коды
    codes = NWAArchiveCodes.objects.all()

    # Создаем список для хранения всех данных
    all_works = []

    # Добавляем информацию из NWAArchiveArts
    for art in arts:
        all_works.append({
            'celebrant_name': art.blog_id.celebrant_name,
            'birthday_date': art.blog_id.birthday_date,
            'work_type': 'Art',  # Указываем тип работы
            'nw_name': art.nw_ID.nw_name,
            'work_date': art.work_publication_date,
        })

    # Добавляем информацию из NWAArchiveTexts
    for text in texts:
        all_works.append({
            'celebrant_name': text.blog_id.celebrant_name,
            'birthday_date': text.blog_id.birthday_date,
            'work_type': 'Text',  # Указываем тип работы
            'nw_name': text.nw_ID.nw_name,
            'work_date': text.work_publication_date,
        })

    # Добавляем информацию из NWAArchiveCodes
    for code in codes:
        all_works.append({
            'celebrant_name': code.blog_id.celebrant_name,
            'birthday_date': code.blog_id.birthday_date,
            'work_type': 'Code',  # Указываем тип работы
            'nw_name': code.nw_ID.nw_name,
            'work_date': code.work_publication_date,
        })

    context = {
        'blogs': all_works,
    }
    return render(request, 'log.html', context)

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')