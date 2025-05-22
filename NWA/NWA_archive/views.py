from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection
from django.db.models import Q

WORK_TYPE_CHOICES_FILTER = [
    ('all', 'Все типы'),
    ('art', 'Арт'),
    ('text', 'Текст'),
    ('code', 'Код'),
    ('congrats', 'Поздравление'),
]

def get_work_type_choices(): # Эта функция используется в шаблоне для генерации <select>
    return WORK_TYPE_CHOICES_FILTER

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
    celebrant_name_filter = request.GET.get('celebrant_name', '')
    selected_work_type_filter = request.GET.get('type_work', 'all')

    all_works_display_list = []

    # Базовые QuerySets с select_related для оптимизации
    arts_qs = NWAArchiveArts.objects.select_related('blog_id', 'nw_ID').all()
    texts_qs = NWAArchiveTexts.objects.select_related('blog_id', 'nw_ID').all()
    codes_qs = NWAArchiveCodes.objects.select_related('blog_id', 'nw_ID').all()
    congrats_qs = NWAArchiveCongratulations.objects.select_related('blog_id', 'nw_ID').all()

    # Фильтрация по имени именинника
    if celebrant_name_filter:
        arts_qs = arts_qs.filter(blog_id__celebrant_name__icontains=celebrant_name_filter)
        texts_qs = texts_qs.filter(blog_id__celebrant_name__icontains=celebrant_name_filter)
        codes_qs = codes_qs.filter(blog_id__celebrant_name__icontains=celebrant_name_filter)
        congrats_qs = congrats_qs.filter(blog_id__celebrant_name__icontains=celebrant_name_filter)

    # Формирование списка работ в зависимости от выбранного типа
    if selected_work_type_filter == 'art' or selected_work_type_filter == 'all':
        for art in arts_qs:
            all_works_display_list.append({
                'celebrant_name': art.blog_id.celebrant_name,
                'birthday_date': art.blog_id.birthday_date.strftime("%d.%m.%Y"),
                'work_type_display': "Арт", # Отображаемый тип работы
                'nw_name': art.nw_ID.nw_name, # Даритель (автор арта)
                'work_date': art.work_publication_date.strftime("%d.%m.%Y"),
            })

    if selected_work_type_filter == 'text' or selected_work_type_filter == 'all':
        for text in texts_qs:
            all_works_display_list.append({
                'celebrant_name': text.blog_id.celebrant_name,
                'birthday_date': text.blog_id.birthday_date.strftime("%d.%m.%Y"),
                'work_type_display': "Текст",
                'nw_name': text.nw_ID.nw_name, # Даритель (автор текста)
                'work_date': text.work_publication_date.strftime("%d.%m.%Y"),
            })

    if selected_work_type_filter == 'code' or selected_work_type_filter == 'all':
        for code in codes_qs:
            all_works_display_list.append({
                'celebrant_name': code.blog_id.celebrant_name,
                'birthday_date': code.blog_id.birthday_date.strftime("%d.%m.%Y"),
                'work_type_display': "Код",
                'nw_name': code.nw_ID.nw_name, # Даритель (автор кода)
                'work_date': code.work_publication_date.strftime("%d.%m.%Y"),
            })

    if selected_work_type_filter == 'congrats' or selected_work_type_filter == 'all':
        for congrat in congrats_qs:
            all_works_display_list.append({
                'celebrant_name': congrat.blog_id.celebrant_name,
                'birthday_date': congrat.blog_id.birthday_date.strftime("%d.%m.%Y"),
                'work_type_display': "Поздравление",
                'nw_name': congrat.nw_ID.nw_name,
                'work_date': congrat.work_publication_date.strftime("%d.%m.%Y"),
            })
    
    # Опционально: Сортировка списка all_works_display_list
    # Например, по дате публикации (если она есть), затем по имени именинника

    context = {
        'blogs': all_works_display_list,
        'celebrant_name': celebrant_name_filter,
        'work_type_choices': get_work_type_choices(),
        'selected_work_type': selected_work_type_filter,
    }
    return render(request, 'log.html', context)

def test_page_view(request):
    return render(request, 'test.html')

def modal_window(request):
    return render(request, 'modal_window.html')