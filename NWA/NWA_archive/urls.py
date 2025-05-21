from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page_view, name="index"),
    path("modal/", views.modal_window, name="modal"),
]