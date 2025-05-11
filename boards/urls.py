from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'board', views.BoardApiView)
print(router.urls)

board_internal_patterns = [
    path('<slug:board_slug>/', views.BoardDetailView.as_view(), name='board-show'),
    path('<slug:board_slug>/thread/', include('threads.urls')),
]

urlpatterns = [
    path('', views.BoardListView.as_view(), name='board-list'),
    path('board/', include((board_internal_patterns, None))),
    path('api/', include(router.urls)),
]

