import random
from django.core.management.base import BaseCommand
from django.db import transaction # Для атомарности операции

from NWA_archive.factories import (
    NorthernWarmersFactory, ModeratorsFactory, BlogsFactory,
    NWAArchiveArtsFactory, NWAArchiveTextsFactory,
    NWAArchiveCongratulationsFactory, NWAArchiveCodesFactory
)
from NWA_archive.models import (
    NorthernWarmers, Moderators, Blogs, NWAArchiveArts,
    NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
)
from faker import Faker

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = 'Seeds the database with sample data using factories'

    @transaction.atomic # Оборачиваем в транзакцию
    def handle(self, *args, **options):
        self.stdout.write("Deleting old data...")
        # Осторожно! Это удалит ВСЕ данные из этих таблиц
        NWAArchiveCodes.objects.all().delete()
        NWAArchiveCongratulations.objects.all().delete()
        NWAArchiveTexts.objects.all().delete()
        NWAArchiveArts.objects.all().delete()
        Blogs.objects.all().delete()
        Moderators.objects.all().delete()
        NorthernWarmers.objects.all().delete()
        self.stdout.write("Old data deleted.")

        self.stdout.write("Creating new sample data...")

        # Создаем базовые сущности
        warmers_list = NorthernWarmersFactory.create_batch(10)
        moderators_list = []
        for warmer in random.sample(warmers_list, k=min(5, len(warmers_list))): # Делаем модераторами 5 случайных "греющих"
            moderators_list.append(ModeratorsFactory(nw_ID=warmer))
        
        if not moderators_list and warmers_list: # Гарантируем хотя бы одного модератора, если есть "греющие"
            moderators_list.append(ModeratorsFactory(nw_ID=warmers_list[0]))

        blogs_list = []
        if moderators_list:
            for i in range(20): # 20 блогов
                # Выбираем случайного модератора для блога
                random_moderator = random.choice(moderators_list)
                blogs_list.append(BlogsFactory(moderator_id=random_moderator))
        
        if blogs_list and warmers_list:
            # Создаем контент для блогов
            for blog_entry in blogs_list:
                # Случайное количество артов для каждого блога (0-6)
                for _ in range(random.randint(0, 6)):
                    NWAArchiveArtsFactory(
                        blog_id=blog_entry,
                        nw_ID=random.choice(warmers_list) # Случайный автор арта
                    )
                # Случайное количество текстов
                for _ in range(random.randint(0, 2)):
                    NWAArchiveTextsFactory(
                        blog_id=blog_entry,
                        nw_ID=random.choice(warmers_list),
                        moderator_id=random.choice(moderators_list) # Тексты курируются модераторами
                    )
                # Случайное количество поздравлений
                for _ in range(random.randint(1, 5)):
                    NWAArchiveCongratulationsFactory(
                        blog_id=blog_entry,
                        nw_ID=random.choice(warmers_list) # Поздравитель
                    )
                # Случайное количество кода
                if fake.boolean(chance_of_getting_true=60): # 60% шанс что будет код в блоге
                     NWAArchiveCodesFactory(
                        blog_id=blog_entry,
                        nw_ID=random.choice(warmers_list),
                        moderator_id=random.choice(moderators_list)
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded data.'))