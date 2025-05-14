from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'thread', views.ListThreadApiView, basename='threads')
router.register(r'thread', views.DetailThreadApiView, basename='thread')

urlpatterns = [
    path('', include(router.urls))
]
