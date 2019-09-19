from django.urls import path

from . import views

urlpatterns = [
    path('v1/index', views.index, name='index'),
    path('v1/feed', views.feed, name='feed'),
]
