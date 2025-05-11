from django.urls import path, include
from rest_framework import routers

from django.views.generic import RedirectView

from . import views

router = routers.SimpleRouter()
router.register(r'thread', views.ThreadApiView, basename='lol')
print(router.urls)

urlpatterns = [
    path('<int:thread_id>/', views.ThreadDetailView.as_view(), name='thread'),
    path('add/', views.AddThreadView.as_view(), name='threads-add-thread'),
    # path('api/', RedirectView.as_view(pattern_name='board-list')),
    path('api/', include(router.urls))
]
