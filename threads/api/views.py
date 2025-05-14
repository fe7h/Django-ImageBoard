from rest_framework import viewsets, mixins

from utils.drf_utils import ParentIDMixin

from threads.models import Thread
from .serializers import DetailThreadSerializers, ListThreadSerializers
from comments.api.views.mixins import CommentApiMixin


class BaseThreadApiView(ParentIDMixin, viewsets.GenericViewSet):
    model = Thread
    parent_field = 'board'


class DetailThreadApiView(mixins.RetrieveModelMixin,
                          CommentApiMixin,
                          BaseThreadApiView):
    serializer_class = DetailThreadSerializers


class ListThreadApiView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        BaseThreadApiView):
    serializer_class = ListThreadSerializers
