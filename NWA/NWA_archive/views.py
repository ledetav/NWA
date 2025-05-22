from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection

def main_page_view(request):
    blog_count = Blogs.objects.count()  # Получаем количество строк
    art_count = NWAArchiveArts.objects.count()  # Получаем количество строк
    text_count = NWAArchiveTexts.objects.count()  # Получаем количество строк
    code_count = NWAArchiveCodes.objects.count()  # Получаем количество строк

    # Получаем всех модераторов и нужные данные
    moderators_list_data = []
    all_moderators = Moderators.objects.select_related('nw_ID').all() # Оптимизация запроса

    for mod in all_moderators:
        moderators_list_data.append({
            'id': mod.id,
            'name': mod.nw_ID.nw_name,
            'position': mod.moderator_position,
            'cat_id': mod.nw_ID.cat_id,
            'avatar_icon_class': 'fa-solid fa-user-secret' # Можно сделать это поле в модели Moderators, если аватарки разные
        })

    context = {
        'blog_count': blog_count,
        'art_count': art_count,
        'text_count': text_count,
        'code_count': code_count,
        'moderators_list': moderators_list_data
    }
    return render(request, 'index.html', context)

def log_page_view(request):
    return render(request, 'log.html')

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')