from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_api.viewsets.dream_viewset import DreamViewSet
from . import views

router = DefaultRouter()
router.register(r'dreams', DreamViewSet, basename='dreams')


urlpatterns = [
    path('v1/index', views.index, name='index'),
    path('v1/feed', views.feed, name='feed'),
    path('v1/profile', views.profile, name='profile'),
    path('v1/my_dream', views.my_dream, name='my_dream'),
    path('v1/upload_file', views.upload_file, name='upload_file'),
    path('v1/', include(router.urls))
]
