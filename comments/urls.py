from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_comment, name='comments-add-comment'),
]