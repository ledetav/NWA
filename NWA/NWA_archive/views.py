from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection
from django.db.models import Q

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
    celebrant_name = request.GET.get('celebrant_name', '')
    all_works = []

    if celebrant_name:
        # Используем Q-объекты для поиска без учета регистра
        q_filter = Q(blog_id__celebrant_name__icontains=celebrant_name) | Q(celebrant_name__icontains=celebrant_name)

        arts = NWAArchiveArts.objects.filter(blog_id__celebrant_name__icontains=celebrant_name)
        texts = NWAArchiveTexts.objects.filter(blog_id__celebrant_name__icontains=celebrant_name)
        codes = NWAArchiveCodes.objects.filter(blog_id__celebrant_name__icontains=celebrant_name)
        blogs = Blogs.objects.filter(celebrant_name__icontains=celebrant_name)
    else:
        arts = NWAArchiveArts.objects.all()
        texts = NWAArchiveTexts.objects.all()
        codes = NWAArchiveCodes.objects.all()
        blogs = Blogs.objects.all()

    for art in arts:
        all_works.append({
            'celebrant_name': art.blog_id.celebrant_name,
            'birthday_date': art.blog_id.birthday_date.strftime("%d.%m.%Y"),
            'work_type': 'Art',
            'nw_name': art.nw_ID.nw_name,
            'work_date': art.work_publication_date,
        })

    for text in texts:
        all_works.append({
            'celebrant_name': text.blog_id.celebrant_name,
            'birthday_date': text.blog_id.birthday_date.strftime("%d.%m.%Y"),
            'work_type': 'Text',
            'nw_name': text.nw_ID.nw_name,
            'work_date': text.work_publication_date,
        })

    for code in codes:
        all_works.append({
            'celebrant_name': code.blog_id.celebrant_name,
            'birthday_date': code.blog_id.birthday_date.strftime("%d.%m.%Y"),
            'work_type': 'Code',
            'nw_name': code.nw_ID.nw_name,
            'work_date': code.work_publication_date,
        })
    
    for blog in blogs:
        all_works.append({
            'celebrant_name': blog.celebrant_name,
            'birthday_date': blog.birthday_date.strftime("%d.%m.%Y"),
            'work_type': 'Blog',
            'nw_name': blog.moderator_id.nw_ID.nw_name,
            'work_date': None,
        })

    context = {
        'blogs': all_works,
        'celebrant_name': celebrant_name,
    }
    return render(request, 'log.html', context)

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')