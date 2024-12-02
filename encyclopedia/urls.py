from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random-entry/", views.random_entry, name="random-entry"),
    path("new-page/", views.new_page, name='new-page'),
    path("edit-page/<str:title>", views.edit_page, name='edit-page'),
]
