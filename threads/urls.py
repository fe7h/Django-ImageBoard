from django.urls import path

from . import views


urlpatterns = [
    path('<int:thread_id>/', views.thread_show, name='thread'),
]