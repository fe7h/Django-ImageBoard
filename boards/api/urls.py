from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'board', views.BoardApiView)

urlpatterns = [
    path('', include(router.urls)),
]
