from django.urls import path

from . import views


urlpatterns = [
    path('<int:thread_id>/', views.ThreadDetailView.as_view(), name='thread'),
    path('add/', views.add_thread, name='threads-add-thread'),
]