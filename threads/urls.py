from django.urls import path

from . import views

urlpatterns = [
    path('<int:thread_id>/', views.ThreadDetailView.as_view(), name='thread'),
    path('add/', views.AddThreadView.as_view(), name='threads-add-thread'),
]
