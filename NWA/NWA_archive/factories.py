import factory
from factory.django import DjangoModelFactory
from faker import Faker
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
import datetime

fake = Faker('ru_RU')

class NorthernWarmersFactory(DjangoModelFactory):
    class Meta:
        model = NorthernWarmers

    cat_id = factory.Sequence(lambda n: n + 1)
    nw_name = factory.Faker('name')
    nw_join_date = factory.Faker('date_object')


class ModeratorsFactory(DjangoModelFactory):
    class Meta:
        model = Moderators

    moderator_position = factory.Faker('job')
    moderator_shedule = factory.Faker('sentence', nb_words=6)
    nw_ID = factory.SubFactory(NorthernWarmersFactory)


class BlogsFactory(DjangoModelFactory):
    class Meta:
        model = Blogs

    moderator_id = factory.SubFactory(ModeratorsFactory)
    celebrant_name = factory.Faker('name')
    birthday_date = factory.Faker('date_object')


class NWAArchiveArtsFactory(DjangoModelFactory):
    class Meta:
        model = NWAArchiveArts

    nw_ID = factory.SubFactory(NorthernWarmersFactory)
    work_art = factory.Faker('sentence', nb_words=4)
    work_publication_date = factory.Faker('date_object')
    work_type = factory.Faker('random_int', min=1, max=5)
    blog_part = factory.Faker('random_int', min=1, max=3)
    blog_id = factory.SubFactory(BlogsFactory)


class NWAArchiveTextsFactory(DjangoModelFactory):
    class Meta:
        model = NWAArchiveTexts

    nw_ID = factory.SubFactory(NorthernWarmersFactory)
    work_text = factory.Faker('text')
    work_publication_date = factory.Faker('date_object')
    work_type = factory.Faker('random_int', min=1, max=5)
    blog_part = factory.Faker('random_int', min=1, max=3)
    blog_id = factory.SubFactory(BlogsFactory)
    moderator_id = factory.SubFactory(ModeratorsFactory)


class NWAArchiveCongratulationsFactory(DjangoModelFactory):
    class Meta:
        model = NWAArchiveCongratulations

    nw_ID = factory.SubFactory(NorthernWarmersFactory)
    congratulation_text = factory.Faker('sentence', nb_words=10)
    sender_name = factory.Faker('name')
    work_publication_date = factory.Faker('date_object')
    blog_id = factory.SubFactory(BlogsFactory)


class NWAArchiveCodesFactory(DjangoModelFactory):
    class Meta:
        model = NWAArchiveCodes

    nw_ID = factory.SubFactory(NorthernWarmersFactory)
    work_code = factory.Faker('word')
    work_publication_date = factory.Faker('date_object')
    blog_id = factory.SubFactory(BlogsFactory)
    moderator_id = factory.SubFactory(ModeratorsFactory)