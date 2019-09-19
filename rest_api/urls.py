from django.urls import path

from . import views

urlpatterns = [
    path('v1/index', views.index, name='index'),
]
