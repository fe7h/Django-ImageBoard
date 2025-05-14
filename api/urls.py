from django.urls import path, include

from boards.api.urls import urlpatterns as boards_urls
from threads.api.urls import urlpatterns as threads_urls


urlpatterns = [
    path('', include(boards_urls)),
    path('board/<int:board>/', include(threads_urls))
]
