from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'thread', views.ThreadApiView, basename='lol')
print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
