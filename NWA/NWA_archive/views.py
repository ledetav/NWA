from django.http import HttpResponse
from django.shortcuts import render
from .models import Moderators, NorthernWarmers, Blogs, NWAArchiveArts, NWAArchiveTexts, NWAArchiveCongratulations, NWAArchiveCodes
from django.db import connection

def index(request):
    # blog = Blogs.objects.all()
    # sum_blogs = len(blog)
    # data = {"sum_blogs":"sum_blogs"}
    return render(request, 'index.html')

def log(request):
    return render(request, 'log.html')
