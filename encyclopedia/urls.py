from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/css" , views.css , name='css')
]
