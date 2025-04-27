from django.urls import path, include

from . import views


urlpatterns = [
    # path('', views.board_list, name='board-list'),
    path('board/<slug:board_slug>/', views.BoardDetailView.as_view(), name='board-show'),
    path('board/<slug:board_slug>/thread/', include('threads.urls')),
]